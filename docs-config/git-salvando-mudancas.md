# Salvando suas mudanças no Git

> As máquinas do laboratório resetam a cada sessão (DeepFreeze). **Tudo que não for enviado ao GitHub será perdido ao desligar o computador.** Siga este guia para não perder seu progresso.

---

## Configuração inicial (fazer uma vez,)

### 1. Faça um fork do repositório do instrutor

Um fork cria uma cópia do repositório **na sua conta do GitHub**, onde você pode salvar seu progresso livremente.

1. Acesse [github.com/pedromatumoto/ia-na-pratica](https://github.com/pedromatumoto/ia-na-pratica)
2. Clique em **Fork** (canto superior direito)
3. Confirme — o repo aparecerá em `github.com/SEU_USUARIO/ia-na-pratica`

---

### 2. Clone o seu fork (não o do instrutor)

```bash
git clone https://github.com/SEU_USUARIO/ia-na-pratica.git
cd ia-na-pratica
```

> Substitua `SEU_USUARIO` pelo seu usuário do GitHub.

---

### 3. Adicione o repositório do instrutor como referência

Isso permite puxar atualizações do instrutor no futuro:

```bash
git remote add instrutor https://github.com/pedromatumoto/ia-na-pratica.git
```

Verifique que está tudo certo:
```bash
git remote -v
```

Saída esperada:
```
instrutor  https://github.com/pedromatumoto/ia-na-pratica.git (fetch)
instrutor  https://github.com/pedromatumoto/ia-na-pratica.git (push)
origin     https://github.com/SEU_USUARIO/ia-na-pratica.git (fetch)
origin     https://github.com/SEU_USUARIO/ia-na-pratica.git (push)
```

---

## Rotina de cada aula

### Início da aula — puxe as atualizações mais recentes

```bash
# Dentro da pasta ia-na-pratica
git pull instrutor main
```

### Durante a aula — crie seus próprios arquivos

Prefira criar arquivos novos em `dev/` com um nome seu (ex: `dev/meu_rag.py`) em vez de editar os arquivos do instrutor. Assim você evita conflitos.

### ⚠️ Antes de sair — salve tudo no GitHub

O computador vai resetar. Rode isso antes de fechar:

```bash
git add .
git commit -m "aula 3 - minha implementação de RAG"
git push
```

```
Seus arquivos     →  git add .  →  git commit  →  git push  →  Seu GitHub
                                   (local)                      (na nuvem ✓)
```

---

## Entendendo o fluxo completo

```
Repo do instrutor          Seu fork (GitHub)         Máquina local
  (pedromatumoto)            (SEU_USUARIO)
        │                         │                        │
        │  fork (uma vez)         │                        │
        ├────────────────────────►│                        │
        │                         │  git clone (uma vez)   │
        │                         ├───────────────────────►│
        │                         │                        │  você trabalha
        │  git pull instrutor     │                        │
        │◄────────────────────────┼────────────────────────┤
        │  (busca updates)        │                        │
        │                         │  git push (todo fim)   │
        │                         │◄───────────────────────┤
        │                         │  seu progresso salvo ✓ │
```

---

## Recebendo atualizações do instrutor sem perder o que fez

Quando o instrutor publicar novos arquivos durante ou entre aulas:

```bash
# 1. Salve o que você fez
git add .
git commit -m "progresso da aula"

# 2. Puxe as atualizações do instrutor
git pull instrutor main --rebase

# 3. Envie tudo para o seu fork
git push
```

> Se aparecer conflito (raro se você criar arquivos próprios), o Git indicará os arquivos. Abra-os, escolha o que manter e rode `git rebase --continue`.

---

## Referência rápida

| Comando | O que faz |
|---|---|
| `git status` | Mostra o que foi alterado |
| `git add .` | Marca tudo para o próximo commit |
| `git add <arquivo>` | Marca só um arquivo |
| `git commit -m "msg"` | Salva um snapshot local |
| `git push` | Envia para o **seu** fork no GitHub |
| `git pull instrutor main` | Baixa updates do repo do instrutor |
| `git remote -v` | Lista os remotes configurados |
| `git log --oneline` | Lista os commits salvos |

---

## Dica: nunca edite os arquivos do instrutor diretamente

Prefira **criar seus próprios arquivos** dentro de `dev/` com um nome diferente (ex: `dev/meu_rag.py`). Assim você nunca terá conflito ao puxar atualizações.
