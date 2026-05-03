<div align="center">

# Memória
### Aula 4: Embeddings, Busca Semântica e Mini-RAG

<br>

📱 **Material da Aula 4:**
`https://github.com/pedromatumoto/ia-na-pratica/`

</div>


---

## 1. O Problema da Memória

Relembrando:
* A API cobra por token. Se temos um manual de 500 páginas e queremos saber a política de reembolso, enviar as 500 páginas toda vez é inviável, lento e caro.


---

## 2. A Solução (RAG): Retrieval-Augmented Generation.

* Retrieval (Busca): Achar só o parágrafo que fala de reembolso.

* Augmented (Aumento): Colar esse parágrafo invisivelmente no Prompt do sistema.

* Generation (Geração): O LLM lê a pergunta + o parágrafo e responde.

---

## 3. O que é Retrieval-Augmented Generation e o que realmente significa Embeddings 

O Computador é Cego para Texto: Como fazer o Python saber que "Cão" e "Cachorro" são a mesma coisa, mas "Cão" e "Caminhão" não são?

* Embeddings: É uma função que converte uma frase em uma lista gigante de números (um vetor matemático de centenas de dimensões). Funciona como uma "Coordenada GPS do Significado".

---

Distância de Cosseno:
![imagem similaridade cosseno](https://brains.dev/wp-content/uploads/2024/01/distancias_10-800x500.png)

$$
d_{\cos}(\mathbf{A}, \mathbf{B}) = 1 - \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}
$$

---

![imagem similaridade cosseno](https://miro.medium.com/v2/resize:fit:2000/0*YmY-dD591kMY8lBO.png)

Se o ângulo é 0∘ (cos=1), os textos são idênticos. Se é 90∘ (cos=0), não têm nada a ver.

---

## 4. Bancos Vetoriais

Para pesquisar alguma coisa no texto, como por exemplo no word, pesquisamos a palavra completa exatamente como ela está escrita, mas e se quisermos pesquisar algo que seja parecido?

No banco vetorial (semântico): "Me dê os 3 textos mais próximos do vetor da palavra cachorro". Ele vai trazer "cãozinho", "pet" e "ração", mesmo que a palavra "cachorro" nunca tenha sido escrita.

---

## 5. Hands-on: O Chatbot do RH

A Ferramenta: Vamos usar o chromadb. É um banco vetorial local feito em Python. Ele é perfeito para estudo porque roda na memória (não precisa instalar servidores Docker).

---

## 6. Fechamento

Como isso vira dinheiro no mercado: Sistemas de suporte ao cliente que leem o histórico de chamados passados para sugerir a solução para o problema atual.