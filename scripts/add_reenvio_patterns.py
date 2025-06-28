#!/usr/bin/env python3
"""
Script para adicionar padrões de reenvio/segunda entrega
Corrige a situação onde cliente pede novo produto sem devolução
"""

import json
import os

def add_reenvio_patterns():
    """Adiciona padrões específicos para reenvio de produtos"""
    
    print("📦 ADICIONANDO PADRÕES DE REENVIO/SEGUNDA ENTREGA")
    print("=" * 60)
    
    # Carregar dados atuais
    current_file = 'e:/MENSAGENS/shopee_complete_training.json'
    reenvio_file = 'e:/MENSAGENS/shopee_reenvio_produtos.json'
    
    try:
        # Carregar dados existentes
        with open(current_file, 'r', encoding='utf-8') as f:
            current_data = json.load(f)
        print(f"✅ {len(current_data)} padrões atuais carregados")
        
        # Carregar novos padrões de reenvio
        with open(reenvio_file, 'r', encoding='utf-8') as f:
            reenvio_patterns = json.load(f)
        print(f"✅ {len(reenvio_patterns)} padrões de reenvio carregados")
        
        # Verificar se já existem padrões de reenvio_produto
        existing_reenvio = sum(1 for item in current_data 
                             if item.get('category') == 'reenvio_produto')
        
        if existing_reenvio > 0:
            print(f"⚠️ Já existem {existing_reenvio} padrões de reenvio_produto")
            response = input("Deseja substituir? (s/n): ").lower()
            if response != 's':
                print("❌ Operação cancelada")
                return False
            
            # Remover padrões antigos de reenvio
            current_data = [item for item in current_data 
                          if item.get('category') != 'reenvio_produto']
            print(f"🔄 Padrões antigos de reenvio_produto removidos")
        
        # Combinar dados
        combined_data = current_data + reenvio_patterns
        
        # Estatísticas
        total_patterns = len(combined_data)
        new_count = len(reenvio_patterns)
        
        print(f"\n📊 ESTATÍSTICAS DA ADIÇÃO:")
        print(f"Padrões anteriores: {len(current_data)}")
        print(f"Novos padrões de reenvio: {new_count}")
        print(f"Total final: {total_patterns}")
        
        # Contar por categoria
        categories = {}
        for item in combined_data:
            category = item.get('category', 'sem_categoria')
            categories[category] = categories.get(category, 0) + 1
        
        print(f"\n🏷️ TOP 10 CATEGORIAS:")
        sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
        for i, (category, count) in enumerate(sorted_categories[:10], 1):
            emoji = "🆕" if category == "reenvio_produto" else "📁"
            print(f"  {i:2d}. {emoji} {category}: {count} padrões")
        
        # Backup
        backup_file = current_file.replace('.json', '_backup_reenvio.json')
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

def show_reenvio_examples():
    """Mostra exemplos dos novos padrões de reenvio"""
    print(f"\n🆕 EXEMPLOS DOS PADRÕES DE REENVIO/SEGUNDA ENTREGA:")
    print("-" * 65)
    
    try:
        with open('e:/MENSAGENS/shopee_reenvio_produtos.json', 'r', encoding='utf-8') as f:
            patterns = json.load(f)
        
        # Categorizar por tipo de reenvio
        tipos_reenvio = {
            'sem_devolucao': [],
            'substituicao': [],
            'segunda_via': [],
            'reposicao': []
        }
        
        for pattern in patterns:
            question = pattern['question'].lower()
            if any(word in question for word in ['sem devolver', 'não devolver', 'não quero devolver']):
                tipos_reenvio['sem_devolucao'].append(pattern)
            elif any(word in question for word in ['substituir', 'trocar', 'substituto']):
                tipos_reenvio['substituicao'].append(pattern)
            elif any(word in question for word in ['segunda via', 'segunda entrega', 'segunda tentativa']):
                tipos_reenvio['segunda_via'].append(pattern)
            elif any(word in question for word in ['reposição', 'reenvio', 'nova unidade']):
                tipos_reenvio['reposicao'].append(pattern)
        
        print("🚫 PEDIDOS SEM DEVOLUÇÃO:")
        for pattern in tipos_reenvio['sem_devolucao'][:3]:
            print(f"  • \"{pattern['question']}\"")
        
        print(f"\n🔄 PEDIDOS DE SUBSTITUIÇÃO:")
        for pattern in tipos_reenvio['substituicao'][:3]:
            print(f"  • \"{pattern['question']}\"")
        
        print(f"\n📦 SEGUNDA VIA/ENTREGA:")
        for pattern in tipos_reenvio['segunda_via'][:3]:
            print(f"  • \"{pattern['question']}\"")
        
        print(f"\n🔁 REPOSIÇÃO/REENVIO:")
        for pattern in tipos_reenvio['reposicao'][:3]:
            print(f"  • \"{pattern['question']}\"")
        
        print(f"\n💬 RESPOSTA PADRÃO PARA REENVIO:")
        sample = patterns[0]
        print(f"👤 Cliente: \"{sample['question']}\"")
        print(f"🤖 Resposta: \"{sample['response']}\"")
        print(f"🏷️ Categoria: {sample['category']}")
        print(f"⭐ Confiança: {sample['confidence']}")
        
    except Exception as e:
        print(f"❌ Erro ao mostrar exemplos: {e}")

