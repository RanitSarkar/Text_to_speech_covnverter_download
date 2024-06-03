import random
import os
import time
from tkinter import *
import pyttsx3
import threading

# Initialize the text-to-speech converter
converter = pyttsx3.init()

# Initialize the lock for thread safety
lock = threading.Lock()

# Create the saved_audios directory if it doesn't exist
if not os.path.exists('saved_audios'):
    os.makedirs('saved_audios')


# Function to update the heading text
def update_heading(text):
    heading_label.config(text=text)


# Function to convert text to speech
def convert_text_to_speech():
    with lock:
        text = text_box.get("1.0", END)
        converter.setProperty('rate', rate_slider.get())
        converter.setProperty('volume', volume_slider.get() / 100)
        converter.say(text)
        converter.runAndWait()
    update_heading("Text to Speech Converter")


# Function to stop the speech
def stop_speech():
    with lock:
        converter.stop()
    update_heading("Text to Speech Converter")


# Function to save the text as an audio file
def download_speech():
    text = text_box.get("1.0", END)
    converter.setProperty('rate', rate_slider.get())
    converter.setProperty('volume', volume_slider.get() / 100)

    # Save the speech to an audio file
    # Get the current time
    current_time = time.localtime()
    # Format the time in a human-readable format
    time_string = time.strftime("%Y_%m_%d", current_time)
    # Generate a random number between 1 and 10,000
    random_num = random.randint(1, 10000)
    # Construct the filename
    filename = os.path.join('saved_audios', f"text_to_speech_{time_string}_{random_num}.mp3")
    converter.save_to_file(text, filename)
    with lock:
        converter.runAndWait()
    update_heading(f"Audio saved as {filename}")


# Function to handle text-to-speech conversion in a separate thread
def start_speech_thread():
    update_heading("Playing")
    speech_thread = threading.Thread(target=convert_text_to_speech)
    print("Conversion Starting")
    speech_thread.start()


# Create the main application window
master = Tk()
master.title("Text to Speech Converter")

# Create and place the heading label
heading_label = Label(master, text='Text to Speech Converter', font=('Helvetica', 16, 'bold'))
heading_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create and place a label and text box for multi-line text entry
Label(master, text='Enter your text:').grid(row=1, column=0, padx=10, pady=10)
text_box = Text(master, height=10, width=50)
text_box.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Create and place a button to convert text to speech
convert_button = Button(master, text='Convert', command=start_speech_thread)
convert_button.grid(row=3, column=0, pady=10)

# Create and place a button to stop the speech
stop_button = Button(master, text='Stop', command=stop_speech,)
stop_button.grid(row=3, column=1, pady=10)

# Create and place a button to download the speech as an audio file
download_button = Button(master, text='Download', command=download_speech)
download_button.grid(row=3, column=2, pady=10)

# Create and place sliders for volume and rate adjustment
Label(master, text='Volume').grid(row=4, column=0, padx=10, pady=5)
volume_slider = Scale(master, from_=0, to=100, orient=HORIZONTAL)
volume_slider.set(70)  # Set initial volume to 70%
volume_slider.grid(row=5, column=0, padx=10, pady=5)

Label(master, text='Rate').grid(row=4, column=1, padx=10, pady=5)
rate_slider = Scale(master, from_=50, to=300, orient=HORIZONTAL)
rate_slider.set(150)  # Set initial rate to 150 words per minute
rate_slider.grid(row=5, column=1, padx=10, pady=5)

# Run the main event loop
mainloop()
