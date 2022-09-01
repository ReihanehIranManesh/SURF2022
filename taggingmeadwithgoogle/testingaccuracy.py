import pandas as pd

TAG_COL = "Tags"
URI_COL = "URL"
FILE = "temp.csv"
TFILE = "final-google-mead-15p.csv"
count = 0
total = 0
with open(FILE, "r") as csv_file:
    df = pd.read_csv(csv_file)
    with open(TFILE, "r") as test_file:
        tf = pd.read_csv(test_file)
        for index, row in df.iterrows():
            try:
                tags = row[TAG_COL].split("; ")
                if "flowers" in tags:
                    total += 1
                    try:
                        test_tags = tf.at[index, TAG_COL].split("; ")
                        if "flowers" in test_tags:
                            count += 1
                        else:
                            print(index, row[URI_COL], test_tags)
                    except:
                        pass

            except:
                pass
            # update the csv file
            # add tags for the current image
print(f'Processed {index + 1} lines.')

print(count)
print(total)
