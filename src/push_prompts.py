import os

def push_prompts():
    print("Simulando push do prompt otimizado para o LangSmith...")
    if os.path.exists("prompts/bug_to_user_story_v2.yml"):
        print("Prompt 'bug_to_user_story_v2.yml' encontrado. Simulação de push bem-sucedida.")
        # Em um cenário real, aqui haveria a lógica para fazer push para o LangSmith
        # com metadados e versionamento.
        print("Metadados simulados: tags=['refatorado', 'few-shot', 'role-prompting'], description='Prompt otimizado para conversão de bug em user story.'")
    else:
        print("Erro: Prompt 'bug_to_user_story_v2.yml' não encontrado. Não foi possível simular o push.")

if __name__ == "__main__":
    push_prompts()
