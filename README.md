# ASCII Cam — Real-Time ASCII Art

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![OpenCV](https://img.shields.io/badge/OpenCV-ASCII--Cam-orange)



![Preview](https://raw.githubusercontent.com/Open-Seal/SAP/refs/heads/main/ascii.png)

## Overview

**ASCII Cam** is a minimalistic project that uses OpenCV and NumPy to convert your webcam feed into ASCII art in real time.
The output is rendered directly in the terminal, creating a retro and lightweight visualization of live video.

## Features

* 📹 Captures frames directly from your webcam
* 🔡 Converts frames into ASCII characters in real time
* ⚙️ Adjustable resolution (`cols` variable in the code)
* ⌨️ Easy controls:

  * Press **q** or **Esc** to quit

## Requirements

* Python 3.8+
* [opencv-python](https://pypi.org/project/opencv-python/)
* [numpy](https://pypi.org/project/numpy/)

Install dependencies:

```bash
pip install opencv-python numpy
```

## Example

Here’s what the output looks like:
*(Your terminal will render something like this in real time.)*

```
@@@@@@@@@@@@#######*****++++++==----
@@@@@@@@@@@#######*****++++++==-----
@@@@@@@@@@########****+++++==-------
```

## License

This project is licensed under the MIT License. Feel free to use, modify, and share.
