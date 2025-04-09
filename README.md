# STT-TTS-Audio-Transcription 🎙️🔄📝

This project demonstrates **Speech-to-Text (STT)** and **Text-to-Speech (TTS)** conversion capabilities using Python. 
Uses **pyttsx3**, **speech_recognition**, **win32com.client**, and **recognize_google** to transcribe live or recorded audio into text and vice versa.

---

## 🔧 Technologies Used

- **Python** 
- **speech_recognition**: For speech-to-text conversion  
- **pyttsx3**: Text-to-speech engine (offline)  
- **win32com.client** of **pywin32**
- **recognize_google**: Google’s speech recognition 

---

## 📂 Project Structure

### 1. `speech-to-text.py`
- Converts **live microphone input** into text.
- Saves recognized text to `text.txt`.
- Stops recording and exits when the user says `"code"`.

### 2. `audio_file-to-text.py`
- Extracts speech from a **Audio file** and converts it to text.
- Saves the output to `file_audio.txt`.

### 3. `text-to-speech_female.py`
- Converts typed text to speech using **female voice** via `pyttsx3`.
- Runs interactively until the user types `"bye"`.

### 4. `text-to-speech_male.py`
- Uses **Windows Speech** to convert text to speech in a **male voice**.
- Runs in a loop until `"bye"` is entered.

---

## ✅ Use Cases

- 🧠 Voice command logging and dictation systems  
- 🔁 Bi-directional audio processing tools  
- 📝 Automated transcription services  
- 💬 Voice-enabled interfaces  

---

## ⚠️ Notes

- The `speech_recognition` module requires internet access.  
- `win32com.client` works only on **Windows** system.  
- Ensure you have a **microphone** and optionally a **WAV file** for testing.

---
