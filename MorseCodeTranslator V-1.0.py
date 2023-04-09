import winsound
letras = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '?',
    '!', ':', ';', '-', '/', '"', "'", '(', ')', '@', '=', '+', '_',
    '$', '&', 'É', 'Ä', 'Ñ', 'Ü', 'Ç', 'È', 'Š', 'Ë', 'ß'
]
letras_str = ''.join(letras)

codigo_morse = [
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-',
    '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--',
    '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....',
    '-....', '--...', '---..', '----.', '.-.-.-', '--..--', '..--..', '-.-.--', '---...',
    '-.-.-.', '-....-', '-..-.', '.-..-.', '.----.', '-.--.', '-.--.-', '.--.-.', '-...-',
    '.-.-.', '..--.-', '...-..-', '.-...', '..-..-', '.-.-', '--.--', '..--', '...--...'
]

opcao = 's'

while opcao != 'n':
    traduzir = input('Insira o que deseja traduzir: ').upper()
    traduzido = ''
    for letra in traduzir:
        if letra == ' ':
            traduzido += ' '
            continue
        if letra not in letras_str:
            print('Um caractere inserido não pode ser traduzido.')
            break
        idc = letras_str.find(letra)
        traduzido += f'{codigo_morse[idc]} '
    print(f'Tradução em Código Morse: {traduzido}')
    for som in traduzido:
        if som == '.':
            winsound.Beep(440, 250)
        elif som == '-':
            winsound.Beep(440, 500)
    opcao = input('Deseja traduzir algo mais?(s/n): ').lower()

print('-=-=-=- Programa encerrado -=-=-=-')