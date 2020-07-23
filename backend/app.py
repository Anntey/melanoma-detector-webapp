from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from models.models import EfficientNetB0, augs_test
import numpy as np
import torch
import imageio
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app)

@app.route('/ping')
def ping():
    print('Someone is pingin')
    return 'pong'

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        # load img
        img = request.files['img']
        img = imageio.imread(img, pilmode = "RGB")
        img = np.array(img)
        img = augs_test(img) # converts to torch.tensor
        img = img.unsqueeze(0) # add batch dim
        # load model
        device = torch.device('cpu')
        model = torch.load('./models/model.pth', map_location = device)
        model.to(device)     
        # predict
        model.eval()
        with torch.no_grad():
            outputs = model(img)
            pred = torch.sigmoid(outputs)
            pred = pred.numpy()
        # format response
        pred = str(float(pred))
        response = jsonify(prediction = pred)
        return response

if __name__ == '__main__':
    app.run('0.0.0.0', port = 8000, debug = True)