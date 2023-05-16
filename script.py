import json 


data = {}

with open('input.json', 'r') as f:
    data = json.load(f)
    
with open('output.txt', 'a') as f:
    f.write('\n*********************************************************************\n')

vector = []
def parser(temp ,tempKey):
    ans = temp + ' = ' + 'ip2pi'
    vector.append(tempKey)
    check = False
    for i in vector:
        if(check == False):
            check = True
            continue
        if(type(i) == int):
            ans += '[' + str(i) + ']'
        else:
            ans +=  '[' + '\'' + str(i) + '\']'
    with open('output.txt', 'a') as f:
        f.write(ans + '\n')
        
def checkKey(key):
    if(type(key) == int):
        return False
    counter = 0
    i = 0
    temp = ''
    tempKey = ''
    while(i<len(key)):
        if(counter == 1 and key[i]!='`'):
            temp+=key[i]
        if(key[i]=='`'):
            counter+=1
        if(counter!=1 and key[i]!='`'):
            tempKey += key[i]
        i+=1
    if(counter == 2):
        parser(temp,tempKey)
        return True
    return False
        
def function(key,value):
    if(checkKey(key)):
        vector.pop()
        return
    elif(type(value) == int or type(value) == float):
        vector.append(key)
        vector.pop()
        return
    else:
        vector.append(key)
        
    if(type(value) == dict):
        for keyy,valuee in value.items():
            function(keyy,valuee)
    elif(type(value) == list):
        for i in range(0,len(value)):
            function(i,value[i])
    vector.pop()

function('ip2pi',data)