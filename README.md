# Driver Drowsiness Detection System

## Overview
The Driver Drowsiness Detection System is a Python-based project that uses computer vision and deep learning to detect drowsiness in drivers. It continuously monitors the driver's facial features through a webcam, analyzes the state of the eyes using a Convolutional Neural Network (CNN), and triggers an alarm if signs of drowsiness are detected.

---

## Features
- Real-time face and eye detection using OpenCV and Haar cascades.
- Eye state prediction (open/closed) using a pre-trained CNN model (`cnncat2.h5`).
- Drowsiness detection based on a scoring system.
- Alarm system to alert the driver when drowsiness is detected.
- Visual feedback with bounding boxes and status display.

---

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  - OpenCV
  - NumPy
  - Keras
  - Pygame

Install the libraries using the following command:
```bash
pip install opencv-python numpy keras pygame
```

---

## Project Structure
```
.
├── drowsiness_detection.py    # Main script for detecting drowsiness
├── models
│   └── cnncat2.h5             # Pre-trained CNN model
├── haar cascade files
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_lefteye_2splits.xml
│   └── haarcascade_righteye_2splits.xml
├── alarm.wav                  # Alarm sound file
└── README.md                  # Project documentation
```

---

## How It Works
1. **Face and Eye Detection**:
   - The system uses Haar cascade classifiers to detect the face, left eye, and right eye from the video feed.

2. **Eye State Prediction**:
   - Captured eye regions are preprocessed and passed to the CNN model (`cnncat2.h5`) to predict if the eyes are open or closed.

3. **Drowsiness Scoring**:
   - A scoring mechanism tracks the driver's alertness:
     - Score increases if both eyes are detected as closed.
     - Score decreases if eyes are detected as open.
   - If the score exceeds a predefined threshold, the system triggers an alarm.

4. **Visual Feedback**:
   - The system displays a bounding box around the face and eyes with the current status (`Open` or `Closed`) and the drowsiness score.

---

## Usage
1. Clone the repository or download the project files.
2. Place the pre-trained CNN model (`cnncat2.h5`), Haar cascade XML files, and `alarm.wav` in the appropriate directories.
3. Run the script:
   ```bash
   python drowsiness_detection.py
   ```
4. The webcam feed will open, and the system will start monitoring for drowsiness.
5. Press `q` to exit the application.

---

## Customization
- **Threshold for Drowsiness Alert**:
  - Modify the `score > 15` condition in the script to adjust sensitivity.

- **Alarm Sound**:
  - Replace `alarm.wav` with any other sound file for the alert.

---

## Limitations
- Works best under good lighting conditions.
- Requires the driver's face and eyes to be visible to the camera.
- Performance may vary with different individuals or camera quality.

---

## Future Improvements
- Integrate advanced deep learning models for improved accuracy.
- Add support for detecting head posture and yawning.
- Develop a mobile or embedded hardware version for real-world deployment.

---

## License
This project is open-source and available for educational and research purposes.
