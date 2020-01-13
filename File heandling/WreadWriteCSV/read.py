from csv import reader, DictReader
# with open("music.csv","r") as f:
#     data = reader(f)
#     for row in data:
#         print(row)

with open("music.csv","r") as f:
    data = DictReader(f)
    for row in data:
        # print(row)
        print(row["age"])