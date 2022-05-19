import json

courses = '{"name": "ReyannAngsioco", "languages": ["Java", "Python"]}'

dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])
#get me first language taught by trainer
#list_languages = dict_courses['languages']
#print(type(list_languages))
#print(list_languages[0]) #java
print(dict_courses['languages'][0])

with open('C:\\Users\\Reyann\\Downloads\\new.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])
#price of course 'RPA'
    print(type(data['courses']))
    for course in data['courses']:
       # print(course)
        if course['title'] == "RPA":
            print(course['price'])
            assert course['price'] == 45

with open('C:\\Users\\Reyann\\Downloads\\new1.json') as fi:
    data1 = json.load(fi)
    assert data == data1
