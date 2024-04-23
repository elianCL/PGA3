from flask import Flask, render_template, redirect, url_for, Response
from PIL import Image, ImageDraw
import io
import random

app = Flask(__name__)

IMAGE_WIDTH = 300
IMAGE_HEIGHT = 300
PIXEL_SIZE = 20

def generate_random_image():
    image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), color='white')
    draw = ImageDraw.Draw(image)

    for x in range(0, IMAGE_WIDTH, PIXEL_SIZE):
        for y in range(0, IMAGE_HEIGHT, PIXEL_SIZE):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            draw.rectangle([x, y, x + PIXEL_SIZE, y + PIXEL_SIZE], fill=color)

    return image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random_image')
def random_image():
    image = generate_random_image()
    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return Response(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
