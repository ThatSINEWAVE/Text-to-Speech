<div align="center">

# Text to Speech Converter

This script allows you to convert text into speech and save the audio file in the MP3 format. It supports English and Spanish languages with both male and female voices.

</div>

## Features

- Convert text to speech in English or Spanish
- Choose between male or female voices
- Generate a random ID for each conversion
- Save the input text, language, gender, and ID in a JSON log file
- Create an "Outputs" folder to store the generated audio files
- Print the path to the saved audio file

<div align="center">

## ☕ [Support my work on Ko-Fi](https://ko-fi.com/thatsinewave)

</div>

## Prerequisites

- Python 3.x
- `gTTS` (Google Text-to-Speech) library

You can install the `gTTS` library using pip:

```
pip install gTTS
```

## Usage

1. Run the script.
2. Select the language and gender for the voice by entering the corresponding number:
   1. English (Male)
   2. English (Female)
   3. Spanish (Male)
   4. Spanish (Female)
3. Enter the text you want to convert to speech.
4. The script will convert the text to speech and save the audio file in the "Outputs" folder.
5. The path to the saved audio file will be printed in the console.

<div align="center">

# [Join my discord server](https://github.com/ThatSINEWAVE/Discord-Redirect)

</div>

## File Structure

- `main.py`: The main script file containing the text-to-speech conversion logic.
- `log.json`: A JSON file that stores the log of converted texts, their IDs, languages, and genders.
- `Outputs/`: A directory where the generated audio files are saved in MP3 format with a random ID in the filename (e.g., `output_abcd12.mp3`).

## Implementation Details

The script uses the `gTTS` (Google Text-to-Speech) library to convert text to speech. It generates a random ID for each conversion and saves the input text, ID, language, and gender in a JSON log file (`log.json`).

The `text_to_speech` function performs the following steps:

1. Creates the "Outputs" directory if it doesn't exist.
2. Generates a random ID for the conversion.
3. Saves the input text, ID, language, and gender in the `log.json` file.
4. Creates a `gTTS` object with the specified language, gender, and voice settings.
5. Saves the generated speech as an MP3 file in the "Outputs" folder, using the random ID in the filename.
6. Prints the path to the saved audio file.

The script prompts the user to select the language and gender for the voice, and then prompts for the input text to be converted to speech.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.
