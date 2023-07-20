import argparse

tak_mapping = {
    "יאללה": "NEW", 
    "תאק": ".",   
    "תיק": "-",     
    "תוק": " ",   
}

morse_language = {
    "א": ".-", "ב": "-...", "ג": "--.", "ד": "-..", "ה": ".", "ו": "..-", "ז": "--..", "ח": "....", "ט": "-.-",
    "י": "..", "כ": "-.-.", "ל": ".-..", "מ": "--", "נ": "-.", "ס": "...", "ע": "---", "פ": ".--.", "צ": "--.-",
    "ק": ".---", "ר": ".-.", "ש": "-..-", "ת": "-", "ן": "-.-..", "ם": "----", "ף": ".--", "ך": ".-.-", "ץ": "-.--",
    "?": "..--..", "!": "-.-.--", ".": ".-.-.-", ",": "--..--", "$": "...-..-", "&": ".-...",
    "@": ".--.-.", "(": "-.--.", ")": "-.--.-", ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.",
}

def tak_to_morse(sentence):
    words = sentence.split()
    morse_translation = []
    
    for word in words:
        if word in tak_mapping:
            morse_translation.append(tak_mapping[word])
    
    return "".join(morse_translation)

reverse_tak_mapping = {value: key for key, value in tak_mapping.items()}

def morse_to_tak(morse_translation):
    words = morse_translation.split()
    hebrew_translation = []

    for word in words:
        if "NEW" in word:
            hebrew_translation.append(reverse_tak_mapping[word])
        else:
            for char in word:
                if char in reverse_tak_mapping:
                    hebrew_translation.append(reverse_tak_mapping[char])
        hebrew_translation.append(reverse_tak_mapping[" "])
    
    return " ".join(hebrew_translation)

def translate_to_morse(sentence):
    words = sentence.split()
    morse_translation = []
    
    for word in words:
        for char in word:
            if char in morse_language:
                morse_translation.append(morse_language[char])
        
        morse_translation.append("NEW") 
    
    return " ".join(morse_translation)

morse_decoding = {value: key for key, value in morse_language.items()}

def decode_morse(morse_message):
    words = morse_message.split(" NEW ")
    decoded_message = []
    
    for word in words:
        morse_chars = word.split(" ")
        decoded_word = ""
        
        for morse_char in morse_chars:
            if morse_char in morse_decoding:
                decoded_word += morse_decoding[morse_char]
        
        decoded_message.append(decoded_word)
    
    return " ".join(decoded_message)

def encode(message):
    morse_message = translate_to_morse(message)
    tak_message = morse_to_tak(morse_message)
    return tak_message

def decode(message):
    morse_message = tak_to_morse(message)
    decoded_message = decode_morse(morse_message)
    return decoded_message

parser = argparse.ArgumentParser(description="tik tak tok")
mut = parser.add_mutually_exclusive_group(required=True)
mut.add_argument("-d","--decode",action="store_true")
mut.add_argument("-e","--encode",action="store_true")
parser.add_argument("message")

if __name__ == "__main__":
    args = parser.parse_args()
    if args.encode:
        print(encode(args.message))
    elif args.decode:
        print(decode(args.message))
    else:
        print("invalid command")