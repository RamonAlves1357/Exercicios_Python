#!/usr/bin/env python
# -*- coding: utf-8 -*-

def questao1():
	def bemvindo(user):
		print(" Login efetuado com sucesso. ")
		print(f" Bem Vindo {user}!")
		print("----------------------------\n")
	
	def erro():
		print(" Ops!")
		print(" Algo de errado não está certo.")
		print(" Usuario ou senha está incorreto. Tente novamente")
		print("-----------------------------\n")

	cont = 0
	while (True):
		cont += 1
		print(f"------------ nº{cont} ------------")
		user = input(" Informe o usuario: ")
		senha = input(" Informe a senha: ")

		if(user == "aluno"):
			if(senha == "aluno"):
				bemvindo(user)
				break
			else:
				erro()

		elif(user == "admin"):
			if(senha == "admin"):
				bemvindo(user)
				break
			else:
				erro()
		
		else:
			erro()

def questao2():
	def quant(palavra):
		cont = 0
		for i in range(len(palavra)):
			if palavra[i] in ("a", "e", "i", "o", "u"):
				cont += 1
			elif palavra[i] in ("â", "ã", "á", "à", "ê", "ẽ", "é", "è", "î", "ĩ", "ì", "í", "ô", "õ", "ó", "ò", "ũ", "û", "ú", "ù"):
				cont += 1
			elif palavra[i] in ("A", "E", "I", "O", "U"):
				cont += 1
			elif palavra[i] in ("Ã", "Â", "Á", "À", "Ẽ", "Ê", "É", "È", "Ĩ", "Î", "Í", "Ì", "Õ", "Ô", "Ó", "Ò", "Ũ", "Û", "Ú", "Ù"):
				cont += 1
			
		return cont

	s = input(" Informe uma palavra: ")

	print(f"Essa palavra/frase tem {quant(s)} vogais.")

def questao3():
	def local(cidade, estado):
		print(cidade + "-" + estado, "eh minha cidade favorita: ")

	cidade = input(" Informe uma cidade: ")
	estado = input(" Informe um estado (UF): ")
	local(cidade.title(), estado.upper())

def questao4():
	def music(album, cantor, faixa):
		dici = {"Nome_Album" : album, "Nome_Cantor" : cantor, "Faixa" : faixa}
		return dici

	album = input(" Informe o nome do album: ")
	cantor = input(" Informe o nome do cantor: ")
	faixa = input(" Informe a quantidade de faixas: ")
	
	print(music(album, cantor, faixa))
	
def questao5():
	def soma(numero):
		acm = 0
		for i in range(1, numero + 1):
			acm += i		
		return acm

	n = int(input(" Digite um número: "))
	
	print(f" A soma de todos os números entre 1 e {n} é {soma(n)}")

def questao6():
	def soma(n1, n2):
		acm = 0
		if (n1 < n2):
			for i in range(n1, n2 + 1):
				acm += i
			return acm

		elif (n2 < n1):
			for i in range(n2, n1+1):
				acm += i
			return acm
		
		elif ( n1 == n2):
			print("Opa, números iguais.")
		
		else:
			print(" Ops! Algo de errado não está certo.")

	n1 = int(input(" Digite o 1º número: "))
	n2 = int(input(" Digite o 2º número: "))
	
	print(f" A soma de todos os números entre {n1} e {n2} é {soma(n1, n2)}")

def questao7():
	def maior(n1, n2):
		if (n1 < n2):
			return n2

		elif (n2 < n1):
			return n1
		
		else:
			print(" Opa, números iguais.")
			return "ambos"

	n1 = int(input(" Digite o 1º número: "))
	n2 = int(input(" Digite o 2º número: "))
	
	print(f" O maior número entre {n1} e {n2} é {maior(n1, n2)}.")

def questao8():
	def MaxMin(n1, n2, param):
		if (param == True):
			if (n1 < n2):
				return print(f" O maior número entre {n1} e {n2} é {n2}.")

			elif (n2 < n1):
				return print(f" O maior número entre {n1} e {n2} é {n1}.")
			
			else:
				return print(" Opa, números iguais.")
		elif (param == False):
			if (n1 > n2):
				return print(f" O menor número entre {n1} e {n2} é {n2}.")

			elif (n2 > n1):
				return print(f" O menor número entre {n1} e {n2} é {n1}.")
			
			else:
				return print(" Opa, números iguais.")
	
	n1 = int(input(" Digite o 1º número: "))
	n2 = int(input(" Digite o 2º número: "))
	param = input(" Agr digite T(True) ou F(False)")
	
	if (param == "T"or param == "t" or param == "True" or param == "true"):
		param = True
	elif (param == "F" or param == "f" or param == "False" or param == "false"):
		param = False
	else:
		print(" Ops! Algo de errado não está certo.")

	MaxMin(n1, n2, param)

def questao9():
	def ordenar(n1, n2, n3):
		tupla = (n1, n2, n3)
		tupla_ordenada = tuple(sorted(tupla))
		return tupla_ordenada

	num1 = int(input(" Informe o 1º número: "))
	num2 = int(input(" Informe o 2º número: "))
	num3 = int(input(" Informe o 3º número: "))

	print(ordenar(num1, num2, num3))

def questao10():
	""" def mySum(*args):
		sum = 0
		for i in args:
				sum = sum + i
		return sum """

	cont = 0
	mult = 1
	lista = []

	while True:
		lista.append(int(input(f" Digite o {cont+1}º número: ")))
		mult *= lista[cont]

		op = input(" Você deseja continuar? (S/n)")
		if (op == "S" or op == "s" or "Y" or op == "y"):
			pass
		else:
			print(f" A multiplicação de todos os números digitados é {mult}")
			break
		cont += 1

def questao11():
	def fatorial(num):
		resultado=1
		count=1

		while count <= num:
			resultado *= count
			count += 1

		return resultado

	num = int(input("Fatorial de: "))
	print(fatorial(num))

def questao12():
	def primo(num):
		factors = []

		if (num == 1):
			return False

		for n in range(1,num+1):
			if num % n == 0:
				factors.append(n)
			if len(factors) > 2:
				return False
				break
		
		if len(factors) == 2:
			return True
		
	num =int(input('Qual numero testar? '))
	print(primo(num))