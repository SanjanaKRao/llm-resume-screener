from backend.llm_engine import generate_resume_summary
from backend.resume_parser import extract_text_from_pdf

resume = extract_text_from_pdf("data/resume1.pdf")
summary = generate_resume_summary(resume)
print(summary)
