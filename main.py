import requests

def search(topic, language):
    if language == 'pt':
        print('Pesquisando...')
    if language == 'en':
        print('Searching...')


    text =
    return text

def savetext(text):
    print('Salvando texto completo...')

def summary():
    print('Resumindo texto automaticamente! ')

def savesummary():


def main():
    language = str(input('Wikipedia search (pt=portuguese, en=english): ')).lower()
    if language == '':
        language = 'pt'
    if language == 'pt':
        topic = input('O que você deseja pesquisar na Wikipedia? ')
        summarytopic = input('Sobre oq você deseja fazer resumo? Ex: O que é, Quem é, A história de : ')
    if language == 'en':
        topic = input('What do you want to search on Wikipedia? ')
    if language == 'pt' or language == 'en':
        text = search(topic, language)
        savetext(text)
        summary()


main()
