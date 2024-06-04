# Text to Speech Converter

This project is a simple Text to Speech Converter application built using Python and the Tkinter library for the GUI. The application allows users to enter text, convert the text to speech, stop the speech, and save the speech as an audio file. The Pyttsx3 library is used for text-to-speech conversion.

## Features

- **Convert Text to Speech**: Enter text in the provided text box and click the "Convert" button to hear the text read aloud.
- **Stop Speech**: Click the "Stop" button to stop the speech.
- **Download Speech**: Save the entered text as an audio file by clicking the "Download" button.
- **Adjust Volume**: Use the volume slider to adjust the volume of the speech.
- **Adjust Rate**: Use the rate slider to adjust the speech rate.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Pyttsx3 library

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/text-to-speech-converter.git
    cd text-to-speech-converter
    ```

2. **Install the required libraries**:
    ```bash
    pip install pyttsx3
    ```

## Usage

1. **Run the application**:
    ```bash
    python text_to_speech_converter.py
    ```

2. **Enter Text**:
   - Enter the text you want to convert to speech in the provided text box.

3. **Convert Text to Speech**:
   - Click the "Convert" button to hear the text read aloud.

4. **Stop Speech**:
   - Click the "Stop" button to stop the speech.

5. **Download Speech**:
   - Click the "Download" button to save the entered text as an audio file. The file will be saved in the `saved_audios` directory with a unique filename.

6. **Adjust Volume**:
   - Use the volume slider to adjust the volume of the speech.

7. **Adjust Rate**:
   - Use the rate slider to adjust the speech rate.

## Code Overview

### Initializing the Text-to-Speech Converter

```python
converter = pyttsx3.init()
```

### Creating the Main Application Window

```python
master = Tk()
master.title("Text to Speech Converter")
```

### Functions for Text-to-Speech Conversion and Control

- **update_heading**: Updates the heading label text.
- **convert_text_to_speech**: Converts the text to speech using the pyttsx3 library.
- **stop_speech**: Stops the speech.
- **download_speech**: Saves the text as an audio file.
- **start_speech_thread**: Handles text-to-speech conversion in a separate thread.

### GUI Elements

- **Heading Label**: Displays the heading of the application.
- **Text Box**: Allows users to enter text.
- **Buttons**: Convert, Stop, and Download buttons to control the speech.
- **Sliders**: Adjust volume and rate.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
