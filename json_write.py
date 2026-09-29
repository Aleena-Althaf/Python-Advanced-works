#write
f=open("data.json","w")

import json
content=[

    {'name':'amal','age':23,'gender':'M'},
    {'name':'arun','age':24}
]
json.dump(content,f) #writes python file dictionary into json file
f.close()