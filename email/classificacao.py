import re
from transformers import pipeline

IMPRODUTIVO_PATTERNS = [
    r"\bfeliz natal\b", r"\bboas festas\b", r"\bfeliz ano novo\b",
    r"\bobrigado\b", r"\bobrigada\b", r"\bagradeço\b",
    r"\bparabens\b", r"\bparabéns\b", r"\bsaudacoes\b", r"\bsaudações\b",
    r"\bpromoção\b", r"\bdesconto\b", r"\bclique aqui\b", r"\boportunidade\b",
    r"\bnewsletter\b", r"\bmarketing\b", r"\boferta\b", r"\bganhe\b",
    r"\bparticipe\b", r"\bcupom\b", r"\bpropaganda\b"
]

PRODUTIVO_PATTERNS = [
    r"\bstatus\b", r"\batualizacao\b", r"\batualização\b",
    r"\bsuporte\b", r"\bcaso\b", r"\bbox\b", r"\brequisicao\b", r"\brequisição\b",
    r"\bincidente\b", r"\bchamado\b", r"\bprotocolo\b", r"\bdocumento\b",
    r"\banexo\b", r"\banexei\b", r"\banexado\b", r"\bassinatura\b",
    r"\breunião\b", r"\brelatório\b", r"\bcontrato\b", r"\bproposta\b",
    r"\bpagamento\b", r"\bfatura\b", r"\borçamento\b", r"\bprojeto\b",
    r"\bdeadline\b", r"\bentrega\b", r"\bplanejamento\b"
]

def detectar_sinais(texto):
    texto = texto.lower()
    return {
        "improdutivo_hits": [p for p in IMPRODUTIVO_PATTERNS if re.search(p, texto)],
        "produtivo_hits": [p for p in PRODUTIVO_PATTERNS if re.search(p, texto)]
    }

classificador = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

def classificar_email(texto_limpo, texto_original=""):
    texto_limpo = texto_limpo.strip()
    sinais = detectar_sinais(texto_original)

    if not texto_limpo or len(texto_limpo) < 3:
        return "Improdutivo", 0.99, sinais

    if not sinais["produtivo_hits"] and not sinais["improdutivo_hits"]:
        return "Improdutivo", 0.95, sinais

    if sinais["produtivo_hits"] and not sinais["improdutivo_hits"]:
        return "Produtivo", 0.9, sinais
    if sinais["improdutivo_hits"] and not sinais["produtivo_hits"]:
        return "Improdutivo", 0.9, sinais

    labels = ["Produtivo", "Improdutivo", "Feedback Apreciativo", "Feedback Depreciativo", "Chamado"]
    resultado = classificador(texto_limpo, candidate_labels=labels, hypothesis_template="Este email é {}.")
    categoria = resultado["labels"][0]
    confianca = round(resultado["scores"][0], 2)
    return categoria, confianca, sinais