import string
import re
import json
import os
import hashedindex
from time import sleep

Path = "./arquivos/"
filelist = os.listdir(Path)

cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

d = dict()

for i in filelist:
    with open(Path + i, "r") as text:
        for line in text:
            line = re.sub(cleanr, '', line)

            line = line.strip()

            line = line.lower()

            line = line.translate(line.maketrans("", "", string.punctuation))

            words = line.split(" ")

            for word in words:
                if word in d:
                    d[word] = d[word] + 1
                else:
                    d[word] = 1

for key in (dict(sorted(d.items(), key=lambda item: item[1]))).__reversed__():
    if(key == ""):
        d.pop(key)
    elif(key.isnumeric()):
        d.pop(key)

sorted_dict = dict(sorted(d.items(),
                          key=lambda item: item[1],
                          reverse=True))

index = hashedindex.HashedIndex()

for i in filelist:
    with open(Path + i, "r") as text:
        for key in sorted_dict:
            index.add_term_occurrence(key, i)

index_dic = index.to_dict()

'''
try:
    print(index.get_documents('laender'))
except Exception as e:
    print("An exception occurred: ", e)
'''

with open("inverted-indexes.json", "w") as outfile:
   json.dump(index_dic, outfile, indent=4)

'''
v = 0
op = '4'
while v != 5:
	while op == '4':
		n1 = int(input('Digite Um Valor: '))
		n2 = int(input('Digite Outro Valor: '))
		op = 0
	print('=-='*20)
	op = str(input('''[1] Somar
                      [2] Multiplicar
                      [3] Maior
                      [4] Novos Números
                      [5] Sair do Progama '''))
	if op == '1':
		print('A soma entre {} e {} é {}'.format(n1,n2,n1+n2))
	elif op == '2':
		print('A multiplicação entre {} e {} é {}'.format(n1,n2,n1*n2))
	elif op == '3':
		if n1 > n2:
			print('{} é maior que {}'.format(n1,n2))
		elif  n1 == n2:
			print('Os números são iguais')
		else:
			print('{} é maior que {}'.format(n2,n1))
	elif op == '4':
		print('Escolha os novos números')
	elif op == '5':
		v = 5
		print('Finalizando...')
		sleep(2)
		print('Fim do progama.')
	else:
		print('Valor invalido, tente novamente.')
	sleep(2)
'''