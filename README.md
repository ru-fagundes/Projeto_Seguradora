# 🩺 Análise de Ocorrências Internas – Seguradora de Convênio Médico

Este projeto tem como objetivo realizar uma análise de dados internos do setor de resolução de problemas de uma seguradora de saúde, com foco na identificação de gargalos operacionais, previsão de ocorrências críticas e sugestões de melhoria baseadas em dados.

---

## 📊 Objetivos

- Analisar ocorrências por tipo de problema, canal de entrada e reincidência
- Medir tempos médios de resolução por classificação
- Prever a gravidade de futuras ocorrências usando Machine Learning
- Auxiliar a tomada de decisão por meio de dashboards e KPIs

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Pandas, Seaborn, Matplotlib, Scikit-learn, Plotly
- **Dashboard em HTML**: Visualização de indicadores
- **Visual Studio Code**: Organização do projeto
- **API Simulada**: Simulação de extração de dados via requests

---

## 🧪 Etapas do Projeto

1. **Simulação da coleta de dados** com API RESTful fictícia
2. **Análise exploratória** com gráficos de frequência e tempo de resolução
3. **Criação de modelo preditivo** para classificar novas ocorrências como críticas, médias ou baixas
4. **Exportação de dados formatados** para uso no Power BI
5. **Geração de insights e recomendações** baseadas nos dados

---

## 🔮 Insights Gerados

- Tipo mais recorrente: erro sistema
- Canal mais eficiente: telefone
- Período crítico: 2024-01
- Setor mais demandado: Setor B
- Cumprimento SLA (≤5 dias): 70.6%
- Tempo médio de resolução: 4.5 dias
- Taxa de reincidência: 30.8%
---

## 📁 Arquivos do Projeto

- `analise_ocorrencias_seguradora.ipynb`: notebook completo com a análise e o modelo
- `dados_ocorrencias_seguradora.csv`: base de dados simulada
- `dados_ocorrencias_formatado.csv`: dataset pronto para importar para geração de dashboards
- `dashboard_interativa_corrigido.py`: dashboard gerada em Python
- `dashboard_ocorrencias_interativo.html`: dashboard interativo em html

---

## 💡 Próximas Melhorias

- Integração real com APIs da seguradora
- Interface web com Streamlit para relatórios automatizados
- Alertas preditivos em tempo real com base nos dados

---

## 👩‍💻 Desenvolvido por

**Rubia Fagundes**  
[LinkedIn](https://www.linkedin.com/in/rubiafagundes) | rubiafagundes_ds@outlook.com
