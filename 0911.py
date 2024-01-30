import json

f = open('result/福建連江地方法院_民事/in_dict.json', encoding="utf-8")
data = json.load(f)

target_id = ["78","57"]
target_law = ["民事訴訟法"]

matching_indices = []

for i in data:
    count = 0
    for law in target_law:
        if target_law[0] in data[i]["law_list"]:
            count += 1

    for id in target_id:
        if target_id[0] in data[i]["id_list"]:
            count += 1

    matching_indices.append((i, count))

sorted_indices = sorted(matching_indices, key=lambda x: x[1], reverse=True)
top_five_counts = sorted_indices[:5]

judgement = []
for item in top_five_counts:
    judgement.append(data[item[0]]['judgement'])
    # print(item[1])

# print(len(judgement))
print(judgement)

f.close()
