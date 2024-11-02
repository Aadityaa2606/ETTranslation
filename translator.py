import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model and tokenizer once when the module is imported
checkpoint = "suriya7/English-to-Tamil"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

def language_translator(text):
    """
    Translates the input text from English to Tamil.
    
    Args:
        text (str): The text to translate.

    Returns:
        str: The translated text in Tamil.
    """
    # Tokenize the input text
    tokenized = tokenizer([text], return_tensors='pt')

    # Generate the translation
    with torch.no_grad():  # Disable gradient calculation
        out = model.generate(**tokenized, max_length=128)

    # Decode the generated output to get the translated text
    return tokenizer.decode(out[0], skip_special_tokens=True)
