from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model="t5-small")

def summarize_text(text):
    if len(text) > 1000:
        text = text[:1000]
    summary = summarizer_pipeline(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']
