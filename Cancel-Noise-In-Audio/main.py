import librosa
import noisereduce as nr
import soundfile as sf
import numpy as np
from scipy.signal import butter, lfilter


# Load the audio file and read the audio data
def load_audio(file_path):
    audio_data, sample_rate = librosa.load(file_path, sr=None)
    return audio_data, sample_rate

audio_data, sample_rate = load_audio('temp.wav')


# Using the noisereduce library to reduce noise in the audio signal
def reduce_noise(audio_data, sample_rate):
    # Perform noise reduction
    reduced_noise = nr.reduce_noise(y=audio_data, sr=sample_rate)
    return reduced_noise

reduced_noise = reduce_noise(audio_data, sample_rate)


# Save the noise-canceled audio to a new file
def save_audio(audio_data, sample_rate, output_path):
    sf.write(output_path, audio_data, sample_rate)

save_audio(reduced_noise, sample_rate, 'output_noise_reduced.wav')