# 🚀 Guia de Uso Rápido

## Abrir Dashboard

```bash
streamlit run src/dashboard_streamlit.py
```

Acesse: **http://localhost:8501**

## Executar Análise (Jupyter)

```bash
jupyter notebook notebooks/analise_ocorrencias_seguradora.ipynb
```

Execute as células em sequência.

## Estrutura de Dados

### Arquivo de Entrada
`data/raw/dados_ocorrencias_seguradora.csv`

### Arquivo Processado
`data/processed/dados_ocorrencias_formatado.csv`

### Colunas Principais
- `data_ocorrencia` - Data da ocorrência
- `tipo_problema` - Categoria do problema
- `tempo_resolucao` - Dias para resolver
- `canal_entrada` - Como chegou (telefone, email, etc.)
- `classificacao` - Criticidade (baixa/média/alta)
- `responsavel_setor` - Departamento responsável
- `cliente_reincidente` - Se é caso repetido (sim/não)

## Comandos Úteis

### Verificar Dados
```bash
python -c "import pandas as pd; df=pd.read_csv('data/processed/dados_ocorrencias_formatado.csv'); print(df.info())"
```

### Instalar Dependências
```bash
pip install -r requirements.txt
```

### Ver Versões
```bash
pip list | findstr "pandas streamlit plotly scikit-learn"
```

## Estrutura Final

```
Projeto_Seguradora/
├── data/
│   ├── raw/dados_ocorrencias_seguradora.csv
│   └── processed/dados_ocorrencias_formatado.csv
├── notebooks/analise_ocorrencias_seguradora.ipynb
├── src/dashboard_streamlit.py
├── models/
├── dashboards/
├── reports/
├── README.md
└── requirements.txt
```

## Troubleshooting

### Dashboard não abre
- Verifique se o Streamlit está instalado: `pip show streamlit`
- Execute do diretório raiz do projeto
- Porta 8501 pode estar em uso: `streamlit run src/dashboard_streamlit.py --server.port 8502`

### Dados não encontrados
- Confirme que `data/processed/dados_ocorrencias_formatado.csv` existe
- Execute o notebook para gerar dados processados

### Erro de imports
- Reinstale dependências: `pip install -r requirements.txt --force-reinstall`
- Verifique versão Python: `python --version` (requer 3.8+)
