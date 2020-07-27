<h1 align="center">Melanoma Detector Web App</h1>
<p align="center"><img src="/images/melanoma-app.png" alt="image" /></p>

## Backend
RESTful API made with Flask that serves a PyTorch model at http://localhost:8000/predict. Given an input image, it predicts the probability the lesion is malignant.

## Frontend
A minimal React frontend at http://localhost:3000 that makes POST requests to the backend when the input image changes.

## How to run?
The following commands build and start the application:
```bash
$ git clone https://github.com/Anntey/melanoma-detector-webapp.git
$ cd melanoma-detector-webapp
$ docker-compose up
```
You can find examples of input images in `/images`
