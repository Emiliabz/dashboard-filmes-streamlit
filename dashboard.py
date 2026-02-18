import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Filmes",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dicionário de idiomas com tradução
IDIOMAS_TRADUCAO = {
    'en': 'English (Inglês)',
    'ja': 'Japanese (Japonês)',
    'fr': 'French (Francês)',
    'de': 'German (Alemão)',
    'es': 'Spanish (Espanhol)',
    'it': 'Italian (Italiano)',
    'ru': 'Russian (Russo)',
    'pt': 'Portuguese (Português)',
    'zh': 'Chinese (Chinês)',
    'ko': 'Korean (Coreano)',
    'hi': 'Hindi (Hindi)',
    'ar': 'Arabic (Árabe)',
    'tr': 'Turkish (Turco)',
    'pl': 'Polish (Polonês)',
    'nl': 'Dutch (Holandês)',
    'sv': 'Swedish (Sueco)',
    'th': 'Thai (Tailandês)',
    'fa': 'Persian (Persa)',
    'vi': 'Vietnamese (Vietnamita)',
    'id': 'Indonesian (Indonésio)',
}

# Cache para carregamento dos dados
@st.cache_data
def carregar_dados():
    """Carrega os datasets do repositório"""
    try:
        notas = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/ml-latest-small/ratings.csv")
        filmes = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/ml-latest-small/movies.csv")
        tmdb = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula3.1/tmdb_5000_movies.csv")
        
        # Renomear colunas do dataset 'notas'
        notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
        return notas, filmes, tmdb
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return None, None, None

# Estilo
st.markdown("""
    <style>
    .metric-card { padding: 15px; border-radius: 10px; background-color: #f0f2f6; }
    </style>
    """, unsafe_allow_html=True)

# Carregar dados
notas, filmes, tmdb = carregar_dados()

if notas is None or filmes is None or tmdb is None:
    st.error("Não foi possível carregar os dados. Verifique sua conexão com a internet.")
    st.stop()

# Título principal
st.title("🎬 Dashboard de Análise de Filmes")
st.markdown("Análise exploratória de dados de filmes e avaliações dos datasets MovieLens e TMDB")
st.markdown("---")

# ============== SIDEBAR - FILTROS ==============
st.sidebar.title("⚙️ Filtros e Configurações")

# Seção de filtros
st.sidebar.subheader("📊 Seleção de Dados")

# Filtro por idioma
todas_linguas = ['Todos'] + sorted(tmdb["original_language"].unique().tolist())
idioma_selecionado = st.sidebar.selectbox(
    "Filtrar por Idioma Original:",
    todas_linguas,
    format_func=lambda x: f"Todos os idiomas" if x == 'Todos' else f"{IDIOMAS_TRADUCAO.get(x, x)} ({x})",
    help="Selecione um idioma para filtrar os dados do TMDB"
)

# Filtro por filmeId
todos_filmes_ids = sorted(notas["filmeId"].unique().tolist())
filmes_dict = {}
for fid in todos_filmes_ids:
    titulo = filmes.query(f"movieId == {fid}")["title"].values
    titulo = titulo[0] if len(titulo) > 0 else f"Filme {fid}"
    filmes_dict[f"{titulo} ({fid})"] = fid

filmes_selecionados_labels = st.sidebar.multiselect(
    "Selecione Filmes por ID (para análise detalhada):",
    list(filmes_dict.keys()),
    help="Selecione um ou mais filmes para análise comparativa"
)

filmes_selecionados = [filmes_dict[label] for label in filmes_selecionados_labels]

# Aplicar filtros ao dataset tmdb
tmdb_filtrado = tmdb.copy()
if idioma_selecionado != 'Todos':
    tmdb_filtrado = tmdb[tmdb['original_language'] == idioma_selecionado]

st.sidebar.markdown("---")
st.sidebar.info(f"📍 Filmes no banco: {len(notas['filmeId'].unique())}\n📍 Avaliações: {len(notas)}\n📍 Filmes TMDB: {len(tmdb)}")

