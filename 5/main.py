from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from nltk.tokenize import word_tokenize  # for token counting

app = FastAPI()

class TextRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    summary: str

class TokenCountResponse(BaseModel):
    token_count: int

@app.post("/summarize/", response_model=SummaryResponse)
def summarize_text(text_request: TextRequest):
    # Perform summarization logic (example: truncate to less than 100 words)
    summary = " ".join(text_request.text.split()[:100])
    return {"summary": summary}

@app.post("/token-count/", response_model=TokenCountResponse)
def count_tokens(text_request: TextRequest):
    # Perform token count using NLTK
    tokens = word_tokenize(text_request.text)
    token_count = len(tokens)
    return {"token_count": token_count}
