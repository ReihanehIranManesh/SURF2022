**The source code for tagging Mead’s collection using Google Cloud Vision API, with adaptive filtering upon the Vision-generated labels.**

We tagged Mead’s collection of 21,996 web images twice. This is the description of the second round of tagging:

Two distinct Vision API requests, label_detection, and object_localization, were sent simultaneously to Vision for each image. The former request is for assigning labels, and the latter is for object recognition and localization. For each API request for a particular image, by default, ten tag terms with the highest confidence scores are returned. We decided to tag the collection with all Vision tags returned in the API responses by finding a match in the Python dictionary loaded from “polished_diction.pkl”. Subsequently, we filtered labels and objects depending on their confidence scores. In the first round, we observed that using a fixed constant threshold for filtering the Vision-generated tags seemed ineffective, so we considered the highest confidence score (HCS) returned in each label and object API response and included any matching Vision term in the range of [HCS - 0.15, HCS] for each API response. Tagging the whole database would have taken nearly nine hours, so we divided the images into six batches to multi-process all six Python scripts concurrently. This resulted in a significantly less amount of tagging, and the whole collection was tagged in approximately half the time! Lastly, all six outputted CSV files were merged into one final file named “1.csv” in the “final file” subfolder.

**Important files and what they contain:**

*ACURLS-simple.csv*

CSV file of Mead’s collection. URL field contains the URLs which the web images can be downloaded from. ID_NUMBER is a unique identifier assigned to each artwork or object in the museum. 

*final-google-mead-15p.csv*

Final CSV file of the whole collection automatically tagged by Google Vision API with adaptive filtering. 

*inference15p.py*

Script for calculating the most frequent Vision-generated tags, after they were matched to a MIMSY tag. This script produced the "table.csv" file that contains the tag terms and their frequencies, sorted descendingly with the most generated tags at the top of the file. 

*inferencemead.py*

Script for calculating the most frequent already existing tags manually done by humans. This script produced the "table3.csv" file that contains the tag terms and their frequencies, sorted descendingly with the most used tags at the top of the file. The source file used for calculation is "mead.csv". This CSV file was derived from a dumped version of the database where the “Tags” field is all the tags that were manually assigned to each image by humans. NULL means that no tagging has been done by humans for that record (web image). 

*merging.py*

Script for merging all the six CSV files, resulting in the final CSV named “1.csv” which includes the whole collection automatically tagged by Google Vision with adaptive filtering. This CSV file was later renamed “final-google-mead-15p.csv”. 

*multi.py*

Script for multiprocessing six python scripts concurrently. The scripts were “tagdb1.py” through “tagdb6.py”, each tagging 4,000 images, except the last script, which tagged 1,996 images.

*tagremainder.py*

Script for tagging the images that were not tagged at all after the whole database was tagged in the multiprocessing stage. This was a reassuring process to check that ALL images that could be tagged by Vision were actually tagged. During the multiprocessing stage, some API requests were unsuccessful and incomplete due to unstable internet connection, connection loss, or error return by Google Vision API. By running this program, we also found that 100 images in the database have corrupted URLs with no file content. These are mostly museum objects with an online webpage but no available image in the database. 
