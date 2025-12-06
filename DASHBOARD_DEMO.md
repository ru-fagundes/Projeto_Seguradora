# 📊 Dashboard de Ocorrências - Demonstração

## 🌐 Acesso ao Dashboard

**⚠️ IMPORTANTE**: Este dashboard é uma aplicação Python/Streamlit que **não pode ser acessada diretamente pelo link do GitHub**.

### Como Visualizar o Dashboard

Para acessar e utilizar o dashboard interativo, siga os passos abaixo:

---

## 🔧 Instrução de Instalação

### Passo 1: Fazer Fork do Repositório
1. Acesse: https://github.com/ru-fagundes/Projeto_Seguradora
2. Clique no botão **"Fork"** no canto superior direito
3. O repositório será copiado para sua conta GitHub

### Passo 2: Clonar o Repositório
```bash
git clone https://github.com/SEU_USUARIO/Projeto_Seguradora.git
cd Projeto_Seguradora
```

### Passo 3: Instalar Dependências
```bash
pip install -r requirements.txt
```

**Dependências instaladas:**
- pandas 2.0.0+ (análise de dados)
- numpy 1.24.0+ (computação numérica)
- matplotlib 3.7.0+ (gráficos estáticos)
- seaborn 0.12.0+ (visualizações estatísticas)
- plotly 5.14.0+ (gráficos interativos)
- streamlit 1.28.0+ (framework web)
- scikit-learn 1.3.0+ (machine learning)

### Passo 4: Executar o Dashboard
```bash
streamlit run src/dashboard_streamlit.py
```

### Passo 5: Acessar no Navegador
O dashboard será aberto automaticamente em:
- **URL Local**: http://localhost:8501
- **URL de Rede**: http://SEU_IP:8501 (para acesso em rede local)

---

## 📱 Interface do Dashboard

### 🎯 Visão Geral da Interface

#### **Cabeçalho Principal**
```
📊 Dashboard de Ocorrências - Seguradora
────────────────────────────────────────────
```

#### **Barra Lateral - Filtros (🔍)**

**Filtros Disponíveis:**
1. **Período**: Seletor de intervalo de datas (date picker)
   - Data inicial: 01/01/2024
   - Data final: 31/12/2024

2. **Tipo de Problema**: Dropdown
   - Todos
   - Atraso no Atendimento
   - Cobrança Indevida
   - Erro de Sistema
   - Falta de Comunicação
   - Negativa de Cobertura

3. **Canal de Entrada**: Dropdown
   - Todos
   - E-mail
   - Telefone
   - Presencial
   - Chat Online
   - App Móvel

4. **Classificação**: Dropdown
   - Todos
   - Urgente
   - Alta
   - Média
   - Baixa

---

### 📊 Seção de KPIs (Métricas Principais)

**Layout em 5 Colunas:**

| 📈 Total de Ocorrências | ⏱️ Tempo Médio (dias) | 🔴 Casos Críticos | 🔁 Taxa de Reincidência | ✅ SLA Cumprido |
|------------------------|---------------------|------------------|----------------------|----------------|
| 500                    | 6.5                | 120              | 15.2%                | 78.4%          |

---

### 📈 Visualizações (10 Gráficos Interativos)

#### **1. Distribuição por Tipo de Problema** (Gráfico de Barras)
- **Eixo X**: Tipo de Problema
- **Eixo Y**: Quantidade de Ocorrências
- **Cores**: Escala de cores diferenciada por tipo
- **Interatividade**: Hover mostra valor exato

**Exemplo de Dados:**
```
Negativa de Cobertura:     145 ocorrências
Atraso no Atendimento:     125 ocorrências
Cobrança Indevida:         98 ocorrências
Erro de Sistema:           82 ocorrências
Falta de Comunicação:      50 ocorrências
```

---

#### **2. Distribuição por Canal de Entrada** (Gráfico de Pizza)
- **Segmentos**: Proporção de cada canal
- **Labels**: Nome do canal + percentual
- **Cores**: Paleta vibrante
- **Interatividade**: Click para destacar fatia

**Exemplo de Dados:**
```
E-mail:        35% (175 casos)
Telefone:      28% (140 casos)
Chat Online:   20% (100 casos)
Presencial:    12% (60 casos)
App Móvel:     5% (25 casos)
```

---

