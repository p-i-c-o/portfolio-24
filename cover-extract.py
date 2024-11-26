import os
import fitz  # PyMuPDF
from ebooklib import epub
from PIL import Image
from io import BytesIO

def extract_pdf_cover(pdf_path, output_path):
    """Extract the cover from a PDF and save it as a PNG."""
    try:
        pdf_document = fitz.open(pdf_path)
        # Get the first page
        page = pdf_document[0]
        # Render page to an image
        pix = page.get_pixmap()
        # Save as PNG
        pix.save(output_path)
        print(f"PDF cover saved: {output_path}")
    except Exception as e:
        print(f"Failed to extract cover from PDF: {pdf_path}. Error: {e}")

def extract_epub_cover(epub_path, output_path):
    """Extract the cover from an EPUB and save it as a PNG."""
    try:
        book = epub.read_epub(epub_path)
        cover_item = None

        # Search for the cover image
        for item in book.items:
            if item.get_type() == epub.ITEM_IMAGE and "cover" in item.get_name().lower():
                cover_item = item
                break

        if cover_item:
            # Convert bytes to an image and save
            image = Image.open(BytesIO(cover_item.get_content()))
            image.save(output_path, "PNG")
            print(f"EPUB cover saved: {output_path}")
        else:
            print(f"No cover found in EPUB: {epub_path}")
    except Exception as e:
        print(f"Failed to extract cover from EPUB: {epub_path}. Error: {e}")

def extract_covers_from_dir(input_dir, output_dir):
    """Scan a directory for EPUB and PDF files and extract their covers."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_name, file_ext = os.path.splitext(file)
            output_path = os.path.join(output_dir, file_name + ".png")

            if file_ext.lower() == ".pdf":
                extract_pdf_cover(file_path, output_path)
            elif file_ext.lower() == ".epub":
                extract_epub_cover(file_path, output_path)

if __name__ == "__main__":
    input_directory = input("Enter the path to the directory to scan: ").strip()
    output_directory = input("Enter the path to the directory to save covers: ").strip()

    if os.path.isdir(input_directory):
        extract_covers_from_dir(input_directory, output_directory)
    else:
        print("Invalid input directory. Please try again.")
