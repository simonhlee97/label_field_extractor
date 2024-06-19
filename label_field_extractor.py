from pdfquery import PDFQuery
import xml.etree.ElementTree as ET
import csv
import json
import argparse
import os
import time


def get_filename(file_path):
    base_name = os.path.basename(file_path)
    file_name, file_extension = os.path.splitext(base_name)
    return file_name


def main():
    parser = argparse.ArgumentParser(description='extract data from a PDF and create CSV and JSON')
    parser.add_argument('filename', type=str, help='name of the PDF file')
    args = parser.parse_args()

    filename = args.filename
    filename_without_extension = get_filename(filename)
    print(f'Processing the pdf file: {filename}')

    pdf = PDFQuery(filename)

    pdf.load()
    pdf.tree.write(f"{filename_without_extension}.xml", pretty_print=True)

    tree = ET.parse(f"{filename_without_extension}.xml")
    root = tree.getroot()

    csv_filepath = f"{filename_without_extension}.csv"
    extract_parse_data(root, csv_filepath)
    # print(f"CSV file: {csv_filepath} has been created")

    json_output_filepath = f"{filename_without_extension}.json"

    csv_to_json(csv_filepath, json_output_filepath)
    print(f"JSON file: {json_output_filepath} has been created")
    time.sleep(2)

    delete_csv(csv_filepath)


def extract_parse_data(root, csv_filepath):
    with open(csv_filepath, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['page_num', 'part_num', 'serial_num'])  # header row

        for page in root.findall('.//LTPage'):
            # get page id
            page_id = page.get('pageid')

            # part # is in the first LT text box
            first_box = page.find('.//LTTextBoxHorizontal')

            # part # is 2nd item (index 1)
            part_number = first_box[1].text.strip()

            # locate serial numbers
            LT_9 = page[8]
            serial_number = LT_9[0].text.strip()

            csvwriter.writerow([page_id, part_number, serial_number])


def csv_to_json(csv_filepath, json_filepath):
    with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        data = []
        for row in csv_reader:
            data.append(row)

    with open(json_filepath, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


def delete_csv(csv_filepath):
    try:
        os.remove(csv_filepath)
        # print("csv file has been deleted")
    except OSError as e:
        print(f"Error: {csv_filepath} : {e.strerror}")


if __name__ == '__main__':
    main()
