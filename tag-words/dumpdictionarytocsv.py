import pickle

# 704 mead tags
# 11,864 Google tags
with open('intersection_dictionary_v2.pkl', 'rb') as diction_file:
    loaded_dict = pickle.load(diction_file)
    print(loaded_dict)

with open("joint-tags-v2.csv", "a") as csv_file:
    csv_file.write("Mead Tag, " + "Google Tag(s)")
    csv_file.write('\n')
    for key, value in loaded_dict.items():
        csv_file.write(key + ", ")
        for index in range(len(value)):
            if index == len(value) - 1:
                csv_file.write(value[index])
            else:
                csv_file.write(value[index] + "; ")
        csv_file.write('\n')
