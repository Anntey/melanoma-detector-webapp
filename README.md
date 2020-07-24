<h1 align="center">Melanoma Detector Web App</h1>
<p align="center"><img src="melanoma-app.png" alt="image" /></p>

## Backend
RESTful API made with Flask serves a PyTorch model at http://localhost:8000/predict. Given an input image, it predicts the probability the lesion is malignant.

## Frontend
A minimal React frontend at http://localhost:3000 that makes POST requests to the backend when the input image changes.

## Install
The following command builds and start the app:
```
docker-compose up
```
