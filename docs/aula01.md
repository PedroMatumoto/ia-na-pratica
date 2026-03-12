# Arquitetura de Sistemas reais com IA

---

## Muito Prazer! Quem sou eu?

**Pedro Matumoto (ou só Matumoto mesmo)**
* Engenheiro de Computação recém-formado pelo Instituto Mauá de Tecnologia com minor de Bioengenharia
* **Background:** Fiz parte da Mauá JR, Kimauanisso, dei monitoria de projetos também! Pra fechar, fiz um TCC sobre robótica autônoma doméstica.
* Hoje em dia trabalho com engenharia de software e IA de grandes quantidades de dados, mas sou apaixonado por robótica.
* **Foco atual:** Arquitetura de Software, Inteligência Artificial e Machine Learning.
  
<figure style="text-align: center;">
    <img width="350"  alt="qr-code_linkedin" src="https://github.com/user-attachments/assets/548643cf-bc54-4b26-8c69-db266309c5ed" />
</figure>

---

## Onde estamos e para onde vamos?

**O cenário atual**

**O problema:**
Usar a interface web é fácil. Mas para poder utilizar em **sistemas reais** isso não basta. Como nós transformamos essa tecnologia e construímos algo robusto? Como um sistema corporativo usa IA sem expor dados e sem custar uma fortuna?

**O objetivo do curso:**
1. Tirar a "magia" da Inteligência Artificial.
2. Entender os limites técnicos das APIs de LLM.
3. Aprender a arquitetar sistemas reais ao redor desses modelos.

---
## 1. A Lente da IA: Como as máquinas enxergam o mundo?

Antes de falarmos de ChatGPT e texto, precisamos entender uma regra fundamental: **toda IA é, no fundo, um tradutor matemático**. 

* O mundo real é analógico, contínuo e cheio de nuances.
* O mundo da IA é discreto, finito e estritamente **numérico**.

Para uma IA entender qualquer coisa, nós precisamos primeiro converter o mundo físico em matrizes de números.

---

## 2. Diferentes IAs, Diferentes "Olhos"

Dependendo do problema que queremos resolver, construímos "olhos" diferentes para a máquina:

* **Visão Computacional (Robótica / Carros Autônomos):** A IA não vê um semáforo ou um pedestre. Ela enxerga tensores — grades tridimensionais de pixels (matrizes de cores RGB) e busca padrões numéricos de contraste que formam bordas.
* **Séries Temporais (Machine Learning Tradicional):** Pensem nos dados de um motor de carro. Para prever uma falha ou otimizar um sistema, a IA enxerga o mundo como um fluxo contínuo de arrays numéricos (velocidade, temperatura, aceleração) ao longo do tempo.

<figure style="display:flex; gap:20px; justify-content:center;">

  <div style="text-align:center;">
    <img width="1200" src="https://iaexpert.academy/wp-content/uploads/2020/10/testes-pedestres.jpg">
    <figcaption>Fonte: IA Expert</figcaption>
  </div>

  <div style="text-align:center;">
    <img height="500" src="https://mariofilho.com/img/guia_ts/0.png">
    <figcaption>Fonte: Mario Filho</figcaption>
  </div>

</figure>


---

## 3. E a Linguagem Humana?

Nós sabemos traduzir a foto de um cachorro em pixels. Sabemos traduzir o motor de um carro em dados numéricos. **Mas como transformamos "ideias", "sarcasmo" e "conversa" em matemática?**

É exatamente para resolver esse problema que nasceram os **LLMs (Large Language Models)**

---

## 4. Como um LLM enxerga o mundo?

* LLMs (Large Language Models) são, na sua essência, motores de probabilidade.
* Eles recebem um texto (Prompt) e preveem a próxima palavra (Token).
* **O segredo:** Para o modelo, o universo inteiro nasce e morre a cada requisição.

---

## 5. O Paradigma Stateless (Sem Estado)

Assim como o protocolo HTTP original, as APIs de LLM são **Stateless**.

* **O que isso significa?** A requisição 2 não sabe absolutamente nada sobre a requisição 1.
* Não existe "memória" nativa no servidor do modelo.
* Cada chamada à API deve conter **toda** a informação necessária para a resposta.

```mermaid
sequenceDiagram
    participant App as Sua Aplicação
    participant LLM as API do LLM (Servidor)

    App->>LLM: 1. "Oi, meu nome é João"
    LLM-->>App: "Olá, João!"
    Note over LLM: O servidor apaga tudo da memória
    
    App->>LLM: 2. "Qual o meu nome?"
    LLM-->>App: "Desculpe, não sei quem é você."
```

---

## 6. Arquitetura Puramente Stateless

**Vantagens:**
* Altamente escalável (fácil balanceamento de carga).
* Menor uso de recursos no servidor.
* Previsibilidade: a mesma entrada tende a gerar saídas muito similares.

**Desvantagens:**
* Impossível manter uma conversa contínua sem intervenção.
* "Zero awareness" do que foi feito um segundo atrás.

---

## 7. A Ilusão da Memória: Entra o Contexto

Se o modelo não tem memória, como o ChatGPT lembra do meu nome?

