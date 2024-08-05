
# Image to PDF Converter

A simple and user-friendly application built using Python and Tkinter to convert images into a PDF file. This tool allows users to select multiple images, arrange them in a desired order, and convert them into a single PDF document.

## Features

- Select multiple images (PNG, JPG, JPEG) from your filesystem.
- Specify a custom name for the output PDF file.
- Automatically scales images to fit within the PDF page while maintaining aspect ratio.
- Progress bar to show conversion progress.
- User-friendly interface with clear instructions.

## Prerequisites

- Python 3.x
- The following Python libraries:
  - `tkinter`
  - `PIL` (Pillow)
  - `reportlab`

You can install the required libraries using pip:

```sh
pip install pillow reportlab
