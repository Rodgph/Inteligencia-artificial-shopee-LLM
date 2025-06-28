#!/usr/bin/env python3
"""
Shopee Neural AI Advanced - Launcher Principal
Sistema de IA Neural para atendimento Shopee
"""

import sys
import os
from pathlib import Path

# Adicionar pasta core ao path
project_root = Path(__file__).parent
core_path = project_root / "core"
sys.path.insert(0, str(core_path))

def main():
    """Função principal do launcher"""
    print("🤖 SHOPEE NEURAL AI ADVANCED")
    print("=" * 40)
    print("🚀 Iniciando sistema neural...")
    
    try:
        from shopee_neural_ai_advanced import ShopeeNeuralAI
        
        # Criar instância do sistema
        ai_system = ShopeeNeuralAI()
        
        # Carregar dados de treinamento
        training_file = project_root / "dados" / "shopee_complete_training.json"
        
        if not training_file.exists():
            print(f"❌ Arquivo de treinamento não encontrado: {training_file}")
            return False
        
        print(f"📊 Carregando dados de: {training_file}")
        success = ai_system.load_advanced_training_data(str(training_file))
        
        if not success:
            print("❌ Falha ao carregar dados de treinamento")
            return False
        
        print("✅ Sistema carregado com sucesso!")
        print("💬 Digite 'sair' para encerrar")
        print("-" * 40)
        
        # Loop principal de interação
        while True:
            try:
                user_input = input("🔮 Você: ").strip()
                
                if user_input.lower() in ['sair', 'exit', 'quit']:
                    print("👋 Encerrando sistema...")
                    break
                
                if not user_input:
                    continue
                
                # Processar entrada
                response, confidence, category = ai_system.advanced_similarity_search(user_input)
                
                print(f"🤖 Shopee Neural AI: {response} ⚡")
                print(f"    🔬 [Confiança: {confidence:.3f} | Categoria: {category}]")
                
            except KeyboardInterrupt:
                print("\n👋 Encerrando sistema...")
                break
            except Exception as e:
                print(f"❌ Erro: {e}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Erro ao importar módulos: {e}")
        print("💡 Verifique se todos os arquivos estão na pasta 'core/'")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

if __name__ == "__main__":
    main()
