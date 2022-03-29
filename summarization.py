import transformers
from transformers import pipeline


#dream="dream.txt"
# transcript="transcript1234.txt"
def sum_text(MyText):
    summarizer = pipeline("summarization")
    summarized = summarizer(MyText, min_length=8, max_length=10)
    return summarized[0]["summary_text"]


