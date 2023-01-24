import whisper

model = whisper.load_model("tiny")
result = model.transcribe("example.mp3")
print(result["text"])