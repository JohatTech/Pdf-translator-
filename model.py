from transformers import AutoTokenizer, T5ForConditionalGeneration
import torch

# Cargar el modelo y el tokenizador
pdf_path = "test.pdf"
tokenizer = AutoTokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")
