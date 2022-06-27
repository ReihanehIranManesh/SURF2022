import requests
import json
import base64

json_string = {
    "base64_Photo_String": "NO",
    "photo_url": "https://museums.fivecolleges.edu/grabimg.php?kv=3309941"
}
json_string = json.dumps(json_string)
data = json.loads(json_string)

usrPass = b'reihaneh iranmanesh:@Reyhoon2003'
b64Val = base64.b64encode(usrPass)
b64Val = str(b64Val, 'utf-8')

resp = requests.post('https://www.de-vis-software.ro/paintingen.aspx',
                     headers={"Authorization": "Basic %s" % b64Val,
                              'Content-Type': 'application/json',
                              'Accept': 'application/json'}, json=data)
resp_data = resp.json()
print(resp_data)

for item in resp_data["predictions"]:
    print(item["tagName"])
