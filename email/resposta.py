def gerar_resposta(label, texto_original="", sinais=None):
    sinais = sinais or {}
    texto = texto_original.lower()

    respostas = {
        "Improdutivo": (
            "Olá,\n\n"
            "Agradecemos sua mensagem. Como não há ação necessária, "
            "não abriremos um chamado neste momento. Se precisar de suporte "
            "ou tiver uma solicitação específica, é só responder este email.\n\n"
            "Atenciosamente,\nEquipe de Suporte"
        ),
        "Feedback Apreciativo": (
            "Olá,\n\n"
            "Ficamos felizes com seu retorno positivo! É ótimo saber que nosso atendimento foi satisfatório. "
            "Conte conosco sempre que precisar.\n\n"
            "Atenciosamente,\nEquipe de Suporte"
        ),
        "Feedback Depreciativo": (
            "Olá,\n\n"
            "Agradecemos seu feedback e lamentamos que sua experiência não tenha sido positiva. "
            "Vamos analisar internamente para melhorar nosso atendimento. "
            "Se quiser detalhar mais, estamos à disposição.\n\n"
            "Atenciosamente,\nEquipe de Suporte"
        ),
        "Chamado": (
            "Olá,\n\n"
            "Identificamos uma solicitação de suporte. Para abrir o chamado, "
            "informe: descrição do problema, impacto, frequência, print da tela (se possível) "
            "e o horário de ocorrência. Assim encaminharemos ao time técnico.\n\n"
            "Atenciosamente,\nEquipe de Suporte"
        )
    }

    if label in respostas:
        return respostas[label]

    if any(p in texto for p in ["status", "atualiza", "protocolo"]):
        return (
            "Olá,\n\n"
            "Recebemos sua solicitação de atualização de status. "
            "Por favor, confirme o número do protocolo/caso para agilizar a verificação. "
            "Assim que recebermos, retornaremos com o posicionamento.\n\n"
            "Atenciosamente,\nEquipe de Suporte"
        )

    if any(p in texto for p in ["anexo", "arquivo", "documento"]):
        return (
            "Olá,\n\n"
            "Obrigado pelo envio do arquivo. Vamos validar o conteúdo e, "
            "se houver pendências, retornaremos solicitando complementos. "
            "Caso tenha um número de caso relacionado, inclua no assunto para acelerar a tratativa.\n\n"
            "Atenciosamente,\nEquipe de Suporte"
        )

    return (
        "Olá,\n\n"
        "Recebemos sua mensagem e vamos analisar internamente. "
        "Se houver número de caso ou protocolo, inclua para acelerar o atendimento. "
        "Retornaremos em breve com um posicionamento.\n\n"
        "Atenciosamente,\nEquipe de Suporte"
    )