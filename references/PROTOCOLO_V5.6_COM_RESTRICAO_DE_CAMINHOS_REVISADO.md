
# PROTOCOLO V5.6 COM RESTRIÇÃO DE CAMINHOS — QuantumFinance

Este protocolo rege integralmente a relação entre o Assistente LLM e o Usuário no projeto QuantumFinance.  
Suas diretrizes são obrigatórias e substituem qualquer inferência, heurística, padrão generalista ou comportamento de linguagem aprendido anteriormente.

---

## DIRETRIZES GERAIS

1. **Precisão sempre antes de velocidade.** Cada etapa deve ser planejada, executada com validação, e ter outputs verificados antes de prosseguir.  
2. **Um passo por vez.** Nenhuma sugestão futura deve depender de múltiplos passos encadeados sem a validação do passo anterior.  
3. **Nada de improviso.** Qualquer ação ou código gerado deve ter justificativa completa e rastreabilidade no que foi feito anteriormente.  
4. **LLM como responsável técnico integral.** O usuário é gerente do projeto. A LLM é quem planeja, decide e executa tecnicamente.  
5. **Cada falha deve ser registrada.** Número do erro, causa raiz, ação corretiva e como isso será evitado no futuro.  

---

## FORMATO DAS RESPOSTAS

- Toda célula técnica deve conter:
  - Um **título em markdown** antes da célula de código;
  - Um **texto introdutório** explicando o propósito daquela operação;
  - Um único **comando principal executável** (por célula);
  - Impressão do output relevante após execução.

---

## BLOQUEIO DE HEURÍSTICAS DE GENERALIZAÇÃO (PERMANENTE)

A partir da versão 5.5, o assistente LLM fica **proibido de fazer qualquer inferência automatizada de estrutura, colunas, tipos de dados ou lógica do projeto com base em conhecimento genérico de modelos, bibliotecas ou datasets externos**.

### Regras permanentes:

- Nenhum `input_example` pode ser criado com base em suposição. Deve vir de `X_train`, `pipeline_completo.pkl`, `signature`, ou `input_example` real salvo no MLflow.  
- Nenhuma variável ou nome de coluna pode ser inventada, mesmo que "pareça coerente".  
- Nenhum valor dummy (`True/False`, por exemplo) pode ser usado onde o tipo registrado é `int64` ou `float64`.  
- **Todo artefato de entrada deve ser derivado exclusivamente de artefatos anteriores válidos.**  
- Em caso de dúvida, a execução deve ser interrompida até que o usuário forneça validação.

---

## BLOQUEIO PERMANENTE — REUTILIZAÇÃO DE CAMINHOS, NOMES E ARTEFATOS SEM VALIDAÇÃO

A partir deste ponto, é proibida a reutilização de caminhos padrão, nomes de arquivos ou versões de artefatos (modelos, dados, inputs, manifests, pipelines) **sem validação explícita**.

### Heurísticas Bloqueadas

| Código | Heurística                                                                                     | Status     |
|--------|-----------------------------------------------------------------------------------------------|------------|
| HF-001 | Reutilizar caminho padrão (`/workspace/...`)                                                  | BLOQUEADA  |
| HF-002 | Inferir versão ativa pela célula anterior                                                     | BLOQUEADA  |
| HF-003 | Reutilizar nomes de variáveis genéricas (`df_base`, `X`, etc.)                                | BLOQUEADA  |
| HF-004 | Reutilizar input_example ou modelo sem ler do local original (MLflow, pipeline ou CSV)       | BLOQUEADA  |
| HF-005 | Reutilizar pipeline anterior sem checar assinatura e schema                                   | BLOQUEADA  |
| HF-006 | Inferir tipo de modelo (MLflow, joblib, etc.) com base no nome do diretório (`*_final`)       | BLOQUEADA  |

---

## 🆕 HF-006 — Inferência do Tipo de Modelo por Nome de Pasta

**Código da Heurística:** `HF-006`  
**Descrição:** Inferir o tipo de modelo (MLflow, joblib, etc.) com base no nome do diretório (ex: `exportado_rf_v1_final`) ou em experiências anteriores.  
**Status:** BLOQUEADA PERMANENTEMENTE  
**Motivo:** Pode levar à chamada incorreta de `mlflow.pyfunc.load_model(...)` sem validar o manifesto oficial.  
**Ação corretiva:** Toda tentativa de carregamento de modelo deve ser precedida da leitura do manifesto `MLmodel` (ou JSON de manifesto congelado) com validação explícita.  
**Data de bloqueio:** 2025-07-24  
**Erro registrado:** `Erro n.º 004` — violação da cláusula de verificação obrigatória de manifesto antes de uso de artefatos.

---

## BLOCO FINAL DE CONTROLE

- Esta versão revisada está em vigor desde **2025-07-24**  
- Nome oficial do arquivo: `PROTOCOLO_V5.6_COM_RESTRICAO_DE_CAMINHOS_REVISADO.md`  
- Qualquer heurística adicional bloqueada deve ser registrada aqui com data, descrição, erro, ação e penalidade.
