import os
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "image")
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

def get_image_files():
    os.makedirs(IMAGE_DIR, exist_ok=True)
    return sorted(name for name in os.listdir(IMAGE_DIR)
                  if os.path.isfile(os.path.join(IMAGE_DIR, name))
                  and os.path.splitext(name)[1].lower() in EXTENSIONS)

@app.route("/image/<path:filename>")
def show_image(filename):
    if filename not in get_image_files():
        return "Картинка не найдена", 404
    return send_from_directory(IMAGE_DIR, filename)

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = image_name = top_text = bottom_text = ""
    images = get_image_files()
    if request.method == "POST":
        image_url = request.form.get("image_url", "").strip()
        image_name = request.form.get("image_name", "").strip()
        top_text = request.form.get("top_text", "")
        bottom_text = request.form.get("bottom_text", "")
        if not image_url.startswith(("http://", "https://")):
            image_url = ""
        if image_name not in images:
            image_name = ""
        if image_url:
            image_name = ""
    return render_template("index.html", image_url=image_url, image_name=image_name,
                           image_list=images, top_text=top_text, bottom_text=bottom_text)

if __name__ == "__main__":
    app.run(debug=True)
