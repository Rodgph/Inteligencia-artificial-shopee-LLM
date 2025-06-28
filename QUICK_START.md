# 🚀 Guia Rápido - Shopee Neural AI

## ⚡ Início Rápido

### 1. Usar o Sistema
```bash
python shopee_ai_launcher.py
```

### 2. Testar Funcionalidades
```bash
# Testar produtos defeituosos
python testes/test_produtos_defeituosos.py

# Testar correção de reenvio
python testes/test_reenvio_fix.py
```

### 3. Adicionar Novos Padrões
```bash
# Adicionar padrões de produtos defeituosos
python scripts/add_produtos_defeituosos.py

# Adicionar padrões de reenvio
python scripts/add_reenvio_patterns.py
```

## 📊 Status do Sistema

- ✅ **291 padrões neurais** carregados
- ✅ **50 clusters semânticos** otimizados
- ✅ **5 categorias principais** configuradas
- ✅ **Sistema 100% funcional**

## 🎯 Categorias Suportadas

| Categoria | Padrões | Descrição |
|-----------|---------|-----------|
| 🚫 produto_defeituoso | 95 | Produtos com defeito |
| ✏️ alteracao_dados | 60 | Mudança de dados/endereço |
| 📦 reenvio_produto | 40 | Segunda entrega |
| 🚫 cancelamento_pedido | 25 | Cancelar pedidos |
| 👋 saudacao | 5 | Saudações |

## 🔧 Manutenção

### Limpar Cache
```bash
rm modelos/shopee_neural_model.pkl
```

### Backup Dados
```bash
cp dados/shopee_complete_training.json dados/backups/backup_$(date +%Y%m%d).json
```

---
*Sistema desenvolvido para excelência em atendimento automatizado* 🤖
