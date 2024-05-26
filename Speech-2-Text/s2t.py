import torch
from transformers import Speech2TextProcessor, Speech2TextForConditionalGeneration
import soundfile as sf
import librosa

model = Speech2TextForConditionalGeneration.from_pretrained("facebook/s2t-small-librispeech-asr")
processor = Speech2TextProcessor.from_pretrained("facebook/s2t-small-librispeech-asr")

# Load the audio file and resample to 16kHz
audio_data, _ = librosa.load('Speech-2-Text/audio.mp3', sr=16000)

# Process the audio data
inputs = processor(audio_data, sampling_rate=16_000, return_tensors="pt")

# Generate the transcription
generated_ids = model.generate(input_features=inputs["input_features"], attention_mask=inputs["attention_mask"])

# Decode the transcription
transcription = processor.batch_decode(generated_ids)

# Write the transcription to a file
with open('Speech-2-Text/textfile.txt', 'w') as outfile:
    outfile.write('\n'.join(transcription))
