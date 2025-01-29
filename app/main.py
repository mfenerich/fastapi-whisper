from fastapi import FastAPI
from app.api.transcribe import router as transcribe_router

app = FastAPI(title="Whisper API", description="API for audio transcription using OpenAI Whisper")

# Register transcription route
app.include_router(transcribe_router, prefix="/v1", tags=["Transcription"])

@app.get("/")
def health_check():
    return {"status": "ok"}
