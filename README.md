# Project Overview

**Project Name:** Mini-Computer-Vision Pipeline with Streamlit  
**Description:** A simple yet powerful image processing pipeline using **OpenCV**, **NumPy**, and **Streamlit**. It supports grayscale conversion, Gaussian blur, Sobel edge detection, Canny edge detection, and histogram visualization.

---

## Table of Contents

- [Project Overview](#project-overview)
  - [Table of Contents](#table-of-contents)
  - [Features](#-features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Example Screenshot and Video](#example-screenshot-and-video)
    - [Example Screenshot (Textual Description)](#-example-screenshot-textual-description)
    - [Example Video](#example-video)
  - [Filtering Techniques and Metrics Definitions](#filtering-techniques-and-metrics-definitions)
  - [Example Use Case](#-example-use-case)
  - [Summary](#-summary)
  - [MIT License](#-mit-license)

---

## Features

- **Image Upload:** Supports `.jpg`, `.jpeg`, and `.png` formats.
- **Grayscale Conversion:** Converts uploaded images to grayscale.
- **Gaussian Blur:** Smooths the image using Gaussian blur.
- **Edge Detection:**
  - Sobel Edge Detection
  - Canny Edge Detection
- **Histogram Visualization:** Displays the intensity distribution of grayscale images.
- **Interactive UI with Streamlit:** Simple and intuitive interface for end-users.

---

## Installation

To install the required dependencies, run:

```bash
pip install streamlit opencv-python numpy pillow
```

> ✅ Make sure you have **Python 3.8+** installed.

To run the application:

```bash
streamlit run app.py
```

---

## Usage

1. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

2. **Upload an Image:**
   - Click on the `Choose an image...` button.
   - Select a `.jpg`, `.jpeg`, or `.png` file.

3. **View the Results:**
   - Grayscale image, blurred image, Sobel edges, and Canny edges will be displayed.
   - A histogram of the grayscale image will appear below.

---

## Example Screenshot and Video

### Example of steps for CV pipeline using streamlit

| Step | Description                   |
| ---- | ----------------------------- |
| 1    | Original Image Loaded         |
| 2    | Grayscale Converted           |
| 3    | Gaussian Blur Applied         |
| 4    | Sobel Edge Detection Output   |
| 5    | Canny Edge Detection Output   |
| 6    | Grayscale Histogram Displayed |

### Example Video


> 📷 **Video of CV Pipeline Streamlit**


https://github.com/user-attachments/assets/b7973998-9be8-45f0-8fd8-250c6477d186

---


## Filtering Techniques and Metrics Definitions

| Technique                | Description                                                | Metric                         |
| ------------------------ | ---------------------------------------------------------- | ------------------------------ |
| **Grayscale Conversion** | Converts RGB image to grayscale using OpenCV's `cvtColor`. | Pixel intensity values (0-255) |
| **Gaussian Blur**        | Smooths the image by applying a Gaussian kernel.           | Kernel size, sigma value       |
| **Sobel Edge Detection** | Detects edges using the Sobel operator.                    | Gradient magnitude, direction  |
| **Canny Edge Detection** | Multi-stage edge detection using hysteresis.               | Two thresholds (low, high)     |
| **Histogram**            | Shows the frequency of pixel intensities in grayscale.     | Intensity range (0-255)        |

---

## Example Use Case

**Use Case:** Detect edges in a scanned document for OCR processing.

**Steps:**
1. Upload a scanned image of a document.
2. Convert to grayscale and apply Gaussian blur to reduce noise.
3. Use Canny edge detection to extract the document's edges.
4. Process the image for further text recognition or segmentation.

**Outcome:** Clean, edge-detected document ready for OCR processing.

---

## Summary

This project provides a complete image processing pipeline with interactive visualization using Streamlit. It is ideal for developers and researchers who need a simple, customizable image processing tool with support for edge detection, noise reduction, and histogram analysis.

---

## MIT License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

