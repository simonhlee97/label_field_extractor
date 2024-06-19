# A Python Script that Parses XML from a PDF file and Writes to CSV and JSON FIles

This script reads the PDF file, extracts each page's id, part number, and serial number, then writes those values into a JSON file.

## Getting Started

### Prerequisites

- Make sure your computer has at least Python version 3.2 installed. If not, go to the [python download page](https://python.org).
- You can check to see if Python is installed on your PC by opening your Command Prompt (Windows) or Terminal (Mac) and running the following command:
- `python --version`
- If it returns version 3.2 or higher, then you are all set.

### Installing

These steps will get you a copy of the python script so that you can run it on your local machine.

Go to the url below:

`https://github.com/simonhlee97/label_field_extractor`

Click on the green Code dropdown button, and click `Download Zip`

Open your Downloads folder and unzip the zip file.

## Navigating to the Script from Command Prompt

Open your Command Prompt and `cd` (change directory) to the unzipped folder so that you see something like the following:

`C:\Users\JohnDoe\Downloads\python-script>`

(You can also do this in VS Code's built-in Terminal)

### (Optional - creating a virtual env)

- Create a virtual environment (optional but recommended) by running `python -m venv venv`
- Activate the virtual environment:
  - on Windows: `.\venv\Scripts\activate`
  - on Mac/Linux: `source venv/bin/activate`

## Install the Dependencies

`pip install -r requirements.txt`

This command will install the dependencies.

## Move (or copy/paste) PDF files

Move (or copy/paste) your PDF files into your project directory.

## Running the Script

Run the following command:

`python label_field_extractor.py HEWITT_THURSDAY_C.pdf`

(replace the "HEWITT_THURSDAY_C.pdf" with other PDF filenames)

The script will create a json file with the same file name. For example:

- `HEWITT_THURSDAY_C.json`

## Resources and Links

- [xml.etree.ElementTree (aka ET)](https://docs.python.org/3/library/xml.etree.elementtree.html)
- [pdfquery](https://pypi.org/project/pdfquery/)
