from pydub import AudioSegment
import librosa
import soundfile as sf
import os

# Function to load raw audio data
def load_raw_audio(file_path):
    audio_data, sample_rate = librosa.load(file_path, sr=None)
    return audio_data, sample_rate

# Function to save raw audio data as WAV
def save_as_wav(audio_data, sample_rate, output_path):
    sf.write(output_path, audio_data, sample_rate)

# Function to encode audio to desired format
def encode_audio(input_wav_path, output_path, format):
    audio = AudioSegment.from_wav(input_wav_path)
    audio.export(output_path, format=format)

# Load raw audio data
audio_data, sample_rate = load_raw_audio('temp.wav')

# Save as WAV (if needed)
wav_path = 'output_audio.wav'
save_as_wav(audio_data, sample_rate, wav_path)

# Encode to MP3
encode_audio(wav_path, 'output_audio.mp3', 'mp3')

# Encode to AAC
encode_audio(wav_path, 'output_audio.aac', 'adts')

# Encode to FLAC
encode_audio(wav_path, 'output_audio.flac', 'flac')

# Encode to OGG
encode_audio(wav_path, 'output_audio.ogg', 'ogg')
