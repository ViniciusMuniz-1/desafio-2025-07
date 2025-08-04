# Desafio 1: Strings

Após ler o [Coding Style do kernel Linux](https://www.kernel.org/doc/html/v4.10/process/coding-style.html), você descobre a mágica que é ter
linhas de código com no máximo 80 caracteres cada uma.

Assim, você decide que de hoje em diante seus e-mails enviados também seguirão
um padrão parecido e resolve desenvolver uma API para te ajudar com isso.
Contudo, sua API aceitará no máximo 40 caracteres por linha.

Usando Python, implemente um endpoint que receba:

1. um texto qualquer;
2. um limite de comprimento;

e seja capaz de gerar os outputs dos desafios abaixo.

## Exemplo input

`Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.`

`Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.`

O texto deve ser parametrizável e você pode, se quiser, utilizar um texto de
input de sua preferência.

### Parte 1 - limite de caracteres

Você deve seguir o exemplo de output [deste arquivo](output_parte1.txt), em que basta o texto
possuir, no máximo, 40 caracteres por linha. **As palavras não podem ser**
**quebradas no meio.**

### Parte 2 - limite de caracteres e formatação

O exemplo de output está [neste arquivo](output-parte2.txt), em que, além dos requisitos da Parte 1,
o texto deve estar **justificado**.

### Extra

- Dispobinibilize a possibilidade de parametrização da quantidade de caracteres
por linha.
