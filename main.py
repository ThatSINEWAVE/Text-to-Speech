import json
import os
import random
import string
from gtts import gTTS


def generate_random_id(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def initialize_json_file(file_name):
    with open(file_name, 'w') as json_file:
        json_file.write("[]")  # Write an empty list to the file


def text_to_speech(text, lang, gender):
    # Create "Outputs" folder if it doesn't exist
    output_dir = "Outputs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate a random ID
    id = generate_random_id()

    # Save the input text, ID, language, and gender in a JSON file
    data = {'id': id, 'text': text, 'lang': lang, 'gender': gender}
    with open('log.json', 'a+') as json_file:
        json_file.seek(0)
        try:
            logs = json.load(json_file)
        except json.decoder.JSONDecodeError:
            initialize_json_file('log.json')
            logs = []
        logs.append(data)
        json_file.seek(0)
        json_file.truncate()  # Truncate the file before writing
        json.dump(logs, json_file, indent=4)

    # Create a text-to-speech object
    tld = 'com'  # Default to Google's base voice
    if gender.lower() == 'male':
        if lang == 'en':
            tld = 'com'  # English male voice
        elif lang == 'es':
            tld = 'es'  # Spanish male voice
    elif gender.lower() == 'female':
        if lang == 'en':
            tld = 'co.uk'  # English female voice
        elif lang == 'es':
            tld = 'com.mx'  # Spanish female voice

    tts = gTTS(text=text, lang=lang, tld=tld, slow=False)

    # Save the speech in the "Outputs" folder with the ID in the filename
    output_file = os.path.join(output_dir, f"output_{id}.mp3")
    tts.save(output_file)

    # Print the path to the saved audio file
    print(f"Text converted to speech successfully. Audio file saved at: {output_file}")


# Display the menu
print("Select the language and gender for the voice:")
print("1. English (Male)")
print("2. English (Female)")
print("3. Spanish (Male)")
print("4. Spanish (Female)")
choice = input("Enter your choice (1-4): ")

# Get the language and gender based on the user's choice
if choice == '1':
    lang = 'en'
    gender = 'male'
elif choice == '2':
    lang = 'en'
    gender = 'female'
elif choice == '3':
    lang = 'es'
    gender = 'male'
elif choice == '4':
    lang = 'es'
    gender = 'female'
else:
    print("Invalid choice. Defaulting to English (Male).")
    lang = 'en'
    gender = 'male'

# Ask user for input text
text = input("Enter the text you want to convert to speech: ")

# Convert text to speech
text_to_speech(text, lang, gender)
