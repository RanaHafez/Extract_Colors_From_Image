import extcolors
from flask import Flask, jsonify, render_template, request, redirect, url_for, send_from_directory
from tkinter import filedialog as fd

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/static/images/"


@app.route('/get-file')
def open_file():
    file_name = fd.askopenfilename(
        title="Choose A Message",
        initialdir='/',
        filetypes=[("Image File", '.jpg'), ("Image File", '.png')],
    )
    if file_name:
        print(file_name[file_name.rfind('/') + 1::])
        colors = open_image(file_name)
        return render_template('index.html', colors=colors, image=file_name)
    return redirect(url_for('home'))


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def open_image(img_url):
    # img_url = open_file()
    color_x = extcolors.extract_from_path(img_url, tolerance=12, limit=10)
    colors = []
    print(color_x[0])
    for i in range(len(color_x[0])):
        colors.append(f"#{rgb_to_hex(color_x[0][i][0])}")

    return colors


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
