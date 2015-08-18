#-*- coding: utf-8 -*-
from analisador import analisador_de_jogada

class TiposDeJogada:

	GENERAL = 40
	QUADRADA = 30
	FU = 10
	SEQUENCIA = 20

	JOGADAS_NUMERICAS = {
		"as": 1,
		"duque": 2,
		"terno": 3,
		"quadra": 4,
		"quina": 5,
		"sena": 6
	}

	@staticmethod
	def eh_jogada_especial(nome_da_jogada):
		return nome_da_jogada in ["general", "fu", "quadrada", "sequencia"]

class Bozo:

	def __init__(self):
		self.placar = {}

	@property
	def jah_acabou(self):
		return len(self.placar) == 10

	def jogar(self, dados, quantidade_de_dados_aleatorios, nome_da_jogada):

		def torar(nome_da_jogada):
			if TiposDeJogada.eh_jogada_especial(nome_da_jogada):
				self.placar[nome_da_jogada] = 0

			
		def marcar_ponto():
			nao_foi_a_jogada_escolhida = analisador_de_jogada(dados) != nome_da_jogada
			if nao_foi_a_jogada_escolhida and TiposDeJogada.eh_jogada_especial(nome_da_jogada):
				torar(nome_da_jogada)
			else:
				eh_de_boca = quantidade_de_dados_aleatorios == 5
				self.placar[nome_da_jogada] = self.obter_pontuacao_da_jogada(nome_da_jogada, eh_de_boca, dados)

		if self.jah_acabou:
			raise Exception("Jogo já foi finalizado!")

		if nome_da_jogada in self.placar:
			raise Exception("Jogada já foi marcada")

		marcar_ponto()

	def obter_pontuacao(self):
		jogadas_escolhidas = filter(lambda valor: valor is not None, self.placar.values());
		return sum(jogadas_escolhidas)

	@staticmethod
	def obter_pontuacao_de_jogada_especial(nome_da_jogada):
		total = 0
		if nome_da_jogada == "general":
			total += TiposDeJogada.GENERAL
		elif nome_da_jogada == "fu":
			total += TiposDeJogada.FU
		elif nome_da_jogada == "quadrada":
			total += TiposDeJogada.QUADRADA
		elif nome_da_jogada == "sequencia":
			total += TiposDeJogada.SEQUENCIA
		return total

	def obter_pontuacao_da_jogada(self, nome_da_jogada, eh_de_boca, dados):

		total = Bozo.obter_adicional_de_boca(nome_da_jogada, eh_de_boca)
		total += Bozo.obter_pontuacao_de_jogada_especial(nome_da_jogada)	
		total += Bozo.obter_pontuacao_da_jogada_numerica(nome_da_jogada, dados)
		return total

	@staticmethod
	def obter_pontuacao_da_jogada_numerica(nome_da_jogada, dados):
		total = 0
		if not TiposDeJogada.eh_jogada_especial(nome_da_jogada):
			numero_do_dado = TiposDeJogada.JOGADAS_NUMERICAS[nome_da_jogada]
			total =+ sum(filter(lambda dado: dado == numero_do_dado, dados))
		return total

	@staticmethod
	def obter_adicional_de_boca(nome_da_jogada, eh_de_boca):
		if not eh_de_boca or not TiposDeJogada.eh_jogada_especial(nome_da_jogada):
			return 0
		if nome_da_jogada == "general":
			return 60
		else:
			return 5


