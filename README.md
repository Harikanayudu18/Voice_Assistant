
# Python Voice Assistant

A voice-controlled desktop assistant built with Python that recognizes spoken commands and responds using text-to-speech. It can open websites, perform Google searches, announce the current time and date, and launch supported desktop applications.

## Overview

The Python Voice Assistant provides a simple, hands-free way to interact with your computer using voice commands. It combines speech recognition, text-to-speech, and Python's built-in system utilities to perform everyday tasks.

## Features

- **Speech Recognition:** Converts spoken commands into text.
- **Text-to-Speech:** Provides spoken responses to user commands.
- **Website Navigation:** Opens YouTube, Google, and GitHub.
- **Google Search:** Searches the web using voice input.
- **Date and Time:** Announces the current date and time.
- **Application Launching:** Opens Notepad and Calculator on supported systems.
- **Help Command:** Explains the available voice commands.
- **Voice-Controlled Exit:** Stops the assistant when the user says "stop", "exit", "quit", or "goodbye".

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| SpeechRecognition | Speech recognition |
| PyAudio | Microphone input |
| pyttsx3 | Text-to-speech conversion |
| webbrowser | Opening websites and search results |
| datetime | Retrieving the current date and time |
| subprocess | Launching desktop applications |

## Project Structure

```text
VoiceAssistant/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Prerequisites

Before running the project, ensure you have:

- Python installed on your computer.
- A working microphone.
- An active internet connection for online speech recognition.
- Permission to access the microphone.
- Git installed if you want to clone the repository.

## Installation

### 1. Clone the Repository

Replace the URL below with your GitHub repository URL.

```bash
git clone https://github.com/YOUR_USERNAME/VoiceAssistant.git
cd VoiceAssistant
```

Alternatively, download the repository and open its folder on your computer.

### 2. Create a Virtual Environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PyAudio installation fails, install the required audio dependencies for your operating system and retry.

### 4. Run the Application

```bash
python main.py
```

The assistant will announce that it is ready. Speak clearly into your microphone to issue a command.

## Available Voice Commands

| Voice Command | Description |
|---|---|
| `Hello assistant` | Responds with a greeting |
| `What is the time?` | Announces the current time |
| `What is today's date?` | Announces the current date |
| `Open YouTube` | Opens YouTube in the browser |
| `Open Google` | Opens Google in the browser |
| `Open GitHub` | Opens GitHub in the browser |
| `Search for Python tutorials` | Searches Google for the specified topic |
| `Open Notepad` | Opens Notepad on supported systems |
| `Open Calculator` | Opens Calculator on supported systems |
| `Help` | Lists available capabilities |
| `Stop` | Stops the assistant |
| `Exit`, `Quit`, `Goodbye` | Exits the application |

## Configuration

The speech output speed and volume can be adjusted in `main.py`:

```python
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)
```

- `rate`: Controls the speech speed.
- `volume`: Controls speech volume, from `0.0` to `1.0`.

The listening timeout and maximum phrase duration can also be adjusted:

```python
audio = recognizer.listen(
    source,
    timeout=5,
    phrase_time_limit=8
)
```

## Troubleshooting

### Microphone Errors

- Check that your microphone is connected and working.
- Allow microphone access for your terminal or code editor.
- Verify that PyAudio is installed correctly.

### Speech Recognition Errors

- Check your internet connection.
- Speak clearly and reduce background noise.
- Remember that Google speech recognition requires an internet connection.

### Application Launch Errors

Application commands vary by operating system. Notepad and Calculator commands may require adjustment on macOS or Linux.

### Missing Dependencies

Activate your virtual environment and run:

```bash
python -m pip install -r requirements.txt
```

## Limitations

- Online speech recognition requires an internet connection.
- Recognition accuracy depends on microphone quality and background noise.
- Only the commands implemented in the source code are supported.
- Desktop application availability depends on the operating system.

## Future Enhancements

- Add offline speech recognition.
- Integrate weather and news information.
- Support additional applications and custom commands.
- Introduce a graphical user interface.
- Add configurable wake-word detection.
- Improve command recognition and accessibility.

## Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Test the application.
5. Submit a pull request.

## License

No license has been specified yet. Add a `LICENSE` file to define the terms under which others may use, modify, and distribute this project.

---

Developed as a Python project to explore speech recognition, text-to-speech, and desktop automation.
