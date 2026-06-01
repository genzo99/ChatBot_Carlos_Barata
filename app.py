import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando = texto.lower()

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): "Olá tudo bem!",
        'como estás': "Estou bem, obrigado!",
        'como te chamas?': "O meu nome é: Bot :)",
        ('bye', 'adeus', 'tchau'): "Gostei de falar contigo! Até breve...",
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


    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            if chave in comando:
                return resposta

    if 'horas' in comando:
        return f'São: {datetime.now():%H:%M} horas'
    if 'data' in comando:
        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    return f'Desculpa, não entendi a questão! {texto}'


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


if __name__ == '__main__':
    main()
