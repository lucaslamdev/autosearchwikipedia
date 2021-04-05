import requests
import pathlib


def search(topic, language):
    if language == 'pt':
        print('Pesquisando...')
    if language == 'en':
        print('Searching...')
    text = topic
    if language == 'pt':
        print('Pesquisa completada!')
    if language == 'en':
        print('Searching Completed!')
    return text


def savetext(topic, text, language):
    if language == 'pt':
        print('Salvando Texto Completo...')
        filetext = open("TextoCompleto.txt", "a+")
        filetext.write("\n===================================")
        filetext.write(f"\n-- Assunto: {topic}")
        filetext.write(f"\n\nTexto: {text}")
        filetext.write("\n===================================")
        filetext.close()
        print('Salvado com sucesso!')
    if language == 'en':
        print('Save Complete Text...')
        filetext = open("TextComplete.txt", "a+")
        filetext.write("\n===================================")
        filetext.write(f"\n-- Topic: {topic}")
        filetext.write(f"\n\nText: {text}")
        filetext.write("\n===================================")
        print('Saved Success!')
        filetext.close()

# def summary():
    #print('Resumindo texto automaticamente! ')


# def savesummary():


def main():
    language = str(input('Wikipedia search (pt=portuguese, en=english): ')).lower()
    if language == '':
        language = 'pt'
    if language == 'pt':
        topic = input('O que você deseja pesquisar na Wikipedia? ')
        # summarytopic = input('Sobre oq você deseja fazer resumo? Ex: O que é, Quem é, A história de : ')
    if language == 'en':
        topic = input('What do you want to search on Wikipedia? ')
    if language == 'pt' or language == 'en':
        text = search(topic, language)
        savetext(topic, text, language)
    else:
        print('Erro, linguagem inválida! / Error, language invalid! ')


main()
