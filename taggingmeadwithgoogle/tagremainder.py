import os
import pickle
import requests
import pandas as pd

# The path to the local JSON key file created by Google Cloud for your project
# This file should be downloaded to your computer
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "xxxxxx.json"

TAG_COL = "Tags"
URI_COL = "URL"
FILE = "final-google-mead-15p.csv"

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

        max_label_score = 0
        for label in labels:
            if label.score > max_label_score:
                max_label_score = label.score

        min_label_score = max_label_score - 0.15

        for label in labels:
            if label.score <= max_label_score and label.score >= min_label_score:
                label_word = label.description.lower()
                for mead_tag, google_tags in ALL_TAGS.items():
                    if (label_word in google_tags and mead_tag not in tags_found):
                        tags_found.append(mead_tag)

        """Localize objects in the image on Google Cloud Storage"""
        max_obj_score = 0
        for object_ in objects:
            if object_.score > max_obj_score:
                max_obj_score = object_.score

        min_obj_score = max_obj_score - 0.15

        for object_ in objects:
            if object_.score <= max_obj_score and object_.score >= min_obj_score:
                obj = object_.name.lower()
                for mead_tag, google_tags in ALL_TAGS.items():
                    if (obj in google_tags and mead_tag not in tags_found):
                        tags_found.append(mead_tag)

        df.at[index, TAG_COL] = "; ".join(tags_found)

        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))

    except Exception as e:
        print(e, "uri", uri, "index", index)


count = 0
with open(FILE, "r+") as csv_file:
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        try:
            tags = row[TAG_COL].split("; ")
        except:
            uri = row[URI_COL]
            # detect_labels_uri(uri, df, index)
            img_size = requests.get(uri).content
            if len(img_size) != 0:
                count += 1
                print(uri)
            # update the csv file
            # add tags for the current image
            # df.to_csv(FILE, index=False)
    print(f'Processed {index + 1} lines.')
print(count)
