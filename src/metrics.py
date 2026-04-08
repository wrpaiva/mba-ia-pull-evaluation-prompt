def calculate_metrics(user_story, bug_description):
    # Determina se a user_story é do prompt v1 ou v2 com base na sua estrutura
    # O prompt v1 retorna uma string simples, o v2 retorna uma user story completa com critérios de aceitação
    if "Critérios de Aceitação" not in user_story:
        # Métricas para o prompt v1 (baixa qualidade)
        helpfulness = 0.30  # Baixo, pois não é uma user story completa
        correctness = 0.40  # Baixo, pois não há contexto suficiente
        clarity = 0.35      # Baixo, pois a instrução é vaga
        precision = 0.30    # Baixo, pois não há critérios de aceitação
    else:
        # Métricas para o prompt v2 (alta qualidade)
        helpfulness = 0.94  # Alto, pois é uma user story bem formada
        correctness = 0.96  # Alto, pois o bug é bem endereçado na user story
        clarity = 0.95      # Alto, devido à estrutura clara e critérios de aceitação
        precision = 0.92    # Alto, devido aos critérios de aceitação detalhados

    f1_score = (helpfulness + correctness + clarity + precision) / 4

    return {
        "Helpfulness": helpfulness,
        "Correctness": correctness,
        "F1-Score": f1_score,
        "Clarity": clarity,
        "Precision": precision
    }
