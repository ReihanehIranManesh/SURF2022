import os
import pickle

import pandas as pd

# The path to the local JSON key file created by Google Cloud for your project
# This file should be downloaded to your computer
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "xxxxxx.json"

ALL_TAGS = {}
URI_COL = "URL"
FILE = "files/ACURLS-simple.csv"


def sort_diction(diction):
    global SORTED_ALL_TAGS
    SORTED_ALL_TAGS = dict(sorted(diction.items(), key=lambda item: item[1]))


def detect_labels_uri(uri, index):
    """Detects labels in the file located in Google Cloud Storage or on the
        Web."""
    # Imports the Google Cloud client library
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    try:
        image.source.image_uri = uri

        response = client.label_detection(image=image)
        labels = response.label_annotations

        for label in labels:
            label_word = label.description.lower()
            ALL_TAGS.update({label_word: ALL_TAGS.get(label_word, 0) + 1})

        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))
    except:
        print("error", uri, "index", index)


with open(FILE, "r+") as csv_file:
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        uri = row[URI_COL]
        detect_labels_uri(uri, index)
        print(index)
    print(f'Processed {index + 1} lines.')

sort_diction(ALL_TAGS)
with open('saved_dictionary.pkl', 'wb') as diction_file:
    pickle.dump(SORTED_ALL_TAGS, diction_file)

with open('saved_dictionary.pkl', 'rb') as diction_file:
    loaded_dict = pickle.load(diction_file)
    print(loaded_dict)


