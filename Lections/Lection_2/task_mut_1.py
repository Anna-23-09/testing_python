a = 5
print(a, id(a))
a += 1
print(a, id(a)) # изменяемый тип

#txt = 'Hello, world!'
#txt[5] = '_' # неизменяемый тип

txt = 'Hello, world!'
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))
