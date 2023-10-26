# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.api_key = "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"

audio_file= open("C://STAGE-POC//IAGORA-API//videos//audio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript)