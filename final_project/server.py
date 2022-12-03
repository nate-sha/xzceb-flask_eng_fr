from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    """Translate English to French"""
    textToTranslate = request.args.get('textToTranslate')
    frenchToEnglish = translator.english_to_french(textToTranslate)
    return frenchToEnglish


@app.route("/frenchToEnglish")
def frenchToEnglish():
    """Translate French to English"""
    textToTranslate = request.args.get('textToTranslate')
    englishText = translator.french_to_english(textToTranslate)
    return englishText


@app.route("/")
def renderIndexPage():
    # Render the index.html page
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
