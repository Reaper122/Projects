from pydub import AudioSegment
import librosa
import soundfile as sf
import os


# Use pydub to load and decode audio files
def load_audio(file_path):
    # Load audio file using pydub
    audio = AudioSegment.from_file(file_path)
    return audio

audio = load_audio(r'audio.mp3')


# Convert the loaded audio into raw audio data
def convert_to_wav(audio, output_path):
    # Export the audio to WAV format
    audio.export(output_path, format='wav')

output_wav_path = 'output_audio.wav'
convert_to_wav(audio, output_wav_path)


# Use librosa or soundfile to load the WAV file for further processing
def load_raw_audio(file_path):
    # Load raw audio data using librosa
    audio_data, sample_rate = librosa.load(file_path, sr=None)
    return audio_data, sample_rate

audio_data, sample_rate = load_raw_audio(output_wav_path)


print(f'Sample Rate: {sample_rate}')
print(f'Audio Data: {audio_data[:10]}')