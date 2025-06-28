#!/usr/bin/env python3
"""
Teste específico para o problema de reenvio corrigido
"""

import sys
import os
sys.path.append('e:/MENSAGENS')

from shopee_neural_ai_advanced import ShopeeNeuralAI

def test_specific_case():
    """Testa o caso específico que estava dando erro"""
    print("🎯 TESTE DO CASO ESPECÍFICO CORRIGIDO")
    print("=" * 50)
    
    # Criar nova instância
    ai_system = ShopeeNeuralAI()
    
    # Carregar dados frescos
    success = ai_system.load_advanced_training_data('e:/MENSAGENS/shopee_complete_training.json')
    if not success:
        print("❌ Falha ao carregar dados")
        return
    
    print(f"✅ {len(ai_system.training_patterns)} padrões carregados")
    
    # Verificar se padrões de reenvio_produto existem
    reenvio_patterns = [p for p in ai_system.training_patterns 
                       if p.get('category') == 'reenvio_produto']
    print(f"📦 {len(reenvio_patterns)} padrões de reenvio_produto encontrados")
    
    # Sequência exata do problema reportado
    test_sequence = [
        ("olá", "saudacao"),
        ("meu produto veio quebrado", "produto_defeituoso"),
        ("não quero devolver pode mandar novamente?", "reenvio_produto")
    ]
    
    print(f"\n🧪 TESTANDO SEQUÊNCIA EXATA DO PROBLEMA:")
    print("-" * 55)
    
    for i, (input_text, expected_category) in enumerate(test_sequence, 1):
        print(f"\n{i}. 👤 \"{input_text}\"")
        
        # Detectar intenção primária
        processed = ai_system.processor.advanced_preprocess(input_text)
        primary_intent = ai_system.detect_primary_intent(processed)
        print(f"   🎯 Intenção: {primary_intent}")
        
        # Buscar resposta
        response, confidence, category = ai_system.advanced_similarity_search(input_text)
        
        # Verificar se está correto
        status = "✅" if category == expected_category else "❌"
        print(f"   🤖 Categoria: {category} (conf: {confidence:.3f}) {status}")
        
        # Mostrar resposta
        print(f"   💬 Resposta: {response[:70]}...")
        
        if category != expected_category:
            print(f"   ⚠️ ERRO: Esperado '{expected_category}', obteve '{category}'")
        else:
            print(f"   🎉 SUCESSO: Categoria correta!")
    
    # Teste adicional de diferenciação
    print(f"\n🔍 TESTE DE DIFERENCIAÇÃO ADICIONAL:")
    print("-" * 45)
    
    differentiation_tests = [
        ("produto veio defeituoso", "produto_defeituoso"),
        ("quero cancelar o pedido", "cancelamento_pedido"),
        ("pode enviar outro produto", "reenvio_produto"),
        ("preciso alterar endereço", "alteracao_dados"),
        ("sem devolver manda novo", "reenvio_produto"),
        ("não quero mais o produto", "cancelamento_pedido")
    ]
    
    correct_count = 0
    
    for input_text, expected_category in differentiation_tests:
        response, confidence, category = ai_system.advanced_similarity_search(input_text)
        status = "✅" if category == expected_category else "❌"
        
        if category == expected_category:
            correct_count += 1
        
        print(f"{status} \"{input_text}\" → {category} (esperado: {expected_category})")
    
    success_rate = (correct_count / len(differentiation_tests)) * 100
    print(f"\n📊 TAXA DE SUCESSO: {success_rate:.1f}% ({correct_count}/{len(differentiation_tests)})")
    
    if success_rate >= 90:
        print("🎉 EXCELENTE! Diferenciação funcionando perfeitamente!")
    elif success_rate >= 70:
        print("✅ BOM! Pequenos ajustes podem ser necessários")
    else:
        print("⚠️ PRECISA MELHORAR! Revisar configurações")

def test_specific_responses():
    """Testa as respostas específicas"""
    print(f"\n💬 TESTE DAS RESPOSTAS ESPECÍFICAS:")
    print("-" * 40)
    
    ai_system = ShopeeNeuralAI()
    ai_system.load_advanced_training_data('e:/MENSAGENS/shopee_complete_training.json')
    
    test_cases = [
        ("meu produto veio quebrado", "Pedimos desculpas pelo ocorrido"),
        ("não quero devolver pode mandar novamente", "não realizamos 2° entrega"),
        ("quero cancelar o pedido", "não podemos cancelar pedidos")
    ]
    
    for question, expected_phrase in test_cases:
        response, confidence, category = ai_system.advanced_similarity_search(question)
        
        contains_expected = expected_phrase.lower() in response.lower()
        status = "✅" if contains_expected else "❌"
        
        print(f"\n{status} \"{question}\"")
        print(f"   📂 {category} (conf: {confidence:.3f})")
        print(f"   💬 {response[:80]}...")
        
        if not contains_expected:
            print(f"   ⚠️ Esperado conter: '{expected_phrase}'")

if __name__ == "__main__":
    test_specific_case()
    test_specific_responses()