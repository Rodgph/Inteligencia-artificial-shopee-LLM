#!/usr/bin/env python3
"""
Script para adicionar padrões de produtos defeituosos
Máxima cobertura para situações de defeitos e problemas
"""

import json
import os

def add_produtos_defeituosos_patterns():
    """Adiciona padrões específicos para produtos defeituosos"""
    
    print("🚫 ADICIONANDO PADRÕES DE PRODUTOS DEFEITUOSOS")
    print("=" * 65)
    
    # Carregar dados atuais
    current_file = 'e:/MENSAGENS/shopee_complete_training.json'
    defeituosos_file = 'e:/MENSAGENS/shopee_produtos_defeituosos.json'
    
    try:
        # Carregar dados existentes
        with open(current_file, 'r', encoding='utf-8') as f:
            current_data = json.load(f)
        print(f"✅ {len(current_data)} padrões atuais carregados")
        
        # Carregar novos padrões de produtos defeituosos
        with open(defeituosos_file, 'r', encoding='utf-8') as f:
            defeituosos_patterns = json.load(f)
        print(f"✅ {len(defeituosos_patterns)} padrões de produtos defeituosos carregados")
        
        # Verificar se já existem padrões de produto_defeituoso
        existing_defeituosos = sum(1 for item in current_data 
                                 if item.get('category') == 'produto_defeituoso')
        
        if existing_defeituosos > 0:
            print(f"⚠️ Já existem {existing_defeituosos} padrões de produto_defeituoso")
            response = input("Deseja substituir? (s/n): ").lower()
            if response != 's':
                print("❌ Operação cancelada")
                return False
            
            # Remover padrões antigos de produto defeituoso
            current_data = [item for item in current_data 
                          if item.get('category') != 'produto_defeituoso']
            print(f"🔄 Padrões antigos de produto_defeituoso removidos")
        
        # Combinar dados
        combined_data = current_data + defeituosos_patterns
        
        # Estatísticas
        total_patterns = len(combined_data)
        new_count = len(defeituosos_patterns)
        
        print(f"\n📊 ESTATÍSTICAS DA ADIÇÃO:")
        print(f"Padrões anteriores: {len(current_data)}")
        print(f"Novos padrões de produtos defeituosos: {new_count}")
        print(f"Total final: {total_patterns}")
        
        # Contar por categoria
        categories = {}
        for item in combined_data:
            category = item.get('category', 'sem_categoria')
            categories[category] = categories.get(category, 0) + 1
        
        print(f"\n🏷️ TOP 10 CATEGORIAS:")
        sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
        for i, (category, count) in enumerate(sorted_categories[:10], 1):
            emoji = "🆕" if category == "produto_defeituoso" else "📁"
            print(f"  {i:2d}. {emoji} {category}: {count} padrões")
        
        # Backup
        backup_file = current_file.replace('.json', '_backup_defeituosos.json')
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(current_data, f, indent=2, ensure_ascii=False)
        print(f"📋 Backup criado: {os.path.basename(backup_file)}")
        
        # Salvar dados combinados
        with open(current_file, 'w', encoding='utf-8') as f:
            json.dump(combined_data, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Dados atualizados salvos: {total_patterns} padrões totais")
        
        return True, new_count, total_patterns
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False, 0, 0

def show_defeituosos_examples():
    """Mostra exemplos dos novos padrões de produtos defeituosos"""
    print(f"\n🆕 EXEMPLOS DOS PADRÕES DE PRODUTOS DEFEITUOSOS:")
    print("-" * 65)
    
    try:
        with open('e:/MENSAGENS/shopee_produtos_defeituosos.json', 'r', encoding='utf-8') as f:
            patterns = json.load(f)
        
        # Categorizar por tipo de defeito
        tipos_defeito = {
            'funcionamento': [],
            'fisico': [],
            'qualidade': [],
            'faltando': [],
            'diferente': []
        }
        
        for pattern in patterns:
            question = pattern['question'].lower()
            if any(word in question for word in ['não funciona', 'não liga', 'não carrega', 'morto', 'travando']):
                tipos_defeito['funcionamento'].append(pattern)
            elif any(word in question for word in ['quebrado', 'rachada', 'trincado', 'arranhão', 'riscado']):
                tipos_defeito['fisico'].append(pattern)
            elif any(word in question for word in ['má qualidade', 'ruim', 'péssimo', 'lixo', 'horrível']):
                tipos_defeito['qualidade'].append(pattern)
            elif any(word in question for word in ['sem peças', 'faltando', 'incompleto', 'vazio']):
                tipos_defeito['faltando'].append(pattern)
            elif any(word in question for word in ['diferente', 'errado', 'não é', 'falso', 'pirata']):
                tipos_defeito['diferente'].append(pattern)
        
        print("⚙️ PROBLEMAS DE FUNCIONAMENTO:")
        for pattern in tipos_defeito['funcionamento'][:4]:
            print(f"  • \"{pattern['question']}\"")
        
        print(f"\n💥 DANOS FÍSICOS:")
        for pattern in tipos_defeito['fisico'][:4]:
            print(f"  • \"{pattern['question']}\"")
        
        print(f"\n👎 PROBLEMAS DE QUALIDADE:")
        for pattern in tipos_defeito['qualidade'][:4]:
            print(f"  • \"{pattern['question']}\"")
        
        print(f"\n📦 PRODUTOS INCOMPLETOS:")
        for pattern in tipos_defeito['faltando'][:3]:
            print(f"  • \"{pattern['question']}\"")
        
        print(f"\n🔄 PRODUTOS DIFERENTES/ERRADOS:")
        for pattern in tipos_defeito['diferente'][:3]:
            print(f"  • \"{pattern['question']}\"")
        
        print(f"\n💬 RESPOSTA PADRÃO PARA PRODUTOS DEFEITUOSOS:")
        sample = patterns[0]
        print(f"👤 Cliente: \"{sample['question']}\"")
        print(f"🤖 Resposta: \"{sample['response']}\"")
        print(f"🏷️ Categoria: {sample['category']}")
        print(f"⭐ Confiança: {sample['confidence']}")
        
    except Exception as e:
        print(f"❌ Erro ao mostrar exemplos: {e}")

def show_coverage_analysis():
    """Mostra análise de cobertura dos padrões"""
    print(f"\n📈 ANÁLISE DE COBERTURA DOS PADRÕES:")
    print("-" * 50)
    
    categorias_cobertas = [
        "📱 Eletrônicos (celular, notebook, tv, etc.)",
        "🏠 Eletrodomésticos (geladeira, microondas, etc.)",
        "👕 Roupas e acessórios",
        "🧸 Brinquedos e jogos",
        "💡 Equipamentos diversos",
        "🔧 Ferramentas e utilidades"
    ]
    
    print("🎯 CATEGORIAS DE PRODUTOS COBERTAS:")
    for categoria in categorias_cobertas:
        print(f"  ✅ {categoria}")
    
    tipos_defeito = [
        "⚙️ Funcionamento (não liga, não funciona, travando)",
        "💥 Danos físicos (quebrado, rachado, arranhado)",
        "👎 Qualidade (ruim, péssimo, má qualidade)",
        "📦 Incompleto (sem peças, faltando acessórios)",
        "🔄 Produto errado (diferente, falso, usado)",
        "🌡️ Problemas específicos (esquenta, barulho, odor)"
    ]
    
    print(f"\n🚫 TIPOS DE DEFEITOS COBERTOS:")
    for tipo in tipos_defeito:
        print(f"  ✅ {tipo}")
    
    print(f"\n🎯 COBERTURA TOTAL:")
    print(f"  📊 80+ padrões diferentes")
    print(f"  🔄 Múltiplas formas de expressar o mesmo problema")
    print(f"  ⚡ Resposta única e direcionada")
    print(f"  🤖 Integração com sistema neural")

def main():
    """Função principal"""
    
    # Mostrar exemplos e análise primeiro
    show_defeituosos_examples()
    show_coverage_analysis()
    
    # Adicionar padrões
    success, new_count, total_count = add_produtos_defeituosos_patterns()
    
    if success:
        print(f"\n🎉 ADIÇÃO DE PRODUTOS DEFEITUOSOS CONCLUÍDA!")
        print(f"✅ {new_count} novos padrões de produtos defeituosos adicionados")
        print(f"📊 Total de padrões disponíveis: {total_count}")
        
        print(f"\n🚀 PRÓXIMOS PASSOS:")
        print("1. Remova o cache: rm e:/MENSAGENS/shopee_neural_model.pkl")
        print("2. Execute: python shopee_neural_ai_advanced.py")
        print("3. Teste os novos padrões de produtos defeituosos")
        
        print(f"\n🧪 FRASES PARA TESTAR:")
        test_phrases = [
            "meu produto veio com defeito",
            "celular chegou quebrado",
            "produto não funciona",
            "veio com defeito de fábrica",
            "produto muito ruim",
            "faltando peças do produto",
            "produto diferente da foto"
        ]
        
        for i, phrase in enumerate(test_phrases, 1):
            print(f"   {i}. \"{phrase}\"")
        
        print(f"\n🎯 EXPECTATIVA:")
        print("• Todos devem ser categorizados como 'produto_defeituoso'")
        print("• Resposta padrão sobre devolução e reembolso")
        print("• Sugestão de mudança de ideia para reembolso rápido")
        
    else:
        print("\n❌ Falha na adição. Verifique os erros acima.")

if __name__ == "__main__":
    main()