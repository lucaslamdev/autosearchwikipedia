import Algorithmia


def search(topic, language):
    if language == 'pt':
        print('Pesquisando...')
    if language == 'en':
        print('Searching...')
    # Connect API Algorithimia and "Download" Wikipedia Text
    # Connecta na API da Algorithimia e "Baixa" texto da Wikipedia
    algorithimiainput = {
        "articleName": topic,
        "lang": language
    }
    apikeyfile = open("algorithmia.txt", "r")
    apikey = apikeyfile.read()
    client = Algorithmia.client(apikey)
    algo = client.algo('web/WikipediaParser/0.1.2')
    text = algo.pipe(algorithimiainput).result
    if language == 'pt':
        print('Pesquisa completada!')
    if language == 'en':
        print('Searching Completed!')
    return text


def savetext(topic, text, language):
    if language == 'pt':
        print('Salvando Texto Completo...')
        filetext = open("TextoCompleto.txt", "a+", encoding="utf-8")
        filetext.write("\n===================================")
        filetext.write(f"\n-- Assunto: {topic}")
        filetext.write(f"\n\nTexto: {text}")
        filetext.write("\n===================================")
        filetext.close()
        print('Salvado com sucesso!')
    if language == 'en':
        print('Save Complete Text...')
        filetext = open("TextComplete.txt", "a+", encoding="utf-8")
        filetext.write("\n===================================")
        filetext.write(f"\n-- Topic: {topic}")
        filetext.write(f"\n\nText: {text}")
        filetext.write("\n===================================")
        print('Saved Success!')
        filetext.close()


# def summary(text, summarytopic):
# print('Resumindo texto automaticamente...')
# summarytext = 'teste'
# return summarytext


# def savesummary(summarytext, language, topic, summarytopic):
#    if language == 'pt':
#        print('Salvando Texto Resumido...')
#        filetext = open("TextoResumido.txt", "a+", encoding="utf-8")
#        filetext.write("\n===================================")
#        filetext.write(f"\n-- Assunto: {topic}")
#        filetext.write(f"\n--- Assunto resumo: {summarytopic}")
#        filetext.write(f"\n\nSummary Texto: {summarytext}")
#        filetext.write("\n===================================")
#        filetext.close()
#        print('Salvado com sucesso!')
#    if language == 'en':
#       print('Save Complete Text...')
#        filetext = open("SummaryText.txt", "a+", encoding="utf-8")
#       filetext.write("\n===================================")
#        filetext.write(f"\n-- Topic: {topic}")
#        filetext.write(f"\n--- Summary Topic: {summarytopic}")
#       filetext.write(f"\n\nSummary Text: {summarytext}")
#        filetext.write("\n===================================")
#       print('Saved Success!')
#       filetext.close()


def main():
    language = str(input('Wikipedia search (pt=portuguese, en=english): ')).lower()
    if language == '':
        language = 'pt'
    if language == 'pt':
        topic = input('O que você deseja pesquisar na Wikipedia? ')
        # summarytopic = input('Sobre oq você deseja fazer resumo? Ex: O que é, Quem é, A história de : ')
    if language == 'en':
        topic = input('What do you want to search on Wikipedia? ')
        # summarytopic = input('What do you want to search summary? Ex: What is, Who is, The History Of : ')
    if language == 'pt' or language == 'en':
        text = search(topic, language)
        savetext(topic, text, language)
        # summarytext = summary(text, summarytopic)
        # savesummary(summarytext, language, topic, summarytopic)

    else:
        print('Erro, linguagem inválida! / Error, language invalid! ')


main()
