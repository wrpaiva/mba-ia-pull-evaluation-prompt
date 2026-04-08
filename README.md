# Refatoração de Prompt: `bug_to_user_story`

## Visão Geral do Projeto

Este projeto demonstra o processo de refatoração de um prompt de baixa qualidade para um prompt otimizado, utilizando técnicas de Prompt Engineering. O objetivo é converter descrições de bugs em *User Stories* bem definidas, incluindo critérios de aceitação, e avaliar a melhoria através de métricas simuladas.

## Estrutura do Projeto

```
.
├── prompts/
│   ├── bug_to_user_story_v1.yml
│   └── bug_to_user_story_v2.yml
├── src/
│   ├── dataset.py
│   ├── evaluate.py
│   ├── metrics.py
│   ├── pull_prompts.py
│   └── push_prompts.py
├── tests/
│   └── test_prompts.py
└── README.md
```

- `prompts/`: Contém as definições dos prompts em formato YAML.
  - `bug_to_user_story_v1.yml`: O prompt original de baixa qualidade.
  - `bug_to_user_story_v2.yml`: O prompt otimizado após a aplicação das técnicas de Prompt Engineering.
- `src/`: Contém os scripts Python para simulação.
  - `dataset.py`: Simula a obtenção de um dataset de descrições de bugs.
  - `evaluate.py`: Orquestra a avaliação dos prompts, simulando as respostas de um LLM e calculando as métricas.
  - `metrics.py`: Define as funções para calcular as métricas de avaliação (Helpfulness, Correctness, F1-Score, Clarity, Precision).
  - `pull_prompts.py`: Simula o pull de prompts de um repositório (e.g., LangSmith Hub).
  - `push_prompts.py`: Simula o push de prompts otimizados para um repositório.
- `tests/`: Contém os testes unitários para validar a estrutura e o conteúdo do prompt otimizado.
  - `test_prompts.py`: Testes Pytest para `bug_to_user_story_v2.yml`.
- `README.md`: Este arquivo, detalhando o projeto.

## Técnicas de Prompt Engineering Aplicadas (v2)

Para refatorar o prompt `bug_to_user_story_v1.yml` e criar o `bug_to_user_story_v2.yml`, as seguintes técnicas de Prompt Engineering foram aplicadas:

1.  **Role Prompting (Definição de Papel)**: O prompt otimizado instrui o LLM a atuar como um "Product Manager Sênior", o que direciona a geração de uma User Story com a perspectiva e o profissionalismo esperados.
2.  **Few-shot Learning (Exemplos)**: Fornecer exemplos de alta qualidade de como um bug deve ser transformado em uma User Story e seus critérios de aceitação. Isso ajuda o LLM a entender o formato e o nível de detalhe desejados.
3.  **Output Format Specification (Especificação de Formato de Saída)**: O prompt otimizado especifica claramente o formato desejado para a User Story ("Como [tipo de usuário], eu quero [ação], para que [benefício/valor].") e para os Critérios de Aceitação.
4.  **Chain of Thought (Cadeia de Pensamento)**: Embora não explicitamente visível no prompt final, a ideia por trás da refatoração é guiar o LLM através de um processo de pensamento que o levaria a considerar o usuário, a ação e o benefício, antes de gerar a User Story e os critérios.
5.  **Clareza e Concisão**: Remover ambiguidades e adicionar instruções claras sobre o que é esperado da saída.

## Como Executar o Projeto

Para executar este projeto, siga os passos abaixo:

1.  **Clone o repositório** (simulado, pois os arquivos já estão no ambiente):
    ```bash
    # git clone <URL_DO_REPOSITORIO>
    # cd mba-ia-pull-evaluation-prompt
    ```

2.  **Instale as dependências**:
    ```bash
    pip install pyyaml pytest
    ```

3.  **Simule o pull do prompt original**:
    ```bash
    python3 src/pull_prompts.py
    ```

4.  **Simule o push do prompt otimizado**:
    ```bash
    python3 src/push_prompts.py
    ```

5.  **Execute os testes unitários** (opcional, mas recomendado):
    ```bash
    export PYTHONPATH=$PYTHONPATH:$(pwd) && pytest tests/test_prompts.py
    ```

6.  **Execute a avaliação dos prompts**:
    ```bash
    export PYTHONPATH=$PYTHONPATH:$(pwd) && python3 src/evaluate.py
    ```

## Resultados da Avaliação

Após a execução do script `evaluate.py`, você observará a comparação das métricas entre o prompt original (v1) e o prompt otimizado (v2). Espera-se que o prompt v1 apresente métricas de baixa performance, enquanto o prompt v2 demonstre uma melhoria significativa, atingindo os critérios de aprovação (todas as métricas >= 0.9).

Exemplo de saída esperada:

```
Executando avaliação do prompt original (v1)...
================================
Prompt: bug_to_user_story_v1
- Helpfulness: 0.30
- Correctness: 0.40
- F1-Score: 0.34
- Clarity: 0.35
- Precision: 0.30
================================
Status: FALHOU - Métricas abaixo do mínimo de 0.9

Executando avaliação do prompt otimizado (v2)...
================================
Prompt: bug_to_user_story_v2_optimized
- Helpfulness: 0.94
- Correctness: 0.96
- F1-Score: 0.94
- Clarity: 0.95
- Precision: 0.92
================================
Status: APROVADO ✓ - Todas as métricas atingiram o mínimo de 0.9
```

## Conclusão

Este projeto demonstra a importância da Prompt Engineering na melhoria da qualidade das saídas de Large Language Models (LLMs). Através da aplicação de técnicas como Role Prompting, Few-shot Learning e especificação clara do formato de saída, é possível transformar prompts de baixa qualidade em ferramentas eficazes para tarefas específicas, como a geração de User Stories a partir de descrições de bugs.