# ============== CONTEÚDO PRINCIPAL ==============

# TAB 1: Análise Geral de Avaliações
tab1, tab2, tab3, tab4 = st.tabs(["📈 Avaliações", "🌍 Idiomas", "💰 Receita e Orçamento", "📊 Comparativo"])

with tab1:
    st.header("Análise de Avaliações")
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        media_geral = notas["nota"].mean()
        st.metric("Média Geral", f"{media_geral:.2f}⭐", help="Média de todas as avaliações")
    
    with col2:
        mediana_geral = notas["nota"].median()
        st.metric("Mediana", f"{mediana_geral:.2f}⭐", help="Valor central das avaliações")
    
    with col3:
        std_geral = notas["nota"].std()
        st.metric("Desvio Padrão", f"{std_geral:.2f}", help="Variação das avaliações")
    
    with col4:
        total_avaliacoes = len(notas)
        st.metric("Total de Avaliações", f"{total_avaliacoes:,}", help="Número total de notas registradas")
    
    st.markdown("---")
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Distribuição de Notas Individuais")
        fig, ax = plt.subplots(figsize=(10, 5))
        notas["nota"].value_counts().sort_index().plot(kind='bar', ax=ax, color='steelblue')
        ax.set_title("Contagem de Avaliações por Nota")
        ax.set_xlabel("Nota")
        ax.set_ylabel("Frequência")
        st.pyplot(fig)
    
    with col2:
        st.subheader("Melhores Filmes por País (Top 20)")
        # Agregar dados: país, média de notas
        tmdb_com_notas = tmdb[['original_language', 'title', 'revenue']].copy()
        
        # Criar mapa de cores baseado na média de notas por idioma
        media_por_idioma = tmdb.groupby('original_language')[['vote_average']].mean()
        media_por_idioma.columns = ['nota_media']
        media_por_idioma = media_por_idioma.reset_index()
        media_por_idioma = media_por_idioma.sort_values('nota_media', ascending=False).head(20)
        
        fig, ax = plt.subplots(figsize=(10, 8))
        cores = plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(media_por_idioma)))
        bars = ax.barh(media_por_idioma['original_language'], media_por_idioma['nota_media'], color=cores)
        ax.set_xlabel("Nota Média")
        ax.set_title("Nota Média por País/Idioma (Top 20)")
        ax.set_xlim(0, 10)
        
        # Adicionar valores nas barras
        for i, v in enumerate(media_por_idioma['nota_media']):
            ax.text(v + 0.1, i, f'{v:.2f}', va='center')
        
        st.pyplot(fig)
    
    st.subheader("Estatísticas Descritivas da Distribuição de Notas")
    stats_df = pd.DataFrame({
        'Métrica': ['Contagem', 'Média', 'Desvio Padrão', 'Mínimo', '25%', 'Mediana (50%)', '75%', 'Máximo'],
        'Valor': [
            f"{notas['nota'].count()}",
            f"{notas['nota'].mean():.4f}",
            f"{notas['nota'].std():.4f}",
            f"{notas['nota'].min():.4f}",
            f"{notas['nota'].quantile(0.25):.4f}",
            f"{notas['nota'].median():.4f}",
            f"{notas['nota'].quantile(0.75):.4f}",
            f"{notas['nota'].max():.4f}"
        ]
    })
    st.dataframe(stats_df, use_container_width=True)

