# Driver-Vigilance-System
An intelligent system that tracks driver alertness and provides timely warnings to prevent accidents caused by drowsiness or distraction.

Features

Real-Time Monitoring: Tracks driver behavior using video input.
Fatigue Detection: Identifies signs of drowsiness such as prolonged eye closure and yawning.
Distraction Analysis: Detects head movements or gaze deviation from the road.
Alert System: Issues audio or visual alerts to keep the driver focused.
Lightweight & Efficient: Optimized for deployment on personal vehicles or fleet systems.

Technologies Used

Programming Language: Python 3.12+
Deep Learning: TensorFlow/Keras for model development.
Computer Vision: OpenCV for real-time face and eye detection.
Pre-Trained Models: CNN for feature extraction and classification.
Hardware: Compatible with standard webcam or dashboard cameras.

Driver-Vigilance-System/

├── model.h5                # Pre-trained Keras model
├── Detector.py             # Google Colab Notebook
├── app.py                  # Main application script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation


Setup Instructions

1. Clone the Repository

git clone https://github.com/Thenameiskaran/Driver-Vigilance-System.git

cd Driver-Vigilance-System

2. Install Dependencies

pip install -r requirements.txt

3. Run the Application

python app.py