def show_problem_solution():
    """Mostra o problema e a solução implementada"""
    print(f"\n🎯 PROBLEMA IDENTIFICADO E SOLUÇÃO:")
    print("-" * 50)
    
    print("❌ PROBLEMA ANTERIOR:")
    print('  👤 Cliente: "não quero devolver pode mandar novamente?"')
    print('  🤖 IA (ERRADO): "...não temos acesso para cancelamentos..."')
    print('  📂 Categoria: cancelamento_pedido (INCORRETA)')
    
    print(f"\n✅ SOLUÇÃO IMPLEMENTADA:")
    print('  👤 Cliente: "não quero devolver pode mandar novamente?"')
    print('  🤖 IA (CORRETO): "Infelizmente não realizamos 2° entrega..."')
    print('  📂 Categoria: reenvio_produto (CORRETA)')
    
    print(f"\n🎯 DIFERENCIAÇÃO CLARA:")
    print("🚫 CANCELAMENTO: Querer cancelar/parar o pedido")
    print("📦 REENVIO: Querer novo produto sem devolver o defeituoso")
    print("💱 DEVOLUÇÃO: Querer devolver produto defeituoso")
    
    print(f"\n🔧 MELHORIAS IMPLEMENTADAS:")
    print("✅ 40+ padrões específicos para reenvio")
    print("✅ Detecção precisa da intenção")
    print("✅ Resposta clara sobre política de não reenvio")
    print("✅ Diferenciação neural avançada")

def main():
    """Função principal"""
    
    # Mostrar problema e solução
    show_problem_solution()
    
    # Mostrar exemplos
    show_reenvio_examples()
    
    # Adicionar padrões
    success, new_count, total_count = add_reenvio_patterns()
    
    if success:
        print(f"\n🎉 ADIÇÃO DE PADRÕES DE REENVIO CONCLUÍDA!")
        print(f"✅ {new_count} novos padrões de reenvio adicionados")
        print(f"📊 Total de padrões disponíveis: {total_count}")
        
        print(f"\n🚀 PRÓXIMOS PASSOS:")
        print("1. Remova o cache: rm e:/MENSAGENS/shopee_neural_model.pkl")
        print("2. Execute: python shopee_neural_ai_advanced.py")
        print("3. Teste o caso específico que estava dando erro")
        
        print(f"\n🧪 TESTE A SITUAÇÃO CORRIGIDA:")
        print('   1. "meu produto veio quebrado" → produto_defeituoso')
        print('   2. "não quero devolver pode mandar novamente?" → reenvio_produto')
        print('   3. "quero cancelar o pedido" → cancelamento_pedido')
        
        print(f"\n🎯 EXPECTATIVA:")
        print("• Cada situação terá categoria específica")
        print("• Resposta adequada para cada caso")
        print("• Fim da confusão entre cancelamento e reenvio")
        
    else:
        print("\n❌ Falha na adição. Verifique os erros acima.")

if __name__ == "__main__":
    main()