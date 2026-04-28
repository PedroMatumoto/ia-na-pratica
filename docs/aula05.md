<div align="center">

# Começando com arquivos
### Aula 5: Base do Pandas (Filtros, Limpeza e Cruzamentos)

<br>

📱 **Material da Aula 5:**
`https://github.com/pedromatumoto/ia-na-pratica/`

</div>

---

## 1. O Paradigma do DataFrame

Apresentando o **Pandas**: é a biblioteca padrão da indústria para manipulação de dados. É a ferramenta que permite processar milhões de linhas com a performance que a engenharia exige, principalmente para ferramentas de dashboard em Python.

* **Series:** Uma única coluna (vetor de 1 dimensão).
* **DataFrame:** A tabela inteira (matriz de 2 dimensões).



---

## 2. Excel vs. Pandas

Por que não usar folhas de cálculo para grandes volumes corporativos ou sistemas reais?

* **Reprodutibilidade:** No Excel, um clique errado apaga um dado permanentemente. No Pandas, o dado original (`.csv` bruto) é imutável. O código é a "receita" de transformação que pode ser auditada.
* **Escala:** O Excel começa a falhar perto de 1 milhão de linhas. O Pandas processa isso em milissegundos.
* **A Linha de Montagem:** O Excel é um trabalho artesanal e manual. O Pandas é uma linha de montagem industrial: você faz o script uma vez e ele processa 1 ou 1.000 planilhas com o mesmo esforço.

---

## 3. Leitura e Inspeção de Dados

Os comandos de "raio-X" para entender a estrutura da base de dados antes da análise:

* `pd.read_csv()` e `pd.read_excel()`: Carregamento para a memória RAM.
* `df.head()`: Visualização das 5 primeiras linhas (o "feel" dos dados).
* `df.info()`: Diagnóstico de tipos de dados e contagem de valores nulos.
* `df.describe()`: Estatística descritiva automática. Calcula métricas como a média $\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i$, desvio padrão, mínimos e máximos de forma instantânea.

---

## 4. Limpando o Caos (A Realidade do Mercado)

Dados corporativos reais são "sujos": vêm com buracos, formatos inconsistentes e erros de sistema.

* **Valores Nulos (NaN):** Identificamos lacunas com `df.isnull()`. Decidimos entre descartar (`df.dropna()`) ou preencher com valores padrão (`df.fillna()`).
* **A Falha do "Object" (String):**
Se uma coluna de preços contém o símbolo "€" ou "R$", o Pandas lê como texto.
Somar texto gera erro de lógica: `"10" + "10" = "1010"`. 
**Engenharia de Dados:** Precisamos de remover caracteres não numéricos e converter a coluna para `float` antes de qualquer cálculo.

---

## 5. Filtros e Cruzamentos Básicos

Como extrair inteligência específica de uma massa de dados bruta:

* **Máscaras Booleanas (Filtros):** Seleção de linhas baseada em condições lógicas de negócio. 
    * Ex: `df[df['Status'] == 'Concluído']`
* **Agrupamentos (Group By):** O equivalente à "Tabela Dinâmica". Consolida dados para gerar KPIs.
    * Ex: `df.groupby('Filial')['Valor_Venda'].sum()` para identificar o faturamento por região.



---

## 6. Hands-on: Auditoria de Vendas

**O Problema Corporativo:**
A equipa de Qualidade exportou milhares de avaliações de clientes. O sistema apenas nos diz se o atendimento está "Concluído" e se a avaliação foi "Negativa", mas não nos diz **porquê**. O motivo está escondido no texto livre deixado pelo cliente.

**O Desafio Prático:**
1. **Setup:** Executar o script `template_cx.py` para simular a exportação da base de dados de *Customer Experience* (CX).
2. **Filtro Duplo no Pandas:** Isolar apenas as linhas onde o `Status` é "Concluído" **E** a `Avaliacao` é "Negativa" (não queremos analisar queixas de pedidos ainda em andamento).
3. **IA no Loop:** Usar a API (OpenAI) para ler os comentários filtrados e classificá-los em três etiquetas estritas: `[Logística, Suporte, Produto]`.
4. **Relatório Final:** Inserir estas etiquetas numa nova coluna e fazer um `groupby()` para descobrir qual é o departamento que está a causar mais problemas aos clientes.

---

## 7. Fechamento

**Valor de Mercado:**
Em consultoria e reestruturação de empresas, o tempo gasto a "limpar" Excel é desperdício de engenharia. Um pipeline bem construído em Pandas automatiza o que antes levava dias de trabalho manual, eliminando o erro humano e permitindo que o foco seja a tomada de decisão baseada em dados reais.
