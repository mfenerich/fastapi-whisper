import whisper
import tempfile

# Load the model once to avoid overhead
model = whisper.load_model("base")

def transcribe_audio(audio_bytes: bytes) -> str:
    """ Transcribes audio using OpenAI Whisper. """
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as tmp:
        tmp.write(audio_bytes)
        tmp.flush()
        result = model.transcribe(tmp.name)
    return result["text"]