from zxcvbn import zxcvbn
import re

def ctd_br(senha):
    original = senha['crack_times_display']
    texto = {"online_throttling_100_per_hour" : "Ataque online com limitação de tentativas (100 tentativas por hora):" , "online_no_throttling_10_per_second" : "Ataque online sem limitação de tentativas (10 tentativas por segundo):" , "offline_slow_hashing_1e4_per_second" : "Ataque offline com proteção de hashing lento (10.000 tentativas por segundo):" , "offline_fast_hashing_1e10_per_second" : "Ataque offline com hashing rápido (10 bilhões de tentativas por segundo):"} 
    traduz = [texto[a] for a in original]
    return traduz

def ctd_br2(senha):
    original = senha['crack_times_display'].values()
    texto = {"less than a second": "menos de um segundo","second": "segundo", "seconds": "segundos","minute": "minuto", "minutes": "minutos","hour" : "hora", "hours": "horas","day" : "dia", "days": "dias","month" : "mês", "months": "meses","year": "ano", "years": "anos","century": "século", "centuries": "séculos"}
    traduz = []
    for a in original:
        numero = re.search(r'\d+', a)  
        fixo = re.sub(r'\d+', '', a)
        if numero:
            a = numero.group() + ' ' + texto[fixo[1:]]
            traduz.append(a)
        else:
            a = texto[fixo]
            traduz.append(a)
    return traduz


def fbw_br(senha):
    original = senha['feedback']
    texto = {"This is a top-10 common password." : "Esta é uma das 10 senhas mais comuns.", "This is a top-100 common password." : "Esta é uma das 100 senhas mais comuns." , "Straight rows of keys are easy to guess." : "Filas retas de chaves são fáceis de adivinhar.","Short keyboard patterns are easy to guess." : "Padrões curtos de teclado são fáceis de adivinhar.", 'Repeats like "aaa" are easy to guess.': 'Repetições como "aaa" são fáceis de adivinhar.', 'Sequences like "abc" or "6543" are easy to guess.': 'Sequências como “abc” ou “6543” são fáceis de adivinhar.', 'Repeats like "abcabcabc" are only slightly harder to guess than "abc".': 'Repetições como "abcabcabc" são apenas um pouco mais difíceis de adivinhar do que "abc".', "This is a very common password.": "Esta é uma senha muito comum", "This is similar to a commonly used password.": "Esta senha é semelhante a uma senha comumente usada", "This is a word by itself.": "Esta senha é uma palavra sozinha", "This is a common password pattern.": "Esta senha segue um padrão de senha comum", "This is based on a common pattern.": "Esta senha segue um padrão comum", "This is a common name.": "Este é um nome comum", "This is a sequence of numbers.": "Esta é uma sequência de números", "This is a date.": "Esta senha parece ser uma data", "Recent years are easy to guess.": "Anos recentes são fáceis de adivinhar", "Avoid years that are associated with you.": "Evite anos associados a você", "Dates are often easy to guess.": "Datas geralmente são fáceis de adivinhar", "Common names and surnames are easy to guess." : "Nomes e sobrenomes comuns são fáceis de adivinhar.", "Names and surnames by themselves are easy to guess." : "Nomes e sobrenomes por si só são fáceis de adivinhar."}
    if original['warning'] in texto:
        return texto[original['warning']]
    elif print(original['warning']) is None:
        return 'Nenhum aviso a acrescentar'
    else:
        return original['warning']

def fbs_br(senha):
    original = senha['feedback']
    texto = {"Use a longer keyboard pattern with more turns.": "Use um padrão de teclado mais longo com mais voltas.", "Use a few words, avoid common phrases.": "Use algumas palavras, evite frases comuns","No need for symbols, digits, or uppercase letters": "Não há necessidade de símbolos, dígitos ou letras maiúsculas.", "Add another word or two. Uncommon words are better.": "Adicione mais uma ou duas palavras. Palavras incomuns são melhores.", "Avoid repeated words and characters.": "Evite palavras e caracteres repetidos", "Avoid sequences.": "Evite sequências", "Avoid recent years": "Evite usar anos recentes", "Avoid years that are associated with you.": "Evite anos que estejam associados a você", "Avoid dates and years that are associated with you.": "Evite datas e anos que estejam associados a você", "Use more characters.": "Use mais caracteres", "Add a symbol, number, or uppercase letter.": "Adicione um símbolo, número ou letra maiúscula", "Add another word or two.": "Adicione mais uma ou duas palavras", "Uncommon words are better.": "Palavras incomuns são melhores", "Capitalization doesn't help very much.": "Capitalização não ajuda muito", "All-uppercase is almost as easy to guess as all-lowercase": "Tudo em maiúsculas é quase tão fácil de adivinhar quanto tudo em minúsculas", "Reversed words aren't much harder to guess.": "Palavras invertidas não são muito mais difíceis de adivinhar", "Predictable substitutions like '@' instead of 'a' don't help very much.": "Substituições previsíveis como '@' em vez de 'a' não ajudam muito"}
    traduz = []
    for s in original['suggestions']:
        if s in texto:
            traduz.append(texto[s])
        else:
            traduz.append(s)    
    if len(traduz) >= 1:
        return traduz
    else:
        return 'Nenhuma sugestão a acrescentar.'



