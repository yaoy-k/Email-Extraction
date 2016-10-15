name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count={}

for line in handle:
    if not line.startswith("From "): continue
    line = line.split()
    time = line[5]
    time = time.split(":")
    hr = time[0]
    count[hr] = count.get(hr,0) +1

lst =list()
for k,v in count.items():
    lst.append((k,v))
    lst.sort()


for k,v in lst:
    print k,v