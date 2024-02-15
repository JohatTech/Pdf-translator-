import nltk 
import fitz
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import textwrap
nltk.download('punkt')

from model import *

def read_file(file_path):
    doc = fitz.open(file_path)
    for page in doc:
        input_text = page.get_text()
    return input_text

def split_text(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

def translate(input_text):
    
    chunks = split_text(input_text)
    translate_chunk = []
    for chunk in chunks:    
        input_id = tokenizer("translate English to German:" + chunk, return_tensors = "pt").input_ids
        outputs = model.generate(input_id, max_length = 100)
        translate_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        translate_chunk.append(translate_text)
        final_translate_text = " ".join(translate_chunk)
    return final_translate_text


text = read_file(pdf_path)
result = translate(text)

print("German: "+ result)

def create_pdf(file_path, text):
    # Tamaño de la página
    width, height = letter

    # Margen
    margin = 50

    # Crear el archivo PDF
    c = canvas.Canvas(file_path, pagesize=letter)
    c.setFont("Helvetica", 12)

    # Ajustar el texto entre renglones
    wrapped_text = textwrap.fill(text, width=70)

    # Configurar la posición inicial
    x, y = margin, height - margin

    # Escribir el texto en el PDF
    for line in wrapped_text.split('\n'):
        c.drawString(x, y, line)
        y -= 15  # Espacio entre renglones

    # Guardar el PDF
    c.save()


# Ruta del archivo PDF de salida
pdf_output_path = "output.pdf"

# Crear el PDF con el texto ajustado entre renglones
create_pdf(pdf_output_path, result)

print(f"El archivo PDF se ha creado exitosamente en: {pdf_output_path}")