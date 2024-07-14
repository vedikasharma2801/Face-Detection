# Face Detection

This project demonstrates a real-time face detection system using OpenCV. The system captures video from the webcam, detects faces using a Haar Cascade classifier, and draws rectangles around the detected faces.

## Features

- Real-time face detection using Haar Cascade classifier.
- Displays rectangles around detected faces.
- Handles errors for missing Haar Cascade file and webcam initialization.

## Requirements

- Python 3.x
- OpenCV

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/vedikasharma2801/face-detection.git
    cd face-detection
    ```

2. Install the required dependencies:

    ```bash
    pip install opencv-python
    ```

## Usage

1. Run the script:

    ```bash
    python face_detection.py
    ```

2. The script will start capturing video from the default webcam. It will detect faces and draw rectangles around them.

3. Press the 'q' key to stop the script and close all windows.
