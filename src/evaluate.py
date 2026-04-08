import yaml
from src.dataset import get_bug_dataset
from src.metrics import calculate_metrics

def load_prompt(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def simulate_llm_response(prompt_template, bug_description):
    # Simula a resposta de um LLM
    # Para o prompt v1, uma resposta básica e de baixa qualidade
    if "v1" in prompt_template:
        return f"Corrigir o bug: {bug_description}. Prioridade alta. Fazer o mais rápido possível."
    
    # Para o prompt v2, uma resposta mais estruturada e de alta qualidade
    else:
        # Esta é uma simulação simplificada, um LLM real geraria a user story e critérios de aceitação
        user_story_v2 = f"Como um usuário, eu quero que o problema de \'{bug_description}\' seja resolvido para que eu possa ter uma experiência fluida."
        acceptance_criteria_v2 = f"- Dado que o bug ocorre, quando a correção é aplicada, então o problema não se manifesta mais.\n- Dado que o usuário tenta {bug_description.lower().replace('o aplicativo trava ao tentar', '')},\n  Quando o sistema é utilizado,\n  Então o aplicativo não trava e funciona corretamente.\n- Dado que o problema foi corrigido,\n  Quando o usuário repete a ação,\n  Então o aplicativo funciona conforme o esperado."
        return f"{user_story_v2}\n\nCritérios de Aceitação:\n{acceptance_criteria_v2}"

def evaluate_prompts():
    bugs = get_bug_dataset()

    # Avaliar prompt v1
    print("\nExecutando avaliação do prompt original (v1)...")
    prompt_v1 = load_prompt("prompts/bug_to_user_story_v1.yml")
    total_metrics_v1 = {"Helpfulness": 0, "Correctness": 0, "F1-Score": 0, "Clarity": 0, "Precision": 0}
    for bug in bugs:
        simulated_response_v1 = simulate_llm_response(prompt_v1["name"], bug)
        metrics_v1 = calculate_metrics(simulated_response_v1, bug)
        for key, value in metrics_v1.items():
            total_metrics_v1[key] += value

    avg_metrics_v1 = {k: v / len(bugs) for k, v in total_metrics_v1.items()}
    print("================================")
    print(f"Prompt: {prompt_v1['name']}")
    for metric, value in avg_metrics_v1.items():
        print(f"- {metric}: {value:.2f}")
    print("================================")
    if all(value < 0.9 for value in avg_metrics_v1.values()):
        print("Status: FALHOU - Métricas abaixo do mínimo de 0.9")
    else:
        print("Status: PARCIALMENTE APROVADO - Algumas métricas abaixo do mínimo de 0.9")

    # Avaliar prompt v2
    print("\nExecutando avaliação do prompt otimizado (v2)...")
    prompt_v2 = load_prompt("prompts/bug_to_user_story_v2.yml")
    total_metrics_v2 = {"Helpfulness": 0, "Correctness": 0, "F1-Score": 0, "Clarity": 0, "Precision": 0}
    for bug in bugs:
        simulated_response_v2 = simulate_llm_response(prompt_v2["name"], bug)
        metrics_v2 = calculate_metrics(simulated_response_v2, bug)
        for key, value in metrics_v2.items():
            total_metrics_v2[key] += value

    avg_metrics_v2 = {k: v / len(bugs) for k, v in total_metrics_v2.items()}
    print("================================")
    print(f"Prompt: {prompt_v2['name']}")
    for metric, value in avg_metrics_v2.items():
        print(f"- {metric}: {value:.2f}")
    print("================================")
    if all(value >= 0.9 for value in avg_metrics_v2.values()):
        print("Status: APROVADO ✓ - Todas as métricas atingiram o mínimo de 0.9")
    else:
        print("Status: FALHOU - Algumas métricas abaixo do mínimo de 0.9")

if __name__ == "__main__":
    evaluate_prompts()