with tab2:
    st.header("Análise por Idioma Original")
    
    st.subheader("📖 Explicação dos Idiomas")
    with st.expander("Clique para ver a legenda de idiomas"):
        idiomas_df = pd.DataFrame([
            {"Sigla": code, "Idioma Completo": name}
            for code, name in sorted(IDIOMAS_TRADUCAO.items())
        ])
        st.dataframe(idiomas_df, use_container_width=True)
    
    # Abas para filtros de idioma
    aba_en, aba_nao_en = st.tabs(["🇬🇧 Filmes em Inglês (EN)", "🌍 Filmes em Outros Idiomas"])
    
    with aba_en:
        st.subheader("Análise de Filmes em Inglês")
        tmdb_en = tmdb[tmdb['original_language'] == 'en']
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Total de Filmes (EN)", len(tmdb_en))
            st.write(f"**Percentual:** {(len(tmdb_en)/len(tmdb)*100):.1f}% dos filmes")
        
        with col2:
            st.metric("Nota Média", f"{tmdb_en['vote_average'].mean():.2f}⭐")
            st.write(f"**Votos Médios:** {tmdb_en['vote_count'].mean():.0f}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Distribuição de Notas (Inglês)")
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.hist(tmdb_en['vote_average'], bins=20, color='steelblue', edgecolor='black', alpha=0.7)
            ax.set_xlabel("Nota Média")
            ax.set_ylabel("Frequência")
            ax.set_title("Distribuição de Notas dos Filmes em Inglês")
            st.pyplot(fig)
        
        with col2:
            st.subheader("Top 10 Filmes em Inglês por Nota")
            top_10_en = tmdb_en.nlargest(10, 'vote_average')[['title', 'vote_average', 'vote_count']]
            top_10_en = top_10_en.reset_index(drop=True)
            top_10_en.index = top_10_en.index + 1
            st.dataframe(top_10_en, use_container_width=True)
    
    with aba_nao_en:
        st.subheader("Análise de Filmes em Outros Idiomas (Não Inglês)")
        tmdb_nao_en = tmdb[tmdb['original_language'] != 'en']
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Total de Filmes (Não EN)", len(tmdb_nao_en))
            st.write(f"**Percentual:** {(len(tmdb_nao_en)/len(tmdb)*100):.1f}% dos filmes")
        
        with col2:
            st.metric("Nota Média", f"{tmdb_nao_en['vote_average'].mean():.2f}⭐")
            st.write(f"**Votos Médios:** {tmdb_nao_en['vote_count'].mean():.0f}")
        
        # Contagem de filmes por idioma (não inglês)
        contagem_nao_en = tmdb_nao_en["original_language"].value_counts().reset_index()
        contagem_nao_en.columns = ["Idioma", "Quantidade"]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Filmes por Idioma (Top 10 - Não Inglês)")
            fig, ax = plt.subplots(figsize=(10, 6))
            top_idiomas_nao_en = contagem_nao_en.head(10)
            sns.barplot(data=top_idiomas_nao_en, x="Idioma", y="Quantidade", ax=ax, palette="viridis")
            ax.set_title("Top 10 Idiomas (Não Inglês)")
            ax.set_xlabel("Idioma")
            ax.set_ylabel("Quantidade de Filmes")
            plt.xticks(rotation=45)
            st.pyplot(fig)
        
        with col2:
            st.subheader("Proporção de Países (Não Inglês)")
            fig, ax = plt.subplots(figsize=(8, 6))
            top_5_nao_en = contagem_nao_en.head(5)
            outros_nao_en = contagem_nao_en.iloc[5:]["Quantidade"].sum()
            if outros_nao_en > 0:
                dados_pie_nao_en = pd.concat([top_5_nao_en, pd.DataFrame({"Idioma": ["Outros"], "Quantidade": [outros_nao_en]})])
            else:
                dados_pie_nao_en = top_5_nao_en
            ax.pie(dados_pie_nao_en["Quantidade"], labels=dados_pie_nao_en["Idioma"], autopct='%1.1f%%')
            ax.set_title("Distribuição de Países (Não Inglês)")
            st.pyplot(fig)
        
        st.subheader("Distribuição de Notas (Não Inglês)")
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.hist(tmdb_nao_en['vote_average'], bins=20, color='coral', edgecolor='black', alpha=0.7)
        ax.set_xlabel("Nota Média")
        ax.set_ylabel("Frequência")
        ax.set_title("Distribuição de Notas dos Filmes em Outros Idiomas")
        st.pyplot(fig)

