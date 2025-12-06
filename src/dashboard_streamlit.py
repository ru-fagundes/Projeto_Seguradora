import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(
    page_title='Dashboard - Ocorrencias Seguradora',
    page_icon='📊',
    layout='wide'
)

@st.cache_data
def load_data():
    script_dir = Path(__file__).parent
    data_path = script_dir.parent / 'data' / 'processed' / 'dados_ocorrencias_formatado.csv'
    df = pd.read_csv(data_path)
    df['data_ocorrencia'] = pd.to_datetime(df['data_ocorrencia'])
    return df

try:
    df = load_data()
    
    st.title('📊 Dashboard de Ocorrencias - Seguradora')
    st.markdown('---')
    
    # Filtros
    st.sidebar.header('🔍 Filtros')
    
    min_date = df['data_ocorrencia'].min().date()
    max_date = df['data_ocorrencia'].max().date()
    date_range = st.sidebar.date_input(
        'Periodo',
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    tipos = ['Todos'] + list(df['tipo_problema'].unique())
    tipo_selecionado = st.sidebar.selectbox('Tipo de Problema', tipos)
    
    canais = ['Todos'] + list(df['canal_entrada'].unique())
    canal_selecionado = st.sidebar.selectbox('Canal de Entrada', canais)
    
    classificacoes = ['Todos'] + list(df['classificacao'].unique())
    class_selecionada = st.sidebar.selectbox('Classificacao', classificacoes)
    
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
    
    if class_selecionada != 'Todos':
        df_filtered = df_filtered[df_filtered['classificacao'] == class_selecionada]
    
    st.sidebar.info(f'**{len(df_filtered)}** registros de **{len(df)}** totais')
    
    # KPIs
    st.header('📈 Indicadores Principais')
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric('Total de Ocorrencias', f'{len(df_filtered):,}')
    
    with col2:
        tempo_medio = df_filtered['tempo_resolucao'].mean()
        st.metric('Tempo Medio (dias)', f'{tempo_medio:.1f}')
    
    with col3:
        pct_criticos = (df_filtered['classificacao'] == 'crítica').mean() * 100
        st.metric('Casos Criticos', f'{pct_criticos:.1f}%')
    
    with col4:
        pct_reincidentes = (df_filtered['cliente_reincidente'] == 'sim').mean() * 100
        st.metric('Taxa Reincidencia', f'{pct_reincidentes:.1f}%')
    
    with col5:
        pct_sla = (df_filtered['tempo_resolucao'] <= 5).mean() * 100
        st.metric('SLA <= 5 dias', f'{pct_sla:.1f}%')
    
    st.markdown('---')
    
    # Secao 1: Analise por Tipo e Canal
    st.header('📊 Analise por Tipo e Canal')
    col1, col2 = st.columns(2)
    
    with col1:
        tipo_counts = df_filtered['tipo_problema'].value_counts().reset_index()
        tipo_counts.columns = ['tipo_problema', 'count']
        
        fig1 = px.bar(
            tipo_counts,
            x='tipo_problema',
            y='count',
            title='Ocorrencias por Tipo de Problema',
            color='count',
            color_continuous_scale='Blues',
            text='count'
        )
        fig1.update_traces(textposition='outside')
        fig1.update_layout(height=400, showlegend=False, xaxis_tickangle=-45)
        st.plotly_chart(fig1, width='stretch')
    
    with col2:
        canal_counts = df_filtered['canal_entrada'].value_counts().reset_index()
        canal_counts.columns = ['canal', 'count']
        
        fig2 = px.pie(
            canal_counts,
            values='count',
            names='canal',
            title='Distribuicao por Canal de Entrada',
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig2.update_traces(textposition='inside', textinfo='percent+label')
        fig2.update_layout(height=400)
        st.plotly_chart(fig2, width='stretch')
    
    st.markdown('---')
    
    # Secao 2: Analise por Classificacao e Setor
    st.header('⚡ Analise por Classificacao e Setor')
    col1, col2 = st.columns(2)
    
    with col1:
        tempo_class = df_filtered.groupby('classificacao')['tempo_resolucao'].mean().reset_index()
        tempo_class = tempo_class.sort_values('tempo_resolucao', ascending=False)
        
        fig3 = px.bar(
            tempo_class,
            x='classificacao',
            y='tempo_resolucao',
            title='Tempo Medio de Resolucao por Classificacao',
            color='tempo_resolucao',
            color_continuous_scale='Oranges',
            text='tempo_resolucao'
        )
        fig3.update_traces(texttemplate='%{text:.1f}d', textposition='outside')
        fig3.update_layout(height=400, showlegend=False, yaxis_title='Dias')
        st.plotly_chart(fig3, width='stretch')
    
    with col2:
        setor_counts = df_filtered['responsavel_setor'].value_counts().reset_index()
        setor_counts.columns = ['setor', 'count']
        
        fig4 = px.bar(
            setor_counts,
            x='setor',
            y='count',
            title='Ocorrencias por Setor Responsavel',
            color='count',
            color_continuous_scale='Greens',
            text='count'
        )
        fig4.update_traces(textposition='outside')
        fig4.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig4, width='stretch')
    
    st.markdown('---')
    
    # Secao 3: Analise Temporal
    st.header('📅 Analise Temporal')
    
    df_temporal = df_filtered.groupby(df_filtered['data_ocorrencia'].dt.date).size().reset_index(name='count')
    
    fig5 = px.area(
        df_temporal,
        x='data_ocorrencia',
        y='count',
        title='Evolucao Diaria de Ocorrencias',
        labels={'data_ocorrencia': 'Data', 'count': 'Numero de Ocorrencias'}
    )
    fig5.update_traces(line_color='#1f77b4', fillcolor='rgba(31, 119, 180, 0.3)')
    fig5.update_layout(height=400)
    st.plotly_chart(fig5, width='stretch')
    
    st.markdown('---')
    
    # Secao 4: Heatmap e Correlacao
    st.header('🔥 Analise de Correlacao')
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Heatmap mensal
        df_heatmap = df_filtered.copy()
        df_heatmap['ano'] = df_heatmap['data_ocorrencia'].dt.year
        df_heatmap['mes'] = df_heatmap['data_ocorrencia'].dt.month
        
        pivot_data = df_heatmap.groupby(['mes', 'ano']).size().reset_index(name='count')
        pivot_table = pivot_data.pivot(index='mes', columns='ano', values='count').fillna(0)
        
        fig6 = px.imshow(
            pivot_table,
            title='Heatmap: Ocorrencias por Mes e Ano',
            labels=dict(x='Ano', y='Mes', color='Ocorrencias'),
            color_continuous_scale='Viridis',
            aspect='auto'
        )
        fig6.update_layout(height=400)
        st.plotly_chart(fig6, width='stretch')
    
    with col2:
        st.subheader('📊 Estatisticas Gerais')
        
        # Estatisticas principais
        stats_data = {
            'Metrica': [
                'Total de Casos',
                'Tempo Medio (dias)',
                'Tempo Maximo (dias)',
                'Tempo Minimo (dias)',
                'Taxa de Reincidencia',
                'Casos Criticos'
            ],
            'Valor': [
                f'{len(df_filtered)}',
                f'{df_filtered["tempo_resolucao"].mean():.1f}',
                f'{df_filtered["tempo_resolucao"].max()}',
                f'{df_filtered["tempo_resolucao"].min()}',
                f'{pct_reincidentes:.1f}%',
                f'{(df_filtered["classificacao"] == "crítica").sum()}'
            ]
        }
        
        st.dataframe(
            pd.DataFrame(stats_data),
            hide_index=True,
            width='stretch'
        )
    
    st.markdown('---')
    
    # Secao 5: Analise Detalhada
    st.header('🔍 Analise Detalhada')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Reincidencia por tipo
        reinc_tipo = df_filtered.groupby(['tipo_problema', 'cliente_reincidente']).size().reset_index(name='count')
        
        fig7 = px.bar(
            reinc_tipo,
            x='tipo_problema',
            y='count',
            color='cliente_reincidente',
            title='Reincidencia por Tipo de Problema',
            barmode='group',
            color_discrete_map={'sim': '#ff7f0e', 'não': '#2ca02c'}
        )
        fig7.update_layout(height=400, xaxis_tickangle=-45)
        st.plotly_chart(fig7, width='stretch')
    
    with col2:
        # Tempo por canal
        tempo_canal = df_filtered.groupby('canal_entrada')['tempo_resolucao'].mean().reset_index()
        tempo_canal = tempo_canal.sort_values('tempo_resolucao', ascending=False)
        
        fig8 = px.bar(
            tempo_canal,
            y='canal_entrada',
            x='tempo_resolucao',
            title='Tempo Medio de Resolucao por Canal',
            orientation='h',
            color='tempo_resolucao',
            color_continuous_scale='Reds',
            text='tempo_resolucao'
        )
        fig8.update_traces(texttemplate='%{text:.1f}d', textposition='outside')
        fig8.update_layout(height=400, xaxis_title='Dias')
        st.plotly_chart(fig8, width='stretch')
    
    st.markdown('---')
    
    # Tabela de dados
    with st.expander('📋 Ver Dados Detalhados'):
        st.dataframe(
            df_filtered[['data_ocorrencia', 'tipo_problema', 'canal_entrada', 
                        'classificacao', 'tempo_resolucao', 'responsavel_setor', 
                        'cliente_reincidente']]
                .sort_values('data_ocorrencia', ascending=False),
            width='stretch',
            height=400
        )
        
        csv = df_filtered.to_csv(index=False).encode('utf-8')
        st.download_button(
            '📥 Download CSV',
            data=csv,
            file_name='ocorrencias_filtradas.csv',
            mime='text/csv'
        )
    
    # Footer com info
    st.markdown('---')
    st.caption(f'📊 Dashboard atualizado | Total de {len(df)} registros no sistema')

except Exception as e:
    st.error(f'Erro ao carregar dados: {e}')
    st.exception(e)
