# Configuração do Ambiente — com venv

> Use este guia se quiser isolar as dependências do projeto em um ambiente virtual (recomendado).

---

## Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/) instalado
- [Git](https://git-scm.com/downloads) instalado

---

## Passo a passo

### 1. Clone o repositório

```bash
git clone https://github.com/pedromatumoto/ia-na-pratica.git
cd ia-na-pratica
```

---

### 2. Crie o ambiente virtual

**Windows:**
```bash
python -m venv venv
```

**macOS / Linux:**
```bash
python3 -m venv venv
```

---

### 3. Ative o ambiente virtual

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

> Se aparecer um erro de permissão no PowerShell, execute antes:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
> ```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

Quando ativo, o terminal mostrará `(venv)` no início da linha.

---

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```
OPENAI_API_KEY=sua_chave_aqui
```

> Você obtém sua chave em [platform.openai.com/api-keys](https://platform.openai.com/api-keys).

---

### 6. Execute um script de exemplo

```bash
python dev/analisando_tabelas.py
```

---

## Desativar o ambiente virtual

Quando terminar, basta rodar:

```bash
deactivate
```

---

## Reativar em sessões futuras

Sempre que abrir um novo terminal, ative o ambiente antes de rodar qualquer script:

**Windows:**
```powershell
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source venv/bin/activate
```
