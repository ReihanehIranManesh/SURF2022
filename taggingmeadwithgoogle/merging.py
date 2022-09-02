import pandas as pd

TAG_COL = "Tags"
RFILE = "6.csv"
WFILE = "1.csv"

with open(RFILE, "r") as read_file:
    rf = pd.read_csv(read_file)
    with open(WFILE, "r+") as write_file:
        wf = pd.read_csv(write_file)
        for index, row in rf.iterrows():
            # the condition should change according to the RFILE you are choosing to merge
            if index >= 20000:
                try:
                    tags = rf[TAG_COL][index]
                    wf.at[index, TAG_COL] = tags
                    print(index)
                except:
                    continue
    wf.to_csv(WFILE, index=False)
