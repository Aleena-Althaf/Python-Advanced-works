
f=open("data.csv","w",newline="")
import csv
content=[
    ['name','age','place'],
    ['arun',23,'ekm'],
    ['amal',21,'tvm']
]
w=csv.writer(f)
w.writerows(content)
f.close()