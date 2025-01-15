# Text-to-Speech Converter

This project is a simple **Text-to-Speech Converter** built using Python and Django. It allows users to input any text, and upon submission, it automatically converts the text into speech and provides a downloadable `.mp3` file of the generated audio.

## Features
- User-friendly interface designed with Bootstrap CSS.
- Converts text input into a speech audio file in `.mp3` format.
- Auto-download feature for the generated speech file.

## How It Works
1. The user enters text into the provided input box on the homepage.
2. The text is processed using the **gTTS (Google Text-to-Speech)** library.
3. An `.mp3` file is generated and immediately made available for download.

## Requirements
To run this project, ensure you have the following installed:
- Python 3.x
- Django 4.x
- gTTS library

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd text_to_speech
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate   # For Windows
   ```

3. Install the required dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

5. Start the development server:
   ```bash
   python3 manage.py runserver
   ```

6. Visit the app in your browser:
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage
- Navigate to the homepage.
- Enter text into the input box.
- Click the **Convert to Speech** button.
- The generated `.mp3` file will automatically start downloading.

## Project Structure
```
text_to_speech/
├── text_to_speech/      # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tts/                 # Django app for Text-to-Speech
│   ├── templates/       # HTML templates
│   │   └── index.html
│   ├── views.py         # Core logic for text-to-speech
│   └── ...
├── media/               # Directory for generated audio files
├── manage.py
└── requirements.txt     # Python dependencies
```

## Dependencies
- Django
- gTTS
- Bootstrap (for frontend styling)

## License
This project is open source and available under the [MIT License](LICENSE).

## Contribution
Feel free to fork this repository, make improvements, and submit a pull request. Suggestions and bug reports are welcome!

---
Enjoy using the Text-to-Speech Converter!

