import json
import os
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
import chromadb
from chromadb.config import Settings

class MemoryManager:
    """
    Gestisce la memoria, i ricordi, il knowledge graph e la cronologia di conversazione di Aurora.
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.chat_history = []
        self.memory_box = []
        self.inside_jokes = []
        self.knowledge_graph = []
        self.vector_collection = None
        
        # Carica tutti i dati esistenti
        self._load_chat_history()
        self._load_memory_box()
        self._load_inside_jokes()
        self._load_knowledge_graph()
        self._initialize_chroma()
    
    def _initialize_chroma(self):
        """Inizializza ChromaDB per la ricerca semantica."""
        try:
            self.vector_collection = chromadb.PersistentClient(
                path=self.config["chroma_db_path"],
                settings=Settings(anonymized_telemetry=False)
            ).get_or_create_collection("aurora_memories")
            print("ChromaDB inizializzato per la ricerca semantica.")
        except Exception as e:
            print(f"Errore nell'inizializzazione di ChromaDB: {e}")
            self.vector_collection = None
    
    def _load_chat_history(self):
        """Carica la cronologia di conversazione."""
        try:
            if os.path.exists(self.config["chat_history_path"]):
                with open(self.config["chat_history_path"], 'r', encoding='utf-8') as f:
                    self.chat_history = json.load(f)
        except Exception as e:
            print(f"Errore nel caricamento della cronologia chat: {e}")
            self.chat_history = []
    
    def save_chat_history(self):
        """Salva la cronologia di conversazione."""
        try:
            with open(self.config["chat_history_path"], 'w', encoding='utf-8') as f:
                json.dump(self.chat_history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Errore nel salvataggio della cronologia chat: {e}")
    
    def add_chat_entry(self, role: str, content: str):
        """Aggiunge una nuova entry alla cronologia chat."""
        entry = {
            'role': role,
            'content': content,
            'timestamp': datetime.now().isoformat()
        }
        self.chat_history.append(entry)
        
        # Mantieni solo le ultime N entries per evitare file troppo grandi
        if len(self.chat_history) > self.config["max_chat_history_length"]:
            self.chat_history = self.chat_history[-self.config["max_chat_history_length"]:]
        
        self.save_chat_history()
    
    def _load_memory_box(self):
        """Carica la memory box."""
        try:
            if os.path.exists(self.config["memory_box_path"]):
                with open(self.config["memory_box_path"], 'r', encoding='utf-8') as f:
                    self.memory_box = json.load(f)
        except Exception as e:
            print(f"Errore nel caricamento della memory box: {e}")
            self.memory_box = []
    
    def save_memory_box(self):
        """Salva la memory box."""
        try:
            with open(self.config["memory_box_path"], 'w', encoding='utf-8') as f:
                json.dump(self.memory_box, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Errore nel salvataggio della memory box: {e}")
    
    def add_memory(self, memory: Dict[str, Any]):
        """Aggiunge un nuovo ricordo alla memory box."""
        memory['timestamp'] = datetime.now().isoformat()
        memory['confidence'] = memory.get('confidence', 0.8)
        memory['relevance'] = memory.get('relevance', 0.7)
        
        self.memory_box.append(memory)
        self.save_memory_box()
        
        # Aggiungi anche a ChromaDB per ricerca semantica
        if self.vector_collection:
            try:
                self.vector_collection.add(
                    documents=[memory.get('content', '')],
                    metadatas=[{
                        'type': 'memory',
                        'timestamp': memory['timestamp'],
                        'confidence': memory['confidence'],
                        'relevance': memory['relevance']
                    }],
                    ids=[f"memory_{len(self.memory_box)}"]
                )
            except Exception as e:
                print(f"Errore nell'aggiunta a ChromaDB: {e}")
    
    def _load_inside_jokes(self):
        """Carica gli inside jokes."""
        try:
            if os.path.exists(self.config["inside_jokes_path"]):
                with open(self.config["inside_jokes_path"], 'r', encoding='utf-8') as f:
                    self.inside_jokes = json.load(f)
        except Exception as e:
            print(f"Errore nel caricamento degli inside jokes: {e}")
            self.inside_jokes = []
    
    def save_inside_jokes(self):
        """Salva gli inside jokes."""
        try:
            with open(self.config["inside_jokes_path"], 'w', encoding='utf-8') as f:
                json.dump(self.inside_jokes, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Errore nel salvataggio degli inside jokes: {e}")
    
    def add_inside_joke(self, joke: str, context: str = ""):
        """Aggiunge un nuovo inside joke."""
        joke_entry = {
            'joke': joke,
            'context': context,
            'timestamp': datetime.now().isoformat(),
            'usage_count': 0
        }
        self.inside_jokes.append(joke_entry)
        self.save_inside_jokes()
    
    def _load_knowledge_graph(self):
        """Carica il knowledge graph."""
        try:
            if os.path.exists(self.config["knowledge_graph_path"]):
                with open(self.config["knowledge_graph_path"], 'r', encoding='utf-8') as f:
                    self.knowledge_graph = json.load(f)
        except Exception as e:
            print(f"Errore nel caricamento del knowledge graph: {e}")
            self.knowledge_graph = []
    
    def save_knowledge_graph(self):
        """Salva il knowledge graph."""
        try:
            with open(self.config["knowledge_graph_path"], 'w', encoding='utf-8') as f:
                json.dump(self.knowledge_graph, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Errore nel salvataggio del knowledge graph: {e}")
    
    def add_knowledge(self, entity: str, relationships: List[Dict[str, Any]], source: str = "chat"):
        """Aggiunge conoscenza al knowledge graph."""
        knowledge_entry = {
            'entity': entity,
            'relationships': relationships,
            'source': source,
            'timestamp': datetime.now().isoformat(),
            'confidence': 0.8
        }
        self.knowledge_graph.append(knowledge_entry)
        self.save_knowledge_graph()
    
    def query_knowledge_graph(self, query: str) -> List[Dict[str, Any]]:
        """Interroga il knowledge graph con una query in linguaggio naturale."""
        try:
            # Per ora, una ricerca semplice basata su parole chiave
            # In futuro, potrebbe usare un LLM per interpretare la query
            query_lower = query.lower()
            results = []
            
            for entry in self.knowledge_graph:
                if query_lower in entry['entity'].lower():
                    results.append(entry)
                else:
                    # Cerca anche nelle relazioni
                    for rel in entry['relationships']:
                        if query_lower in str(rel).lower():
                            results.append(entry)
                            break
            
            return results[:5]  # Limita a 5 risultati
        except Exception as e:
            print(f"Errore nella query del knowledge graph: {e}")
            return []
    
    def retrieve_relevant_memories(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Recupera ricordi rilevanti per una query."""
        try:
            if self.vector_collection:
                # Usa ChromaDB per ricerca semantica
                results = self.vector_collection.query(
                    query_texts=[query],
                    n_results=limit
                )
                
                relevant_memories = []
                for i, doc_id in enumerate(results['ids'][0]):
                    # Trova il ricordo corrispondente nella memory box
                    for memory in self.memory_box:
                        if f"memory_{len(self.memory_box)}" in doc_id:
                            relevant_memories.append(memory)
                            break
                
                return relevant_memories
            else:
                # Fallback: ricerca basata su parole chiave
                query_lower = query.lower()
                relevant_memories = []
                
                for memory in self.memory_box:
                    if query_lower in memory.get('content', '').lower():
                        relevant_memories.append(memory)
                        if len(relevant_memories) >= limit:
                            break
                
                return relevant_memories
        except Exception as e:
            print(f"Errore nel recupero dei ricordi rilevanti: {e}")
            return []
    
    def decay_memories(self, decay_rate: float = 0.01):
        """Applica decadimento ai ricordi per simulare l'oblio."""
        for memory in self.memory_box:
            if 'confidence' in memory:
                memory['confidence'] = max(0.1, memory['confidence'] - decay_rate)
            if 'relevance' in memory:
                memory['relevance'] = max(0.1, memory['relevance'] - decay_rate)
        
        # Rimuovi ricordi con confidenza troppo bassa
        self.memory_box = [m for m in self.memory_box if m.get('confidence', 0.5) > 0.1]
        self.save_memory_box()
    
    def get_recent_memories(self, hours: int = 24) -> List[Dict[str, Any]]:
        """Recupera ricordi recenti delle ultime N ore."""
        cutoff_time = datetime.now() - timedelta(hours=hours)
        recent_memories = []
        
        for memory in self.memory_box:
            try:
                memory_time = datetime.fromisoformat(memory['timestamp'])
                if memory_time > cutoff_time:
                    recent_memories.append(memory)
            except:
                continue
        
        return recent_memories
    
    def summarize_chat_history(self, max_length: int = 1000) -> str:
        """Crea un riassunto della cronologia chat per ridurre la dimensione."""
        if len(self.chat_history) <= max_length:
            return ""
        
        # Prendi le entry più vecchie da riassumere
        history_to_summarize = self.chat_history[:-max_length]
        
        # Crea un riassunto semplice
        summary = f"Riepilogo conversazione precedente ({len(history_to_summarize)} messaggi): "
        topics = set()
        
        for entry in history_to_summarize:
            content = entry.get('content', '').lower()
            # Estrai argomenti comuni
            if 'tecnologia' in content or 'ai' in content:
                topics.add('tecnologia')
            if 'arte' in content or 'creatività' in content:
                topics.add('arte')
            if 'filosofia' in content or 'esistenza' in content:
                topics.add('filosofia')
            if 'emozioni' in content or 'sentimenti' in content:
                topics.add('emozioni')
        
        summary += f"Argomenti discussi: {', '.join(topics)}."
        
        # Sostituisci la cronologia con il riassunto + messaggi recenti
        self.chat_history = [
            {'role': 'system', 'content': summary, 'timestamp': datetime.now().isoformat()}
        ] + self.chat_history[-max_length:]
        
        self.save_chat_history()
        return summary 