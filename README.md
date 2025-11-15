# 📧 AutoU - Classificação Automática de E-mails

## 🚀 Visão Geral
Este projeto foi desenvolvido para uma empresa do setor financeiro que recebe um alto volume de e-mails diariamente.  
O objetivo é automatizar a leitura e classificação dos e-mails e sugerir respostas automáticas, liberando tempo da equipe e evitando trabalho manual repetitivo.

---

## 🎯 Funcionalidades
- Upload de arquivos `.txt` ou `.pdf` com conteúdo de e-mails.
- Inserção direta de texto na interface web.
- Classificação automática em categorias:
  - Produtivo → requer ação ou resposta.
  - Improdutivo → não requer ação (felicitações, marketing).
  - Chamado → abertura de ticket de suporte.
  - Feedback Apreciativo → elogios.
  - Feedback Depreciativo → críticas.
- Exibição de:
  - Categoria atribuída.
  - Nível de confiança da classificação.
  - Sinais detectados (palavras-chave).
  - Resposta automática sugerida.
- Botão para copiar a resposta sugerida.

---

## 📂 Estrutura do Projeto
email/
│
├── static/
│   ├── imagens/
│   │   ├── autou_logo.png
│   │   └── background_autou.jpg
│   ├── style.css        # Estilos visuais
│   └── app.js           # Lógica frontend
│
├── templates/
│   └── index.html       # Interface web
│
├── app.py               # Backend Flask
├── classificacao.py     # Classificação (regras + Hugging Face)
├── nlp.py               # Pré-processamento de texto (spaCy)
├── resposta.py          # Geração de respostas automáticas
├── utilidades.py        # Leitura de arquivos .txt/.pdf
├── emails_dataset.csv   # Dataset de exemplo
├── requirements.txt     # Dependências
└── README.txt           # Documentação

---

## ⚙️ Instalação

No terminal do VS Code:

pip install flask
pip install transformers
pip install torch
pip install spacy
python -m spacy download pt_core_news_sm
pip install pdfminer.six
pip install -r requirements.txt
pip install sentencepiece
pip3 install protobuf

💡 Extensão recomendada no VS Code: Rainbow CSV (para visualizar o dataset).

---

## ▶️ Como Executar Localmente

cd email
python app.py

Abra no navegador:  
http://localhost:5000

---

## 🧠 Como Funciona

1. Upload ou texto → usuário envia e-mail.
2. Leitura → utilidades.py extrai conteúdo de .txt ou .pdf.
3. Pré-processamento → nlp.py limpa e lematiza o texto.
4. Classificação → classificacao.py aplica:
   - Regras simples (regex).
   - Modelo Hugging Face (zero-shot-classification).
5. Resposta → resposta.py gera mensagem automática adequada.
6. Interface → index.html + app.js exibem resultados.

---

## 📊 Dataset de Exemplo

Arquivo: emails_dataset.csv

Categorias:
- Produtivo → solicitações, contratos, status, suporte.
- Improdutivo → felicitações, promoções, spam.
- Chamado → abertura de tickets.
- Feedback Apreciativo → elogios.
- Feedback Depreciativo → críticas.

---

## 🌐 Deploy na Nuvem

Plataformas recomendadas:
- Render (Free) → simples para Flask.
- Hugging Face Spaces → ótimo para demos (pode usar Gradio).
- Vercel → mais voltado para frontend, exige setup extra para Python.

Procfile para Render:
web: gunicorn app:app

---

## 🎥 Vídeo Demonstrativo

Grave um vídeo de 3–5 minutos mostrando:
1. Introdução rápida ao desafio.
2. Upload de e-mail e classificação na interface.
3. Explicação técnica (pipeline, bibliotecas, modelo Hugging Face).
4. Conclusão com aprendizados.

---

## 🔮 Próximos Passos

- Treinar um modelo Hugging Face com dataset próprio (em vez de zero-shot).
- Expandir categorias (ex.: financeiro, jurídico, RH).
- Melhorar interface com recursos visuais e UX.
- Adicionar fallback rápido por regras para evitar cold start do modelo.

---

## 👨‍💻 Autor
Projeto desenvolvido por Diego como parte de um desafio de solução digital para automação de e-mails.