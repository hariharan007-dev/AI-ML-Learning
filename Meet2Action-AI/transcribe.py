import whisper

model = whisper.load_model("base")

audio_file = input("Enter audio file name: ")

result = model.transcribe(audio_file)

print("\nTRANSCRIPT:")
print(result["text"])
  