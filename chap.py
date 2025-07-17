from termcolor import colored   

casas = {
    "Grifinória": ("red", "bold"),
    "Sonserina": ("green", "bold"),
    "Corvinal": ("blue", "bold"),
    "Lufa-Lufa": ("yellow", "bold")
}

def print_casa(texto, casa):
    cor, estilo = casas.get(casa, ("white", None))
    print(colored(texto, cor, attrs=[estilo]))



print("Olá eu sou o Chapéu Seletor! Não há nada escondido em sua cabeça ")
 #aqui colocar algo introduzindo como dumbledore fazia nos livros/filmes

nomealuno = input("Qual seu nome ") #aqui colocamos o nome do aluno/aluna

#abaixo as casa de hogwarts
casa1 = 'grifinoria'
casa2 = 'sonserina'
casa3 = 'lufa-lufa'
casa4 = 'corvinal'

#abaixo pontuação
grifinoria = 0
sonserina = 0
lufalufa = 0
corvinal = 0

print(f'ola {nomealuno}, seja bem vindo a Hogwarts, por favor,sente-se no cadeira para o chapéu seletor lhe dizer a qual casa pertence ')

def escolhecasa():
    global grifinoria, sonserina, lufalufa, corvinal
    resposta = input(f"\nCHAPÉU SELETOR: Quem sabe sua moradia é a {casa1}, quem sabe é na {casa3} que você vai morar, Ou será a velha e sábia {casa4}, ou então quem sabe a {casa2} será a sua casa")
    if resposta == casa1:
        print("ah, você gosta da grinifinória então, hum....") # aqui adiciona um ponto para grifinória um para lufalufa e tira 1 da sonserina
        grifinoria += 1
        lufalufa += 1
        sonserina -= 1
    elif resposta == casa2:
        print("ah, você gosta da sonserina então, hum....") #aqui adiciona um ponto para sonserina
        sonserina += 1
        grifinoria -= 1
    elif resposta == casa3:
        print("ah, você gosta da lufalufa então, hum....") #aqui adiciona um ponto para lufalufa
        lufalufa += 2
        grifinoria += 1
        
    elif resposta == casa4:
        print("ah, você gosta da corvinal então, hum....") #aqui adiciona um ponto para corvinal
        corvinal += 2
        grifinoria -= 1
    else:
        print("resposta invalida"    )    


        
    # resposta2 = input("1. O sábio. 2. O bom 3. O Grande 4. O ousado")
def escolhecasa2():
    global grifinoria, sonserina, lufalufa, corvinal 
    print(f'Preciso saber mais de você, {nomealuno}, me diga...')
    print('Como você gostaria de ser conhecido pela história? ') 
    resposta2 = input("1. O sábio. 2. O bom 3. O Grande 4. O ousado\n")        

    if "1" in resposta2:  # O sábio
        print('Hmm... inteligência acima de tudo.')
        corvinal += 2
        lufalufa += 1
    elif "2" in resposta2:  # O bom
        print('Ah sim, valoriza a bondade...')
        lufalufa += 2
        grifinoria += 1
    elif "3" in resposta2:  # O Grande
        print(f'Bela resposta, {nomealuno}, ambição é importante.')
        sonserina += 2
        corvinal += 1
    elif "4" in resposta2 or "ousado" in resposta2:
        print('Ousadia! Isso cheira à Grifinória.')
        grifinoria += 2
        sonserina += 1
    else:
        print(f"Não te entendi, {nomealuno}. Pode repetir.")
    

    
    print("Você se deparou com alguém sofrendo bulllying. O que você faz?")
    resposta3 = input('1. Enfrento o agressor\n'
                  '2. Ignoro a situação\n'
                  '3. Uso um argumento lógico pra intervir\n'
                  '4. Peço educadamente para parar\n')

    if "1" in resposta3:
        print('Corajoso! Isso é típico da Grifinória.')
        grifinoria += 2
        lufalufa += 1
    elif "2" in resposta3:
        print(f'Hmm... pensei que você fosse mais gentil, {nomealuno}.')
        sonserina += 2
    elif "3" in resposta3:
        print('Sabedoria e inteligência, muito Corvinal!')
        corvinal += 2
        grifinoria += 1
    elif "4" in resposta3:
        print('Empatia e gentileza... isso é Lufa-Lufa!')
        lufalufa += 2
        grifinoria += 1
    else:
        print(f"Não te entendi, {nomealuno}. Pode repetir.")
   

    print("Você acorda após um pesadelo. Sobre o que ele era?")
    resposta4 = input('1. Perda de alguém querido\n'
                  '2. Ser forçado a seguir regras\n'
                  '3. Ir mal na escola\n'
                  '4. Tratar mal um amigo\n')
    if "1" in resposta4:
        print('Sensibilidade... pode ser Lufa-Lufa ou Grifinória.')
        lufalufa += 2
        grifinoria += 1
    elif "2" in resposta4:
        print('Espírito livre e rebelde... Sonserina talvez.')
        sonserina += 2
        grifinoria += 1
    elif "3" in resposta4:
        print('Aprecia o conhecimento, isso é Corvinal.')
        corvinal += 2
        lufalufa += 1
    elif "4" in resposta4:
        print('Gentileza é uma grande virtude.')
        lufalufa += 2
        corvinal += 1
    else:
        print(f"Não te entendi, {nomealuno}. Pode repetir.")

    maior = max(grifinoria, sonserina, lufalufa, corvinal)
    if maior == grifinoria:
        print_casa(f"\nParabéns, {nomealuno}! Sua casa é... GRIFINÓRIA!!! 🦁", "Grifinória")
    elif maior == sonserina:
        print_casa(f"\nParabéns, {nomealuno}! Sua casa é... SONSERINA!!! 🐍", "Sonserina")
    elif maior == lufalufa:
            print_casa(f"\nParabéns, {nomealuno}! Sua casa é... LUFA-LUFA!!! 🦡", "Lufa-Lufa")
    elif maior == corvinal:
            print(f"\nParabéns, {nomealuno}! Sua casa é... CORVINAL!!! 🦅", "Corvinal")
    else:
        print_casa("Empate mágico! O diretor decidirá com sabedoria...")        

escolhecasa()
escolhecasa2()