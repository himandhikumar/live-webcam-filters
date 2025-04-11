# Webcam Filters Application 🎥✨

A real-time webcam filter application built with Python and OpenCV. Apply various fun filters to your webcam feed with simple keyboard controls!



## Features 🎨

- **Multiple Filters**: Choose from 7 different visual effects
- **Real-time Processing**: Smooth performance with FPS counter
- **Face Detection**: Built-in face detection with rectangle overlay
- **Simple Controls**: Change filters with single key presses
- **Lightweight**: Runs on most systems with just a webcam

## Available Filters 🌈

| Filter       | Key | Description                          |
|--------------|-----|--------------------------------------|
| Normal       | n   | Original webcam feed                 |
| Grayscale    | g   | Classic black and white effect       |
| Blur         | b   | Soft Gaussian blur                   |
| Edge Detect  | e   | Artistic edge detection              |
| Cartoonify   | c   | Fun cartoon-style effect             |
| Sepia        | s   | Vintage brown-toned filter           |
| Face Detect  | f   | Highlights detected faces            |

## Installation ⚙️

1. **Prerequisites**:
   - Python 3.6+
   - OpenCV (`pip install opencv-python`)
   - OpenCV Haar Cascade data (included in OpenCV)

2. **Run the application**:
   ```bash
   git clone https://github.com/yourusername/live-webcam-filters.git
   cd webcam-filters
   python live_webcam_filters.py

**Usage 🚀**

1. Run the script
2. View the control legend in the console
3. Press corresponding keys to switch filters
4. Press 'q' to quit the application


**Technical Details 🔧**

1. Uses OpenCV's Haar Cascade classifier for face detection
2. Implements various computer vision techniques:
3. Color space transformations
4. Edge detection (Canny)
5. Adaptive thresholding
6. Image filtering (Gaussian, bilateral)
7. Color matrix transformations


**Future Enhancements 🔮**

1. Add more filter options
2. Implement filter combinations
3. Add screenshot functionality
4. Create GUI controls
5. Add video recording option

**Contributing 🤝**

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

**License 📄**

MIT License - Feel free to use and modify!
