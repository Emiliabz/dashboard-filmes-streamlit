# Dashboard de AnÃ¡lise de Filmes

Dashboard interativo para explorar, analisar e visualizar dados de filmes com estatÃ­sticas e grÃ¡ficos dinÃ¢micos.

## ðŸ“Š DescriÃ§Ã£o

AplicaÃ§Ã£o web que fornece anÃ¡lises exploratÃ³rias de dados cinematogrÃ¡ficos, permitindo visualizar tendÃªncias, correlaÃ§Ãµes e padrÃµes no universo do cinema atravÃ©s de visualizaÃ§Ãµes interativas.

## ðŸ› ï¸ Tecnologias Utilizadas

- **Python** - Linguagem de programaÃ§Ã£o
- **Streamlit** - Framework para criaÃ§Ã£o de aplicaÃ§Ãµes web em dados
- **Pandas** - ManipulaÃ§Ã£o e anÃ¡lise de dados
- **Matplotlib/Seaborn** - VisualizaÃ§Ã£o de dados

## ðŸ“¦ InstalaÃ§Ã£o

`ash
# Clonar o repositÃ³rio
git clone https://github.com/seu-usuario/dashboard-filmes-streamlit.git
cd dashboard-filmes-streamlit

# Criar ambiente virtual (opcional mas recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar dependÃªncias
pip install -r requirements.txt
`

## ðŸš€ ExecuÃ§Ã£o

`ash
# Executar o dashboard
streamlit run app.py
`

O dashboard abrirÃ¡ em http://localhost:8501

## ðŸ“ Estrutura do Projeto

`
dashboard-filmes-streamlit/
â”œâ”€â”€ app.py
â”œâ”€â”€ data/
â”‚   â””â”€â”€ filmes.csv
â”œâ”€â”€ utils/
â”‚   â”œâ”€â”€ processamento.py
â”‚   â””â”€â”€ visualizacoes.py
â”œâ”€â”€ requirements.txt
â””â”€â”€ README.md
`

## ðŸ“Š Funcionalidades

- ExploraÃ§Ã£o de dados interativa
- AnÃ¡lise de gÃªneros, atores e diretores
- GrÃ¡ficos de correlaÃ§Ã£o e distribuiÃ§Ã£o
- Filtros dinÃ¢micos por perÃ­odo, gÃªnero e avaliaÃ§Ã£o

---
