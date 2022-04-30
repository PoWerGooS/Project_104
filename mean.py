import csv
with open("data.csv", newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
newdata = []
for i in range(len(filedata)):
    number = filedata[i][1]
    newdata.append(number)
n = len(newdata)
total = 0
for x in newdata:
    total = total + int(x)
mean = total/n
print(mean)