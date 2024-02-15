from transformers import pipeline
import re 
from pypdf import PdfReader

pipe = pipeline(model= "t5-small")

pdf_path = "/home/johattech/pdf-translator/test.pdf"
pdf_reader = PdfReader(pdf_path)
firt_page = pdf_reader.pages[0]
input_text = firt_page.extract_text()