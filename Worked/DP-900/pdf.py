import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfMerger

def convert_png_to_pdf(png_file, pdf_file):
    image = Image.open(png_file)
    c = canvas.Canvas(pdf_file, pagesize=image.size)
    c.drawImage(png_file, 0, 0)
    c.save()

file_number = '47'

def combine_pdfs(pdf_files, output_file):
    merger = PdfMerger()

    for pdf_file in pdf_files:
        merger.append(pdf_file)

    merger.write(output_file)
    merger.close()

if __name__ == "__main__":
    png_folder = f"/Users/aayushgupta/Desktop/DP-900/pages/Images/251-304/"
    output_folder = "/Users/aayushgupta/Desktop/DP-900/pages/temp/"

    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    png_files = [f for f in os.listdir(png_folder) if f.endswith('.png')]
    png_files.sort(key=lambda x: int(x.split('-')[-1].split('.')[0]))  # Sort based on numeric part

    # Convert PNG files to PDF
    pdf_files = []
    for png_file in png_files:
        pdf_file = os.path.join(output_folder, os.path.splitext(png_file)[0] + ".pdf")
        convert_png_to_pdf(os.path.join(png_folder, png_file), pdf_file)
        pdf_files.append(pdf_file)

    # Combine PDF files
    output_pdf = f"/Users/aayushgupta/Desktop/DP-900/pages/251-304.pdf"
    combine_pdfs(pdf_files, output_pdf)

    # Clean up intermediate PDF files
    for pdf_file in pdf_files:
        os.remove(pdf_file)
