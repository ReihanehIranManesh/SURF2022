import pickle
import pandas as pd

POLISHED_DICTION = {}

# 630 tags
# 1297 google tags
with open("joint-tags-final.csv", "r") as csv_file:
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        mead_tag = row[0].lower()
        try:
            google_tags = row[1].split("; ")
            for TAG in google_tags:
                TMPTAG = TAG.lower()
                if not POLISHED_DICTION.get(mead_tag):
                    POLISHED_DICTION.update({mead_tag: [TMPTAG]})
                else:
                    POLISHED_DICTION[mead_tag].append(TMPTAG)
        except:
            print(index)

count = 0
for key, value in POLISHED_DICTION.items():
    print(key, ":", value)
    count += len(value)

with open('polished_diction.pkl', 'wb') as diction_file:
    pickle.dump(POLISHED_DICTION, diction_file)

print(count)
print(len(POLISHED_DICTION))
