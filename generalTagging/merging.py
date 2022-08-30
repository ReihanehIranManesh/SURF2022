import pandas as pd

TAG_COL = "Tags"
RFILE = "/home/reihaneh/Music/remainder.csv"
WFILE = "/home/reihaneh/Music/ACURLS-all-google-mead-tags.csv"

with open(RFILE, "r") as read_file:
    rf = pd.read_csv(read_file)
    with open(WFILE, "r+") as write_file:
        wf = pd.read_csv(write_file)
        for index, row in rf.iterrows():
            if index >= 13000:
                try:
                    tags = rf[TAG_COL][index].split("; ")
                    for i in range(len(tags)):
                        if i == 0:
                            wf.at[index, TAG_COL] = tags[i]
                        else:
                            wf.at[index, TAG_COL] += "; " + tags[i]
                    print(index)
                except:
                    continue
    wf.to_csv(WFILE, index=False)