#### **3. Tempo Médio de Resolução por Classificação** (Gráfico de Barras Horizontal)
- **Eixo X**: Tempo médio (dias)
- **Eixo Y**: Classificação
- **Cores**: Gradiente vermelho (urgente) → verde (baixa)

**Exemplo de Dados:**
```
Urgente:    12.5 dias
Alta:       8.3 dias
Média:      5.2 dias
Baixa:      3.1 dias
```

---

#### **4. Distribuição por Setor Responsável** (Gráfico de Barras)
- **Eixo X**: Setor
- **Eixo Y**: Número de casos
- **Cores**: Por setor

**Exemplo de Dados:**
```
Atendimento:        180 casos
Financeiro:         145 casos
TI:                 95 casos
Médico:             80 casos
```

---

#### **5. Evolução Temporal das Ocorrências** (Gráfico de Área)
- **Eixo X**: Meses (Jan - Dez 2024)
- **Eixo Y**: Número de ocorrências
- **Área**: Preenchida com gradiente
- **Linha**: Tendência ao longo do tempo

**Visualização:**
```
Picos em: Março (65 casos), Julho (70 casos), Outubro (68 casos)
Vales em: Fevereiro (35 casos), Setembro (38 casos)
```

---

#### **6. Heatmap Mensal de Ocorrências** (Mapa de Calor)
- **Eixo X**: Meses
- **Eixo Y**: Tipos de Problema
- **Cores**: Azul (baixo) → Vermelho (alto)
- **Valores**: Quantidade em cada célula

**Estrutura:**
```
              Jan  Fev  Mar  Abr  Mai  Jun  Jul  Ago  Set  Out  Nov  Dez
Negativa      12   10   15   13   11   12   14   13   10   15   11   9
Atraso        10   8    12   11   9    10   13   11   8    12   10   11
Cobrança      8    7    9    8    7    9    10   8    7    9    8    8
...
```

---

#### **7. Estatísticas Gerais** (Tabela de Dados)

**Colunas:**
| Métrica | Valor |
|---------|-------|
| Total de Ocorrências | 500 |
| Tempo Médio de Resolução | 6.5 dias |
| Desvio Padrão | 3.2 dias |
| Tempo Mínimo | 1 dia |
| Tempo Máximo | 18 dias |
| Mediana | 6 dias |
| Taxa de Reincidência | 15.2% |
| Casos Urgentes | 85 (17%) |
| Casos Alta Prioridade | 120 (24%) |
| Casos Média Prioridade | 195 (39%) |
| Casos Baixa Prioridade | 100 (20%) |

---

#### **8. Reincidência por Tipo de Problema** (Gráfico de Barras Agrupadas)
- **Eixo X**: Tipo de Problema
- **Eixo Y**: Quantidade
- **Grupos**: Primeira Ocorrência vs Reincidente
- **Cores**: Azul (primeira) vs Laranja (reincidente)

**Exemplo:**
```
Negativa de Cobertura:
  ▓▓▓▓▓▓▓▓▓▓▓▓ Primeira: 123
  ▓▓▓ Reincidente: 22

Atraso no Atendimento:
  ▓▓▓▓▓▓▓▓▓▓ Primeira: 106
  ▓▓ Reincidente: 19
```

---

#### **9. Tempo de Resolução por Canal** (Gráfico de Barras Horizontal)
- **Eixo X**: Tempo médio (dias)
- **Eixo Y**: Canal de Entrada
- **Cores**: Por eficiência (verde → vermelho)

**Exemplo:**
```
App Móvel:      4.2 dias ▓▓▓▓▓▓
Chat Online:    5.8 dias ▓▓▓▓▓▓▓▓
E-mail:         6.9 dias ▓▓▓▓▓▓▓▓▓▓
Telefone:       7.5 dias ▓▓▓▓▓▓▓▓▓▓▓
Presencial:     8.1 dias ▓▓▓▓▓▓▓▓▓▓▓▓
```

---

#### **10. Tabela de Dados Detalhados** (Data Table)

**Colunas Exibidas:**
| Data | Tipo Problema | Tempo (dias) | Canal | Classificação | Setor | Reincidente |
|------|---------------|--------------|-------|---------------|-------|-------------|
| 2024-01-05 | Negativa Cobertura | 8 | E-mail | Alta | Médico | Não |
| 2024-01-07 | Atraso Atendimento | 5 | Telefone | Média | Atendimento | Sim |
| 2024-01-10 | Cobrança Indevida | 12 | Chat | Urgente | Financeiro | Não |
| ... | ... | ... | ... | ... | ... | ... |

