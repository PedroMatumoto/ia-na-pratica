import os
import chromadb
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

cliente_ia = OpenAI() 

cliente_vetorial = chromadb.Client()
colecao_documentos = cliente_vetorial.create_collection(name="regras_corporativas")

# Se quiser, substitua esses textos por regras da sua empresa ou algo mais específico do seu dia a dia.
textos_empresa = [
    "A Nexus valoriza a resolução de problemas complexos e a entrega de resultados tangíveis.",
    "Para solicitar reembolso de aplicativos de transporte, o recibo deve ser enviado até o dia 5 do mês seguinte.",
    "A reestruturação de aplicações desktop para webapps na Azure requer aprovação prévia da arquitetura de nuvem.",
    "O código de vestimenta em clientes corporativos é 'business casual', salvo exigência específica do cliente.",
    "Todo deploy em produção deve passar por validação de segurança e não pode ocorrer às sextas-feiras."
]

# Inserindo os documentos no banco 
colecao_documentos.add(
    documents=textos_empresa,
    ids=[f"doc_{i}" for i in range(len(textos_empresa))]
)

while True:
    pergunta = input("Digite sua dúvida para o RH/TI (ou 'sair'): ")
    if pergunta.lower() == 'sair':
        break

    # Documentação do ChromaDB: https://docs.trychroma.com/docs/querying-collections/query-and-get
    # ----------------------------------------------------------------
    # TODO 1: BUSCA 
    # ----------------------------------------------------------------
    # Use a 'colecao_documentos' para buscar os 2 textos que mais 
    # se aproximam semanticamente da 'pergunta' do usuário.
    
    # resultados = colecao_documentos.query(...)
    
    # textos_recuperados = resultados['documents'][0]
    # contexto_unido = " ".join(textos_recuperados)
    
    # -> Apague esse contexto falso e use a lógica de busca acima:
    contexto_unido = "CONTEXTO FALSO PARA TESTE." 

    print(f"\nDocumentos encontrados pelo Banco Vetorial: \n{contexto_unido}\n")

    # ----------------------------------------------------------------
    # TODO 2: AUMENTO
    # ----------------------------------------------------------------
    # Dê a "personalidade" ao robô e injete o 'contexto_unido' nele.

    prompt_sistema = f"""
    Você é um assistente interno corporativo. 
    Responda a pergunta do usuário baseando-se APENAS nas informações abaixo.
    Se a informação não estiver no texto, diga "Não encontrei essa regra".
    
    CONTEXTO DA EMPRESA:
    {contexto_unido}
    """

    # ----------------------------------------------------------------
    # TODO 3: GERAÇÃO
    # ----------------------------------------------------------------
    # resposta = cliente_ia.chat.completions.create(
    #     model="gpt-4o-mini", 
    #     temperature=0.1,
    #     messages=[
    #         {"role": "system", "content": prompt_sistema},
    #         {"role": "user", "content": pergunta}
    #     ]
    # )
    
    # print(f"Resposta da IA: {resposta.choices[0].message.content}\n")
    
    print("-" * 50)