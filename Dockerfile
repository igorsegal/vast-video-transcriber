FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y \
    python3 python3-pip ffmpeg rclone git \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir "av<19" faster-whisper deep-translator huggingface_hub nvidia-cublas-cu12 "nvidia-cudnn-cu12<9"

RUN python3 -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='Systran/faster-whisper-large-v3', local_dir='/app/whisper-model')"

ENV LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/cuda/lib64

WORKDIR /app
COPY process.py .

CMD ["python3", "process.py"]
