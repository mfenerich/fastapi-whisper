FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg curl build-essential git \
    && rm -rf /var/lib/apt/lists/*

# Properly install Rust and configure PATH
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc \
    && export PATH="$HOME/.cargo/bin:$PATH"

# Copy dependencies and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ensure Whisper is up to date
RUN pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

# Download the model to avoid downloading it at each execution
RUN python -c "import whisper; whisper.load_model('base')"

# Copy the project code into the container
COPY . .  

# Expose the API port
EXPOSE 8000

# Command to run FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
