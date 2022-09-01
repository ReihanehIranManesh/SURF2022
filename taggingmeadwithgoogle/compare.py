import os

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"] = "/home/reihaneh/PycharmProjects/SURF2022/spring-market-354613-75fa6f1b5111.json"

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/adamrogers/PycharmProjects/SURF2022/testdomcolor-5cbfa6dc7bc4.json"

def detect_labels_uri(uri):
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

        for label in labels:
            label_word = label.description.lower()
            print(label_word, label.score)

        """Localize objects in the image on Google Cloud Storage"""
        for object_ in objects:
            obj = object_.name.lower()
            print(obj, object_.score)
        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))

    except Exception as e:
        print(e, "uri", uri)

uri = "https://museums.fivecolleges.edu/grabimg.php?wm=1&kv=3292497"
detect_labels_uri(uri)
