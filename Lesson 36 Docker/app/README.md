# Setting Up and Using the Docker Image
 
## Prerequisites
Docker must be installed on your system. You can download and install Docker from the official Docker website.

## Building the Docker Image
1. Clone the repository to your local machine
2. Navigate to the project directory: 
    ```cmd
    cd your_repository
3. Build the Docker image using the provided Dockerfile:
    ```docker
    docker build -t my_image .
## Running the Docker Container

1. After building the Docker image, you can run the container using the following command:
    ``` cmd
    docker run -d -p 5000:5000 my_image
This command will start the FastAPI server inside a Docker container and map port 5000 of the container to port 5000 on your host machine.

2. Once the container is running, you can access the FastAPI server by opening your web browser and navigating to http://127.0.0.1:5000/view/


## Modeling Info
The hand landmark detection model used in this project is provided by MediaPipe. It is based on deep learning and can detect landmarks on human hands with high accuracy. The model is loaded from the `hand_landmarker.task` file and used to process input images.

## Interface Description
### Endpoints/Event Handlers:
1. **GET `/`**: Renders the main web page with "hello world"
2. **POST `/read_post_image/`**: Receives an image file uploaded by the user, processes it using the hand landmark detection model, and returns the annotated image.

### Functionality:
- **GET `/view/`**: Displays a web page with an upload form where users can select an image file to upload. Accepts an uploaded image file, processes it using the hand landmark detection model, and returns the annotated image with hand landmarks visualized.