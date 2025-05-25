from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_id = "tiiuae/falcon-rw-1b"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Setup text generation pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_resume_summary(resume_text):
    prompt = f"Summarize this resume for a software engineering role:\n{resume_text}\nSummary:"
    output = generator(prompt, max_length=256, do_sample=True, temperature=0.7)
    return output[0]["generated_text"].strip()
