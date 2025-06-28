#!/usr/bin/env python3
"""
SHOPEE NEURAL AI ADVANCED - Sistema de IA Neural Completo
Versão única com máxima eficácia e recursos avançados
Implementa técnicas de Deep Learning, NLP avançado e IA conversacional
"""

import numpy as np
import json
import pickle
import re
import math
import random
import logging
import hashlib
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional, Any
from collections import defaultdict, deque
import threading
import time
import os

class AdvancedNeuralProcessor:
    """
    Processador Neural Avançado para NLP
    Implementa embeddings sophisticados e análise semântica profunda
    """
    
    def __init__(self, embedding_dim: int = 150, context_window: int = 10):
        self.embedding_dim = embedding_dim
        self.context_window = context_window
        self.word_vectors = {}
        self.phrase_vectors = {}
        self.semantic_clusters = defaultdict(list)
        self.context_memory = deque(maxlen=context_window)
        
        # Inicializar camadas neurais
        self.attention_weights = np.random.randn(embedding_dim, embedding_dim) * 0.01
        self.context_weights = np.random.randn(embedding_dim, embedding_dim) * 0.01
        self.semantic_weights = np.random.randn(embedding_dim, embedding_dim) * 0.01
        
        # Configurar logging avançado
        self.setup_logging()
        
    def setup_logging(self):
        """Configura sistema de logging avançado"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f'e:/MENSAGENS/shopee_neural_{datetime.now().strftime("%Y%m%d")}.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger('ShopeeNeuralAI')
    
    def advanced_preprocess(self, text: str) -> Dict[str, Any]:
        """
        Preprocessamento avançado com análise morfológica e sintática
        """
        # Normalização avançada
        text = text.lower().strip()
        
        # Remoção de caracteres especiais mas preserva estrutura
        text = re.sub(r'[^\w\s\-\.]', ' ', text)
        
        # Tokenização inteligente
        tokens = re.findall(r'\b\w+\b', text)
        
        # Análise de n-gramas
        unigrams = tokens
        bigrams = [f"{tokens[i]}_{tokens[i+1]}" for i in range(len(tokens)-1)]
        trigrams = [f"{tokens[i]}_{tokens[i+1]}_{tokens[i+2]}" for i in range(len(tokens)-2)]
        
        # Extração de entidades
        entities = self.extract_entities(text)
        
        # Análise de sentimento básica
        sentiment = self.analyze_sentiment(tokens)
        
        return {
            'original': text,
            'tokens': tokens,
            'unigrams': unigrams,
            'bigrams': bigrams,
            'trigrams': trigrams,
            'entities': entities,
            'sentiment': sentiment,
            'length': len(tokens),
            'complexity': self.calculate_complexity(tokens)
        }
    
    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """Extrai entidades nomeadas do texto com detecção de intenções"""
        entities = {
            'enderecos': [],
            'numeros': [],
            'locais': [],
            'servicos': [],
            'problemas': [],
            'intencoes': [],
            'acoes': []
        }
        
        # Padrões para endereços
        if re.search(r'\b(endereço|endereco|casa|apartamento|numero|cep|rua|avenida)\b', text):
            entities['enderecos'].append('endereco_mencionado')
        
        # Padrões para números
        numeros = re.findall(r'\b\d+\b', text)
        entities['numeros'].extend(numeros)
        
        # Padrões para locais
        locais_patterns = r'\b(casa|trabalho|faculdade|hotel|empresa|estado|cidade)\b'
        locais = re.findall(locais_patterns, text)
        entities['locais'].extend(locais)
        
        # Padrões para serviços Shopee
        servicos_patterns = r'\b(pedido|entrega|pagamento|pix|reembolso|devolucao|cupom)\b'
        servicos = re.findall(servicos_patterns, text)
        entities['servicos'].extend(servicos)
        
        # Detecção de intenções específicas
        if re.search(r'\b(cancelar|cancela|não quero|desistir|parar)\b', text):
            entities['intencoes'].append('cancelamento')
        
        if re.search(r'\b(alterar|mudar|corrigir|atualizar|erro)\b', text) and not re.search(r'\b(defeito|quebrado|não funciona)\b', text):
            entities['intencoes'].append('alteracao')
        
        if re.search(r'\b(devolver|trocar|reembolso)\b', text):
            entities['intencoes'].append('devolucao')
        
        # Detecção de produtos defeituosos (alta prioridade)
        if re.search(r'\b(defeito|defeituoso|quebrado|não funciona|não liga|estragado|danificado|com problema)\b', text):
            entities['intencoes'].append('produto_defeituoso')
        
        if re.search(r'\b(veio|chegou)\b.*\b(quebrado|defeito|estragado|com problema|usado|sujo)\b', text):
            entities['intencoes'].append('produto_defeituoso')
        
        if re.search(r'\b(produto|celular|notebook|tv|fone|mouse|teclado)\b.*\b(não funciona|não liga|quebrado|defeito)\b', text):
            entities['intencoes'].append('produto_defeituoso')
        
        # Detecção de reenvio/segunda entrega (situação específica)
        if re.search(r'\b(não quero devolver|sem devolver|não devolver)\b.*\b(mandar|enviar|novo|outro)\b', text):
            entities['intencoes'].append('reenvio_produto')
        
        if re.search(r'\b(pode mandar|pode enviar|reenvia|reenviar|segunda entrega|segunda via)\b', text):
            entities['intencoes'].append('reenvio_produto')
        
        if re.search(r'\b(substituir|substituto|trocar por outro|produto de reposição)\b', text):
            entities['intencoes'].append('reenvio_produto')
        
        # Detecção de ações
        acoes_patterns = r'\b(quero|preciso|como|onde|quando|posso)\b'
        acoes = re.findall(acoes_patterns, text)
        entities['acoes'].extend(acoes)
        
        return entities
    
    def analyze_sentiment(self, tokens: List[str]) -> Dict[str, float]:
        """Análise de sentimento avançada"""
        positive_words = {'bom', 'ótimo', 'excelente', 'perfeito', 'obrigado', 'parabéns'}
        negative_words = {'erro', 'errado', 'problema', 'ruim', 'péssimo', 'reclamação'}
        urgent_words = {'urgente', 'emergência', 'rápido', 'imediato', 'já'}
        
        sentiment_scores = {
            'positive': sum(1 for word in tokens if word in positive_words),
            'negative': sum(1 for word in tokens if word in negative_words),
            'urgent': sum(1 for word in tokens if word in urgent_words),
            'neutral': 0
        }
        
        total = sum(sentiment_scores.values())
        if total == 0:
            sentiment_scores['neutral'] = 1
            total = 1
        
        # Normalizar scores
        for key in sentiment_scores:
            sentiment_scores[key] /= total
        
        return sentiment_scores
    
    def calculate_complexity(self, tokens: List[str]) -> float:
        """Calcula complexidade textual"""
        if not tokens:
            return 0.0
        
        unique_words = len(set(tokens))
        total_words = len(tokens)
        avg_word_length = sum(len(word) for word in tokens) / total_words
        
        complexity = (unique_words / total_words) * (avg_word_length / 10)
        return min(complexity, 1.0)
    
    def create_advanced_embedding(self, processed_text: Dict[str, Any]) -> np.ndarray:
        """
        Cria embeddings avançados usando múltiplas técnicas
        """
        # Embedding base dos tokens
        token_embeddings = []
        for token in processed_text['tokens']:
            if token not in self.word_vectors:
                # Criar embedding baseado em hash + características
                self.word_vectors[token] = self.generate_smart_embedding(token)
            token_embeddings.append(self.word_vectors[token])
        
        if not token_embeddings:
            return np.zeros(self.embedding_dim)
        
        # Embedding médio ponderado
        base_embedding = np.mean(token_embeddings, axis=0)
        
        # Incorporar n-gramas
        ngram_features = self.process_ngrams(processed_text)
        
        # Incorporar características semânticas
        semantic_features = self.extract_semantic_features(processed_text)
        
        # Incorporar análise de sentimento
        sentiment_features = self.encode_sentiment(processed_text['sentiment'])
        
        # Combinar todas as características garantindo dimensões corretas
        dim1 = self.embedding_dim//3
        dim2 = self.embedding_dim//3  
        dim3 = self.embedding_dim//6
        dim4 = self.embedding_dim - dim1 - dim2 - dim3  # Restante para sentiment
        
        final_embedding = np.concatenate([
            base_embedding[:dim1],
            ngram_features[:dim2],
            semantic_features[:dim3],
            sentiment_features[:dim4]
        ])
        
        # Aplicar transformações neurais
        final_embedding = self.apply_neural_transformations(final_embedding)
        
        return final_embedding
    
    def generate_smart_embedding(self, word: str) -> np.ndarray:
        """Gera embedding inteligente para uma palavra"""
        # Hash-based initialization
        hash_obj = hashlib.md5(word.encode())
        hash_bytes = hash_obj.digest()
        
        # Converter para números
        hash_numbers = [b / 255.0 for b in hash_bytes]
        
        # Expandir para dimensão desejada
        embedding = np.array(hash_numbers * (self.embedding_dim // len(hash_numbers) + 1))
        embedding = embedding[:self.embedding_dim]
        
        # Adicionar características linguísticas
        linguistic_features = np.array([
            len(word) / 20.0,  # Comprimento normalizado
            word.count('a') / len(word),  # Densidade de vogais
            word.count('e') / len(word),
            word.count('i') / len(word),
            word.count('o') / len(word),
            word.count('u') / len(word),
            1.0 if word.endswith('ão') else 0.0,  # Padrões morfológicos
            1.0 if word.startswith('des') else 0.0,
            1.0 if 'shop' in word else 0.0,  # Relevância para Shopee
            1.0 if any(c.isdigit() for c in word) else 0.0  # Contém números
        ])
        
        # Mesclar características
        embedding[:len(linguistic_features)] += linguistic_features
        
        # Normalizar
        embedding = embedding / (np.linalg.norm(embedding) + 1e-8)
        
        return embedding
    
    def process_ngrams(self, processed_text: Dict[str, Any]) -> np.ndarray:
        """Processa n-gramas para features avançadas"""
        features = np.zeros(self.embedding_dim // 3)
        
        # Processar bigramas
        for i, bigram in enumerate(processed_text['bigrams'][:10]):
            if bigram not in self.phrase_vectors:
                self.phrase_vectors[bigram] = np.random.randn(self.embedding_dim // 6)
            features[:self.embedding_dim//6] += self.phrase_vectors[bigram]
        
        # Processar trigramas
        for i, trigram in enumerate(processed_text['trigrams'][:5]):
            if trigram not in self.phrase_vectors:
                self.phrase_vectors[trigram] = np.random.randn(self.embedding_dim // 6)
            features[self.embedding_dim//6:] += self.phrase_vectors[trigram]
        
        return features
    
    def extract_semantic_features(self, processed_text: Dict[str, Any]) -> np.ndarray:
        """Extrai características semânticas avançadas"""
        target_size = max(6, self.embedding_dim // 6)
        features = np.zeros(target_size)
        
        # Características baseadas em entidades
        entities = processed_text['entities']
        features[0] = len(entities['enderecos']) / 5.0
        features[1] = len(entities['numeros']) / 10.0
        features[2] = len(entities['locais']) / 5.0
        features[3] = len(entities['servicos']) / 5.0
        
        # Características de complexidade
        if target_size > 4:
            features[4] = processed_text['complexity']
        if target_size > 5:
            features[5] = processed_text['length'] / 20.0
        
        # Adicionar características extras se necessário
        for i in range(6, target_size):
            features[i] = random.random() * 0.1  # Ruído baixo para dimensões extras
        
        return features
    
    def encode_sentiment(self, sentiment: Dict[str, float]) -> np.ndarray:
        """Codifica análise de sentimento com dimensão flexível"""
        base_sentiment = np.array([
            sentiment['positive'],
            sentiment['negative'],
            sentiment['urgent'],
            sentiment['neutral']
        ])
        
        # Expandir para pelo menos embedding_dim//6 elementos
        target_size = max(4, self.embedding_dim//6)
        if len(base_sentiment) < target_size:
            # Repetir valores ou adicionar zeros conforme necessário
            padding_size = target_size - len(base_sentiment)
            padding = np.zeros(padding_size)
            return np.concatenate([base_sentiment, padding])
        
        return base_sentiment[:target_size]
    
    def apply_neural_transformations(self, embedding: np.ndarray) -> np.ndarray:
        """Aplica transformações neurais avançadas"""
        # Garantir dimensionalidade correta
        if embedding.shape[0] != self.embedding_dim:
            # Redimensionar embedding para corresponder à dimensão esperada
            if embedding.shape[0] > self.embedding_dim:
                embedding = embedding[:self.embedding_dim]
            else:
                # Expandir com zeros se necessário
                padding = np.zeros(self.embedding_dim - embedding.shape[0])
                embedding = np.concatenate([embedding, padding])
        
        # Atenção
        attention_output = np.tanh(np.dot(embedding, self.attention_weights))
        
        # Contexto
        if self.context_memory:
            context_vector = np.mean(list(self.context_memory), axis=0)
            # Garantir que context_vector tem a dimensão correta
            if context_vector.shape[0] != self.embedding_dim:
                if context_vector.shape[0] > self.embedding_dim:
                    context_vector = context_vector[:self.embedding_dim]
                else:
                    padding = np.zeros(self.embedding_dim - context_vector.shape[0])
                    context_vector = np.concatenate([context_vector, padding])
            
            context_output = np.tanh(np.dot(context_vector, self.context_weights))
            embedding = 0.7 * attention_output + 0.3 * context_output
        else:
            embedding = attention_output
        
        # Normalização final
        embedding = embedding / (np.linalg.norm(embedding) + 1e-8)
        
        return embedding

class ShopeeNeuralAI:
    """
    Sistema de IA Neural Avançado para Atendimento Shopee
    Implementa aprendizado profundo, contexto avançado e análise semântica
    """
    
    def __init__(self):
        self.processor = AdvancedNeuralProcessor()
        self.training_patterns = []
        self.conversation_context = deque(maxlen=20)
        self.user_profiles = {}
        self.performance_metrics = defaultdict(float)
        self.learning_rate = 0.01
        self.confidence_threshold = 0.3
        
        # Sistemas avançados
        self.semantic_clusters = defaultdict(list)
        self.response_cache = {}
        self.dynamic_learning = True
        self.session_stats = defaultdict(int)
        
        # Configurar persistência
        self.model_file = 'e:/MENSAGENS/shopee_neural_model.pkl'
        self.metrics_file = 'e:/MENSAGENS/shopee_metrics.json'
        
        # Inicializar logger
        self.logger = self.processor.logger
        
    def load_advanced_training_data(self, file_path: str) -> bool:
        """Carrega dados de treinamento com processamento avançado"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
            
            self.logger.info(f"Carregando {len(raw_data)} padrões de treinamento...")
            
            # Processar cada padrão
            for item in raw_data:
                processed_question = self.processor.advanced_preprocess(item['question'])
                question_embedding = self.processor.create_advanced_embedding(processed_question)
                
                pattern = {
                    'question': item['question'],
                    'response': item['response'],
                    'confidence': item.get('confidence', 0.8),
                    'category': item.get('category', 'geral'),
                    'embedding': question_embedding,
                    'processed': processed_question,
                    'hash': hashlib.md5(item['question'].encode()).hexdigest()
                }
                
                self.training_patterns.append(pattern)
                self.semantic_clusters[pattern['category']].append(pattern)
            
            self.logger.info(f"✅ {len(self.training_patterns)} padrões processados")
            self.logger.info(f"📊 {len(self.semantic_clusters)} categorias semânticas criadas")
            
            # Otimizar clusters
            self.optimize_semantic_clusters()
            
            return True
            
        except Exception as e:
            self.logger.error(f"Erro ao carregar dados: {e}")
            return False
    
    def optimize_semantic_clusters(self):
        """Otimiza clusters semânticos para busca mais eficiente"""
        self.logger.info("🔧 Otimizando clusters semânticos...")
        
        for category, patterns in self.semantic_clusters.items():
            if len(patterns) > 1:
                # Calcular centroide do cluster
                embeddings = [p['embedding'] for p in patterns]
                centroid = np.mean(embeddings, axis=0)
                
                # Adicionar centroide ao cluster
                for pattern in patterns:
                    pattern['cluster_centroid'] = centroid
                    pattern['cluster_distance'] = np.linalg.norm(pattern['embedding'] - centroid)
        
        self.logger.info("✅ Otimização de clusters concluída")
    
    def advanced_similarity_search(self, user_input: str) -> Tuple[Dict, float, str]:
        """
        Busca avançada com múltiplas métricas de similaridade e detecção de intenção
        """
        processed_input = self.processor.advanced_preprocess(user_input)
        input_embedding = self.processor.create_advanced_embedding(processed_input)
        
        # Adicionar ao contexto
        self.processor.context_memory.append(input_embedding)
        
        best_match = None
        best_score = 0.0
        scoring_details = {}
        
        # Detectar intenção primária
        primary_intent = self.detect_primary_intent(processed_input)
        
        for pattern in self.training_patterns:
            # Múltiplas métricas de similaridade
            cosine_sim = self.cosine_similarity(input_embedding, pattern['embedding'])
            semantic_sim = self.semantic_similarity(processed_input, pattern['processed'])
            context_sim = self.context_similarity(pattern)
            category_boost = self.category_relevance_boost(processed_input, pattern['category'])
            intent_boost = self.intent_alignment_boost(primary_intent, pattern['category'])
            
            # Score combinado com pesos neurais ajustados
            combined_score = (
                0.3 * cosine_sim +
                0.25 * semantic_sim +
                0.15 * context_sim +
                0.2 * category_boost +
                0.1 * intent_boost
            )
            
            # Aplicar boost de confiança
            confidence_boost = pattern['confidence'] * 0.05
            final_score = combined_score + confidence_boost
            
            if final_score > best_score:
                best_score = final_score
                best_match = pattern
                scoring_details = {
                    'cosine': cosine_sim,
                    'semantic': semantic_sim,
                    'context': context_sim,
                    'category_boost': category_boost,
                    'intent_boost': intent_boost,
                    'confidence_boost': confidence_boost,
                    'final_score': final_score,
                    'primary_intent': primary_intent
                }
        
        if best_match:
            response = self.enhance_response(best_match, processed_input, best_score)
            category = best_match['category']
            
            # Atualizar métricas
            self.update_performance_metrics(user_input, best_match, best_score)
            
            return response, best_score, category
        
        return self.generate_fallback_response(processed_input), 0.0, 'fallback'
    
    def detect_primary_intent(self, processed_input: Dict) -> str:
        """Detecta a intenção primária do usuário com prioridade para produtos defeituosos"""
        entities = processed_input['entities']
        tokens = processed_input['tokens']
        text = ' '.join(tokens)
        
        # PRIORIDADE MÁXIMA: Reenvio/Segunda entrega (situação muito específica)
        if 'reenvio_produto' in entities['intencoes']:
            return 'reenvio_produto'
        
        if any(pattern in text for pattern in ['não quero devolver', 'sem devolver', 'pode mandar novamente', 'pode enviar outro']):
            return 'reenvio_produto'
        
        # PRIORIDADE ALTA: Produtos defeituosos
        if 'produto_defeituoso' in entities['intencoes'] and 'reenvio_produto' not in entities['intencoes']:
            return 'produto_defeituoso'
        
        if any(word in text for word in ['defeito', 'defeituoso', 'quebrado', 'não funciona', 'não liga', 'estragado', 'danificado']):
            return 'produto_defeituoso'
        
        if any(pattern in text for pattern in ['veio quebrado', 'chegou quebrado', 'produto ruim', 'má qualidade', 'não presta']):
            return 'produto_defeituoso'
        
        # Palavras-chave de alta prioridade
        if any(word in text for word in ['cancelar', 'cancela', 'não quero', 'desistir', 'parar', 'anular']):
            return 'cancelamento'
        
        if any(word in text for word in ['alterar', 'mudar', 'corrigir', 'atualizar']) and 'dados' in text:
            return 'alteracao_dados'
        
        if any(word in text for word in ['endereço', 'endereco', 'casa', 'apartamento']):
            return 'alteracao_endereco'
        
        if any(word in text for word in ['devolver', 'trocar', 'reembolso']):
            return 'devolucao'
        
        if any(word in text for word in ['pedido', 'compra', 'onde', 'status']):
            return 'consulta_pedido'
        
        if any(word in text for word in ['pagar', 'pagamento', 'pix', 'cartão']):
            return 'pagamento'
        
        return 'geral'
    
    def intent_alignment_boost(self, primary_intent: str, category: str) -> float:
        """Boost baseado no alinhamento entre intenção detectada e categoria"""
        intent_category_map = {
            'reenvio_produto': ['reenvio_produto'],
            'produto_defeituoso': ['produto_defeituoso'],
            'cancelamento': ['cancelamento_pedido'],
            'alteracao_dados': ['alteracao_dados'],
            'alteracao_endereco': ['alteracao_dados'],
            'devolucao': ['devolucao', 'reembolso'],
            'consulta_pedido': ['pedidos'],
            'pagamento': ['pagamento', 'pix', 'shopeepay'],
            'geral': ['saudacao', 'suporte', 'geral']
        }
        
        if primary_intent in intent_category_map:
            if category in intent_category_map[primary_intent]:
                return 1.0  # Boost forte para alinhamento perfeito
            
            # Verificar alinhamentos parciais
            if primary_intent == 'cancelamento' and category == 'pedidos':
                return 0.3  # Boost menor para relação parcial
            if primary_intent == 'alteracao_dados' and category == 'conta':
                return 0.3
        
        return 0.0
    
    def cosine_similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
        """Similaridade cosseno otimizada"""
        dot_product = np.dot(vec1, vec2)
        norm_product = np.linalg.norm(vec1) * np.linalg.norm(vec2)
        return dot_product / (norm_product + 1e-8)
    
    def semantic_similarity(self, proc1: Dict, proc2: Dict) -> float:
        """Similaridade semântica avançada"""
        # Similaridade de entidades
        entities1 = set(proc1['entities']['enderecos'] + proc1['entities']['servicos'])
        entities2 = set(proc2['entities']['enderecos'] + proc2['entities']['servicos'])
        
        if entities1 or entities2:
            entity_sim = len(entities1.intersection(entities2)) / (len(entities1.union(entities2)) + 1e-8)
        else:
            entity_sim = 0.0
        
        # Similaridade de tokens
        tokens1 = set(proc1['tokens'])
        tokens2 = set(proc2['tokens'])
        token_sim = len(tokens1.intersection(tokens2)) / (len(tokens1.union(tokens2)) + 1e-8)
        
        # Similaridade de sentimento
        sent1 = proc1['sentiment']
        sent2 = proc2['sentiment']
        sentiment_sim = 1.0 - sum(abs(sent1[k] - sent2[k]) for k in sent1.keys()) / len(sent1)
        
        return 0.5 * entity_sim + 0.3 * token_sim + 0.2 * sentiment_sim
    
    def context_similarity(self, pattern: Dict) -> float:
        """Similaridade baseada no contexto da conversa"""
        if not self.conversation_context:
            return 0.0
        
        # Analisar contexto recente
        recent_categories = [ctx.get('category', '') for ctx in list(self.conversation_context)[-3:]]
        
        if pattern['category'] in recent_categories:
            return 0.8  # Boost para categoria relacionada ao contexto
        
        return 0.0
    
    def category_relevance_boost(self, processed_input: Dict, category: str) -> float:
        """Boost baseado na relevância da categoria com detecção precisa"""
        category_keywords = {
            'reenvio_produto': ['não quero devolver', 'sem devolver', 'pode mandar', 'pode enviar', 'reenvia', 'reenviar', 'segunda entrega', 'segunda via', 'substituir', 'substituto', 'reposição'],
            'produto_defeituoso': ['defeito', 'defeituoso', 'quebrado', 'não funciona', 'não liga', 'estragado', 'danificado', 'problema', 'ruim', 'péssimo', 'usado', 'sujo', 'rachado', 'arranhão'],
            'alteracao_dados': ['alterar', 'mudar', 'endereço', 'endereco', 'dados', 'erro', 'corrigir', 'atualizar'],
            'cancelamento_pedido': ['cancelar', 'cancela', 'parar', 'anular', 'desfazer', 'reverter', 'estornar', 'remover', 'excluir', 'desistir'],
            'pedidos': ['pedido', 'compra', 'status', 'onde', 'rastrear', 'acompanhar'],
            'pagamento': ['pagar', 'pix', 'cartão', 'cartao', 'pagamento', 'valor', 'preco'],
            'entrega': ['entrega', 'prazo', 'correios', 'rastrear', 'chegou', 'receber'],
            'devolucao': ['devolver', 'trocar', 'reembolso', 'devoluçao', 'troca']
        }
        
        # Palavras que indicam forte intenção para cada categoria
        strong_indicators = {
            'reenvio_produto': ['não quero devolver pode mandar', 'sem devolver quero outro', 'pode enviar outro', 'segunda entrega'],
            'produto_defeituoso': ['veio com defeito', 'produto quebrado', 'não funciona', 'chegou quebrado', 'defeito de fábrica'],
            'cancelamento_pedido': ['cancelar', 'cancela', 'não quero', 'desistir', 'parar'],
            'alteracao_dados': ['alterar dados', 'mudar endereço', 'corrigir', 'atualizar']
        }
        
        if category in category_keywords:
            keywords = category_keywords[category]
            matches = sum(1 for token in processed_input['tokens'] if token in keywords)
            
            # Boost extra para indicadores fortes
            if category in strong_indicators:
                text_full = ' '.join(processed_input['tokens'])
                for indicator in strong_indicators[category]:
                    if indicator in text_full:
                        matches += 2  # Boost extra
            
            return min(matches / max(len(keywords), 1), 1.5)  # Permite boost > 1.0
        
        return 0.0
    
    def enhance_response(self, pattern: Dict, user_input: Dict, score: float) -> str:
        """Aprimora resposta com base no contexto e score"""
        base_response = pattern['response']
        
        # Adicionar personalização baseada no sentimento
        if user_input['sentiment']['urgent'] > 0.5:
            urgency_phrases = [
                "Entendemos a urgência da situação. ",
                "Sabemos que é importante resolver rapidamente. ",
                "Compreendemos que precisa de uma solução rápida. "
            ]
            base_response = random.choice(urgency_phrases) + base_response
        
        # Adicionar empatia se detectar frustração
        if user_input['sentiment']['negative'] > 0.3:
            empathy_phrases = [
                "Lamentamos pelo inconveniente. ",
                "Compreendemos sua frustração. ",
                "Pedimos desculpas pelo transtorno. "
            ]
            base_response = random.choice(empathy_phrases) + base_response
        
        return base_response
    
    def generate_fallback_response(self, processed_input: Dict) -> str:
        """Gera resposta de fallback inteligente"""
        # Analisar tipo de pergunta para fallback contextual
        if processed_input['entities']['enderecos']:
            return ("Para questões relacionadas a endereço e entrega, recomendamos entrar em "
                   "contato com o suporte oficial da Shopee através do app ou site.")
        
        if processed_input['entities']['servicos']:
            servicos = processed_input['entities']['servicos']
            if 'pedido' in servicos:
                return ("Para dúvidas sobre pedidos, acesse 'Meus Pedidos' no app Shopee ou "
                       "entre em contato com o atendimento oficial.")
            elif 'pagamento' in servicos:
                return ("Para questões de pagamento, verifique as opções disponíveis no checkout "
                       "ou contate o suporte da Shopee.")
        
        # Fallback genérico baseado em sentimento
        if processed_input['sentiment']['urgent'] > 0.3:
            return ("Entendemos que é urgente. Para assistência imediata, recomendamos "
                   "contatar diretamente o atendimento oficial da Shopee.")
        
        return ("Não consegui encontrar uma resposta específica para sua pergunta. "
               "Pode reformular ou entrar em contato com o suporte oficial da Shopee?")
    
    def update_performance_metrics(self, user_input: str, pattern: Dict, score: float):
        """Atualiza métricas de performance"""
        self.performance_metrics['total_interactions'] += 1
        self.performance_metrics['average_confidence'] = (
            (self.performance_metrics['average_confidence'] * 
             (self.performance_metrics['total_interactions'] - 1) + score) /
            self.performance_metrics['total_interactions']
        )
        
        category = pattern['category']
        self.performance_metrics[f'category_{category}'] += 1
        
        if score > 0.7:
            self.performance_metrics['high_confidence_responses'] += 1
        elif score > 0.4:
            self.performance_metrics['medium_confidence_responses'] += 1
        else:
            self.performance_metrics['low_confidence_responses'] += 1
    
    def dynamic_learning(self, user_input: str, expected_response: str, category: str = 'geral'):
        """Sistema de aprendizado dinâmico em tempo real"""
        if not self.dynamic_learning:
            return False
        
        try:
            # Processar nova entrada
            processed_input = self.processor.advanced_preprocess(user_input)
            input_embedding = self.processor.create_advanced_embedding(processed_input)
            
            # Criar novo padrão
            new_pattern = {
                'question': user_input,
                'response': expected_response,
                'confidence': 0.8,
                'category': category,
                'embedding': input_embedding,
                'processed': processed_input,
                'hash': hashlib.md5(user_input.encode()).hexdigest(),
                'learned_at': datetime.now().isoformat(),
                'learned_dynamically': True
            }
            
            # Verificar se já existe padrão similar
            for existing_pattern in self.training_patterns:
                similarity = self.cosine_similarity(input_embedding, existing_pattern['embedding'])
                if similarity > 0.9:  # Muito similar
                    self.logger.info(f"Padrão similar já existe (sim: {similarity:.3f})")
                    return False
            
            # Adicionar novo padrão
            self.training_patterns.append(new_pattern)
            self.semantic_clusters[category].append(new_pattern)
            
            # Reotimizar clusters se necessário
            if len(self.semantic_clusters[category]) % 10 == 0:
                self.optimize_semantic_clusters()
            
            self.logger.info(f"✅ Novo padrão aprendido dinamicamente: {category}")
            return True
            
        except Exception as e:
            self.logger.error(f"Erro no aprendizado dinâmico: {e}")
            return False
    
    def save_model(self) -> bool:
        """Salva modelo completo com todas as informações"""
        try:
            model_data = {
                'training_patterns': self.training_patterns,
                'processor_word_vectors': self.processor.word_vectors,
                'processor_phrase_vectors': self.processor.phrase_vectors,
                'semantic_clusters': dict(self.semantic_clusters),
                'performance_metrics': dict(self.performance_metrics),
                'conversation_context': list(self.conversation_context),
                'neural_weights': {
                    'attention': self.processor.attention_weights.tolist(),
                    'context': self.processor.context_weights.tolist(),
                    'semantic': self.processor.semantic_weights.tolist()
                },
                'saved_at': datetime.now().isoformat(),
                'version': '2.0_advanced'
            }
            
            with open(self.model_file, 'wb') as f:
                pickle.dump(model_data, f)
            
            # Salvar métricas separadamente em JSON
            with open(self.metrics_file, 'w', encoding='utf-8') as f:
                json.dump(dict(self.performance_metrics), f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"💾 Modelo salvo: {self.model_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"Erro ao salvar modelo: {e}")
            return False
    
    def load_model(self) -> bool:
        """Carrega modelo salvo"""
        if not os.path.exists(self.model_file):
            return False
        
        try:
            with open(self.model_file, 'rb') as f:
                model_data = pickle.load(f)
            
            # Restaurar dados
            self.training_patterns = model_data.get('training_patterns', [])
            self.processor.word_vectors = model_data.get('processor_word_vectors', {})
            self.processor.phrase_vectors = model_data.get('processor_phrase_vectors', {})
            self.semantic_clusters = defaultdict(list, model_data.get('semantic_clusters', {}))
            self.performance_metrics = defaultdict(float, model_data.get('performance_metrics', {}))
            self.conversation_context = deque(model_data.get('conversation_context', []), maxlen=20)
            
            # Restaurar pesos neurais
            neural_weights = model_data.get('neural_weights', {})
            if neural_weights:
                self.processor.attention_weights = np.array(neural_weights.get('attention'))
                self.processor.context_weights = np.array(neural_weights.get('context'))
                self.processor.semantic_weights = np.array(neural_weights.get('semantic'))
            
            saved_at = model_data.get('saved_at', 'desconhecido')
            version = model_data.get('version', 'legacy')
            
            self.logger.info(f"✅ Modelo carregado: {len(self.training_patterns)} padrões")
            self.logger.info(f"📅 Salvo em: {saved_at}, Versão: {version}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Erro ao carregar modelo: {e}")
            return False
    
    def get_detailed_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas detalhadas do sistema"""
        stats = {
            'system_info': {
                'total_patterns': len(self.training_patterns),
                'categories': len(self.semantic_clusters),
                'vocabulary_size': len(self.processor.word_vectors),
                'phrase_vectors': len(self.processor.phrase_vectors),
                'context_memory': len(self.processor.context_memory),
                'conversation_context': len(self.conversation_context)
            },
            'performance': dict(self.performance_metrics),
            'categories': {cat: len(patterns) for cat, patterns in self.semantic_clusters.items()},
            'recent_activity': {
                'session_stats': dict(self.session_stats)
            }
        }
        
        # Calcular estatísticas adicionais
        if self.performance_metrics['total_interactions'] > 0:
            total = self.performance_metrics['total_interactions']
            stats['performance']['success_rate'] = (
                (self.performance_metrics['high_confidence_responses'] + 
                 self.performance_metrics['medium_confidence_responses']) / total * 100
            )
        
        return stats
    
    def advanced_chat_interface(self):
        """Interface de chat avançada com recursos completos"""
        print("🚀 SHOPEE NEURAL AI - SISTEMA AVANÇADO DE ATENDIMENTO")
        print("=" * 70)
        print("🤖 Assistente de IA Neural com Deep Learning e NLP Avançado")
        print("\n🎯 CAPACIDADES AVANÇADAS:")
        print("  🧠 Processamento Neural Profundo")
        print("  🔍 Análise Semântica Avançada")
        print("  💭 Compreensão de Contexto")
        print("  📊 Aprendizado Dinâmico em Tempo Real")
        print("  🎨 Personalização de Respostas")
        print("  📈 Métricas de Performance Avançadas")
        
        print(f"\n📊 STATUS DO SISTEMA:")
        stats = self.get_detailed_stats()
        print(f"  📚 {stats['system_info']['total_patterns']} padrões neurais")
        print(f"  🏷️ {stats['system_info']['categories']} categorias semânticas")
        print(f"  🔤 {stats['system_info']['vocabulary_size']} palavras no vocabulário")
        print(f"  ⚡ Modelo neural otimizado e carregado")
        
        print(f"\n⚙️ COMANDOS AVANÇADOS:")
        print("  'stats' - Estatísticas detalhadas do sistema")
        print("  'learn [pergunta] | [resposta] | [categoria]' - Aprendizado dinâmico")
        print("  'context' - Ver contexto da conversa")
        print("  'metrics' - Métricas de performance")
        print("  'save' - Salvar modelo neural")
        print("  'reset' - Limpar contexto")
        print("  'sair' - Encerrar sistema")
        print("=" * 70)
        
        while True:
            try:
                user_input = input("\n🔮 Você: ").strip()
                
                if not user_input:
                    continue
                
                # Comandos especiais
                if user_input.lower() in ['sair', 'quit', 'exit']:
                    print("🤖 Sistema: Salvando estado do sistema...")
                    self.save_model()
                    print("🚀 Shopee Neural AI encerrado. Até logo! 👋")
                    break
                
                elif user_input.lower() == 'stats':
                    self.show_detailed_stats()
                    continue
                
                elif user_input.lower().startswith('learn '):
                    self.handle_dynamic_learning_command(user_input)
                    continue
                
                elif user_input.lower() == 'context':
                    self.show_conversation_context()
                    continue
                
                elif user_input.lower() == 'metrics':
                    self.show_performance_metrics()
                    continue
                
                elif user_input.lower() == 'save':
                    success = self.save_model()
                    status = "✅ Sucesso" if success else "❌ Erro"
                    print(f"💾 Salvamento: {status}")
                    continue
                
                elif user_input.lower() == 'reset':
                    self.conversation_context.clear()
                    self.processor.context_memory.clear()
                    print("🔄 Contexto limpo!")
                    continue
                
                # Processar pergunta normal
                start_time = time.time()
                response_data, confidence, category = self.advanced_similarity_search(user_input)
                processing_time = time.time() - start_time
                
                # Adicionar ao contexto da conversa
                self.conversation_context.append({
                    'user_input': user_input,
                    'response': response_data,
                    'confidence': confidence,
                    'category': category,
                    'timestamp': datetime.now().isoformat(),
                    'processing_time': processing_time
                })
                
                # Determinar emoji de confiança
                if confidence > 0.8:
                    emoji = "🎯"
                elif confidence > 0.6:
                    emoji = "✅"
                elif confidence > 0.4:
                    emoji = "⚡"
                else:
                    emoji = "🤔"
                
                # Exibir resposta
                print(f"🤖 Shopee Neural AI: {response_data} {emoji}")
                
                # Exibir métricas se confiança baixa ou solicitado
                if confidence < 0.6:
                    print(f"    🔬 [Confiança: {confidence:.3f} | Categoria: {category} | {processing_time:.3f}s]")
                
                # Atualizar estatísticas da sessão
                self.session_stats['total_queries'] += 1
                self.session_stats[f'category_{category}'] += 1
                
                if confidence > 0.6:
                    self.session_stats['successful_responses'] += 1
                
            except KeyboardInterrupt:
                print("\n\n🔄 Salvando estado antes de encerrar...")
                self.save_model()
                print("🚀 Sistema encerrado com segurança! 👋")
                break
            
            except Exception as e:
                self.logger.error(f"Erro na interface: {e}")
                print(f"❌ Erro inesperado: {e}")
                print("🔧 Sistema continua funcionando...")
    
    def show_detailed_stats(self):
        """Mostra estatísticas detalhadas"""
        stats = self.get_detailed_stats()
        
        print("\n📊 ESTATÍSTICAS DETALHADAS DO SISTEMA NEURAL")
        print("=" * 60)
        
        print("🖥️ INFORMAÇÕES DO SISTEMA:")
        for key, value in stats['system_info'].items():
            print(f"  📋 {key.replace('_', ' ').title()}: {value:,}")
        
        print(f"\n⚡ PERFORMANCE GERAL:")
        perf = stats['performance']
        for key, value in perf.items():
            if isinstance(value, float):
                print(f"  📈 {key.replace('_', ' ').title()}: {value:.3f}")
            else:
                print(f"  📊 {key.replace('_', ' ').title()}: {value:,}")
        
        print(f"\n🏷️ DISTRIBUIÇÃO POR CATEGORIAS:")
        sorted_categories = sorted(stats['categories'].items(), key=lambda x: x[1], reverse=True)
        for category, count in sorted_categories[:10]:
            percentage = (count / stats['system_info']['total_patterns']) * 100
            print(f"  📁 {category}: {count} padrões ({percentage:.1f}%)")
        
        if len(sorted_categories) > 10:
            print(f"  ... e mais {len(sorted_categories) - 10} categorias")
    
    def handle_dynamic_learning_command(self, command: str):
        """Processa comando de aprendizado dinâmico"""
        try:
            # Formato: learn pergunta | resposta | categoria
            parts = command[6:].split(' | ')
            if len(parts) != 3:
                print("❌ Formato incorreto. Use: learn pergunta | resposta | categoria")
                return
            
            question, response, category = [part.strip() for part in parts]
            
            if self.dynamic_learning(question, response, category):
                print(f"🎓 ✅ Aprendizado realizado!")
                print(f"   📝 Pergunta: {question}")
                print(f"   💬 Resposta: {response[:50]}...")
                print(f"   🏷️ Categoria: {category}")
            else:
                print("⚠️ Aprendizado não realizado (padrão similar já existe)")
                
        except Exception as e:
            print(f"❌ Erro no aprendizado: {e}")
    
    def show_conversation_context(self):
        """Mostra contexto da conversa atual"""
        print(f"\n💭 CONTEXTO DA CONVERSA ({len(self.conversation_context)} interações)")
        print("-" * 50)
        
        if not self.conversation_context:
            print("📝 Nenhuma conversa no contexto atual")
            return
        
        for i, ctx in enumerate(list(self.conversation_context)[-5:], 1):
            timestamp = datetime.fromisoformat(ctx['timestamp']).strftime('%H:%M:%S')
            confidence_emoji = "🎯" if ctx['confidence'] > 0.8 else "✅" if ctx['confidence'] > 0.6 else "⚡"
            
            print(f"{i}. [{timestamp}] {confidence_emoji}")
            print(f"   👤 Você: {ctx['user_input'][:40]}...")
            print(f"   🤖 Bot: {ctx['response'][:40]}...")
            print(f"   📊 Conf: {ctx['confidence']:.3f} | Cat: {ctx['category']}")
    
    def show_performance_metrics(self):
        """Mostra métricas de performance da sessão"""
        print(f"\n📈 MÉTRICAS DE PERFORMANCE DA SESSÃO")
        print("-" * 45)
        
        total = self.session_stats.get('total_queries', 0)
        successful = self.session_stats.get('successful_responses', 0)
        
        if total > 0:
            success_rate = (successful / total) * 100
            print(f"📊 Total de consultas: {total}")
            print(f"✅ Respostas bem-sucedidas: {successful}")
            print(f"📈 Taxa de sucesso: {success_rate:.1f}%")
            
            print(f"\n🏷️ Categorias consultadas:")
            for key, value in self.session_stats.items():
                if key.startswith('category_') and value > 0:
                    category = key.replace('category_', '')
                    print(f"  📁 {category}: {value} consultas")
        else:
            print("📝 Nenhuma consulta realizada na sessão atual")

def main():
    """Função principal - Inicialização do sistema avançado"""
    print("🚀 INICIALIZANDO SHOPEE NEURAL AI ADVANCED...")
    print("⚡ Sistema de IA Neural com Deep Learning")
    
    # Criar instância do sistema
    ai_system = ShopeeNeuralAI()
    
    # Tentar carregar modelo existente
    print("🔄 Verificando modelo salvo...")
    model_loaded = ai_system.load_model()
    
    if not model_loaded:
        print("📚 Carregando dados de treinamento...")
        
        # Arquivos de dados para carregar
        training_files = [
            'e:/MENSAGENS/shopee_complete_training.json',
            'e:/MENSAGENS/training_data.json'
        ]
        
        loaded = False
        for file_path in training_files:
            if os.path.exists(file_path):
                if ai_system.load_advanced_training_data(file_path):
                    loaded = True
                    break
        
        if not loaded:
            print("❌ Nenhum arquivo de treinamento encontrado!")
            print("💡 Certifique-se de que os dados estão disponíveis")
            return
    
    print("🎯 Sistema Neural carregado e otimizado!")
    print("🔥 Pronto para atendimento avançado com IA!")
    
    # Iniciar interface de chat
    ai_system.advanced_chat_interface()

if __name__ == "__main__":
    main()