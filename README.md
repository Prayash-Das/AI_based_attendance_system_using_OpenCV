# Facial Recognition Attendance System

This project provides a robust facial recognition system for automating attendance marking using Python. The system compares facial features between two images and determines the likelihood of them belonging to the same individual. The probability scale ranges from 0 to 1, with values below 0.5 indicating similarity and values above 0.5 suggesting dissimilarity.

## Features

- **Facial Feature Comparison**: Utilizing the `main.py` script, the system can compare the facial features of two images and label them as either True (same individual) or False (different individuals) based on a probability scale.

- **Attendance Marking**: The `project.py` script automates the attendance process by capturing faces using the webcam and marking the attendance in real-time. Images are sourced from the `Attendance2` folder.

- **CSV Logging**: The attendance details, including the individual's name and the time of capture, are logged in the `Attendance.csv` file.

- **Multiple Face Capture**: The system is capable of capturing multiple faces simultaneously, streamlining the attendance process for group settings.

## Usage

1. Ensure that the necessary dependencies are installed by referring to the requirements file.
2. Run the `main.py` script to compare facial features between two images.
3. Execute the `project.py` script to start the facial recognition attendance system. The webcam captures faces, recognizes them, and updates the attendance log in the CSV file.

## Directory Structure

- **main.py**: Script for comparing facial features between two images.
- **project.py**: Script for automating attendance using webcam captures.
- **Attendance2**: Folder containing images for attendance comparison.
- **Attendance.csv**: CSV file logging attendance details.

## Getting Started

Clone this repository and follow the instructions in the respective script files to set up and run the facial recognition attendance system. Adjust parameters and customize the system to suit your specific use case.

Feel free to contribute, report issues, or suggest improvements! Let's build a smarter and more efficient attendance solution together.
