# 🗂️ Backup - Arquivos Não Essenciais

Esta pasta contém arquivos que foram removidos da estrutura principal do projeto para mantê-lo limpo e focado apenas nos componentes essenciais para execução.

## 📦 Conteúdo do Backup

### 📁 docs/
Documentação adicional do projeto:
- **DASHBOARD_DEMO.md** - Demonstração em texto do dashboard
- **DASHBOARD_DEMONSTRACAO.pdf** - Manual completo em PDF com screenshots
- **GUIA_RAPIDO.md** - Guia rápido de uso
- **README.md** - Índice da documentação

### 📁 assets/
Imagens de demonstração (screenshots dos gráficos):
- grafico_01_tipo_problema.png
- grafico_02_canal_entrada.png
- grafico_03_tempo_classificacao.png
- grafico_04_setor.png
- grafico_05_evolucao_temporal.png
- grafico_06_heatmap.png
- grafico_07_reincidencia.png
- grafico_08_tempo_canal.png

### 📁 config/
- **config.toml** - Configuração do Streamlit (duplicado, mantido em .streamlit/)

## ❓ Por que foram removidos?

Estes arquivos foram movidos para backup porque:
- **Não são necessários** para executar o notebook ou dashboard
- **Documentação redundante** - informações já presentes no README principal
- **Screenshots** - são gerados automaticamente pela dashboard ao executar
- **Arquivos duplicados** - config.toml existe em .streamlit/

## 🔄 Como recuperar?

Se precisar de algum arquivo, basta copiar de volta para a pasta original:

```bash
# Exemplo: recuperar documentação
cp _backup_arquivos/docs/* docs/
```

## ⚠️ Importante

- Esta pasta pode ser **excluída permanentemente** se não precisar dos arquivos
- Os arquivos aqui **não afetam** a execução do projeto
- O projeto está **100% funcional** sem estes arquivos

---

**Data do backup**: 16 de dezembro de 2025
**Motivo**: Organização e limpeza do projeto para GitHub
