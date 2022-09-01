import pandas as pd

TAG_COL = "Tags"
FILE = "final-google-mead-15p.csv"
WFILE = "table.csv"

ALL_GOOGLE_TAGS = {}


def sort_diction(diction):
    global sorted_diction
    sorted_diction = dict(sorted(diction.items(), key=lambda item: item[1], reverse=True))
    print(len(sorted_diction))


empty = 0
total = 0
with open(FILE, "r") as csv_file:
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        try:
            tags = row[TAG_COL].split("; ")
            total += len(tags)
            for tag in tags:
                ALL_GOOGLE_TAGS.update({tag: ALL_GOOGLE_TAGS.get(tag, 0) + 1})
        except:
            empty += 1

sort_diction(ALL_GOOGLE_TAGS)
print("total", total)
with open(WFILE, "a") as csv_file:
    csv_file.write("Tag, " + "Count")
    csv_file.write('\n')
    for key, value in sorted_diction.items():
        csv_file.write(key + ", " + str(value))
        csv_file.write('\n')

print("emtpy", empty)