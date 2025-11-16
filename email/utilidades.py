def ler_arquivo(arquivo_storage):
    nome_arquivo = arquivo_storage.filename.lower()
    if nome_arquivo.endswith(".txt"):
        return arquivo_storage.read().decode("utf-8", errors="ignore")
    if nome_arquivo.endswith(".pdf"):
        from pdfminer.high_level import extract_text
        import tempfile, os
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as copia_arquivo:
            arquivo_storage.save(copia_arquivo.name)
            texto = extract_text(copia_arquivo.name)
        os.remove(copia_arquivo.name)
        return texto
    return arquivo_storage.read().decode("utf-8", errors="ignore")