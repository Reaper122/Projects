import wave
import numpy as np
import librosa
import webrtcvad
from pydub import AudioSegment
from scipy.io import wavfile
from pyAudioAnalysis import audioSegmentation as aS

# Load the audio file and convert it to the required format
def load_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    audio = audio.set_channels(1).set_frame_rate(16000)
    return audio

audio = load_audio('audio.mp3')


# Use WebRTC VAD to detect speech segments
def apply_vad(audio, aggressiveness=3):
    vad = webrtcvad.Vad(aggressiveness)
    sample_rate = audio.frame_rate
    frame_duration = 30  # ms
    frames = frame_generator(frame_duration, audio.raw_data, sample_rate)
    segments = vad_collector(sample_rate, frame_duration, 300, vad, frames)
    return segments

def frame_generator(frame_duration, audio, sample_rate):
    n = int(sample_rate * (frame_duration / 1000.0) * 2)
    offset = 0
    while offset + n < len(audio):
        yield audio[offset:offset + n]
        offset += n

def vad_collector(sample_rate, frame_duration, padding_duration, vad, frames):
    num_padding_frames = int(padding_duration / frame_duration)
    ring_buffer = collections.deque(maxlen=num_padding_frames)
    triggered = False
    voiced_frames = []
    segments = []
    for frame in frames:
        is_speech = vad.is_speech(frame, sample_rate)
        if not triggered:
            ring_buffer.append((frame, is_speech))
            num_voiced = len([f for f, speech in ring_buffer if speech])
            if num_voiced > 0.9 * ring_buffer.maxlen:
                triggered = True
                segments.extend([f for f, s in ring_buffer])
                ring_buffer.clear()
        else:
            segments.append(frame)
            ring_buffer.append((frame, is_speech))
            num_unvoiced = len([f for f, speech in ring_buffer if not speech])
            if num_unvoiced > 0.9 * ring_buffer.maxlen:
                triggered = False
                segments.append(None)
                ring_buffer.clear()
    if triggered:
        segments.append(None)
    return segments

segments = apply_vad(audio)

# Convert segments back to audio format and save them
def save_segments(segments, output_dir):
    segment_audio = b''
    segment_counter = 0
    for segment in segments:
        if segment is None:
            if segment_audio:
                save_path = f"{output_dir}/segment_{segment_counter}.wav"
                segment = AudioSegment(
                    segment_audio, frame_rate=16000, sample_width=2, channels=1)
                segment.export(save_path, format="wav")
                segment_audio = b''
                segment_counter += 1
        else:
            segment_audio += segment
    if segment_audio:
        save_path = f"{output_dir}/segment_{segment_counter}.wav"
        segment = AudioSegment(
            segment_audio, frame_rate=16000, sample_width=2, channels=1)
        segment.export(save_path, format="wav")

save_segments(segments, 'output_segments_directory')



