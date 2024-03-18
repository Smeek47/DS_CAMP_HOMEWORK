import fastapi as fa
import uvicorn
import io
import os
from view import router as view_router

# ==== [ ML PART ] ====

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import cv2

MARGIN = 100  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54) # vibrant green

def draw_landmarks_on_image(rgb_image, detection_result): # This function draws landmarks on inferenced image
  hand_landmarks_list = detection_result.hand_landmarks
  handedness_list = detection_result.handedness
  annotated_image = np.copy(rgb_image)

  # Loop through the detected hands to visualize.
  for idx in range(len(hand_landmarks_list)):
    hand_landmarks = hand_landmarks_list[idx]
    handedness = handedness_list[idx]

    # Draw the hand landmarks.
    hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    hand_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
    ])
    solutions.drawing_utils.draw_landmarks(
      annotated_image,
      hand_landmarks_proto,
      solutions.hands.HAND_CONNECTIONS,
      solutions.drawing_styles.get_default_hand_landmarks_style(),
      solutions.drawing_styles.get_default_hand_connections_style())

    # Get the top left corner of the detected hand's bounding box.
    height, width, _ = annotated_image.shape
    x_coordinates = [landmark.x for landmark in hand_landmarks]
    y_coordinates = [landmark.y for landmark in hand_landmarks]
    text_x = int(min(x_coordinates) * width)
    text_y = int(min(y_coordinates) * height) - MARGIN

    # Draw handedness (left or right hand) on the image.
    cv2.putText(annotated_image, f"{handedness[0].category_name}",
                (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX,
                FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

  return annotated_image


def hand_landmark_detector(image):
  """Process image through google hand landmarks
  Input
  ------
  Image 

  Output
  ------
  Inferenced image using google hand_landmarker
  """
  base_path = os.path.dirname(__file__) 
  model_asset_path = os.path.join(base_path, "hand_landmarker.task")

  base_options = python.BaseOptions(model_asset_path=model_asset_path)
  options = vision.HandLandmarkerOptions(base_options=base_options,
                                      num_hands=2)
  detector = vision.HandLandmarker.create_from_options(options)

  mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
  detection_result = detector.detect(mp_image)
  annotated_image = draw_landmarks_on_image(image, detection_result)

  return annotated_image

# ==== =========== ====


app = fa.FastAPI()

@app.get("/")
def read_root():
  return {"hello" : "hello world"}


@app.post("/read_post_image/")
async def read_post_image(image: fa.UploadFile = fa.File(...)):
  """Inferences hand_landmarker model on the input image

  Parameters
  ----------
  image : UploadFile
      Input image file

  Returns
  -------
  StreamingResponse
      Image with plotted objects
  """
  contents = await image.read()
  nparr = np.frombuffer(contents, np.uint8)
  image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
  # === [Processing] ===
  image_processed = hand_landmark_detector(image)
  # === ============ ===
  # Convert to bytes
  _, im_buf_arr = cv2.imencode(".jpg", image_processed)
  byte_im = im_buf_arr.tobytes()

  return fa.responses.StreamingResponse(io.BytesIO(byte_im), media_type="image/jpeg")

app.include_router(view_router)
# uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
