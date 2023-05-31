#%%capture
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from threading import Lock
from werkzeug.utils import secure_filename
import time

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, allow_headers='Content-Type')
queue = []
gate_open = False
lock = Lock()


# Server requests prompt
@app.route("/prompt")
def get_prompt():
    global queue
    try:
        lock.acquire()
        if len(queue) > 0:
            prompt = queue[0]
            queue.pop(0)
            return prompt
        else: return "[NONE]"
    finally:
        lock.release()


# Server sends images
@app.route("/gen_images", methods=["POST"])
def receive_images():
    global gate_open
    images = request.files.getlist('image')
    for image in images:
        filename = secure_filename(image.filename)
        image.save(filename)
    lock.acquire()
    gate_open = True
    lock.release()
    return "[DONE]"


# Client get html
@app.route("/")
def home():
    return send_file("./site.html")

# Client sends prompt
@app.route('/send_prompt', methods=['POST'])
def process_request():
    global queue
    global gate_open
    data = request.get_json()
    prompt = data['text']
    print("[PROMPT]", prompt)
    
    lock.acquire()
    queue.append(prompt)
    
    while not gate_open:
        lock.release()
        time.sleep(1)
        lock.acquire()
    gate_open = False
    lock.release()

    response = {'images': ["image_1.png", "image_2.png", "image_3.png"]}
    
    return jsonify(response)


# Client request images
@app.route('/images/<path:image_name>')
def serve_image(image_name):
    image_path = f'./{image_name}'
    return send_file(image_path, mimetype='image/png')


@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    response.headers.add('Access-Control-Expose-Headers', '*')
    return response

app.run(host="0.0.0.0", port=8080)