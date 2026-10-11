
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    image_url = ""

    if request.method == "POST":
        image_url = request.form.get("image_url", "").strip()

        if not image_url.startswith(("http://", "https://")):
            image_url = ""

    return render_template("index.html", image_url=image_url)


if __name__ == "__main__":
    app.run(debug=True)
