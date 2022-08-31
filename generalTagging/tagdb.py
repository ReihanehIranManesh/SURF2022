import os
import pickle

import pandas as pd


# The path to the local JSON key file created by Google Cloud for your project
# This file should be downloaded to your computer
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "xxxxxx.json"

TAG_COL = "Tags"
URI_COL = "URL"
FILE = "ACURLS-simple-google-tags.csv"

with open('polished_diction.pkl', 'rb') as diction_file:
    ALL_TAGS = pickle.load(diction_file)


def detect_labels_uri(uri, df, index):
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

        objects = client.object_localization(
            image=image).localized_object_annotations

        tags_found = []
        tag_list = ""
        for label in labels:
            if label.score >= 0.8:
                label_word = label.description.lower()
                for mead_tag, google_tags in ALL_TAGS.items():
                    if (label_word in google_tags and mead_tag not in tags_found):
                        if len(tags_found) == 0:
                            tag_list = mead_tag
                        else:
                            tag_list = tag_list + "; " + mead_tag
                        tags_found.append(mead_tag)

        """Localize objects in the image on Google Cloud Storage"""

        for object_ in objects:
            if object_.score >= 0.8:
                obj = object_.name.lower()
                for mead_tag, google_tags in ALL_TAGS.items():
                    if (obj in google_tags and mead_tag not in tags_found):
                        if len(tags_found) == 0:
                            tag_list = mead_tag
                        else:
                            tag_list = tag_list + "; " + mead_tag
                        tags_found.append(mead_tag)

        df._set_value(index, TAG_COL, tag_list)

        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))

        # update the csv file
        # add tags for the current image
    except Exception as e:
        print(e, "uri", uri, "index", index)


with open(FILE, "r+") as csv_file:
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        uri = row[URI_COL]
        detect_labels_uri(uri, df, index)
        print(index)

    df.to_csv(FILE, index=False)
    print(f'Processed {index + 1} lines.')