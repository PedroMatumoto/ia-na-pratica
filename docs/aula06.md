<div align="center">

# Lendo o Inlegível
### Aula 6: Extração de Dados em Arquivos Complexos (PDFs e IA)

<br>

📱 **Material da Aula 6:**
`https://github.com/pedromatumoto/ia-na-pratica/`

</div>

---

## 1. O Mundo Real não vem em Excel

Na aula passada, o Pandas processou arquivos `.csv` perfeitos. Mas muitas vezes na realidade, os dados estão presos em formatos não estruturados:

* Notas Fiscais em PDF.
* Relatórios gerenciais antigos exportados em `.txt`.
* E-mails de clientes.

**O Problema:** Como extraímos apenas o valor do imposto ou o CNPJ de uma folha de PDF com 30 parágrafos de texto inútil?

---

## 2. A Força Bruta: Expressões Regulares (Regex)

Antes da IA, a extração de texto dependia de **Regex** (Regular Expressions). É uma linguagem matemática para encontrar padrões em texto.

* **Exemplo:** `\d{3}\.\d{3}\.\d{3}-\d{2}` encontra *qualquer* CPF num texto gigante.
* **A Vantagem:** É incrivelmente rápido e barato (custa zero).
* **O Problema (Fragilidade):** Se o cliente digitar o CPF sem pontos (apenas números), o Regex quebra. Se o layout do PDF mudar, o script de extração inteiro para de funcionar.

---

## 3. A Solução Inteligente: IA como Extrator

Em vez de escrevermos dezenas de regras complexas (`if/else` e Regex) para tentar "adivinhar" onde o dado está no PDF, usamos o modelo de Inteligência Artificial para **ler o PDF**.

* Lembram-se da Aula 3 (Structured JSON Outputs)?
* Nós enviamos o texto sujo do PDF para a IA e forçamos o LLM a devolver um objeto JSON limpo:
  `{"cnpj": "...", "valor_total": "...", "data": "..."}`

---

## 4. O Fluxo de Arquitetura (O "Pipeline")

Para processar PDFs em massa, a arquitetura que vamos utilizar é:

1. **Leitura (Python):** Usamos a biblioteca `PyPDF2` (ou `pdfplumber`) para abrir o arquivo PDF e transformar as páginas em uma única string de texto bruto.
2. **Extração (IA):** Enviamos a string gigante para a OpenAI com um `System Prompt` estrito exigindo um formato JSON.
3. **Consolidação (Pandas):** Pegamos o JSON gerado, convertemos numa linha de DataFrame e juntamos tudo numa planilha.



---

## 5. Custo vs. Benefício (Decisão de Engenharia)

Como engenheiros, quando usamos Regex e quando usamos IA?

* **Use Regex:** Quando o formato for **100% previsível** (ex: códigos de barras, logs de servidores internos, matrículas padronizadas). É mais rápido e não tem custo de API.
* **Use IA:** Quando o formato variar (ex: recibos de Uber, onde cada país tem um layout; ou e-mails de clientes). A IA adapta-se a mudanças de layout sem precisar reescrever código.

---

## 6. Hands-on: O Leitor de Faturas

**O Desafio Prático:**
1. Usar o `PyPDF2` para extrair o texto de dentro de um aquivo PDF.
2. Usar a API da OpenAI para procurar o "Nome da Empresa", "Data de Vencimento" e "Valor Total" no meio da confusão de texto do PDF.
3. Salvar o resultado final numa linha de um DataFrame Pandas.