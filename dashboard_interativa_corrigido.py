import pandas as pd
from plotly.subplots import make_subplots
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# Dashboard Interativo de Ocorrências - Seguradora
# =====================================================

try:
    # ----------------------------
    # 1. Carregar dados
    # ----------------------------
    df = pd.read_csv("dados_ocorrencias_formatado.csv")
    
    # Verificar se as colunas necessárias existem
    required_columns = ['data_ocorrencia', 'tipo_problema', 'tempo_resolucao', 
                       'canal_entrada', 'classificacao', 'responsavel_setor', 'cliente_reincidente']
    
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Colunas faltando no dataset: {missing_columns}")
    
    # Converter datas
    df['data_ocorrencia'] = pd.to_datetime(df['data_ocorrencia'])
    
    print(f"✅ Dados carregados com sucesso: {len(df)} registros")
    
    # ----------------------------
    # 2. Calcular KPIs
    # ----------------------------
    total_ocorrencias = len(df)
    tempo_medio = df['tempo_resolucao'].mean()
    pct_criticos = (df['classificacao'].eq("crítica").mean() * 100)
    pct_reincidentes = (df['cliente_reincidente'].eq("sim").mean() * 100)
    pct_sla5 = (df['tempo_resolucao'].le(5).mean() * 100)
    
    # ----------------------------
    # 3. KPIs (cards grandes)
    # ----------------------------
    fig_kpis = make_subplots(rows=1, cols=5, specs=[[{"type": "domain"}]*5],
                             subplot_titles=("Total Ocorrências",
                                             "Tempo Médio (dias)",
                                             "% Casos Críticos",
                                             "% Reincidentes",
                                             "% SLA ≤ 5 dias"))
    
    kpi_values = [total_ocorrencias, tempo_medio, pct_criticos, pct_reincidentes, pct_sla5]
    kpi_suffix = ["", " dias", "%", "%", "%"]
    
    for i, (val, suf) in enumerate(zip(kpi_values, kpi_suffix)):
        fig_kpis.add_trace(go.Indicator(mode="number",
                                        value=round(val, 1),
                                        number={'suffix': suf, 'font': {'size': 24}}),
                           row=1, col=i+1)
    
    fig_kpis.update_layout(title_text="📊 KPIs Gerais", height=300, showlegend=False)
    
    # ----------------------------
    # 4. Gráficos principais
    # ----------------------------
    
    # Distribuição por tipo de problema
    tipo_counts = df['tipo_problema'].value_counts().reset_index()
    tipo_counts.columns = ['tipo_problema', 'count']
    fig_tipos = px.bar(tipo_counts,
                       x='tipo_problema', y='count',
                       title="📋 Ocorrências por Tipo de Problema",
                       labels={'count':'Quantidade', 'tipo_problema':'Tipo de Problema'},
                       color='count',
                       color_continuous_scale='Blues')
    fig_tipos.update_layout(xaxis_tickangle=45)
    
    # Tempo médio por tipo de problema
    tempo_tipo = df.groupby('tipo_problema')['tempo_resolucao'].mean().reset_index()
    fig_tempo_tipo = px.bar(tempo_tipo,
                            x='tipo_problema', y='tempo_resolucao',
                            title="⏱️ Tempo Médio de Resolução por Tipo",
                            labels={'tempo_resolucao':'Dias', 'tipo_problema':'Tipo de Problema'},
                            color='tempo_resolucao',
                            color_continuous_scale='Reds')
    fig_tempo_tipo.update_layout(xaxis_tickangle=45)
    
    # Ocorrências por canal de entrada
    canal_counts = df['canal_entrada'].value_counts().reset_index()
    canal_counts.columns = ['canal_entrada', 'count']
    fig_canais = px.pie(canal_counts,
                        values='count', names='canal_entrada',
                        title="📞 Distribuição por Canal de Entrada",
                        color_discrete_sequence=px.colors.qualitative.Set3)
    
    # Tempo médio por canal
    tempo_canal = df.groupby('canal_entrada')['tempo_resolucao'].mean().reset_index()
    fig_tempo_canal = px.bar(tempo_canal,
                             x='canal_entrada', y='tempo_resolucao',
                             title="📈 Tempo Médio por Canal",
                             labels={'tempo_resolucao':'Dias', 'canal_entrada':'Canal'},
                             color='tempo_resolucao',
                             color_continuous_scale='Oranges')
    
    # Ocorrências por setor
    setor_counts = df['responsavel_setor'].value_counts().reset_index()
    setor_counts.columns = ['setor', 'count']
    fig_setores = px.treemap(setor_counts, 
                             path=['setor'], values='count',
                             title="🏢 Distribuição por Setor Responsável",
                             color='count',
                             color_continuous_scale='Greens')
    
    # Evolução temporal
    df_temporal = df.groupby(df['data_ocorrencia'].dt.date).size().reset_index(name='count')
    fig_evolucao = px.line(df_temporal,
                           x='data_ocorrencia', y='count',
                           title="📅 Evolução Temporal das Ocorrências",
                           labels={'count':'Número de Ocorrências', 'data_ocorrencia':'Data'})
    fig_evolucao.update_traces(line_color='#2E86AB', line_width=3)
    
    # Heatmap mensal
    df['ano'] = df['data_ocorrencia'].dt.year
    df['mes'] = df['data_ocorrencia'].dt.month
    df['mes_nome'] = df['data_ocorrencia'].dt.month_name()
    
    heatmap_data = df.groupby(['ano','mes_nome']).size().reset_index(name='count')
    fig_heatmap = px.density_heatmap(heatmap_data, 
                                     x='ano', y='mes_nome', z='count',
                                     title="🗓️ Heatmap Mensal de Ocorrências",
                                     color_continuous_scale="Viridis",
                                     labels={'count':'Número de Ocorrências'})
    
    # ----------------------------
    # 5. Montar HTML final
    # ----------------------------
    graphs_html = ""
    graph_list = [
        (fig_kpis, "KPIs"),
        (fig_tipos, "Tipos de Problema"),
        (fig_tempo_tipo, "Tempo por Tipo"),
        (fig_canais, "Canais de Entrada"),
        (fig_tempo_canal, "Tempo por Canal"),
        (fig_setores, "Setores"),
        (fig_evolucao, "Evolução Temporal"),
        (fig_heatmap, "Heatmap Mensal")
    ]
    
    for fig, name in graph_list:
        try:
            graphs_html += fig.to_html(full_html=False, include_plotlyjs='cdn') + "<br><hr><br>"
            print(f"✅ Gráfico '{name}' gerado com sucesso")
        except Exception as e:
            print(f"⚠️ Erro ao gerar gráfico '{name}': {e}")
            continue
    
    # Calcular insights com tratamento de erros
    try:
        tipo_mais_comum = df['tipo_problema'].mode()[0]
        canal_mais_rapido = df.groupby('canal_entrada')['tempo_resolucao'].mean().idxmin()
        mes_critico = df['data_ocorrencia'].dt.to_period('M').value_counts().idxmax()
        setor_mais_demandado = df['responsavel_setor'].mode()[0]
    except Exception as e:
        print(f"⚠️ Erro ao calcular insights: {e}")
        tipo_mais_comum = "N/A"
        canal_mais_rapido = "N/A"
        mes_critico = "N/A"
        setor_mais_demandado = "N/A"
    
    html_content = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>Dashboard Interativo - Ocorrências Seguradora</title>
        <style>
            body {{ 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                margin: 20px; 
                background-color: #f8f9fa;
            }}
            h1 {{ 
                color: #2c3e50; 
                text-align: center; 
                background: linear-gradient(45deg, #3498db, #2c3e50);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-size: 2.5em;
                margin-bottom: 30px;
            }}
            h2 {{ 
                color: #34495e; 
                border-left: 4px solid #3498db;
                padding-left: 15px;
            }}
            ul {{ 
                background-color: #ffffff; 
                padding: 20px; 
                border-radius: 10px; 
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                line-height: 1.6;
            }}
            li {{
                margin-bottom: 10px;
                font-size: 1.1em;
            }}
            footer {{
                margin-top: 50px; 
                text-align: center; 
                color: #7f8c8d;
                border-top: 1px solid #ecf0f1;
                padding-top: 20px;
            }}
            hr {{
                border: none;
                height: 2px;
                background: linear-gradient(45deg, #3498db, #2c3e50);
                margin: 30px 0;
            }}
        </style>
    </head>
    <body>
        <h1>🏥 Dashboard Interativo - Análise de Ocorrências</h1>
        {graphs_html}
        <h2>🔍 Insights Automáticos Gerados</h2>
        <ul>
            <li>📊 <strong>Tipo mais recorrente:</strong> {tipo_mais_comum}</li>
            <li>⚡ <strong>Canal mais eficiente:</strong> {canal_mais_rapido}</li>
            <li>📅 <strong>Período crítico:</strong> {mes_critico}</li>
            <li>🏢 <strong>Setor mais demandado:</strong> {setor_mais_demandado}</li>
            <li>🎯 <strong>Cumprimento SLA (≤5 dias):</strong> {pct_sla5:.1f}%</li>
            <li>⏱️ <strong>Tempo médio de resolução:</strong> {tempo_medio:.1f} dias</li>
            <li>🔄 <strong>Taxa de reincidência:</strong> {pct_reincidentes:.1f}%</li>
        </ul>
        <footer>
            <p>📈 Dashboard gerado automaticamente em {pd.Timestamp.now().strftime('%d/%m/%Y às %H:%M')}</p>
            <p>🔄 Dados atualizados em tempo real</p>
        </footer>
    </body>
    </html>
    """
    
    # Salvar arquivo HTML
    output_file = Path("dashboard_ocorrencias_interativo.html")
    output_file.write_text(html_content, encoding="utf-8")
    print(f"✅ Dashboard gerado com sucesso: {output_file.absolute()}")
    
except FileNotFoundError:
    print("❌ Erro: Arquivo 'dados_ocorrencias_formatado.csv' não encontrado!")
except Exception as e:
    print(f"❌ Erro geral no processamento: {e}")
