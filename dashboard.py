import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configurações da Página ---
st.set_page_config(
    page_title="Dashboard COVID-19 Interativo",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# --- Funções Utilitárias ---
# -----------------------------

@st.cache_data
def load_data(file_path='covid_19_data.csv'):
    """Carrega e pré-processa os dados do COVID-19."""
    colunas_necessarias = [
        'SNo', 'ObservationDate', 'Province/State', 'Country/Region',
        'Last Update', 'Confirmed', 'Deaths', 'Recovered'
    ]
    df = pd.read_csv(file_path, usecols=colunas_necessarias, parse_dates=['ObservationDate'])
    
    df.rename(columns={
        'SNo': 'id',
        'ObservationDate': 'data_observacao',
        'Province/State': 'provincia_estado',
        'Country/Region': 'pais_regiao',
        'Last Update': 'ultima_atualizacao',
        'Confirmed': 'confirmados',
        'Deaths': 'mortes',
        'Recovered': 'recuperados'
    }, inplace=True)
    
    df[['confirmados', 'mortes', 'recuperados']] = df[['confirmados','mortes','recuperados']].fillna(0).astype('int32')
    
    return df

@st.cache_data
def get_countries(df):
    return sorted(df['pais_regiao'].unique())

@st.cache_data
def get_global_metrics(df):
    df_latest = df[df['data_observacao'] == df['data_observacao'].max()]
    return {
        'confirmados': int(df_latest['confirmados'].sum()),
        'mortes': int(df_latest['mortes'].sum()),
        'recuperados': int(df_latest['recuperados'].sum()),
        'data': df_latest['data_observacao'].max()
    }

@st.cache_data
def global_evolution(df):
    """Retorna evolução global acumulada."""
    return df.groupby('data_observacao')[['confirmados','mortes','recuperados']].sum().reset_index()

@st.cache_data
def country_metrics(df, country):
    """Retorna métricas e evolução para um país específico."""
    df_country = df[df['pais_regiao'] == country]
    df_grouped = df_country.groupby('data_observacao')[['confirmados','mortes','recuperados']].sum().reset_index()
    latest = df_grouped[df_grouped['data_observacao'] == df_grouped['data_observacao'].max()]
    metrics = {
        'confirmados': int(latest['confirmados'].sum()),
        'mortes': int(latest['mortes'].sum()),
        'recuperados': int(latest['recuperados'].sum())
    }
    return df_grouped, metrics

# -----------------------------
# --- Carregamento de Dados ---
# -----------------------------
df = load_data()
paises_disponiveis = get_countries(df)

# -----------------------------
# --- Sidebar ---
# -----------------------------
st.sidebar.title("Opções de Análise")
st.sidebar.markdown("Use os filtros abaixo para explorar os dados.")

pais_selecionado = st.sidebar.selectbox(
    "Selecione um País/Região para Detalhes:",
    options=['Todos'] + paises_disponiveis,
    index=paises_disponiveis.index('Mainland China') + 1 if 'Mainland China' in paises_disponiveis else 0
)

st.sidebar.markdown("---")

# -----------------------------
# --- Estrutura Principal ---
# -----------------------------
st.title("🌍 Painel de Análise de COVID-19")
st.markdown("### Uma Visão Dinâmica e Autoexplicativa da Pandemia")

tab1, tab2 = st.tabs(["📊 Visão Geral Global", "🔍 Análise Detalhada por País"])

# -----------------------------
# --- Aba 1: Visão Global ---
# -----------------------------
with tab1:
    st.header("Visão Geral Global da Pandemia")
    
    metrics_global = get_global_metrics(df)
    st.subheader(f"Métricas Globais até {metrics_global['data'].strftime('%d/%m/%Y')}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Casos Confirmados", f"{metrics_global['confirmados']:,}".replace(",", "."))
    with col2:
        st.metric("Mortes", f"{metrics_global['mortes']:,}".replace(",", "."))
    with col3:
        st.metric("Recuperados", f"{metrics_global['recuperados']:,}".replace(",", "."))
    
    st.markdown("---")
    
    # Evolução global
    st.subheader("📈 Evolução Acumulada de Casos Globais")
    df_global_evolution = global_evolution(df)
    fig_global = px.area(
        df_global_evolution,
        x='data_observacao',
        y=['confirmados','mortes','recuperados'],
        labels={'value':'Número de Casos','data_observacao':'Data'},
        color_discrete_map={'confirmados':'orange','mortes':'red','recuperados':'green'},
        title="Evolução Acumulada Global"
    )
    fig_global.update_layout(hovermode="x unified")
    st.plotly_chart(fig_global, use_container_width=True)
    
    # Top 10 países
    st.subheader("🏆 Países com Maior Número de Casos Confirmados")
    df_latest = df[df['data_observacao'] == metrics_global['data']]
    df_top10 = df_latest.groupby('pais_regiao')[['confirmados','mortes','recuperados']].sum().reset_index().sort_values('confirmados', ascending=False)
    st.dataframe(df_top10.head(10).style.background_gradient(subset=['confirmados'], cmap='Oranges'), use_container_width=True)

# -----------------------------
# --- Aba 2: Análise por País ---
# -----------------------------
with tab2:
    st.header(f"Detalhes para: {pais_selecionado}")
    
    if pais_selecionado == 'Todos':
        st.info("Selecione um país na barra lateral para ver a análise detalhada.")
    else:
        df_country_grouped, metrics_country = country_metrics(df, pais_selecionado)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Casos Confirmados", f"{metrics_country['confirmados']:,}".replace(",", "."))
        col2.metric("Mortes", f"{metrics_country['mortes']:,}".replace(",", "."))
        col3.metric("Recuperados", f"{metrics_country['recuperados']:,}".replace(",", "."))
        
        st.markdown("---")
        
        st.subheader(f"Evolução Histórica em {pais_selecionado}")
        fig_country = px.line(
            df_country_grouped,
            x='data_observacao',
            y=['confirmados','mortes','recuperados'],
            labels={'value':'Número de Casos','data_observacao':'Data'},
            color_discrete_map={'confirmados':'orange','mortes':'red','recuperados':'green'},
            title=f"Evolução Diária de Casos em {pais_selecionado}"
        )
        st.plotly_chart(fig_country, use_container_width=True)
        
        with st.expander("Ver Tabela de Dados Detalhada do País"):
            st.dataframe(df_country_grouped.sort_values('data_observacao', ascending=False), use_container_width=True)

st.markdown("---")
st.markdown("Análises - Kelven Silva")
