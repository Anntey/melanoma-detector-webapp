from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from models.models import EfficientNetB0, augs_test
from dotenv import load_dotenv
import numpy as np
import os
import torch
import imageio
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app)

# Some helper functions for /predict
def load_img(request):
    img = request.files['img']
    img = imageio.imread(img, pilmode = "RGB")
    img = np.array(img)
    img = augs_test(img) # also converts to torch.tensor
    img = img.unsqueeze(0) # add batch dim
    return img

def load_model():
    device = torch.device('cpu')
    model = torch.load('./models/model.pth', map_location = device)
    model.to(device)
    return model

def get_prediction(img):
    model.eval()
    with torch.no_grad():
        output = model(img)
        pred = torch.sigmoid(output)
        pred = pred.numpy()
    return pred

@app.route('/ping')
def ping():
    print('Someone is pingin')
    return 'pong'

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        img = load_img(request)
        pred = get_prediction(img)
        return jsonify(prediction = str(float(pred)))

if __name__ == '__main__':
    print('Loading model...')
    global model
    model = load_model()
    if(isinstance(model, torch.nn.Module)):
        print('...Successful')
    else:
        print('...Failed')
    load_dotenv()
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    debug = os.getenv('HOST') == 'development'
    print(f'Starting backend at {host}:{port}')
    app.run(host, port = port, debug = debug)