* **A resposta:** A interface do usuário (o cliente ou o backend da sua aplicação) é quem gerencia o estado.
* Nós reenviamos o histórico da conversa a cada nova mensagem.
```mermaid
sequenceDiagram
    participant App as Sua Aplicação
    participant LLM as API do LLM (Servidor)

    App->>LLM: [User: "Oi, sou João"]
    LLM-->>App: "Olá, João!"
    
    App->>LLM: [User: "Oi, sou João", Assist: "Olá", User: "Qual meu nome?"]
    LLM-->>App: "Seu nome é João!"
```
---
## Qual é o grande problema arquitetural de reenviar o histórico inteiro a cada mensagem?

---

## 8. O Custo do Contexto e a Janela de Tokens

* **Tokens:** A unidade de medida do LLM (aprox. 3/4 de uma palavra).
* **Janela de Contexto (Context Window):** O limite máximo de tokens que o modelo consegue processar de uma vez (ex: 8k, 128k, 1M, 2M).

**O Gargalo da Arquitetura:**
1. **Financeiro:** Você paga por token enviado (Input). Históricos longos = requisições caras.
2. **Latência:** Mais contexto = mais tempo de processamento.
3. **Atenção:** Modelos tendem a esquecer ou ignorar informações no "meio" de contextos gigantes (Lost in the Middle).

<figure style="text-align: center;">
  <img width="500" alt="tokenization-example" src="https://miro.medium.com/1*QVXvydRMEWTWiUP42bYBAg.png" />
  <figcaption style="text-align: center;">Fonte: <a href="https://miro.medium.com/1*QVXvydRMEWTWiUP42bYBAg.png">Medium</a></figcaption>
</figure>

---

## 9. Arquiteturas para Gestão de Contexto

Como arquitetos de software, não podemos apenas jogar texto infinito no modelo. Precisamos de estratégias:

1. **Sliding Window:** Manter apenas as últimas *N* mensagens.
2. **Summarization:** Usar o próprio LLM ou outras bibliotecas para resumir conversas antigas e guardar apenas o resumo.
3. **Arquitetura Baseada em RAG:** Buscar apenas o contexto relevante sob demanda.

---

## 10. A Arquitetura RAG (Retrieval-Augmented Generation)

A forma mais eficiente de dar "conhecimento" ao LLM sem estourar a janela de contexto.

1. **Recuperação (Retrieval):** O usuário faz uma pergunta. O sistema busca em um banco de dados (geralmente Vetorial) os documentos relevantes.
2. **Aumento (Augmentation):** O sistema junta a pergunta do usuário com os documentos encontrados.
3. **Geração (Generation):** O LLM lê esse pacote focado e responde.

<figure style="text-align: center;">
  <img width="500" alt="rag-example" src="https://blog.langchain.com/content/images/2024/02/image-16.png" />
  <figcaption style="text-align: center;">Fonte: <a href="https://blog.langchain.com/content/images/2024/02/image-16.png">LangChain Blog</a></figcaption>
</figure>


---

## 11. Banco Vetorial vs. Banco Tradicional

Por que não usamos um banco de dados SQL normal para o RAG?

Pensando em uma biblioteca:

* Banco Relacional (SQL): Você chega no balcão e pede o título exato. Se errar uma letra, o sistema retorna vazio. O SQL é literal.

* Banco Vetorial: Você chega no balcão e diz: "Quero ler sobre andar no mato, natureza e mochilão". O bibliotecário entende a "vibe" do que você pediu e te traz os livros certos, mesmo que nenhuma daquelas palavras exatas esteja no título.

O Banco Vetorial busca por significado (semântica), não por palavras-chave.

---
## 12. Embeddings: Como o computador entende a "vibe"?

Para o computador fazer essa processo, precisamos transformar texto em números através de Embeddings.

Imagine um mapa. Cidades parecidas ficam na mesma vizinhança.

O Embedding pega uma frase e dá a ela uma "coordenada GPS" em um espaço matemático.

Ideias parecidas ficam fisicamente próximas umas das outras.

<figure style="text-align: center;">
  <img width="500" alt="embedding-example" src="https://corpling.hypotheses.org/files/2018/04/Screen-Shot-2018-04-25-at-13.21.44.png" />
  <figcaption style="text-align: center;">Fonte:  <a href="https://corpling.hypotheses.org/files/2018/04/Screen-Shot-2018-04-25-at-13.21.44.png">Around the word</a>
  </figcaption>
</figure>

---

## 13. Conclusão: O Papel do Engenheiro/Desenvolvedor

Trabalhar com LLMs não é só "fazer prompts legais". É projetar sistemas robustos:

* O LLM é apenas o motor de raciocínio lógico (o processador).
* A sua arquitetura é que deve fornecer a memória (RAM) e os arquivos (Disco).
* **Stateless** é a regra do modelo. O **Contexto** é a responsabilidade do sistema que você constrói ao redor dele.

---

## Dúvidas e Discussão Aberta

* Perguntas?
* Ideias de projetos que vocês gostariam de construir usando LLMs?

Obrigado pela atenção!
