import json
lst=[]
for name in ['java.json','python.json','php.json','前端.json','android.json']:
    with open (name,'r',encoding="utf-8") as fp:
        data = json.load(fp)
        lst +=data
nelst=[]
for item in lst:
    if item not in nelst:
        nelst.append(item)
with open('getjob.json', 'a',encoding="utf-8") as f:
    js=json.dumps(nelst,ensure_ascii=False)
    f.write(js)

print(len(lst))
print(len(nelst))
