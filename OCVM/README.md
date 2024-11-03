# Real-Time Object and Hand Detection with Flask

This project demonstrates a real-time object detection and hand tracking application using Flask, TensorFlow, MediaPipe, and OpenCV. It captures video from the webcam, performs object detection and hand tracking, and streams the video with the detected objects and hand landmarks over a web interface.

## Features

- **Object Detection**: Uses TensorFlow's SSD MobileNet v2 model to detect various objects from a pre-defined category list.
- **Hand Tracking**: Uses MediaPipe to track hand landmarks in real-time.
- **Web Interface**: Provides a web interface to view the video stream with annotations for detected objects and hand landmarks.

## Prerequisites

- Python 3.6 or higher
- Flask
- OpenCV
- TensorFlow
- MediaPipe
- NumPy

## Installation

1. **Create a Virtual Environment (Optional but recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install the Required Packages**:

    ```bash
    pip install Flask opencv-python tensorflow mediapipe numpy
    ```

3. **Download the Pre-trained Model**:

    Ensure you have the SSD MobileNet v2 model. Place the `ssd_mobilenet_v2/saved_model` directory in the same location as this script.

## Usage

1. **Run the Flask Application**:

    ```bash
    python app.py
    ```

2. **Access the Application**:

    Open a web browser and navigate to `http://127.0.0.1:5000/` to view the video stream.

## Code Overview

- **app.py**: Contains the Flask application and video processing logic.
  - `generate_frames()`: Captures video from the webcam, performs object detection and hand tracking, and yields frames for streaming.
  - `index()`: Renders the main page with the video stream.
  - `video_feed()`: Streams the processed video feed.

- **index.html**: (Should be placed in the `templates` directory)
  - Basic HTML to display the video feed from the `/video_feed` endpoint.

## Troubleshooting

- **Webcam Access**: Ensure that your webcam is properly connected and accessible.
- **Model Loading Issues**: Verify that the model path is correct and the model files are present.
- **Dependencies**: Make sure all required packages are installed.

## Acknowledgements

- TensorFlow
- MediaPipe
- OpenCV
- Flask

Feel free to contribute to the project by submitting issues or pull requests.


