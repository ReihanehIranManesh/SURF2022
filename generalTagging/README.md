**The source code for tagging Mead’s collection using Google Cloud Vision API, with no adaptive filtering upon the Vision-generated labels.**

We tagged Mead’s collection of 21,996 web images twice. This is the description of the first round of tagging:

Two distinct Vision API requests, label_detection, and object_localization, were sent simultaneously to Vision for each image. The former request is for assigning labels, and the latter is for object recognition and localization. For each API request for a particular image, by default, ten tag terms with the highest confidence scores are returned. We decided to tag the collection with all Vision tags returned in the API responses, with confidence scores higher than or equal to 0.80 (80%) by finding a match in the Python dictionary loaded from “polished_diction.pkl”. You can see the source code for all of these in the “tagdb.py” script. 
