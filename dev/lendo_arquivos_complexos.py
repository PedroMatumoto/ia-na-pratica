import os
import pandas as pd
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
cliente_ia = OpenAI()

# ====================================================================
# TODO 1: LEITURA DO "PDF" (Lendo o texto sujo)
# ====================================================================
# Leia o arquivo 'fatura_suja_01.txt' e guarde todo o conteúdo 
# em uma variável chamada 'texto_bruto'.

caminho_arquivo = 'exemplos/nota-fiscal-notebook-dell.pdf'

# texto_bruto = ...

# ====================================================================
# TODO 2: EXTRAÇÃO INTELIGENTE COM IA (Structured Output)
# ====================================================================
# Use a API da OpenAI para analisar o 'texto_bruto'.
# CRIE UM SYSTEM PROMPT EXTREMAMENTE RÍGIDO pedindo que a IA 
# devolva a resposta NO FORMATO JSON com as chaves:
# "nome_empresa", "data_vencimento", "valor" (só os números).

# prompt_sistema = """ ... """
# resposta = ...

# ====================================================================
# TODO 3: CONSOLIDANDO NO PANDAS
# ====================================================================
# 1. Pegue a resposta em JSON gerada pela IA (que é uma string).
# 2. Converta ela em um dicionário Python (use a biblioteca 'json').
# 3. Transforme esse dicionário em uma linha de um DataFrame do Pandas.

import json
json_extraido = json.loads(...)
df_resultado = pd.DataFrame([json_extraido])
print("\n📊 Dado Extraído e Estruturado:")
print(df_resultado)