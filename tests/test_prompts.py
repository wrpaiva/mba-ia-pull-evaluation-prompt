import pytest
import yaml

def load_prompt(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

@pytest.fixture
def optimized_prompt():
    return load_prompt('prompts/bug_to_user_story_v2.yml')

def test_prompt_has_system_prompt(optimized_prompt):
    # Para prompts YAML, o 'system prompt' é geralmente a parte inicial do template que define o papel.
    # Vamos verificar se o template começa com uma definição de papel clara.
    assert 'template' in optimized_prompt
    assert optimized_prompt['template'].strip().startswith('Você é um Product Manager Sênior')

def test_prompt_has_role_definition(optimized_prompt):
    assert 'template' in optimized_prompt
    assert 'Product Manager' in optimized_prompt['template']

def test_prompt_mentions_format(optimized_prompt):
    assert 'template' in optimized_prompt
    assert 'formato "Como [tipo de usuário], eu quero [ação], para que [benefício/valor]."' in optimized_prompt['template']

def test_prompt_has_few_shot_examples(optimized_prompt):
    assert 'template' in optimized_prompt
    assert 'Exemplo de Few-shot Learning:' in optimized_prompt['template']
    assert 'Bug Original:' in optimized_prompt['template']
    assert 'User Story Otimizada:' in optimized_prompt['template']

def test_prompt_no_todos(optimized_prompt):
    assert 'template' in optimized_prompt
    assert '[TODO]' not in optimized_prompt['template']

def test_minimum_techniques(optimized_prompt):
    # As técnicas são documentadas na descrição do prompt para este exemplo
    assert 'description' in optimized_prompt
    description = optimized_prompt['description'].lower()
    techniques_found = 0
    if 'role prompting' in description: techniques_found += 1
    if 'few-shot learning' in description: techniques_found += 1
    if 'chain of thought' in description: techniques_found += 1
    # Adicione outras técnicas que você mencionou na descrição, se aplicável
    assert techniques_found >= 2
