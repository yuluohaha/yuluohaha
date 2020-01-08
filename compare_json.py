import json

with open('./base.json', 'r') as fp:
    text_base = json.load(fp)

with open('./new.json', 'r') as fp:
    text_new = json.load(fp)

def compareDict(myDict1, myDict2):
    for key1 in myDict1.keys():
        if key1 not in myDict2:
            print("additional item in base.json: ('%s':%s)" % (key1,myDict1[key1]))
        elif myDict1[key1] != myDict2[key1]:
            if isinstance(myDict1[key1], dict) and isinstance(myDict2[key1], dict):
                print('different key is %s'%(key1))
                compareDict(myDict1[key1], myDict2[key1])
            else:
                print('different sub-key is %s'%(key1))
                print('different value in base.json is %s'%(myDict1[key1]))
                print('different value in new.json is %s'%(myDict2[key1]))
        del myDict2[key1]
    if len(myDict2):
        print('additional items in new.json:', myDict2.items())

compareDict(text_base, text_new)