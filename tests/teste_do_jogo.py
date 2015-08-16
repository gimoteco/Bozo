#-*- coding: utf-8 -*-
import unittest
from core.jogo import Bozo

class TesteDoBozo(unittest.TestCase):

	def setUp(self):
		self.jogo = Bozo()

	def testa_jogada_de_general_de_boca(self):
		self.jogo.jogar([5, 5, 5 ,5 ,5], 5, "general")

		self.assertEqual(100, self.jogo.placar["general"])

	def testa_jogada_de_quadrada_de_boca(self):
		self.jogo.jogar([1,2,2,2,2], 5, "quadrada")

		self.assertEqual(35, self.jogo.placar["quadrada"])
		self.assertEqual(35, self.jogo.obter_pontuacao())

	def testa_jogada_de_fu_de_boca(self):
		self.jogo.jogar([1,1,2,2,2], 5, "fu")

		self.assertEqual(15, self.jogo.placar["fu"])
		self.assertEqual(15, self.jogo.obter_pontuacao())

	def testa_sequencia_de_boca(self):
		self.jogo.jogar([1, 2, 3, 4, 5], 5, "sequencia")

		self.assertEqual(25, self.jogo.placar["sequencia"])
		self.assertEqual(25, self.jogo.obter_pontuacao())

	def testa_maximo_dados_as(self):
		self.jogo.jogar([1,3,1,1,3], 5, "as")

		self.assertEqual(3, self.jogo.placar["as"])
		self.assertEqual(3, self.jogo.obter_pontuacao())

	def testa_maximo_dados_duque(self):
		self.jogo.jogar([2,3,2,1,2], 5, "duque")

		self.assertEqual(6, self.jogo.placar["duque"])
		self.assertEqual(6, self.jogo.obter_pontuacao())

	def testa_jogada_terno(self):
		self.jogo.jogar([1,2,3,3,3],5,"terno")

		self.assertEqual(9, self.jogo.placar["terno"])
		self.assertEqual(9, self.jogo.obter_pontuacao())

	def testa_jogada_quadra(self):
		self.jogo.jogar([1,4,4,5,6],5,"quadra")

		self.assertEqual(8, self.jogo.placar["quadra"])
		self.assertEqual(8, self.jogo.obter_pontuacao())

	def testa_jogada_quina(self):
		self.jogo.jogar([5,5,5,5,5],5,"quina")

		self.assertEqual(25, self.jogo.placar["quina"])
		self.assertEqual(25, self.jogo.obter_pontuacao())

	def testa_jogada_sena(self):
		self.jogo.jogar([6,1,6,2,6],5,"sena")

		self.assertEqual(18, self.jogo.placar["sena"])
		self.assertEqual(18, self.jogo.obter_pontuacao())

	def testa_nao_permite_jogada_repetida(self):
		self.jogo.jogar([6,1,6,2,6], 5, "sena")

		with self.assertRaises(Exception) as contexto:
			self.jogo.jogar([6,1,6,2,6], 5, "sena")
		self.assertEqual("Jogada já foi marcada", contexto.exception.message)

	def testa_torada_no_general(self):
		self.jogo.jogar([6,1,6,2,6], 5, "general")

		self.assertEqual(0, self.jogo.placar["general"])

	def testa_fim_do_jogo(self):
		self.preparar_um_jogo_completo()

		resultado_do_placar = self.jogo.obter_pontuacao()

		self.assertEqual(244, resultado_do_placar)
		self.assertTrue(self.jogo.jah_acabou)

	def testa_que_nao_pode_jogar_depois_que_terminou_o_jogo(self):
		self.preparar_um_jogo_completo()

		with self.assertRaises(Exception) as contexto:
			self.jogo.jogar([6,1,6,2,6], 5, "general")

		self.assertEqual("Jogo já foi finalizado!", contexto.exception.message)
 
	def preparar_um_jogo_completo(self):
		self.jogo.jogar([1,3,1,1,3], 5, "as")
		self.jogo.jogar([2,3,2,1,2], 5, "duque")
		self.jogo.jogar([1,2,3,3,3], 5, "terno")
		self.jogo.jogar([1,4,4,5,6], 5, "quadra")
		self.jogo.jogar([5,5,5,5,5], 5, "quina")
		self.jogo.jogar([6,1,6,2,6], 5, "sena")
		self.jogo.jogar([1,1,2,2,2], 5, "fu")
		self.jogo.jogar([1,2,3,4,5], 5, "sequencia")
		self.jogo.jogar([1,2,2,2,2], 5, "quadrada")
		self.jogo.jogar([6,6,6,6,6], 5, "general")