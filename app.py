import os
import openai
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_prompt = request.form["prompt"]
        number_of_images = int(request.form["num_images"])
        openai.api_key = os.getenv("OPENAI_API_KEY")

        response = openai.Image.create(
            prompt=f"{user_prompt}",
            n=number_of_images,
            size="512x512"
        )

        return render_template("gallery.html", images=response["data"])

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
