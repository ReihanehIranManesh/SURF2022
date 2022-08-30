# Image Recognition with Image Url
# 222 Classes
import requests

api_key = "c9e4090c-0847-4ada-af5f-b0038e230359"
uri = "https://museums.fivecolleges.edu/grabimg.php?kv=3412359"
id = [382]
url = "https://api.chooch.ai/predict/image?url={uri}&apikey={api_key}&model_id=382".format(uri=uri, api_key=api_key)
print(url)


response = requests.post(url)

with open("chooch.json", "w") as outfile:
    outfile.write(str(response.json()))
for item in response.json()["predictions"]:
    print(item["class_title"])