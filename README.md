# Video Transciber

For a video transcriber project, the components should be arranged in the following order to ensure a smooth workflow from video input to text transcription:

1. **Decode-Audio**
   - **Function**: Decodes the audio from the video file or audio file format to a standard format (e.g., WAV) for further processing.
   - **Interaction**: This is the first step where the audio is prepared for noise cancellation and speech recognition.

2. **Cancel-Noise-In-Audio**
   - **Function**: Reduces background noise in the decoded audio to improve the accuracy of the transcription.
   - **Interaction**: Takes the decoded audio as input and produces a cleaner audio file for the next stage.

3. **Segment-Speech**
   - **Function**: Segments the cleaned audio into manageable parts, especially useful for long audio files.
   - **Interaction**: Processes the noise-cancelled audio and segments it for efficient speech recognition.

4. **Speech-2-Text**
   - **Function**: Converts the segmented, noise-cancelled audio into text using speech recognition.
   - **Interaction**: Takes the segmented audio as input and outputs the transcribed text.

5. **Encode-Audio** (optional, if needed for re-encoding or output formatting)
   - **Function**: Re-encodes the audio if necessary for storage or further use.
   - **Interaction**: Usually applied after transcription if the audio needs to be stored in a different format or quality.

### Final Workflow Order

1. **Decode-Audio**
   - Prepares the audio from the video or any encoded audio file.
2. **Cancel-Noise-In-Audio**
   - Cleans the audio for better transcription accuracy.
3. **Segment-Speech**
   - Segments the audio for efficient processing.
4. **Speech-2-Text**
   - Transcribes the segmented audio into text.
5. **Encode-Audio** (optional)
   - Re-encodes the audio if required for specific needs.

### Visual Workflow

```
Video/Audio Input
    |
    v
Decode-Audio
    |
    v
Cancel-Noise-In-Audio
    |
    v
Segment-Speech
    |
    v
Speech-2-Text
    |
    v
Encode-Audio (optional)
    |
    v
Final Outputs: Transcribed Text (and possibly re-encoded audio)
```

This sequence ensures that each step builds upon the previous one, leading to a clear and accurate transcription of the audio extracted from the video.
