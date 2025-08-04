# API de Formatação de Texto - Desafio Op2B

Este projeto implementa uma API em FastAPI para formatar textos com limite de caracteres por linha, com suporte para quebra de linhas e texto justificado.

---

## Funcionalidades

- Aceita texto com parágrafos para formatação.
- Limita o número de caracteres por linha.
- Texto pode ser enviado com quebras de linha.

---

## Endpoints

### 1. `/quebrar-texto` (JSON)

- Método: `POST`
- Content-Type: `application/json`
- Parâmetros:

```json
{
  "text": "string com texto, com quebras de linha representadas por \n",
  "limit": número inteiro (limite de caracteres por linha)
}
```

**Observação:**  
Ao enviar o texto via JSON, as quebras de linha devem ser representadas explicitamente como `\n` (exemplo: `"linha1\\nlinha2"`).

Exemplo de payload válido:

```json
{
  "text": "Exemplo da primeira linha.\nExemplo segunda linha do texto.",
  "limit": 40
}
```

---

### 2. `/justificar-texto` (texto puro)

- Método: `POST`
- Content-Type: `text/plain`
- Parâmetros:

```json
{
  "text": "string com texto, com quebras de linha representadas por \n",
  "limit": número inteiro (limite de caracteres por linha)
}
```

**Observação:**  
Ao enviar o texto via JSON, as quebras de linha devem ser representadas explicitamente como `\n` (exemplo: `"linha1\\nlinha2"`).

Exemplo de payload válido:

```json
{
  "text": "Exemplo da primeira linha.\nExemplo segunda linha do texto.",
  "limit": 40
}
```

---

## Como rodar o projeto

### Requisitos

- Python 3.8+
- pip

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/ViniciusMuniz-1/desafio-2025-07.git
cd desafio-2025-07.git
```

2. Crie o ambiente de desenvolvimento:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Para construir a imagem Docker:

```bash
cd strings
docker build -t op2b-strings .
```

4. Rodar o container

```
docker run -p 8000:8000 op2b-strings
```

---

## Processo de Resolução dos Desafios

A ideia central do desafio era criar uma API capaz de formatar textos de forma que cada linha tivesse um número máximo de caracteres, sem quebrar palavras no meio. Além disso, o texto poderia conter múltiplos parágrafos, e havia também a opção de justificar o conteúdo.

Para resolver isso, dividi a solução em duas partes principais:

- **Formatação simples:** quebra o texto em linhas respeitando o limite de caracteres e mantendo a integridade das palavras e parágrafos.
- **Justificação:** ajusta o espaçamento entre as palavras para que todas as linhas (exceto a última de cada parágrafo) fiquem alinhadas dos dois lados.

Também me preocupei em manter a estrutura do texto original, respeitando as quebras de parágrafo e facilitando a leitura.
---

## Como Utilizar a Solução

A API tem dois endpoints principais — um para formatar o texto em linhas limitadas e outro para justificar o conteúdo.

- Se você estiver enviando texto via JSON, lembre-se de que as quebras de linha precisam ser representadas como `\n`. Isso é necessário porque o JSON não aceita ENTERs diretamente dentro das strings.
- O parâmetro `limit` define o número máximo de caracteres por linha. Basta ajustar esse valor conforme sua necessidade.
- A resposta da API retorna o texto formatado da forma esperada: com quebras organizadas e, se solicitado, justificado.

---

## Tratamento de Erros e Exceções

O principal erro identificado foi o formato do texto enviado via JSON. Como o JSON não aceita quebras de linha reais dentro de strings, o cliente deve enviar as quebras como a sequência `\n` (barra invertida + n). Caso isso não seja feito, a API retorna um erro de decodificação JSON (`Unprocessable Entity`).

Para evitar esse erro:
- Para textos com múltiplas linhas via JSON, substituir ENTERs por `\n`.

Outros casos de erro podem incluir limites inválidos (não numéricos ou negativos), que a API pode tratar retornando mensagens claras de erro, mas o foco principal deste desafio foi o correto envio do texto com quebras de linha.

Outros erros, como valores inválidos no campo limit (ex: letras ou números negativos), também são tratados e retornam mensagens de erro apropriadas.