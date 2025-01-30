# Whisper API

Whisper API is a FastAPI-based application for transcribing audio files using OpenAI Whisper.

## Features
- Supports multiple audio formats: `.wav`, `.mp3`, `.m4a`, `.flac`, `.ogg`
- Uses OpenAI's Whisper model for transcription
- Provides a RESTful API for uploading and processing audio files
- Dockerized for easy deployment

## Installation

### Prerequisites
- Docker
- Docker compose

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/mfenerich/fastapi-whisper.git
   cd whisper-api
   ```

2. Create a virtual environment and activate it:
   ```sh
   docker compose up
   ```

## Usage

### API Endpoints

| Method | Endpoint            | Description                   |
|--------|---------------------|-------------------------------|
| `GET`  | `/`                 | Health check                  |
| `POST` | `/v1/transcribe/`   | Upload an audio file for transcription |

### Example API Call

Api docs: `http://0.0.0.0:8000/doc`

Using `curl`:
```sh
curl -X 'POST' \
  'http://0.0.0.0:8000/v1/transcribe/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@recorded_audio.flac;type=audio/flac'
```

## License
MIT License. See [LICENSE](LICENSE) for details.