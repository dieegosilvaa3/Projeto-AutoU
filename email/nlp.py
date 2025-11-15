import re
import unicodedata
import spacy

nlp = spacy.load("pt_core_news_sm")
PALAVRAS_VAZIAS = set([
    "a","o","os","as","de","do","da","dos","das",
    "e","para","por","com","sem","em","no","na","nos","nas",
    "um","uma","uns","umas","que","se","eu","você","ele","ela"
])

def formate(texto):
    texto = unicodedata.normalize("NFKD", texto).encode("ASCII", "ignore").decode("ASCII")
    texto = texto.lower()
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()

def preparar_texto(texto):
    t = formate(texto)
    documento = nlp(t)
    tokens = []
    for token in documento:
        if token.is_stop or token.is_punct or token.like_num:
            continue
        lemma = token.lemma_.strip()
        if lemma and lemma not in PALAVRAS_VAZIAS:
            tokens.append(lemma)
    return " ".join(tokens)