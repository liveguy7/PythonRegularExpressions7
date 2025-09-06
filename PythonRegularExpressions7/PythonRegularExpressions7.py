import re

def snakeToCamel(txt):
    tmp = ''.join(x.capitalize() or '_' for x in txt.split('_'))
    return tmp

print(snakeToCamel("python_exercises"))

def cameltoSnake(txt):
    str1 = re.sub('(.)([A-Z][a-z]+)',r'\1_\2',txt)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

print(cameltoSnake("PythonExercises"))

text3 = '"One","Two","Three"'
tmp = re.findall(r'"(.*?)"', text3)
print(tmp)
text3 = '**//Python Exercises// - 12.'
tmp = re.compile('[\W_]+')
result = tmp.sub('',text3)
print(result)

text = "Ten 10, Twenty 20, Thirty 30, apple eaton and eddy aeton."
street = "110 North Road"
result = re.split('\D+', text)
for element in result:
    print(element)

lst = re.findall("[ae]\w+", text)
print(lst)

for m in re.finditer('\d+',text):
    print(m.group(0))
    print("Index", m.start())

print(re.sub('Road$','Rd.',street))
print(re.sub("[ ,.]", ":", text))
print(re.findall(r'\b\w{5}\b', text))



