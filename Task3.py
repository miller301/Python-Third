import re
def WhatLang(text):
	return bool(re.search('[а-яА-Я]', text))
rus = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
        8:'ШЭЮ',
      	10:'ФЩЪ'}

eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}

text = input("Введите слово для подсчета очков").upper()
if WhatLang(text):
	print(sum([l for i in text for l, n in rus.items() if i in n]))
else:
	print(sum([l for i in text for l, n in eng.items() if i in n]))