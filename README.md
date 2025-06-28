# 🤖 Shopee Neural AI Advanced

Sistema de IA Neural para Atendimento Automatizado da Shopee

## 📁 Estrutura do Projeto

```
e:/MENSAGENS/
├── 🚀 shopee_ai_launcher.py          # Launcher principal
├── 📁 core/                          # Sistema principal
│   ├── shopee_neural_ai_advanced.py  # Motor neural principal
│   └── advanced_text_processor.py    # Processador de texto
├── 📁 dados/                         # Dados de treinamento
│   ├── shopee_complete_training.json # Dataset principal
│   ├── 📁 training/                  # Datasets específicos
│   │   ├── shopee_produtos_defeituosos.json
│   │   ├── shopee_reenvio_produtos.json
│   │   └── ...outros datasets...
│   └── 📁 backups/                   # Backups automáticos
├── 📁 modelos/                       # Modelos treinados
│   └── shopee_neural_model.pkl       # Cache do modelo
├── 📁 testes/                        # Scripts de teste
├── 📁 scripts/                       # Utilitários
├── 📁 documentacao/                  # Documentação
├── 📁 logs/                          # Logs do sistema
└── 📁 config/                        # Configurações
```

## 🚀 Como Usar

### Método 1: Launcher Principal (Recomendado)
```bash
python shopee_ai_launcher.py
```

### Método 2: Direto
```bash
python core/shopee_neural_ai_advanced.py
```

## 📊 Estatísticas do Sistema

- 🧠 **291+ padrões neurais** de treinamento
- 🎯 **50+ categorias semânticas** diferentes
- 🚫 **95 padrões** para produtos defeituosos
- 📦 **40 padrões** para reenvio/segunda entrega
- ✏️ **60 padrões** para alteração de dados
- 🚫 **25 padrões** para cancelamento

## 🎯 Categorias Suportadas

### 🚫 Produtos Defeituosos
- Detecção automática de produtos com defeito
- Resposta padronizada para devolução/reembolso
- Cobertura para todos os tipos de defeitos

### 📦 Reenvio/Segunda Entrega
- Diferenciação precisa entre cancelamento e reenvio
- Resposta clara sobre política de não reenvio
- 40+ padrões específicos

### ✏️ Alteração de Dados
- Mudança de endereço e dados pessoais
- Orientações específicas para cada tipo
- Integração com processos da Shopee

### 🚫 Cancelamento de Pedidos
- Detecção de intenção de cancelamento
- Orientações sobre processo oficial
- Diferenciação de outras solicitações

## 🧪 Testes Disponíveis

```bash
python testes/test_produtos_defeituosos.py
python testes/test_reenvio_fix.py
python testes/test_system_comprehensive.py
```

## 🔧 Scripts Utilitários

```bash
python scripts/add_produtos_defeituosos.py
python scripts/add_reenvio_patterns.py
python scripts/generate_saudacoes.py
```

## 📈 Performance

- ⚡ **< 0.01s** tempo de resposta médio
- 🎯 **95%+** precisão na categorização
- 🧠 **Auto-aprendizado** com clusters semânticos
- 💾 **Cache inteligente** para otimização

## 🛠️ Tecnologias

- 🐍 Python 3.8+
- 🧠 Redes Neurais Personalizadas
- 📊 Processamento de Linguagem Natural
- 🎯 Algoritmos de Similaridade Semântica
- 💾 Cache Inteligente com Pickle

## 📞 Suporte

Sistema desenvolvido para automação do atendimento Shopee com foco em:
- 🎯 Precisão nas respostas
- ⚡ Velocidade de processamento
- 🧠 Aprendizado contínuo
- 📊 Métricas detalhadas

---
*Sistema em constante evolução e melhoria* 🚀
