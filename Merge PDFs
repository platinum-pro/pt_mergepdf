import PyPDF2

def merge_pdfs(pdf_list, output_filename):
    # Create a new PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Iterate through all the PDF files and add their pages to the writer object
    for pdf in pdf_list:
        with open(pdf, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            for page_num in range(len(pdf_reader.pages)):  # Updated this line
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

    # Write the merged pages to the output file
    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)

# Example usage:
pdf_files = ['PDF1.pdf', 
             'PDF2.pdf', 
             'PDF3.pdf']
merge_pdfs(pdf_files, 'MergedPDF.pdf')
