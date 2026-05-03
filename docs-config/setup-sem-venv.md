# Configuração do Ambiente — sem venv

> Use este guia se quiser instalar as dependências diretamente no Python global da sua máquina (mais simples, porém pode causar conflitos com outros projetos).

---

## Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/) instalado
- [Git](https://git-scm.com/downloads) instalado

---

## Passo a passo

### 1. Clone o repositório

```bash
git config --global user.name "seu nome"
git config --global user.email "seuemail"
git clone https://github.com/pedromatumoto/ia-na-pratica.git
cd ia-na-pratica
```

---

### 2. Instale as dependências globalmente

**Windows:**
```bash
pip install -r requirements.txt
```

**macOS / Linux:**
```bash
pip3 install -r requirements.txt
```

---

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```
OPENAI_API_KEY=sua_chave_aqui
```

> Você obtém sua chave em [platform.openai.com/api-keys](https://platform.openai.com/api-keys).

---

### 4. Execute um script de exemplo

```bash
python dev/analisando_tabelas.py
```

---

## Problemas comuns

| Problema | Solução |
|---|---|
| `python` não reconhecido | Tente `python3` no lugar de `python` |
| `pip` não reconhecido | Tente `pip3` ou `python -m pip` |
| Conflito de versão de pacote | Considere usar o guia **com venv** para isolar o projeto |
| Erro de permissão no pip | Adicione `--user` ao final: `pip install -r requirements.txt --user` |

---

## Atualizar o projeto futuramente

Sempre que o repositório for atualizado pelo instrutor, rode dentro da pasta do projeto:

```bash
git pull
pip install -r requirements.txt
```
