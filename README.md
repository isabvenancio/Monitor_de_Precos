# 🛒 Monitor de Preços

Um sistema desenvolvido em Python para monitorar preços de produtos em lojas online. O projeto utiliza **Web Scraping com Selenium** para obter o preço atualizado, registra um histórico das consultas e envia notificações quando o produto atinge o preço desejado.

## 🚀 Funcionalidades

- 🔍 Monitoramento automático de produtos
- 🌐 Web Scraping com Selenium
- 💰 Comparação entre preço atual e preço desejado
- 📧 Envio de notificações por e-mail
- 📱 Envio de notificações via WhatsApp
- 📊 Histórico de preços em arquivo CSV
- ⏰ Possibilidade de execução automática em horários definidos

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Selenium
- Pandas
- PyWhatKit
- SMTP (envio de e-mails)

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/monitor-precos.git
```

Entre na pasta do projeto:

```bash
cd monitor-precos
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 📦 Configuração

### 1. Adicione os produtos

No arquivo `produtos.py`:

```python
produtos = [
    {
        "nome": "Notebook Dell",
        "url": "https://site.com/produto",
        "preco_desejado": 3000
    }
]
```

### 2. Configure o e-mail

No arquivo `notificacoes.py`:

```python
email = "seuemail@gmail.com"
senha = "SUA_SENHA_DE_APP"
```

### 3. Configure o WhatsApp

No arquivo `notificacoes.py`:

```python
numero = "+5511999999999"
```

### 4. Configure o seletor do preço

Cada site possui uma estrutura HTML diferente. No arquivo `scraping.py`, ajuste o seletor conforme o site monitorado.

Exemplo:

```python
driver.find_element(By.CLASS_NAME, "price")
```

---

## ▶️ Executando o projeto

```bash
python main.py
```

---

## 📈 Histórico de preços

Todas as verificações são registradas automaticamente no arquivo:

```
historico_precos.csv
```

Exemplo:

| Produto | Preço | Data |
|---------|-------|------|
| Notebook Dell | 2899.90 | 05/03/2026 14:00 |

---

## 📌 Melhorias Futuras

- Dashboard com Streamlit
- Banco de dados SQLite ou PostgreSQL
- Monitoramento de múltiplas lojas
- Gráficos de evolução dos preços
- Interface gráfica
- Agendamento automático via Scheduler ou Cron
- Deploy em servidor ou nuvem
- Docker para facilitar a execução
