import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud import translate_v2 as translate

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/reihaneh/PycharmProjects/SURF2022/testdomcolor-5cbfa6dc7bc4.json"
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/adamrogers/PycharmProjects/SURF2022/testdomcolor-5cbfa6dc7bc4.json"

langs = {"af": "Afrikaans", "sq": "Albanian",
         "ar": "Arabic", "hy": "Armenian",
         "be": "Belarusian", "bn": "Bengali",
         "bg": "Bulgarian", "ca": "Bengali",
         "zh": "Chinese", "hr": "Croatian",
         "cs": "Czech", "da": "Danish",
         "nl": "Dutch", "en": "English",
         "et": "Estonian", "fil": "Filipino",
         "tl": "Filipino", "fi": "Finnish",
         "fr": "French", "de": "German",
         "el": "Greek", "gu": "Gujarati",
         "iw": "Hebrew", "hi": "Hindi",
         "hu": "Hungarian", "is": "Icelandic",
         "id": "Indonesian", "it": "Italian",
         "ja": "Japanese", "kn": "Kannada",
         "km": "Khmer", "ko": "Korean",
         "lo": "Lao", "lv": "Latvian",
         "lt": "Lithuanian", "mk": "Macedonian",
         "ms": "Malay	", "ml": "Malayalam",
         "mr": "Marathi", "ne": "Nepali",
         "no": "Norwegian", "fa": "Persian",
         "pl": "Polish", "pt": "Portuguese",
         "pa": "Punjabi", "ro": "Romanian",
         "ru": "Russian", "ru-PETR1708": "Russian",
         "pa": "Punjabi", "ro": "Romanian",
         "sr": "Serbian", "sr-Latn	": "Serbian",
         "sk": "Slovak", "sl": "Slovenian",
         "es": "Spanish", "sv": "Swedish",
         "ta": "Tamil", "te": "Telugu",
         "th": "Thai", "tr": "Turkish",
         "uk": "Ukrainian", "vi": "Vietnamese",
         "yi": "Yiddish	",
         # Experimental languages
         "am": "Amharic", "grc": "Ancient Greek",
         "as": "Assamese", "az": "Azerbaijani",
         "az-Cyrl": "Azerbaijani", "eu": "Basque",
         "bs": "Azerbaijani", "my": "Burmese",
         "ceb": "Cebuano", "chr": "Cherokee",
         "dv" : "Dhivehi", "dz": "Dzonkha",
         "sw": "Swahili", "syr": "Syriac",
         "haw": "Hawaiian", "so": "Somali",
         "zu": "Zulu", "mi": "Maori"
         }

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the local image file to annotate
# file_name = os.path.abspath('1967-77-cc.jpg')

# Loads the image into memory
# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()

# image = vision.Image(content=content)


# The uri of image file (somewhere on internet)
image = vision.Image()
image.source.image_uri = "https://museums.fivecolleges.edu/grabimg.php?wm=1&kv=3063427"


# OCR
all_words = []
response = client.text_detection(image=image)
texts = response.text_annotations
print("----------------------********----------------------")
print('Texts:')
isFirst = True
for text in texts:
    print('\n"{}"'.format(text.description))
    if isFirst:
        print("The source language is: ")
        # print('\n"{}"'.format(text.locale), langs[text.locale])
        isFirst = False
    all_words.append(text.description)
    vertices = (['({},{})'.format(vertex.x, vertex.y)
                 for vertex in text.bounding_poly.vertices])

    print('bounds: {}'.format(','.join(vertices)))

print("----------------------********----------------------")
all_words_new = []
print('Handwritten texts:')
response = client.document_text_detection(image=image)

for page in response.full_text_annotation.pages:
    for block in page.blocks:
        print('\nBlock confidence: {}\n'.format(block.confidence))

        for paragraph in block.paragraphs:
            print('Paragraph confidence: {}'.format(
                paragraph.confidence))

            for word in paragraph.words:
                word_text = ''.join([
                    symbol.text for symbol in word.symbols
                ])
                print('Word text: {} (confidence: {})'.format(
                    word_text, word.confidence))
                all_words_new.append(word_text)

                for symbol in word.symbols:
                    print('\tSymbol: {} (confidence: {})'.format(
                        symbol.text, symbol.confidence))

translate_client = translate.Client()

# Text can also be a sequence of strings, in which case this method
# will return a sequence of results for each text.
for item in all_words_new:
    result = translate_client.detect_language(item)
    print("Text: {}".format(item))
    print("Confidence: {}".format(result["confidence"]))
    print("Code: {}".format(result["language"]))
    if (langs.get(result["language"])):
        print("Language: {}".format(langs[result["language"]]))
    else:
        print("UNKNOWN")



client = vision.ImageAnnotatorClient()

image = vision.Image()
image.source.image_uri = "https://thumbs.dreamstime.com/b/watermelons-stacked-multiple-grocery-store-orderly-design-has-melons-all-their-stripes-going-horizontally-vivid-102501460.jpg"

objects = client.object_localization(
    image=image).localized_object_annotations

print('Number of objects found: {}'.format(len(objects)))
for object_ in objects:
    print('\n{} (confidence: {})'.format(object_.name, object_.score))
    print('Normalized bounding polygon vertices: ')
    for vertex in object_.bounding_poly.normalized_vertices:
        print(' - ({}, {})'.format(vertex.x, vertex.y))