import pandas as pd

TAG_COL = "OPTION7"
RFILE = "/home/reihaneh/Music/ACURLS.csv"
WFILE = "/home/reihaneh/Music/ACURLS-all-google-mead-tags.csv"

with open(RFILE, "r") as read_file:
    rf = pd.read_csv(read_file)
    with open(WFILE, "r+") as write_file:
        wf = pd.read_csv(write_file)
        tags = rf[TAG_COL]

print(tags)