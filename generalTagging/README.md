**The source code for tagging Mead’s collection using Google Cloud Vision API, with no adaptive filtering upon the Vision-generated labels.**

We tagged Mead’s collection of 21,996 web images twice. This is the description of the first round of tagging:

Two distinct Vision API requests, label_detection, and object_localization, were sent simultaneously to Vision for each image. The former request is for assigning labels, and the latter is for object recognition and localization. For each API request for a particular image, by default, ten tag terms with the highest confidence scores are returned. We decided to tag the collection with all Vision tags returned in the API responses, with confidence scores higher than or equal to 0.80 (80%) by finding a match in the Python dictionary loaded from “polished_diction.pkl”. You can see the source code for all of these in the “tagdb.py” script. 


*allgoogletags.py*

A script that can find the distribution of all Vision-generated tags for any CSV source file of the database. Tags will be stored as keys in a Python dictionary, along with their frequencies as their values. This dictionary is then sorted ascendingly according to the frequencies of tags. 

*mergegoogleandmeadtags.py*

Source code for combining Mead’s already tagged objects with “ACURLS-all-google-mead-tags.csv", the output CSV file for the automatically tagged database by Google Vision. In the Mead database, 29% of 21,996 total images are already tagged, an initiative of the museum over the last three years largely engaging student interns. So, we wanted to have a file where we can combine both human-generated and computer-generated tags and be able to compare them easily. 


*merging.py*

Tagging the whole database would have taken nearly nine hours, so we divided the
images into two batches (13000, and 8996) and tagged each batch using a different computer. This is the source code for retrieving the results from the second batch stored in “remainder.csv” and combining it with the first batch, resulting in “ACURLS-all-google-mead-tags.csv" file, which contains the final CSV file with all the records of the database being tagged by Vision API. 
