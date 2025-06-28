#!/usr/bin/env python3
"""
Teste específico para produtos defeituosos
Verifica se o sistema neural reconhece corretamente
"""

import sys
import os
sys.path.append('e:/MENSAGENS')

from shopee_neural_ai_advanced import ShopeeNeuralAI

def test_produtos_defeituosos():
    """Testa a detecção de produtos defeituosos"""
    print("🚫 TESTE DE DETECÇÃO DE PRODUTOS DEFEITUOSOS")
    print("=" * 60)
    
    # Criar nova instância
    ai_system = ShopeeNeuralAI()
    
    # Carregar dados frescos
    success = ai_system.load_advanced_training_data('e:/MENSAGENS/shopee_complete_training.json')
    if not success:
        print("❌ Falha ao carregar dados")
        return
    
    print(f"✅ {len(ai_system.training_patterns)} padrões carregados")
    
    # Verificar se padrões de produto_defeituoso existem
    defeituoso_patterns = [p for p in ai_system.training_patterns 
                          if p.get('category') == 'produto_defeituoso']
    print(f"🚫 {len(defeituoso_patterns)} padrões de produto_defeituoso encontrados")
    
    if defeituoso_patterns:
        print("📝 Exemplos de padrões de produto defeituoso:")
        for i, pattern in enumerate(defeituoso_patterns[:5], 1):
            print(f"  {i}. \"{pattern['question']}\"")
    
    # Testar frases de produtos defeituosos
    test_phrases = [
        "meu produto veio com defeito",
        "celular chegou quebrado", 
        "produto não funciona",
        "veio com defeito de fábrica",
        "produto muito ruim",
        "faltando peças do produto",
        "produto diferente da foto",
        "tela do celular está rachada",
        "notebook não liga",
        "produto chegou danificado",
        # Frases de controle (não defeituosas)
        "quero cancelar o pedido",
        "preciso alterar meus dados"
    ]
    
    print(f"\n🔍 TESTANDO FRASES DE PRODUTOS DEFEITUOSOS:")
    print("-" * 60)
    
    successes = 0
    total_defeituoso_tests = 0
    
    for phrase in test_phrases:
        print(f"\n👤 \"{phrase}\"")
        
        # Detectar intenção primária
        processed = ai_system.processor.advanced_preprocess(phrase)
        primary_intent = ai_system.detect_primary_intent(processed)
        print(f"🎯 Intenção detectada: {primary_intent}")
        
        # Buscar melhor resposta
        response, confidence, category = ai_system.advanced_similarity_search(phrase)
        
        # Verificar se é teste de produto defeituoso
        is_defeituoso_test = any(word in phrase.lower() for word in [
            'defeito', 'quebrado', 'não funciona', 'ruim', 'faltando', 
            'diferente', 'rachada', 'não liga', 'danificado'
        ])
        
        if is_defeituoso_test:
            total_defeituoso_tests += 1
            expected_category = "produto_defeituoso"
            status = "✅" if category == expected_category else "❌"
            if category == expected_category:
                successes += 1
        else:
            # Testes de controle
            expected_category = "cancelamento_pedido" if "cancelar" in phrase else "alteracao_dados"
            status = "✅" if category == expected_category else "❌"
        
        print(f"🤖 Categoria: {category} | Confiança: {confidence:.3f} {status}")
        print(f"💬 Resposta: {response[:80]}...")
        
        if is_defeituoso_test and category != "produto_defeituoso":
            print(f"⚠️ ERRO: Esperado 'produto_defeituoso', obteve '{category}'")
    
    # Estatísticas
    if total_defeituoso_tests > 0:
        success_rate = (successes / total_defeituoso_tests) * 100
        print(f"\n📊 RESULTADOS DOS TESTES:")
        print(f"✅ Sucessos: {successes}/{total_defeituoso_tests}")
        print(f"📈 Taxa de sucesso: {success_rate:.1f}%")
        
        if success_rate >= 90:
            print("🎉 EXCELENTE! Sistema funcionando perfeitamente!")
        elif success_rate >= 70:
            print("✅ BOM! Apenas pequenos ajustes necessários")
        else:
            print("⚠️ PRECISA MELHORAR! Revisar configurações")
    
    # Testar resposta específica
    print(f"\n💬 TESTE DA RESPOSTA ESPECÍFICA:")
    print("-" * 40)
    
    test_response, test_confidence, test_category = ai_system.advanced_similarity_search("meu produto veio com defeito")
    expected_response_part = "Pedimos desculpas pelo ocorrido"
    
    if expected_response_part in test_response:
        print("✅ Resposta correta contém a mensagem esperada")
        print(f"📝 Resposta: {test_response}")
    else:
        print("❌ Resposta não contém a mensagem esperada")
        print(f"📝 Obtida: {test_response}")
        print(f"📋 Esperada: Deve conter '{expected_response_part}'")

def test_response_quality():
    """Testa a qualidade das respostas"""
    print(f"\n🎯 TESTE DE QUALIDADE DAS RESPOSTAS:")
    print("-" * 45)
    
    # Criar sistema
    ai_system = ShopeeNeuralAI()
    ai_system.load_advanced_training_data('e:/MENSAGENS/shopee_complete_training.json')
    
    test_cases = [
        ("meu produto veio com defeito", "produto_defeituoso"),
        ("celular chegou quebrado", "produto_defeituoso"),
        ("produto não funciona", "produto_defeituoso"),
        ("quero cancelar pedido", "cancelamento_pedido"),
        ("alterar endereço", "alteracao_dados")
    ]
    
    for question, expected_category in test_cases:
        response, confidence, category = ai_system.advanced_similarity_search(question)
        
        status = "✅" if category == expected_category else "❌"
        print(f"\n{status} \"{question}\"")
        print(f"   📂 {category} (conf: {confidence:.3f})")
        print(f"   💬 {response[:60]}...")

if __name__ == "__main__":
    test_produtos_defeituosos()
    test_response_quality()