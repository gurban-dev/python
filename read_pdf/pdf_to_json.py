import os
import json
from pdfminer.high_level import extract_text

def extract_pdf_to_json(input_folder, output_folder):
  '''
  This ensures that the output folder exists.
  If it doesn't, the function creates it.

  exist_ok=True means that if the folder already
  exists, no error will be raised.'''
  os.makedirs(output_folder, exist_ok=True)

  # os.listdir(input_folder) returns a list of
  # all file names in the specified folder.
  print(f'os.listdir({input_folder}): {os.listdir(input_folder)}')

  # Loop through all PDF files in the input folder.
  for filename in os.listdir(input_folder):
    # Verify that the current file has a .pdf extension.
    if filename.endswith(".pdf"):
      print(f'input_folder: {input_folder}\n'
            f'filename: {filename}')

      pdf_path = os.path.join(input_folder, filename)

      print('\npdf_path:', pdf_path)

      json_filename = os.path.splitext(filename)[0] + ".json"

      print('\njson_filename:', json_filename)

      json_path = os.path.join(output_folder, json_filename)

      print('\njson_path:', json_path)

      try:
        # Extract the text from the PDF file.
        text = extract_text(pdf_path)

        # Split the input string into a list of strings
        # based on the newline escape sequence \n.
        # Each string will represent a line of text.
        text_separated_by_newline = text.split("\n")

        # Create a Python dictionary named "data" that
        # will hold the structured data that will be
        # written into the JSON file.
        data = {
          "file_name": filename,
          "content": text_separated_by_newline
        }

        '''
        Open the file at the path specified by json_path
        in write mode ("w"), meaning the contents of the
        file will be overwritten if it already exists.

        The with statement ensures the file is automatically
        closed after the block of code is executed, even if
        an error occurs.

        The encoding="utf-8" argument ensures that the file
        is written using the UTF-8 encoding, which supports
        many different character sets (including non-ASCII
        characters).

        as json_file assigns the opened file to the variable
        json_file, which is used to write data into the file.
        '''
        with open(json_path, "w", encoding="utf-8") as json_file:
          '''
          Write the data dictionary to the json_file as a
          properly formatted JSON string.

          indent=2 makes the JSON output more readable by
          adding indentation with 4 spaces for each level
          of nested structure.

          ensure_ascii=False allows the JSON to include
          non-ASCII characters like accented letters without
          escaping them into ASCII equivalents.

          E.g., é will be saved as é, not \u00e9.'''
          json.dump(data, json_file, indent=2, ensure_ascii=False)

        print(f"Processed: {filename} -> {json_filename}")
      except Exception as e:
        print(f"Failed to process {filename}: {e}")

# Define input and output folders.
input_folder = '/home/deniz/python/read_pdf/pdf'
output_folder = '/home/deniz/python/read_pdf/json'

extract_pdf_to_json(input_folder, output_folder)