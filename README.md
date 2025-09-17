# ASCII Cam — Real-Time ASCII Art

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![OpenCV](https://img.shields.io/badge/OpenCV-ASCII--Cam-orange)

![Preview](https://raw.githubusercontent.com/Open-Seal/SAP/refs/heads/main/ascii.png)

---

## Overview

**ASCII Cam** is a Python application that converts a live webcam feed into **ASCII art in real time**.
It uses **OpenCV** for video capture and rendering, and **NumPy** for efficient pixel-to-character mapping.
The output can be displayed in monochrome or colored ASCII characters, with configurable resolution, font size, intensity inversion, and multiple character sets.

---

## Features

* **Real-time ASCII Rendering**: Live conversion of webcam input into ASCII art.
* **Adjustable Resolution**: Dynamically increase or decrease the ASCII grid size.
* **Color and Monochrome Modes**: Option to render ASCII characters with original frame colors or in white on black.
* **Invert Mapping**: Reverse brightness-to-character mapping for stylistic variation.
* **Multiple Character Sets**: Choose between a detailed 70-character set or a simplified 10-character set.
* **Frame Export**: Save individual ASCII-rendered frames as PNG images.
* **Interactive Controls**: Modify settings during runtime using keyboard input.

---

## Requirements

* Python **3.8+**
* OpenCV (`opencv-python`)
* NumPy

Install dependencies via pip:

```bash
pip install opencv-python numpy
```

---

## Usage

Run the script:

```bash
python ascii_cam.py
```

The application will open a resizable OpenCV window named **"ASCII Cam"** showing the live ASCII-rendered video stream.

---

## Keyboard Controls

| Key         | Action                                             |
| ----------- | -------------------------------------------------- |
| `q` / `Esc` | Exit the application                               |
| `s`         | Save the current ASCII frame as a PNG file         |
| `[`         | Decrease ASCII output width (minimum: 20 columns)  |
| `]`         | Increase ASCII output width (maximum: 400 columns) |
| `g`         | Toggle between colored and monochrome rendering    |
| `i`         | Invert brightness mapping                          |
| `1`         | Switch to the detailed ASCII set (70 characters)   |
| `2`         | Switch to the simplified ASCII set (10 characters) |
| `=`         | Increase font scale                                |
| `-`         | Decrease font scale                                |
| `t`         | Cycle through font thickness values (1–3)          |

---

## Parameters

* **`ascii_set_id`** — Character set selection (`0` = detailed, `1` = simple).
* **`cols`** — Number of columns in the ASCII image (default: `160`).
* **`colorize`** — Enable/disable color rendering (default: `False`).
* **`invert`** — Invert pixel intensity mapping (default: `False`).
* **`font_scale`** — Font size for ASCII characters (default: `0.45`).
* **`thickness`** — Font thickness (default: `1`).

---

## Code Structure

* **`ASCII_SETS`**: Defines two ASCII character sets (70 and 10 symbols).
* **`map_to_ascii`**: Maps normalized grayscale pixel intensities to ASCII characters.
* **`render_ascii`**: Draws ASCII characters onto an OpenCV canvas with optional colorization.
* **`main`**: Handles webcam capture, frame processing, and interactive controls.

---

## Notes

* Ensure that your webcam is properly connected and accessible by OpenCV.
* The ASCII image maintains the original aspect ratio.
* Performance may vary depending on system resources and webcam resolution.
* Uses OpenCV’s `FONT_HERSHEY_SIMPLEX` for cross-platform compatibility.

---

## License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

* Built with **OpenCV** and **NumPy**.
* Inspired by traditional ASCII art rendering techniques applied to real-time video.
