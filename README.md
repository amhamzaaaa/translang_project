# 🌍 Flask Translation & Text-to-Speech App  

This project is a **Flask web application** that translates text from one language to another using **Hugging Face MarianMT models** and then converts the translated text into **speech** using **gTTS (Google Text-to-Speech)**.  

It provides both **text translation** and **audio playback/download** of the translated text.  

---

## ⚡ Features  

- 🔤 **Translate text** between different languages (English, French, German, Spanish, Hindi, Arabic, etc.)  
- 🔊 **Text-to-Speech (TTS)** for translated text using `gTTS`  
- 🌐 **Flask Web Interface** with input fields for source & target languages  
- 🎧 **Play or download audio** of translated text  
- 📦 Uses **Hugging Face Transformers** (`MarianMTModel` & `MarianTokenizer`)  

---

## 📊 Workflow  

1. User enters text, selects source language, and target language.  
2. App uses **Helsinki-NLP MarianMT model** to translate the text.  
3. Translated text is converted to **speech** using Google TTS.  
4. Webpage shows:  
   - Original text  
   - Translated text  
   - Option to listen to or download the audio.  

---

## 🛠️ Tech Stack  

- **Backend:** Python, Flask  
- **NLP Models:** Hugging Face MarianMT (`Helsinki-NLP/opus-mt-xx-yy`)  
- **Text-to-Speech:** gTTS  
- **Frontend:** HTML (Jinja2 Templates)  