**Features:**
- 📄 Paginação (10 registros por página)
- 🔍 Scroll horizontal
- ⬆️⬇️ Ordenação por coluna (click no cabeçalho)
- 🎨 Linhas alternadas (zebra striping)

---

### 📥 Botão de Download

**Localização**: Abaixo da tabela de dados

```
┌─────────────────────────────────┐
│  📥 Download CSV - Dados        │
│      Filtrados                  │
└─────────────────────────────────┘
```

**Funcionalidade**: Exporta os dados atualmente filtrados em formato CSV

---

## 🎨 Design e UX

### Paleta de Cores
- **Primary**: #FF4B4B (vermelho vibrante)
- **Background**: #FFFFFF (branco)
- **Secondary Background**: #F0F2F6 (cinza claro)
- **Text**: #262730 (cinza escuro)

### Tipografia
- **Fonte**: Sans Serif (sistema)
- **Títulos**: Bold, tamanho maior
- **Textos**: Regular, legível

### Layout
- **Responsivo**: Adapta a diferentes tamanhos de tela
- **Sidebar**: Sempre visível (pode ser recolhida)
- **Gráficos**: Width 100% (estica toda a largura)
- **Espaçamento**: Margens consistentes

---

## 🔄 Interatividade

### Filtros Dinâmicos
- Todos os gráficos atualizam **automaticamente** ao alterar filtros
- KPIs recalculam em **tempo real**
- Tabela de dados reflete seleção atual

### Gráficos Plotly
- **Zoom**: Scroll do mouse ou pinça (touch)
- **Pan**: Arrastar com mouse
- **Hover**: Tooltip com detalhes
- **Select**: Click para destacar
- **Reset**: Botão "🏠 Reset axes"
- **Download**: Botão "📷 Download plot as png"

---

## 💡 Casos de Uso

### Para Gestores
1. Identificar tipos de problema mais frequentes
2. Analisar eficiência por canal de entrada
3. Monitorar tempo médio de resolução
4. Avaliar taxa de reincidência
5. Tomar decisões baseadas em dados

### Para Analistas
1. Explorar tendências temporais
2. Correlacionar variáveis
3. Exportar dados para análises externas
4. Identificar gargalos operacionais

### Para Equipes
1. Visualizar volume de trabalho por setor
2. Priorizar casos urgentes
3. Acompanhar métricas de SLA
4. Comunicar resultados com stakeholders

---

## 🚀 Performance

- **Carregamento inicial**: < 2 segundos
- **Atualização de filtros**: < 0.5 segundos
- **Renderização de gráficos**: < 1 segundo
- **Responsividade**: Sem lag perceptível

---

## 📚 Tecnologias Utilizadas

- **Frontend**: Streamlit (framework web Python)
- **Gráficos**: Plotly (biblioteca interativa)
- **Dados**: Pandas (análise e manipulação)
- **Estilização**: CSS customizado via Streamlit config

---

## 🆘 Suporte

**Problemas comuns:**

### Dashboard não abre
```bash
# Verifique se a porta 8501 está livre
netstat -ano | findstr :8501

# Mate processos usando a porta
taskkill /PID <número_do_pid> /F

# Execute novamente
streamlit run src/dashboard_streamlit.py
```

### Erro de dependências
```bash
# Reinstale os pacotes
pip install --upgrade -r requirements.txt
```

### Dados não carregam
```bash
# Verifique se o arquivo existe
ls data/processed/dados_ocorrencias_formatado.csv

# Verifique o encoding
python -c "import pandas as pd; print(pd.read_csv('data/processed/dados_ocorrencias_formatado.csv').shape)"
```

---

## 📞 Contato

**Desenvolvedora**: Rubia Fagundes  
**E-mail**: rubiafagundes_ds@outlook.com  
**LinkedIn**: https://www.linkedin.com/in/rubiafagundes  
**GitHub**: https://github.com/ru-fagundes

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

---

**Data do Documento**: 06 de Dezembro de 2025  
**Versão do Dashboard**: 1.0.0  
**Última Atualização**: 06/12/2025
