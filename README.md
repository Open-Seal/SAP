# ASCII Cam — Real-Time ASCII Art

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![OpenCV](https://img.shields.io/badge/OpenCV-ASCII--Cam-orange)



![Preview](https://raw.githubusercontent.com/Open-Seal/SAP/refs/heads/main/ascii.png)


Overview
This Python script transforms live webcam video into an ASCII art representation in real-time using OpenCV. It captures frames from a webcam, converts them to grayscale, maps pixel intensities to ASCII characters, and renders the result as a colored or monochrome ASCII image. The script supports interactive controls to adjust resolution, toggle colorization, invert intensity, switch ASCII character sets, and save frames as PNG images.
Features

Real-time ASCII Art: Converts webcam video feed into ASCII art displayed in a window.
Customizable Resolution: Adjusts the ASCII image resolution dynamically using keyboard controls.
Color Support: Option to render ASCII characters in colors matching the original image or in monochrome.
Invert Mode: Toggle between mapping light pixels to dense or sparse ASCII characters.
Multiple ASCII Sets: Switch between a detailed or simple ASCII character set for rendering.
Frame Saving: Save the current ASCII frame as a PNG file.
Interactive Controls: Keyboard inputs to modify settings during runtime.

Requirements

Python 3.x
OpenCV (opencv-python): For webcam capture, image processing, and rendering.
NumPy: For efficient array operations.

Install the dependencies using pip:
pip install opencv-python numpy

Usage

Run the Script:
python ascii_cam.py

Ensure a webcam is connected to your device. The script will open a window displaying the ASCII-rendered video feed.

Keyboard Controls:

q or Esc: Quit the application.
s: Save the current ASCII frame as a PNG file (e.g., ascii_frame_00001.png).
[ : Decrease the ASCII image width (minimum 20 columns).
] : Increase the ASCII image width (maximum 400 columns).
g: Toggle between colored and monochrome ASCII rendering.
i: Toggle intensity inversion (light pixels map to dense or sparse characters).
1: Use the detailed ASCII character set.
2: Use the simple ASCII character set.


Output:

The ASCII art is displayed in a resizable OpenCV window named "ASCII Cam".
Saved frames are stored in the working directory with filenames like ascii_frame_XXXXX.png.



Code Structure

ASCII_SETS: Defines two sets of ASCII characters for mapping pixel intensities:
Detailed set: 70 characters for finer granularity.
Simple set: 10 characters for a minimalistic look.


map_to_ascii: Converts a grayscale image to an ASCII array by mapping normalized pixel intensities to characters.
render_ascii: Renders the ASCII array onto a canvas, with options for colorization, font scale, and thickness.
main: Handles webcam capture, frame processing, and user input for real-time rendering.

Parameters

ascii_set_id: Selects the ASCII character set (0 for detailed, 1 for simple).
cols: Number of columns in the ASCII image (default: 160).
colorize: Enables/disables colored ASCII rendering (default: False).
invert: Inverts pixel intensity mapping (default: False).
font_scale: Font size for rendering ASCII characters (default: 0.45).
thickness: Font thickness for rendering (default: 1).

Notes

Ensure your webcam is properly connected and accessible by OpenCV.
The aspect ratio of the ASCII image is maintained based on the webcam's resolution.
Performance may vary depending on the webcam resolution and system resources.
The script uses OpenCV's FONT_HERSHEY_SIMPLEX for rendering, ensuring compatibility across platforms.

Example
Run the script, and a window will display your webcam feed as ASCII art. Press g to toggle colors, i to invert the intensity, or s to save a frame. Adjust the resolution with [ or ] for finer or coarser ASCII output.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

Built using OpenCV and NumPy for efficient image processing.
Inspired by ASCII art generation techniques for real-time video rendering.
