import re
import PyPDF2

OUTPUT_FILE = "abbreviations.txt"
PATTERN = r"\b[A-Z]{2,}\b"

reader = PyPDF2.PdfReader("main.pdf")

N_pages = 230

acronyms_list = []

for i in range(N_pages):

    # print progress
    print(f"Processing page {i+1}/{N_pages}")

    page = reader.pages[i]

    text = page.extract_text()

    acronyms = re.findall(PATTERN, text)

    if acronyms:
        acronyms_list.extend(acronyms)

acronyms_list = sorted(list(set(acronyms_list)))

# writing the acronyms to a file
with open(OUTPUT_FILE, "w") as file:
    for acronym in acronyms_list:

        text = "\\newacronym{%s}{%s}{}" % (acronym.lower(), acronym)

        file.write(text + "\n")
