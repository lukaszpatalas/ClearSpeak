import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        text = request.form["text"]
        prompt = generate_prompt(text)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        generated_text = response["choices"][0]["message"]["content"]
        generated_text = generated_text.strip()
        return redirect(url_for("index", result=generated_text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(text):
    return f"""Please rephrase the following text in a way that is clear, balanced, and understandable by a non-technical audience with a touch of creativity:

{text}""".format(
        text
    )
