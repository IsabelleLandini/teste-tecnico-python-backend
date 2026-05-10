def calcular_diagnostico(registros):
    media_foco = round(sum(r.nivel_foco for r in registros) / len(registros), 2)
    # Volume de produtividade acumulada
    tempo_total = sum(r.tempo_minutos for r in registros)

    # Feedback baseado em análise de produtividade do usuário
    if media_foco < 3:
        feedback = 'Pausas mais longas e menos notificações podem ajudar.'
    elif media_foco <= 4:
        feedback = 'Seu foco está bom, mas ainda há espaço para melhorar.' 
    else:
        feedback = 'Você está em uma maratona produtiva de alto nível!'
    # Retorno estruturado do diagnóstico final
    return {
        'media_foco': media_foco,
        'tempo_total_focado': tempo_total,
        'feedback': feedback
    }
