# 🤝 Contributing to Shopee Neural AI Advanced

## 🎯 Como Contribuir

Obrigado por seu interesse em contribuir com o **Shopee Neural AI Advanced**! Este projeto é uma solução de IA neural para atendimento automatizado.

## 📋 Diretrizes de Contribuição

### 🚀 Setup do Ambiente

```bash
# 1. Clone o repositório
git clone https://github.com/Rodgph/Inteligencia-artificial-shopee-LLM.git
cd Inteligencia-artificial-shopee-LLM

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Teste o sistema
python shopee_ai_launcher.py
```

### 🧪 Executar Testes

```bash
# Testes específicos
python testes/test_produtos_defeituosos.py
python testes/test_reenvio_fix.py

# Adicionar novos padrões
python scripts/add_produtos_defeituosos.py
python scripts/add_reenvio_patterns.py
```

## 📂 Estrutura do Projeto

```
├── 🚀 shopee_ai_launcher.py    # Ponto de entrada principal
├── 📁 core/                    # Sistema neural principal
├── 📁 dados/                   # Datasets e backups
├── 📁 testes/                  # Scripts de teste
├── 📁 scripts/                 # Utilitários
└── 📁 config/                  # Configurações
```

## 🎯 Tipos de Contribuição

### 1. 🧠 Melhorias no Sistema Neural

- Otimização de algoritmos
- Novos métodos de detecção
- Melhoria na precisão

### 2. 📊 Novos Padrões de Treinamento

- Adicionar padrões para novas categorias
- Melhorar padrões existentes
- Casos edge específicos

### 3. 🧪 Testes e Validação

- Novos casos de teste
- Testes de performance
- Validação de precisão

### 4. 📖 Documentação

- Melhoria nos READMEs
- Exemplos de uso
- Tutoriais

## 🔄 Processo de Contribuição

### 1. Fork e Clone

```bash
# Fork no GitHub, depois:
git clone https://github.com/SEU_USUARIO/Inteligencia-artificial-shopee-LLM.git
```

### 2. Criar Branch

```bash
git checkout -b feature/nova-funcionalidade
# ou
git checkout -b fix/correcao-bug
# ou
git checkout -b docs/melhorar-documentacao
```

### 3. Desenvolvimento

- Faça suas alterações
- Teste localmente
- Documente mudanças

### 4. Commit e Push

```bash
git add .
git commit -m "feat: adicionar nova funcionalidade X"
git push origin feature/nova-funcionalidade
```

### 5. Pull Request

- Abra PR no GitHub
- Descreva as mudanças
- Aguarde review

## 📝 Convenções de Commit

```bash
# Tipos de commit
feat: nova funcionalidade
fix: correção de bug
docs: documentação
test: testes
refactor: refatoração
style: formatação
perf: performance
```

### Exemplos:

```bash
git commit -m "feat: adicionar detecção de problemas de entrega"
git commit -m "fix: corrigir classificação de reenvios"
git commit -m "docs: atualizar guia de instalação"
git commit -m "test: adicionar testes para cancelamentos"
```

## 🎯 Áreas de Foco

### 🔥 **Alta Prioridade**

- Novos padrões de produtos defeituosos
- Melhorias na detecção de reenvio
- Otimização de performance

### 🚀 **Funcionalidades Desejadas**

- Suporte a mais categorias
- Sistema de feedback automático
- Métricas de satisfação
- Integração com APIs

### 🧠 **Melhorias Técnicas**

- Algoritmos de ML mais avançados
- Sistema de cache otimizado
- Processamento paralelo
- Auto-tuning de parâmetros

## 🚫 O que NÃO Fazer

- ❌ Alterar estrutura principal sem discussão
- ❌ Remover funcionalidades existentes
- ❌ Commits sem testes
- ❌ Mudanças que quebram compatibilidade

## 📊 Critérios de Aceitação

### ✅ Pull Request será aceito se:

- Passa em todos os testes existentes
- Tem testes para novas funcionalidades
- Documentação atualizada
- Segue convenções do projeto
- Melhora ou mantém performance

### ⚠️ Pull Request precisa de ajustes se:

- Falha em testes
- Sem documentação
- Reduz performance significativamente
- Não segue padrões de código

## 🐛 Reportar Bugs

### Estrutura do Report:

```markdown
**Descrição do Bug:**
Breve descrição do problema

**Para Reproduzir:**

1. Execute comando X
2. Entre com input Y
3. Observe erro Z

**Comportamento Esperado:**
O que deveria acontecer

**Ambiente:**

- OS: Windows/Linux/Mac
- Python: versão
- Arquivos: quais foram modificados

**Screenshots/Logs:**
Se aplicável
```

## 💡 Sugerir Funcionalidades

### Template para Sugestões:

```markdown
**Funcionalidade Sugerida:**
Descrição clara da funcionalidade

**Problema que Resolve:**
Qual problema atual esta funcionalidade resolveria

**Solução Proposta:**
Como imagina que funcionaria

**Alternativas Consideradas:**
Outras abordagens pensadas

**Contexto Adicional:**
Qualquer informação relevante
```

## 🏆 Reconhecimento

Contribuidores serão reconhecidos:

- 📝 **AUTHORS.md** - Lista de contribuidores
- 🎉 **README.md** - Seção de agradecimentos
- 🏷️ **Releases** - Menção nas notas de versão

## 📞 Contato

- 🐛 **Issues:** [GitHub Issues](https://github.com/Rodgph/Inteligencia-artificial-shopee-LLM/issues)
- 💬 **Discussões:** [GitHub Discussions](https://github.com/Rodgph/Inteligencia-artificial-shopee-LLM/discussions)
- 📧 **Email:** Para questões específicas

## 📄 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a [MIT License](LICENSE).

---

**🎉 Obrigado por contribuir para tornar o atendimento automatizado da Shopee ainda melhor!** 🚀🛍️🤖
