from fastapi import APIRouter, UploadFile, File, HTTPException
from app.core.whisper_service import transcribe_audio

router = APIRouter()

@router.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    if not file.filename.endswith((".wav", ".mp3", ".m4a", ".flac", ".ogg")):
        raise HTTPException(status_code=400, detail="Unsupported audio format.")

    try:
        audio_bytes = await file.read()
        text = transcribe_audio(audio_bytes)
        return {"transcription": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing audio: {str(e)}")