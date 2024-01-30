import json
import os

print("123")
path = os.getcwd() + "\福建金門地方法院_民事" 
#path = os.getcwd() + "\測試"
file = os.listdir(path)
count = 0
out_file = open("福建金門地方法院_民事.txt", 'w')
out_file2 = open("福建金門地方法院_民事_title.txt", 'w')

out_f = open("福建金門地方法院_民事_非民法.txt", 'w')
out_f2 = open("福建金門地方法院_民事_非民法_title.txt", 'w')
for f in file:

    f_temp = os.path.join(path, f)
    # json 讀取
    with open(f_temp, 'r', encoding = 'utf-8') as d:
        data = json.load(d)

    temp = data['relatedIssues']
    count = 0
    count2 = 0
    for issue in temp:
        law = issue["lawName"]
        id = issue["issueRef"].split()[0]
        if law == "民法":
            if not id.isnumeric():
                index = 0
                while id[index].isdigit():
                    index = index + 1
                id = id[:index]
            if 1 <= int(id) and int(id) <= 966 :
                if count == 0:
                    out_file.write(f)
                    out_file.write("\n")
                    out_file2.write(f)
                    out_file2.write("\n")
                out_file.write(issue["lawName"])
                out_file.write(" ")
                out_file.write(issue["issueRef"])
                out_file.write("\n")
                count = count + 1
        else:
            if count2 == 0:
                out_f.write(f)
                out_f.write("\n")
                out_f2.write(f)
                out_f2.write("\n")
            out_f.write(issue["lawName"])
            out_f.write(" ")
            out_f.write(issue["issueRef"])
            out_f.write("\n")
            count2 = count2 + 1

