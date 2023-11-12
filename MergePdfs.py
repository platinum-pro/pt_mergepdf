import os
from PyPDF2 import PdfWriter, PdfReader

def merge_pdfs_updated(pdf_list, output_filename):
    print("Merging PDFs...")  # Debug print
    pdf_writer = PdfWriter()
    pdf_readers = []

    # Open all PDF files and create reader objects
    for pdf in pdf_list:
        print(f"Opening file: {pdf}")  # Debug print
        f = open(pdf, 'rb')
        pdf_reader = PdfReader(f)
        pdf_readers.append((pdf_reader, f))

    # Iterate through all the PDF reader objects and add their pages
    for pdf_reader, _ in pdf_readers:
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    # Write the merged pages to the output file
    with open(output_filename, 'wb') as out:
        print(f"Writing to output file: {output_filename}")  # Debug print
        pdf_writer.write(out)

    # Close all the opened PDF files
    for _, file in pdf_readers:
        file.close()

    print("Merge completed.")  # Debug print

# Your list of PDF files to merge
pdf_files = ['PDF1.pdf', 
             'PDF2.pdf', 
             'PDF3.pdf']

# The name of the output merged PDF file
output_file = 'Output.pdf'


# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# Call the function to merge the PDFs
merge_pdfs_updated(pdf_files, output_file)

# Check if the file has been created
output_path = os.path.join(os.getcwd(), output_file)
if os.path.exists(output_path):
    print(f"Output file created successfully: {output_path}")
else:
    print(f"Output file not found: {output_path}")
