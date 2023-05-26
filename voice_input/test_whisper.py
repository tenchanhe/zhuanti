import whisper

model = whisper.load_model("base")
result = model.transcribe("oxxostudio.wav")
print(result["text"])