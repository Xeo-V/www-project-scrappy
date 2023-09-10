import os
import sys
import json
from scipy.stats import entropy
from collections import Counter
import PyPDF2
import re
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

print("Available languages: en, es, de, fr, ru, zh")
language = input("Select a language: ")

script_dir = os.path.dirname(os.path.realpath(__file__))
localization_path = os.path.join(script_dir, "localizations", f"{language}.json")

if not os.path.exists(localization_path):
    print("Error: Localization file does not exist.")
    sys.exit(1)

with open(localization_path, 'r') as f:
    localization = json.load(f)

log_path = os.path.join(script_dir, "ScrapPY.log")
with open(log_path, "w") as log_file:
    log_file.write(localization["starting"] + "\n")

print(localization["choose_mode"])
print("Available Modes:")
print("  word-frequency: List 100 most common words in the PDF")
print("  full: List all unique words in the PDF")
print("  metadata: Display metadata information about the PDF")
print("  entropy: Calculate entropy for unique words in the PDF")
mode_choice = input("Select a mode: ")

pdf_file_path = input(localization["enter_path"])

if not os.path.exists(pdf_file_path):
    print(localization["file_not_exist"])
    sys.exit(1)

if not pdf_file_path.lower().endswith('.pdf'):
    print(localization["not_pdf"])
    sys.exit(1)

output_file_name = input(localization["output_file"])

def read_page(page):
    try:
        page_text = page.extract_text()
        keywords = re.findall(r'[a-zA-Z]\w+', page_text.lower())
        return keywords
    except Exception as e:
        with open(log_path, "a") as log_file:
            log_file.write(f"Error reading page: {e}\n")
        return []

def main():
    try:
        with open(log_path, "a") as log_file:
            log_file.write(localization["processing"] + "\n")

        pdf_file = open(pdf_file_path, 'rb')
        read_pdf = PyPDF2.PdfReader(pdf_file)
        num_pages = len(read_pdf.pages)

        keywords = []
        with ThreadPoolExecutor() as executor:
            future_to_page = {executor.submit(read_page, read_pdf.pages[i]): i for i in range(num_pages)}
            for future in future_to_page:
                keywords += future.result()

        if mode_choice == 'metadata':
            metadata_dict = metadata(pdf_file_path)
            output_to_file(metadata_dict, output_file_name)
        else:
            if mode_choice == 'word-frequency':
                result = word_frequency(keywords)
            elif mode_choice == 'full':
                result = dedup(keywords)
            elif mode_choice == 'entropy':
                result = calculate_entropy(keywords)
            else:
                print("Invalid mode selected.")
                sys.exit(1)
            output_to_file(result, output_file_name)

        with open(log_path, "a") as log_file:
            log_file.write(localization["complete"] + "\n")

    except Exception as e:
        with open(log_path, "a") as log_file:
            log_file.write(localization["error"] + f": {e}\n")

def metadata(file_path):
    with open(file_path, 'rb') as pdf_file:
        read_pdf = PyPDF2.PdfReader(pdf_file)
        pdf_info = read_pdf.metadata
        return {
            "Title": pdf_info.get('/Title', 'N/A'),
            "Subject": pdf_info.get('/Subject', 'N/A'),
            "Author": pdf_info.get('/Author', 'N/A'),
            "Creator": pdf_info.get('/Creator', 'N/A'),
            "Producer": pdf_info.get('/Producer', 'N/A'),
            "Creation Date": str(pdf_info.get('/CreationDate', 'N/A'))
        }

def word_frequency(keywords):
    return Counter(keywords).most_common(100)

def calculate_entropy(keywords):
    keyword_bytearray_list = [bytearray(word, 'utf-8') for word in keywords]
    entropy_scores = [float(entropy(pd.Series(word).value_counts())) for word in keyword_bytearray_list]
    return dict(sorted({keywords[i]: entropy_scores[i] for i in range(len(keywords))}.items(), key=lambda x: x[1], reverse=True))

def dedup(keywords):
    return list(set(keywords))

def output_to_file(result, output_file_name):
    output_path = os.path.join(script_dir, output_file_name if output_file_name else "ScrapPY.txt")
    with open(output_path, 'w') as f:
        if isinstance(result, dict):
            for key, value in result.items():
                f.write(f"{key}: {value}\n")
        else:
            for item in result:
                f.write(f"{item}\n")

if __name__ == "__main__":
    main()
