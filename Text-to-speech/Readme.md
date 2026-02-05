# 🎙️ Text to Speech Web Application

This project is a simple and interactive **Text to Speech Converter** developed using Python and Streamlit. The application allows users to enter text and convert it into speech with different English accent options. It focuses on providing a clean interface, proper input validation, and modular code design.

---------------------------------------

## Project Overview

The goal of this application is to demonstrate how text input can be transformed into spoken audio using Text-to-Speech technology. The project is designed with a structured approach where UI, validation, testing, and speech generation are separated into different modules for better readability and maintainability.

---------------------------------------

## Key Features

- Convert written text into audio speech  
- Support for multiple English accents  
  - US English  
  - Indian English  
  - British English  
- Voice type selection interface  
- Adjustable speech speed and volume sliders  
- Text validation before speech generation  
- Unit testing support for validation logic  
- Simple and responsive user interface  

--------------------------------

## Technologies Used

- **Python**
- **Streamlit** – Used for building the web interface
- **gTTS / Speech Engine** – Used for converting text into audio
- **Pytest** – Used for testing validation functions
- **Custom CSS** – Used for improving UI design

---------------------------------

## Project Structure
Text-To-Speech
│
├── app.py
├── validator.py
├── test_validator.py
├── tts_engine.py
└── README.md

---------------------------------------


### Module Description

**app.py**  
Handles the main Streamlit application interface and user interaction.

**validator.py**  
Contains functions that check whether the entered text meets required conditions.

**test_validator.py**  
Includes automated test cases to verify the validation module.

**tts_engine.py**  
Responsible for generating speech audio from text input.

---

##  Installation Guide

### Step 1: Clone the Repository
git clone https://github.com/your-username/Text-To-Speech-App.git

### Step 2: Move to Project Directory
cd Text-To-Speech-App

### Step 3: Install Dependencies
pip install streamlit gTTS pyttsx3 pytest

## Step 4: Run the Application
streamlit run app.py

## Running Test Cases

To verify validation functionality:

pytest test_validator.py

## How to Use the Application

Launch the application using Streamlit
Enter text inside the text input area
Select preferred voice type
Choose the accent
Adjust speech speed or volume if needed
Click the Generate Speech button
Listen to the generated audio output

##  Known Limitations

1. Accent variations depend on the speech engine capabilities

2. Gender voice difference may not be fully supported in some engines

3. Internet connection may be required when using certain speech libraries

## Future Improvements

Adding support for multiple languages
Integration with advanced AI-based speech engines
Audio download functionality
Dark mode user interface
Real-time speech preview

##  License

This project is open-source and available for learning and development purposes.

## Developer

Developed by Anusha Lokasani