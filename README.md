# 🎬 Dashboard de Análise de Filmes - Streamlit

Um dashboard interativo para análise exploratória de dados de filmes e avaliações dos datasets MovieLens e TMDB.

## 📊 Sobre

Este projeto transforma análises de dados em um dashboard interativo usando Streamlit, permitindo explorar:

- 📊 Distribuição de avaliações de filmes
- 🌍 Análise de filmes por idioma original
- 💰 Distribuição de receita e orçamento (TMDB)
- 📈 Comparação detalhada entre filmes

## 🚀 Quick Start Local

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes)
- Git (para versionamento)

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/dashboard-filmes-streamlit.git
   cd dashboard-filmes-streamlit
   ```

2. **Crie um ambiente virtual (recomendado):**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements_streamlit.txt
   ```

4. **Execute o dashboard:**
   ```bash
   streamlit run dashboard.py
   ```

O app abrirá em `http://localhost:8501`

## 📦 Dependências

- `streamlit` - Framework para dashboards
- `pandas` - Manipulação de dados
- `numpy` - Computação numérica
- `matplotlib` - Visualizações
- `seaborn` - Gráficos estatísticos
- `plotly` - Gráficos interativos

## 🌐 Deploy no Streamlit Cloud

### Passo 1: Preparar o Repositório Git

```bash
# Inicializar Git (se não estiver inicializado)
git init
git config user.email "seu-email@example.com"
git config user.name "Seu Nome"

# Adicionar e fazer commit
git add .
git commit -m "Dashboard Streamlit de Análise de Filmes"
```

### Passo 2: Criar Repositório no GitHub

1. Acesse [github.com/new](https://github.com/new)
2. Nome do repositório: `dashboard-filmes-streamlit`
3. Descrição: `Dashboard interativo de análise de filmes`
4. Clique em "Create repository"

### Passo 3: Conectar e Fazer Push

```bash
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/dashboard-filmes-streamlit.git
git push -u origin main
```

### Passo 4: Deploy no Streamlit Cloud

1. Acesse [streamlit.io/cloud](https://streamlit.io/cloud)
2. Clique em "New app"
3. Selecione seu repositório GitHub
4. Selecione `dashboard.py` como main file
5. Clique em "Deploy"

Seu app estará disponível em: `https://seu-usuario-dashboard-filmes-streamlit.streamlit.app`

## 📊 Funcionalidades

### Aba 1: Análise de Avaliações
- Métricas principais (média, mediana, desvio padrão)
- Distribuição de notas individuais
- Histograma com KDE
- Estatísticas descritivas

### Aba 2: Análise por Idioma
- Filmes por idioma (Top 10)
- Gráfico de proporção (Pizza)
- Tabela detalhada
- Filtro por idioma original

### Aba 3: Receita e Orçamento
- Distribuição de receita (filmes com revenue > 0)
- Distribuição de orçamento
- Métricas financeiras médias
- Dados do TMDB

### Aba 4: Comparativo
- Análise detalhada de filmes selecionados
- Tabela comparativa com estatísticas
- Boxplot comparativo
- Seleção múltipla de filmes

## 🎯 Filtros Interativos

- **Filtro por Idioma:** Selecione um idioma para filtrar todos os dados
- **Seleção de Filmes:** Escolha múltiplos filmes para análise comparativa

## 📊 Dados

O dashboard utiliza dados de:
- **MovieLens Small Dataset:** Avaliações de filmes
- **TMDB 5000 Movies:** Dados financeiros e metadados

Todos os dados são carregados diretamente dos repositórios GitHub originais.

## 🔧 Estrutura do Projeto

```
.
├── dashboard.py                 # Arquivo principal do Streamlit
├── requirements_streamlit.txt   # Dependências Python
├── setup_github.ps1             # Script de configuração Git
├── .gitignore                   # Arquivos a ignorar no Git
└── README.md                    # Este arquivo
```

## 🐛 Troubleshooting

### "No module named streamlit"
```bash
pip install --upgrade streamlit
```

### Erro ao carregar dados
- Verifique sua conexão com a internet
- Os dados são carregados de repositórios externos

## 🤝 Contribuindo

Contribuições são bem-vindas! Abra uma issue primeiro para discutir mudanças.

## 📝 Licença

MIT License - veja LICENSE para detalhes

## 📞 Suporte

- Abra uma [issue](https://github.com/seu-usuario/dashboard-filmes-streamlit/issues)
- Consulte a [documentação do Streamlit](https://docs.streamlit.io/)

---

**Desenvolvido com ❤️ usando Streamlit | Última atualização: Fevereiro 2026**
