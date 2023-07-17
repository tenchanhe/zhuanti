import whisper

model = whisper.load_model("base")
result = model.transcribe("sound.wav")
print(result["text"])
