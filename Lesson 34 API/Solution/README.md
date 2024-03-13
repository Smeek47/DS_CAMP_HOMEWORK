# Hand Landmark Detection with FastAPI and MediaPipe

## Overview
This project demonstrates real-time hand landmark detection using the MediaPipe library integrated with FastAPI. It allows users to upload an image containing 2 hands, and the application will infer and visualize the hand landmarks on the image. The web interface is built using HTML templates served by FastAPI.

## Deployment Info
The application is designed to be deployed as a web service. It can be deployed on any platform that supports Python web applications

## Installation Instruction
1. Clone this repository to your local machine
2. To run project, i used python==3.9.18
( if your file `hand_landmarker.task` is damaged, or you want to update it use 
`!wget -q https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task` )
3. Install the required dependencies using pip:
pip install -r requirements.txt
4. Run the FastAPI server:
uvicorn app:app --reload


## Requirements.txt
The `requirements.txt` file lists all the Python dependencies required to run the application. Make sure to install these dependencies using `pip install -r requirements.txt` before running the application.

## Modeling Info
The hand landmark detection model used in this project is provided by MediaPipe. It is based on deep learning and can detect landmarks on human hands with high accuracy. The model is loaded from the `hand_landmarker.task` file and used to process input images.

## Interface Description
### Endpoints/Event Handlers:
1. **GET `/`**: Renders the main web page with "hello world"
2. **POST `/read_post_image/`**: Receives an image file uploaded by the user, processes it using the hand landmark detection model, and returns the annotated image.

### Functionality:
- **GET `/view/`**: Displays a web page with an upload form where users can select an image file to upload. Accepts an uploaded image file, processes it using the hand landmark detection model, and returns the annotated image with hand landmarks visualized.
