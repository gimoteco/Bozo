from collections import Counter
import random

def analisador_de_jogada(jogada):
	agrupados = Counter(jogada)
	quantidade_dos_dados = agrupados.values()
	dados_tirados = agrupados.keys()
	todos_sao_iguais = 5 in quantidade_dos_dados
	quatro_sao_iguais = 4 in quantidade_dos_dados
	eh_full_house = 3 in quantidade_dos_dados and 2 in quantidade_dos_dados
	eh_sequencia =  set(range(1, 6)).issubset(set(jogada)) or set(range(2, 7)).issubset(set(jogada))

	if todos_sao_iguais:
		return "general"
	elif quatro_sao_iguais:
		return "quadrada"
	elif eh_full_house:
		return "fu"
	elif eh_sequencia:
		return "sequencia"