import speech_recognition as sr
from pydub import AudioSegment
import os

# Load the audio file and convert it to the required format (WAV)

def load_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    audio = audio.set_channels(1).set_frame_rate(16000)
    return audio

def save_temp_wav(audio, temp_wav_path='temp.wav'):
    audio.export(temp_wav_path, format='wav')
    return temp_wav_path

audio = load_audio('Speech-2-Text/audio.mp3')
temp_wav_path = save_temp_wav(audio)

#  Initialize the Recognizer and Audio File

recognizer = sr.Recognizer()

def transcribe_audio(file_path):
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
        return audio_data

audio_data = transcribe_audio(temp_wav_path)


def recognize_speech_google(audio_data):
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

transcription = recognize_speech_google(audio_data)
print(transcription)