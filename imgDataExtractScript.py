"""
Objective:
Extracts all body metric values from a screenshot of the 
ArboLeaf smartphone app result page following a recorded measurement

Initilization:
    # Specify the following:
    # [1] Network path to the original jpeg image
    # [2] Destination path where the PDF conversion of the original image will be saved
    # [3] Date the image was read or processed
    # [4] Network path to the Microsoft Excel file where body statistics will be recorded

Returns:
    Microsoft Excel file used to store data from current and follow-up measurements.  
"""

import os
import re

import cv2
import img2pdf

import numpy as np
import pandas as pd

import pytesseract
from PIL import Image
from pdf2image import convert_from_path

# Define critical initial variables
pdf_file_path = "C:/Screenshot_Network_Location/Screenshot_FileName.pdf"
jpeg_file_path = "C:/Screenshot_Network_Location/Screenshot_FileName.jpeg"
reading_date = "Date_Screenshot_Taken"

output_xls = 'C:/Screenshot_Network_Location/ExcleFileName_WhereBodyData_WiilBeSaved.xlsx'


def sharpen_and_replace_image(image_path, brightness, contrast):
    """
    Sharpens an image and adjusts brightness and contrast.

    Args:
        image_path (str): Path to the image file
        brightness (float): Value to adjust brightness
        contrast (float): Value to adjust contrast

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        image = cv2.imread(image_path)
        sharpened_image = cv2.addWeighted(
            image, contrast, np.zeros(image.shape, image.dtype), 0, brightness
        )
        cv2.imwrite(image_path, sharpened_image)
        return True
    except Exception as e:
        print(f"Error processing image {image_path}: {str(e)}")
        return False


def jpeg_2_pdf_img2pdf(image_path, pdf_path):
    """
    Converts a JPEG image to PDF using img2pdf.

    Args:
        image_path (str): Path to the JPEG image
        pdf_path (str): Path to save the PDF
    """
    try:
        img = Image.open(image_path)
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(img.filename))
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def jpeg_2_pdf_cv(image_path, pdf_path):
    """
    Converts a JPEG image to a PDF using OpenCV and Pillow.

    Args:
        image_path (str): Path to the JPEG image
        pdf_path (str): Path to save the PDF
    """
    try:
        image = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(image_rgb)
        pil_image.save(pdf_path)
    except Exception as e:
        print(f"Error converting {image_path} to PDF: {e}")


def extract_text_from_image(image_path):
    """Extracts text from an image using pytesseract."""
    try:
        img = Image.open(image_path)
        return pytesseract.image_to_string(img)
    except Exception as e:
        return f"Error: {e}"


def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF using pytesseract and pdf2image."""
    pages = convert_from_path(pdf_path)
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page)
    return text


def remove_first_two_lines(text):
    """Removes the first two lines from the given text."""
    lines = text.splitlines(True)
    if len(lines) > 2:
        return ''.join(lines[2:])
    elif len(lines) > 0:
        return ''
    return text


def remove_lines_without_numbers(str_content):
    """Removes lines without numeric characters from the text."""
    return_str_content = ''
    lines = str_content.splitlines()
    for line in lines:
        if re.search(r'\d', line):
            return_str_content += line + "\r\n"
    return return_str_content


def replace_except_numbers_dots(text):
    """Replaces all characters except numbers and dots with spaces."""
    return re.sub(r"[^0-9\.]", " ", text)


def replace_multiple_spaces(text):
    """Replaces multiple spaces with a single space."""
    return re.sub(r"\s+", " ", text)


def replace_bad_characters(text):
    """Replaces bad characters with spaces.

    Args:
        text: The input string.

    Returns:
        The string without the bad chars, or the original string if no bad chars waere found.
    """

    bad_chars = ['1b']
    for c in bad_chars:
        text = re.sub(c, " ", text)
    return text

def remove_trailing_period(input_string):
    """
    Removes the trailing period from a string, if present.

    Args:
        input_string: The string to process.

    Returns:
        The string with the trailing period removed, or the original string if no period was found.
    """
    if input_string and input_string[-1] == '.':
        return input_string[:-1]
    return input_string


# Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Process image
sharpen_and_replace_image(jpeg_file_path, 1, 0.5)
jpeg_2_pdf_img2pdf(jpeg_file_path, pdf_file_path)

# Extract and clean text
extracted_text = extract_text_from_pdf(pdf_file_path)
extracted_text = remove_first_two_lines(extracted_text)
print("pre-processed: ", extracted_text)

extracted_text = remove_lines_without_numbers(extracted_text)
extracted_text = replace_bad_characters(extracted_text)
extracted_text = replace_except_numbers_dots(extracted_text)
extracted_text = replace_multiple_spaces(extracted_text)
extracted_text = extracted_text.split()
extracted_text = [remove_trailing_period(item) for item in extracted_text]
print("after-processing: ", extracted_text)

# Initialize dictionary with metrics
Msmnt_Vars = {
    'Reading_Date': reading_date
}

if extracted_text[0][-1] == '.':
    extracted_text[0] = extracted_text[0][:-1]

Msmnt_Vars['Weight'] = float("{:.3f}".format(float(extracted_text[0])))
Msmnt_Vars['Boday Fat'] = float("{:.3f}".format(float(extracted_text[1]) / 100.0))
Msmnt_Vars['BMI'] = extracted_text[2]
Msmnt_Vars['Skeletal Muscle'] = float("{:.3f}".format(float(extracted_text[3]) / 100.0))
Msmnt_Vars['Muscle Mass'] = float("{:.1f}".format(float(extracted_text[4])))
Msmnt_Vars['Muscle Storage Ability Level'] = float(extracted_text[5])
Msmnt_Vars['Protein'] = float("{:.3f}".format(float(extracted_text[6]) / 100.0))
Msmnt_Vars['BMR'] = float(extracted_text[7])
Msmnt_Vars['Fat-Free Body Weight'] = float(extracted_text[8])
Msmnt_Vars['Subcutaneous Fat'] = float("{:.3f}".format(float(extracted_text[9]) / 100.0))
Msmnt_Vars['Visceral Fat'] = float(extracted_text[10])
Msmnt_Vars['Body Water'] = float("{:.3f}".format(float(extracted_text[11]) / 100.0))
Msmnt_Vars['Bone Mass'] = float(extracted_text[12])

print(Msmnt_Vars)

# Export to Excel
df = pd.DataFrame(data=Msmnt_Vars, index=[0])

if not os.path.exists(output_xls):
    df.to_excel(output_xls, index=False)
else:
    existing_df = pd.read_excel(output_xls)

    # if the new record has the same date with an existing 
    # then it drops the latter and keeps the former
    existing_df = existing_df.drop(existing_df[existing_df['Reading_Date'] == reading_date].index)

    new_df = pd.DataFrame(data=Msmnt_Vars, index=[0])
    
    combined_df = pd.concat([existing_df, new_df], ignore_index=True)
    combined_df.to_excel(output_xls, index=False)