from flask import Flask, render_template, request, send_file
from transformers import MarianMTModel, MarianTokenizer
from gtts import gTTS
import os

# model_pairs = {
#     ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
#     ("en", "de"): "Helsinki-NLP/opus-mt-en-de",
#     ("en", "es"): "Helsinki-NLP/opus-mt-en-es",
#     ("en", "hi"): "Helsinki-NLP/opus-mt-en-hi",
#     ("en", "ar"): "Helsinki-NLP/opus-mt-en-ar"
# }

# os.makedirs("models", exist_ok=True)

# for (src, tgt), model_name in model_pairs.items():
#     save_dir = f"models/{src}-{tgt}"
#     if not os.path.exists(save_dir):
#         print(f"Downloading {model_name} to {save_dir}...")
#         tokenizer = MarianTokenizer.from_pretrained(model_name)
#         model = MarianMTModel.from_pretrained(model_name)
#         tokenizer.save_pretrained(save_dir)
#         model.save_pretrained(save_dir)


def translate_text(text, src_lang, tgt_lang):
    model_dir = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'

    tokenizer = MarianTokenizer.from_pretrained(model_dir)
    model = MarianMTModel.from_pretrained(model_dir)

    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs, use_cache=True)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    
    return translated_text


def text_to_speech(text, lang_code, output_path="output.mp3"):
    tts = gTTS(text=text, lang=lang_code)
    tts.save(output_path)
    return output_path

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['text']
        src_lang = request.form['src_lang']
        tgt_lang = request.form['tgt_lang']

        translated_text = translate_text(input_text, src_lang, tgt_lang)
        audio_file = text_to_speech(translated_text, tgt_lang)

        return render_template('index.html',
                       translated=translated_text,
                       input_text=input_text,
                       selected_src=src_lang,
                       selected_tgt=tgt_lang)


    return render_template('index.html')

@app.route('/audio')
def audio():
    return send_file("output.mp3", mimetype="audio/mpeg")

if __name__ == '__main__':
    app.run(debug=True)