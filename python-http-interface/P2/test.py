import json
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
with open('C:/Users/Administrator/Desktop/data.json','r') as f:
    data=json.load(f)