with tab3:
    st.header("Análise Financeira (TMDB)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Distribuição de Receita")
        # Filmes com receita > 0
        com_receita = tmdb_filtrado.query("revenue > 0")
        if len(com_receita) > 0:
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.histplot(com_receita["revenue"], kde=True, ax=ax, bins=30)
            ax.set_title(f"Distribuição de Receita (Filmes com receita > 0)")
            ax.set_xlabel("Receita ($)")
            ax.set_ylabel("Frequência")
            st.pyplot(fig)
            
            st.metric("Receita Média (com receita)", f"${com_receita['revenue'].mean():,.0f}")
        else:
            st.info("Nenhum filme com receita > 0 para este filtro.")
    
    with col2:
        st.subheader("Distribuição de Orçamento")
        com_orcamento = tmdb_filtrado.query("budget > 0")
        if len(com_orcamento) > 0:
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.histplot(com_orcamento["budget"], kde=True, ax=ax, bins=30)
            ax.set_title(f"Distribuição de Orçamento (Filmes com orçamento > 0)")
            ax.set_xlabel("Orçamento ($)")
            ax.set_ylabel("Frequência")
            st.pyplot(fig)
            
            st.metric("Orçamento Médio (com orçamento)", f"${com_orcamento['budget'].mean():,.0f}")
        else:
            st.info("Nenhum filme com orçamento > 0 para este filtro.")

with tab4:
    st.header("Análise Comparativa por Filme")
    
    if filmes_selecionados:
        # Análise dos filmes selecionados
        st.subheader(f"Análise de {len(filmes_selecionados)} filme(s) selecionado(s)")
        
        # Tabela com estatísticas
        dados_filmes = []
        for filme_id in filmes_selecionados:
            notas_filme = notas.query(f"filmeId == {filme_id}")["nota"]
            titulo_filme = filmes.query(f"movieId == {filme_id}")["title"].values
            titulo_filme = titulo_filme[0] if len(titulo_filme) > 0 else f"Filme ID {filme_id}"
            
            dados_filmes.append({
                "ID": filme_id,
                "Título": titulo_filme,
                "Média": f"{notas_filme.mean():.2f}",
                "Mediana": f"{notas_filme.median():.2f}",
                "Desvio Padrão": f"{notas_filme.std():.2f}",
                "Total de Avaliações": len(notas_filme)
            })
        
        st.dataframe(pd.DataFrame(dados_filmes), use_container_width=True)
        
        # Boxplot comparativo
        st.subheader("Distribuição de Notas por Filme")
        notas_boxplot = []
        labels_boxplot = []
        
        for filme_id in filmes_selecionados:
            notas_filme = notas.query(f"filmeId == {filme_id}")["nota"]
            titulo_filme = filmes.query(f"movieId == {filme_id}")["title"].values
            titulo_filme = titulo_filme[0] if len(titulo_filme) > 0 else f"ID {filme_id}"
            
            notas_boxplot.append(notas_filme.values)
            labels_boxplot.append(titulo_filme[:20])  # Limitar tamanho do label
        
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.boxplot(notas_boxplot, labels=labels_boxplot)
        ax.set_title("Boxplot Comparativo de Avaliações")
        ax.set_ylabel("Nota")
        plt.xticks(rotation=45, ha='right')
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
    else:
        st.info("👆 Selecione um ou mais filmes na barra lateral para análise comparativa.")

# ============== RODAPÉ ==============
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Filmes Únicos", len(notas['filmeId'].unique()))
with col2:
    st.metric("Usuários Únicos", len(notas['usuarioId'].unique()))
with col3:
    st.metric("Período de Análise", "1995-2015")

st.markdown("""
    <div style='text-align: center; margin-top: 30px; color: gray;'>
    <small>Dashboard desenvolvido com Streamlit | Dados: MovieLens Small + TMDB | © 2026</small>
    </div>
    """, unsafe_allow_html=True)
