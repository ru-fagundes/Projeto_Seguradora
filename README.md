<div align="center">
  <img src="assets/images/banner.png" alt="Banner Projeto Seguradora" width="100%">
  
  # 🏥 Sistema de Análise de Ocorrências - Seguradora
  
  ##### Análise de Dados, Machine Learning e Dashboard Interativo para Gestão de Seguros de Saúde
  
  ![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat) ![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
  
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
  
</div>

---

## 📋 Sobre o Projeto

Sistema completo de análise preditiva para otimização de processos operacionais em seguradoras de saúde. Combina análise exploratória de dados (EDA), algoritmos de machine learning e dashboard web interativo para identificar padrões, reduzir tempo de resolução e melhorar a tomada de decisão.

### 🎯 Principais Recursos

- **Análise Exploratória Completa**: Estatísticas descritivas, correlações e visualizações avançadas
- **Modelos Preditivos**: 5 algoritmos de ML comparados (Random Forest, SVM, Gradient Boosting, KNN, Logistic Regression)
- **Dashboard Interativo**: Interface web com filtros dinâmicos, KPIs em tempo real e exportação de dados
- **Insights Acionáveis**: Identificação automática de gargalos operacionais e padrões de reincidência

### 📊 Principais Resultados

| Métrica | Resultado |
|---------|-----------|
| **Acurácia do Modelo** | >80% na classificação de criticidade |
| **Redução de Tempo** | Identificação de canais 40% mais eficientes |
| **Padrões Detectados** | Análise de sazonalidade e tendências temporais |
| **Visualizações** | 10+ gráficos interativos com Plotly |

---

## 🗂️ Estrutura do Projeto

```
Projeto_Seguradora/
├── 📁 assets/              # Recursos visuais (banner, imagens)
├── 📁 config/              # Arquivos de configuração
│   └── requirements.txt    # Dependências Python
├── 📁 data/
│   ├── raw/                # Dados originais (CSV)
│   └── processed/          # Dados processados pelo notebook
├── 📁 notebooks/           # Análise exploratória e ML
│   └── analise_ocorrencias_seguradora.ipynb
├── 📁 src/                 # Código-fonte da aplicação
│   └── dashboard_streamlit.py
└── README.md
```

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1️⃣ **Clone o repositório**
```bash
git clone https://github.com/ru-fagundes/Projeto_Seguradora.git
cd Projeto_Seguradora
```

2️⃣ **Instale as dependências**
```bash
pip install -r config/requirements.txt
```

3️⃣ **Execute o dashboard**
```bash
streamlit run src/dashboard_streamlit.py
```

O dashboard estará disponível em **http://localhost:8501**

### Executar Notebook Jupyter

```bash
jupyter notebook notebooks/analise_ocorrencias_seguradora.ipynb
```

---

## 💡 Funcionalidades do Dashboard

### KPIs e Métricas
- Total de ocorrências registradas
- Tempo médio de resolução
- Taxa de ocorrências críticas
- Percentual de clientes reincidentes
- Cumprimento de SLA por setor

### Visualizações Interativas
- Distribuição por tipo de problema (barras)
- Tempo de resolução por canal (área)
- Matriz de correlação (heatmap)
- Análise de reincidência (pizza)
- Tendências temporais (linha)

### Recursos Avançados
- ✅ Filtros dinâmicos por período, tipo e classificação
- ✅ Exportação de dados em CSV
- ✅ Interface responsiva e otimizada
- ✅ Atualização em tempo real

---

##  Metodologia

1. **Coleta e Preparação**: Limpeza e formatação de 500+ registros de ocorrências
2. **Análise Exploratória**: Estatísticas descritivas, distribuições e correlações
3. **Feature Engineering**: Criação de variáveis derivadas e codificação
4. **Modelagem**: Treinamento e comparação de 5 algoritmos de classificação
5. **Validação**: Cross-validation e análise de feature importance
6. **Deploy**: Dashboard interativo para visualização e insights

---

## 👩‍💻 Autora

**Rubia Fagundes**  
Data Scientist | Machine Learning | Business Intelligence

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rubiafagundes)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:rubiafagundes_ds@outlook.com)

---

## 📄 Licença

Este projeto utiliza dados fictícios e tem finalidade **exclusivamente educacional**.  
Desenvolvido como portfólio de ciência de dados e análise preditiva.

---

<div align="center">
  
  **⭐ Se este projeto foi útil, considere dar uma estrela!**
  
</div>
