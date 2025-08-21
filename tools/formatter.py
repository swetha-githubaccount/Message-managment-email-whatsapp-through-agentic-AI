from transformers import pipeline

llm_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def format_text_local(raw_message: str, mode: str = "email"):
    
    if mode == "email":
        prompt = f"Rewrite the following into a formal professional email:\n\n{raw_message}\n\nEmail:"
    else:
        prompt = f"Rewrite the following into a polite WhatsApp message:\n\n{raw_message}\n\nMessage:"

    output = llm_pipeline(prompt, max_length=150, num_return_sequences=1)
    
    text = output[0]["generated_text"]
    return text.replace(prompt, "").strip()