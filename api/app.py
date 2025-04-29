from flask import Flask, render_template_string, request
import random
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

def generate_otp(length=6):
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

@app.route('/', methods=['GET'])
def index():
    return render_template_string(open(os.path.join(app.template_folder, 'index.html')).read(), otp=None)

@app.route('/generate', methods=['POST'])
def generate():
    otp = generate_otp()
    return render_template_string(open(os.path.join(app.template_folder, 'index.html')).read(), otp=otp)

def handler(request):
    return app(request.environ, start_response=lambda *args: None)
