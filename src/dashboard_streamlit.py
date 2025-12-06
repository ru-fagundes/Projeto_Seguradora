"""
Dashboard Interativo Profissional - Análise de Ocorrências
Usando Streamlit para interface moderna e responsiva
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path

# =====================================================
# Configuração da Página
# =====================================================
st.set_page_config(
    page_title="Dashboard - Ocorrências Seguradora",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para melhorar visual
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1 {
        color: #1f77b4;
        padding-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# =====================================================
# Carregar Dados
# =====================================================
@st.cache_data
def load_data():
    """Carrega e processa os dados"""
    # Caminho absoluto baseado no local deste script
    script_dir = Path(__file__).parent
    data_path = script_dir.parent / "data" / "processed" / "dados_ocorrencias_formatado.csv"
    df = pd.read_csv(data_path)
    df['data_ocorrencia'] = pd.to_datetime(df['data_ocorrencia'])
    return df

try:
    df = load_data()
    
    # =====================================================
    # Header
    # =====================================================
    st.title("🏥 Dashboard de Análise de Ocorrências - Seguradora")
    st.markdown("---")
    
    # =====================================================
    # Sidebar - Filtros
    # =====================================================
    st.sidebar.header("🔍 Filtros")
    
    # Filtro por período
    min_date = df['data_ocorrencia'].min().date()
    max_date = df['data_ocorrencia'].max().date()
    
    date_range = st.sidebar.date_input(
        "Período",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Filtro por tipo de problema
    tipos_problema = ['Todos'] + list(df['tipo_problema'].unique())
    tipo_selecionado = st.sidebar.selectbox("Tipo de Problema", tipos_problema)
    
    # Filtro por canal
    canais = ['Todos'] + list(df['canal_entrada'].unique())
    canal_selecionado = st.sidebar.selectbox("Canal de Entrada", canais)
    
    # Filtro por classificação
    classificacoes = ['Todos'] + list(df['classificacao'].unique())
    classificacao_selecionada = st.sidebar.selectbox("Classificação", classificacoes)
    
    # Aplicar filtros
    df_filtered = df.copy()
    
    if len(date_range) == 2:
        df_filtered = df_filtered[
            (df_filtered['data_ocorrencia'].dt.date >= date_range[0]) &
            (df_filtered['data_ocorrencia'].dt.date <= date_range[1])
        ]
    
    if tipo_selecionado != 'Todos':
        df_filtered = df_filtered[df_filtered['tipo_problema'] == tipo_selecionado]
    
    if canal_selecionado != 'Todos':
        df_filtered = df_filtered[df_filtered['canal_entrada'] == canal_selecionado]
    
    if classificacao_selecionada != 'Todos':
        df_filtered = df_filtered[df_filtered['classificacao'] == classificacao_selecionada]
    
    st.sidebar.markdown("---")
    st.sidebar.info(f"📊 **{len(df_filtered)}** registros selecionados de **{len(df)}** totais")
    
    # =====================================================
    # KPIs Principais
    # =====================================================
    st.header("📊 Indicadores Principais")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    total_ocorrencias = len(df_filtered)
    tempo_medio = df_filtered['tempo_resolucao'].mean()
    pct_criticos = (df_filtered['classificacao'].eq("crítica").mean() * 100)
    pct_reincidentes = (df_filtered['cliente_reincidente'].eq("sim").mean() * 100)
    pct_sla5 = (df_filtered['tempo_resolucao'].le(5).mean() * 100)
    
    with col1:
        st.metric(
            label="Total de Ocorrências",
            value=f"{total_ocorrencias:,}",
            delta=f"{(total_ocorrencias/len(df)*100):.1f}% do total"
        )
    
    with col2:
        st.metric(
            label="Tempo Médio (dias)",
            value=f"{tempo_medio:.1f}",
            delta="Meta: 5 dias",
            delta_color="inverse" if tempo_medio > 5 else "normal"
        )
    
    with col3:
        st.metric(
            label="Casos Críticos",
            value=f"{pct_criticos:.1f}%",
            delta=f"{df_filtered['classificacao'].eq('crítica').sum()} casos"
        )
    
    with col4:
        st.metric(
            label="Taxa Reincidência",
            value=f"{pct_reincidentes:.1f}%",
            delta=f"{df_filtered['cliente_reincidente'].eq('sim').sum()} casos"
        )
    
    with col5:
        st.metric(
            label="SLA ≤ 5 dias",
            value=f"{pct_sla5:.1f}%",
            delta="Objetivo: 80%",
            delta_color="normal" if pct_sla5 >= 80 else "inverse"
        )
    
    st.markdown("---")
    
    # =====================================================
    # Gráficos - Linha 1
    # =====================================================
    st.header("📈 Análise por Tipo de Problema")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Distribuição por tipo
        tipo_counts = df_filtered['tipo_problema'].value_counts().reset_index()
        tipo_counts.columns = ['tipo_problema', 'count']
        
        fig_tipos = px.bar(
            tipo_counts,
            x='tipo_problema',
            y='count',
            title="Ocorrências por Tipo de Problema",
            labels={'count': 'Quantidade', 'tipo_problema': 'Tipo'},
            color='count',
            color_continuous_scale='Blues',
            text='count'
        )
        fig_tipos.update_traces(textposition='outside')
        fig_tipos.update_layout(
            xaxis_tickangle=-45,
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig_tipos, width='stretch')
    
    with col2:
        # Tempo médio por tipo
        tempo_tipo = df_filtered.groupby('tipo_problema')['tempo_resolucao'].mean().reset_index()
        tempo_tipo = tempo_tipo.sort_values('tempo_resolucao', ascending=False)
        
        fig_tempo = px.bar(
            tempo_tipo,
            x='tipo_problema',
            y='tempo_resolucao',
            title="Tempo Médio de Resolução por Tipo",
            labels={'tempo_resolucao': 'Dias', 'tipo_problema': 'Tipo'},
            color='tempo_resolucao',
            color_continuous_scale='Reds',
            text='tempo_resolucao'
        )
        fig_tempo.update_traces(texttemplate='%{text:.1f}d', textposition='outside')
        fig_tempo.update_layout(
            xaxis_tickangle=-45,
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig_tempo, width='stretch')
    
    st.markdown("---")
    
    # =====================================================
    # Gráficos - Linha 2
    # =====================================================
    st.header("📞 Análise por Canal e Setor")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Distribuição por canal
        canal_counts = df_filtered['canal_entrada'].value_counts().reset_index()
        canal_counts.columns = ['canal', 'count']
        
        fig_canal = px.pie(
            canal_counts,
            values='count',
            names='canal',
            title="Distribuição por Canal de Entrada",
            color_discrete_sequence=px.colors.qualitative.Set3,
            hole=0.4
        )
        fig_canal.update_traces(textposition='inside', textinfo='percent+label')
        fig_canal.update_layout(height=400)
        st.plotly_chart(fig_canal, width='stretch')
    
    with col2:
        # Distribuição por setor
        setor_counts = df_filtered['responsavel_setor'].value_counts().reset_index()
        setor_counts.columns = ['setor', 'count']
        
        fig_setor = px.bar(
            setor_counts,
            x='setor',
            y='count',
            title="Ocorrências por Setor Responsável",
            labels={'count': 'Quantidade', 'setor': 'Setor'},
            color='count',
            color_continuous_scale='Greens',
            text='count'
        )
        fig_setor.update_traces(textposition='outside')
        fig_setor.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_setor, width='stretch')
    
    st.markdown("---")
    
    # =====================================================
    # Evolução Temporal
    # =====================================================
    st.header("📅 Evolução Temporal")
    
    # Evolução diária
    df_temporal = df_filtered.groupby(df_filtered['data_ocorrencia'].dt.date).size().reset_index(name='count')
    
    fig_evolucao = px.area(
        df_temporal,
        x='data_ocorrencia',
        y='count',
        title="Evolução Diária de Ocorrências",
        labels={'count': 'Número de Ocorrências', 'data_ocorrencia': 'Data'}
    )
    fig_evolucao.update_traces(
        line_color='#1f77b4',
        fillcolor='rgba(31, 119, 180, 0.3)'
    )
    fig_evolucao.update_layout(height=400)
    st.plotly_chart(fig_evolucao, width='stretch')
    
    # =====================================================
    # Heatmap Mensal
    # =====================================================
    col1, col2 = st.columns([2, 1])
    
    with col1:
        df_filtered['ano'] = df_filtered['data_ocorrencia'].dt.year
        df_filtered['mes'] = df_filtered['data_ocorrencia'].dt.month
        df_filtered['mes_nome'] = df_filtered['data_ocorrencia'].dt.strftime('%b')
        
        heatmap_data = df_filtered.groupby(['ano', 'mes', 'mes_nome']).size().reset_index(name='count')
        heatmap_pivot = heatmap_data.pivot(index='mes_nome', columns='ano', values='count').fillna(0)
        
        # Ordenar meses corretamente
        month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        heatmap_pivot = heatmap_pivot.reindex([m for m in month_order if m in heatmap_pivot.index])
        
        fig_heatmap = px.imshow(
            heatmap_pivot,
            title="Heatmap Mensal de Ocorrências",
            labels=dict(x="Ano", y="Mês", color="Ocorrências"),
            color_continuous_scale="Viridis",
            aspect="auto"
        )
        fig_heatmap.update_layout(height=400)
        st.plotly_chart(fig_heatmap, width='stretch')
    
    with col2:
        st.subheader("🔍 Insights Principais")
        
        tipo_mais_comum = df_filtered['tipo_problema'].mode()
        tipo_mais_comum = tipo_mais_comum[0] if len(tipo_mais_comum) > 0 else "N/A"
        
        canal_mais_rapido = df_filtered.groupby('canal_entrada')['tempo_resolucao'].mean().idxmin()
        
        setor_mais_demandado = df_filtered['responsavel_setor'].mode()
        setor_mais_demandado = setor_mais_demandado[0] if len(setor_mais_demandado) > 0 else "N/A"
        
        st.info(f"""
        **📊 Tipo mais recorrente:**  
        {tipo_mais_comum}
        
        **⚡ Canal mais eficiente:**  
        {canal_mais_rapido}
        
        **🏢 Setor mais demandado:**  
        {setor_mais_demandado}
        
        **📈 Cumprimento SLA:**  
        {pct_sla5:.1f}% dos casos
        
        **⏱️ Tempo médio:**  
        {tempo_medio:.1f} dias
        """)
    
    st.markdown("---")
    
    # =====================================================
    # Tabela de Dados
    # =====================================================
    with st.expander("📋 Ver Dados Detalhados"):
        st.dataframe(
            df_filtered[['data_ocorrencia', 'tipo_problema', 'canal_entrada', 
                        'classificacao', 'tempo_resolucao', 'responsavel_setor']]\
                .sort_values('data_ocorrencia', ascending=False),
            width='stretch',
            height=400
        )
        
        # Botão de download
        csv = df_filtered.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name='ocorrencias_filtradas.csv',
            mime='text/csv',
        )
    
    # =====================================================
    # Footer
    # =====================================================
    st.markdown("---")
    st.caption(f"📈 Dashboard atualizado em {pd.Timestamp.now().strftime('%d/%m/%Y às %H:%M')} | 🔄 Dados processados: {len(df)} registros")

except FileNotFoundError:
    st.error("❌ Arquivo de dados não encontrado! Certifique-se de que o arquivo `dados_ocorrencias_formatado.csv` está na pasta `data/processed/`")
except Exception as e:
    st.error(f"❌ Erro ao carregar dados: {e}")
    st.exception(e)
