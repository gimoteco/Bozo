import unittest
from core.analisador import analisador_de_jogada

class AnalisadorTeste(unittest.TestCase):

	def testa_que_deu_general(self):
		for dado in range(1, 7):
			jogada = (dado, ) * 5

			jogada_analisada = analisador_de_jogada(jogada)

			self.assertEqual("general", jogada_analisada)

	def testa_que_deu_quadrada(self):
		possibilidade1 = [1, 2, 2, 2, 2]
		possibilidade2 = [2, 2, 2, 2, 1]

 		jogada_analisada1 = analisador_de_jogada(possibilidade1)
		jogada_analisada2 = analisador_de_jogada(possibilidade2)

		self.assertEqual("quadrada", jogada_analisada1)
		self.assertEqual("quadrada", jogada_analisada2)

	def testa_que_deu_full_house(self):
		possibilidades = [
			(1, 2, 1, 1, 2), (2, 1, 1, 1, 2),
			(2, 1, 2, 1, 1), (2, 1, 1, 2, 1),
			(1, 1, 2, 1, 2), (1, 1, 1, 2, 2),
			(1, 2, 1, 2, 1), (1, 1, 2, 2, 1),
			(1, 2, 2, 1, 1), (2, 2, 1, 1, 1)
		]

		for possibilidade in possibilidades:
			resultado_da_jogada_analisada = analisador_de_jogada(possibilidade)
			self.assertEqual("fu", resultado_da_jogada_analisada, possibilidade)

	def testa_sequencia(self):
		possibilidades = (range(1, 6), range(2, 7))

		for possibilidade in possibilidades:
			resultado_da_jogada_analisada = analisador_de_jogada(possibilidade)

			self.assertEqual("sequencia", resultado_da_jogada_analisada)

	def testa_que_nao_deu_nenhuma(self):
		self.assertIsNone(analisador_de_jogada([1, 2, 5, 5, 6]))