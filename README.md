# 🏥 Análise de Ocorrências - Seguradora

> Sistema completo de análise de dados, machine learning e dashboard interativo para gestão de ocorrências em seguradora de convênio médico.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://projeto-seguradora.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🌐 Acesso Rápido

**Dashboard Online**: [https://projeto-seguradora.streamlit.app](https://projeto-seguradora.streamlit.app)

> Acesse o dashboard interativo diretamente pelo navegador, sem necessidade de instalação!

## 📊 Visão Geral

Projeto de análise exploratória (EDA) e modelagem preditiva para identificar padrões, otimizar processos e reduzir tempo de resolução de ocorrências. Inclui dashboard web interativo com Streamlit para visualização e tomada de decisão em tempo real.

## ✨ Funcionalidades

- **Análise Exploratória**: Estatísticas, distribuições e correlações entre variáveis
- **Machine Learning**: Classificação de criticidade com 5 algoritmos (Random Forest, SVM, etc.)
- **Dashboard Interativo**: Interface web com filtros dinâmicos, KPIs e gráficos responsivos
- **Insights Automáticos**: Identificação de gargalos, reincidências e oportunidades

## 🗂️ Estrutura

```
Projeto_Seguradora/
├── data/
│   ├── raw/                          # Dados originais
│   └── processed/                    # Dados processados
├── notebooks/
│   └── analise_ocorrencias_seguradora.ipynb  # EDA + ML
├── src/
│   └── dashboard_streamlit.py        # Dashboard web
├── models/                           # Modelos salvos (após treinamento)
├── dashboards/                       # Exportações HTML (opcional)
└── reports/                          # Relatórios finais
```

## 🚀 Execução Local (Opcional)

Caso queira rodar o projeto localmente:

### 1. Clonar Repositório

```bash
git clone https://github.com/ru-fagundes/Projeto_Seguradora.git
cd Projeto_Seguradora
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Executar Dashboard

```bash
streamlit run src/dashboard_streamlit.py
```

Acesse em: **http://localhost:8501**

### 4. Análise Completa (Notebook)

```bash
jupyter notebook notebooks/analise_ocorrencias_seguradora.ipynb
```

## 📊 Features do Dashboard
## 📊 Features do Dashboard

- 📊 5 KPIs principais (total, tempo médio, críticos, reincidentes, SLA)
- 🔍 Filtros por período, tipo, canal e classificação
- 📈 10 visualizações interativas (barras, pizza, área, heatmap)
- 📥 Exportação de dados filtrados em CSV
- 📱 Layout responsivo e otimizado

## 📦 Dependências

- **Python 3.8+**
- **Análise**: pandas, numpy, matplotlib, seaborn
- **Machine Learning**: scikit-learn
- **Dashboard**: streamlit, plotly
- **Notebook**: jupyter

## 📈 Resultados

- **Tempo médio**: Análise de resolução por tipo de ocorrência
- **Canais eficientes**: Identificação dos canais mais rápidos
- **Padrões temporais**: Sazonalidade e tendências
- **Predição**: Classificação automática de criticidade com >80% acurácia

## 📝 Documentação Adicional

- **Notebook**: Comentários inline explicando cada etapa da análise
- **Dashboard**: Interface intuitiva com tooltips e labels descritivos
- **Código**: Funções documentadas com docstrings

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-green)
![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Plotly](https://img.shields.io/badge/Plotly-Interactive_Viz-purple)

---

**📌 Projeto desenvolvido para otimização de processos operacionais em seguradoras de saúde**

---

## 👩‍💻 Desenvolvido por

**Rubia Fagundes**  
[LinkedIn](https://www.linkedin.com/in/rubiafagundes) | rubiafagundes_ds@outlook.com

---

## 📄 Licença / Aviso  
Dados são fictícios / simulados. Projeto tem finalidade educacional.  
