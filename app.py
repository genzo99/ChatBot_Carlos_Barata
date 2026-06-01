import os
from datetime import datetime
import unittest


def obter_resposta(texto: str) -> str:
    comando = texto.lower()

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): "Olá tudo bem!",
        'como estás': "Estou bem, obrigado!",
        'como te chamas?': "O meu nome é: Bot :)",
        ('bye', 'adeus', 'tchau'): "Gostei de falar contigo! Até breve...",

        # Novas interações exigidas pelos testes
        'história de portugal': "Portugal tem uma história rica que inclui os Descobrimentos e a expansão marítima.",
        'cozinhar': "Cozinhar é uma arte que combina ingredientes, técnicas e criatividade.",
        'programar': "Programar é escrever instruções para que o computador execute tarefas.",
        'desenvolvimento web': "O desenvolvimento web envolve a criação de sites e aplicações web...",
        'ia': "A inteligência artificial é um campo da ciência da computação que se concentra na criação de sistemas que podem realizar tarefas que normalmente requerem inteligência humana.",
        'saúde': "A saúde é um estado de completo bem-estar físico, mental e social, e não apenas a ausência de doenças ou enfermidades.",
        'indisposição': "Sintomas de indisposição podem incluir fadiga, dor de cabeça, náusea e outros sinais de que algo não está bem.",
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    if "horas" in comando:
        return f"São: {datetime.now():%H:%M} horas"

    if "data" in comando:
        return f"Hoje é dia: {datetime.now():%d-%m-%Y}"

    return f"Desculpa, não entendi a questão! {texto}"



def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \nComo te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()



class TestObterResposta(unittest.TestCase):

    def teste_saudacoes(self):
        self.assertEqual(obter_resposta("olá"), "Olá tudo bem!")
        self.assertEqual(obter_resposta("bom dia"), "Olá tudo bem!")
        self.assertEqual(obter_resposta("boa tarde"), "Olá tudo bem!")

    def teste_perguntas_simples(self):
        self.assertEqual(obter_resposta("como estás"), "Estou bem, obrigado!")
        self.assertEqual(obter_resposta("como te chamas?"), "O meu nome é: Bot :)")
        self.assertEqual(obter_resposta("tempo"), "Está um dia de sol!")
        self.assertEqual(obter_resposta("qual é o teu nome?"), "O meu nome é: Bot :)")

    def teste_despedidas(self):
        self.assertEqual(obter_resposta("bye"), "Gostei de falar contigo! Até breve...")
        self.assertEqual(obter_resposta("adeus"), "Gostei de falar contigo! Até breve...")
        self.assertEqual(obter_resposta("tchau"), "Gostei de falar contigo! Até breve...")

    def teste_historia_portugal(self):
        self.assertEqual(
            obter_resposta("história de portugal"),
            "Portugal tem uma história rica que inclui os Descobrimentos e a expansão marítima."
        )

    def teste_cozinhar(self):
        self.assertEqual(
            obter_resposta("cozinhar"),
            "Cozinhar é uma arte que combina ingredientes, técnicas e criatividade."
        )

    def teste_programar(self):
        self.assertEqual(
            obter_resposta("programar"),
            "Programar é escrever instruções para que o computador execute tarefas."
        )
        self.assertEqual(
            obter_resposta("gosto de programar"),
            "Programar é escrever instruções para que o computador execute tarefas."
        )

    def teste_desenvolvimento(self):
        self.assertEqual(
            obter_resposta("desenvolvimento web"),
            "O desenvolvimento web envolve a criação de sites e aplicações web..."
        )
        self.assertEqual(
            obter_resposta("curso de desenvolvimento web"),
            "O desenvolvimento web envolve a criação de sites e aplicações web..."
        )
        self.assertEqual(
            obter_resposta("quero aprender desenvolvimento web"),
            "O desenvolvimento web envolve a criação de sites e aplicações web..."
        )
        self.assertEqual(
            obter_resposta("web desenvolvimento"),
            "O desenvolvimento web envolve a criação de sites e aplicações web..."
        )

    def teste_ia(self):
        self.assertEqual(
            obter_resposta("ia"),
            "A inteligência artificial é um campo da ciência da computação que se concentra na criação de sistemas que podem realizar tarefas que normalmente requerem inteligência humana."
        )
        self.assertEqual(
            obter_resposta("inteligência artificial"),
            "A inteligência artificial é um campo da ciência da computação que se concentra na criação de sistemas que podem realizar tarefas que normalmente requerem inteligência humana."
        )
        self.assertEqual(
            obter_resposta("fala-me sobre ia"),
            "A inteligência artificial é um campo da ciência da computação que se concentra na criação de sistemas que podem realizar tarefas que normalmente requerem inteligência humana."
        )

    def teste_saude(self):
        self.assertEqual(
            obter_resposta("saúde"),
            "A saúde é um estado de completo bem-estar físico, mental e social, e não apenas a ausência de doenças ou enfermidades."
        )
        self.assertEqual(
            obter_resposta("o que é saúde"),
            "A saúde é um estado de completo bem-estar físico, mental e social, e não apenas a ausência de doenças ou enfermidades."
        )
        self.assertEqual(
            obter_resposta("falar sobre saúde"),
            "A saúde é um estado de completo bem-estar físico, mental e social, e não apenas a ausência de doenças ou enfermidades."
        )

    def teste_indisposicao(self):
        self.assertEqual(
            obter_resposta("indisposição"),
            "Sintomas de indisposição podem incluir fadiga, dor de cabeça, náusea e outros sinais de que algo não está bem."
        )
        self.assertEqual(
            obter_resposta("tenho indisposição"),
            "Sintomas de indisposição podem incluir fadiga, dor de cabeça, náusea e outros sinais de que algo não está bem."
        )
        self.assertEqual(
            obter_resposta("sintomas de indisposição"),
            "Sintomas de indisposição podem incluir fadiga, dor de cabeça, náusea e outros sinais de que algo não está bem."
        )

    def teste_horas_e_data(self):
        hora_atual = datetime.now().strftime("%H:%M")
        data_atual = datetime.now().strftime("%d-%m-%Y")

        self.assertEqual(obter_resposta("que horas são"), f"São: {hora_atual} horas")
        self.assertEqual(obter_resposta("qual é a data"), f"Hoje é dia: {data_atual}")

    def teste_resposta_padrao(self):
        texto_aleatorio = "xyz123"
        self.assertEqual(obter_resposta(texto_aleatorio), f"Desculpa, não entendi a questão! {texto_aleatorio}")

        texto_aleatorio2 = "teste123"
        self.assertEqual(obter_resposta(texto_aleatorio2), f"Desculpa, não entendi a questão! {texto_aleatorio2}")

        texto_aleatorio3 = "banana azul"
        self.assertEqual(obter_resposta(texto_aleatorio3), f"Desculpa, não entendi a questão! {texto_aleatorio3}")

        texto_aleatorio4 = "isto não faz sentido"
        self.assertEqual(obter_resposta(texto_aleatorio4), f"Desculpa, não entendi a questão! {texto_aleatorio4}")


if __name__ == '__main__':
    unittest.main()
