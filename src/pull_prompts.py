import os

def pull_prompts():
    print("Simulando pull do prompt leonanluppi/bug_to_user_story_v1...")
    # Em um cenário real, aqui haveria a lógica para puxar do LangSmith Hub
    # Por simplicidade, vamos apenas verificar se o arquivo existe localmente
    if os.path.exists('prompts/bug_to_user_story_v1.yml'):
        print("Prompt 'bug_to_user_story_v1.yml' encontrado localmente.")
    else:
        print("Erro: Prompt 'bug_to_user_story_v1.yml' não encontrado. Por favor, crie-o manualmente para a simulação.")

if __name__ == "__main__":
    pull_prompts()
