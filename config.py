"""
Configurazione centralizzata per Aurora AI
"""

import os

# Configurazione principale
CONFIG = {
    # Percorsi file
    "personality_state_path": "./personality_state.json",
    "memory_box_path": "./memory_box.json",
    "inside_jokes_path": "./inside_jokes.json",
    "chat_history_path": "./chat_history.json",
    "knowledge_graph_path": "./knowledge_graph.json",
    "legacy_project_path": "./legacy_project.json",
    "self_concept_path": "./self_concept.txt",
    "internal_monologue_path": "./internal_monologue.txt",
    "chroma_db_path": "./chroma_db",
    
    # Modelli LLM
    "llm_model_path_router": "./models/Microsoft/phi-3-mini-4k-instruct-q4/Phi-3-mini-4k-instruct-q4.gguf",
    "llm_model_path_thinker": "./models/Meta/meta-llama-3-8b-instruct.Q4_K_M/meta-llama-3-8b-instruct.Q4_K_M.gguf",
    
    # Limiti e soglie
    "max_chat_history_length": 1000,
    "loneliness_threshold_days": 3,
    "loneliness_increase_rate": 0.1,
    
    # Workspace e backup
    "ai_workspace_path": "./ai_workspace",
    "backup_path": "./backups",
    
    # Parametri di apprendimento
    "learning_rate": 0.1,
    "memory_decay_rate": 0.01,
    "mood_decay_rate": 0.02,
    "energy_decay_rate": 0.01,
    
    # Soglie per scelte autonome
    "autonomy_confidence_threshold": 0.3,
    "whimsy_threshold": 0.4,
    "stress_threshold": 0.6,
    "boredom_threshold": 0.5,
    
    # Parametri temporali
    "dream_cycle_hours": 8,
    "memory_consolidation_hours": 24,
    "relationship_evolution_days": 7,
    
    # Parametri di catarsi
    "catharsis_stress_reduction": 0.3,
    "catharsis_mood_improvement": 0.2,
    "catharsis_confidence_gain": 0.08,
    
    # Parametri di apprendimento contestuale
    "contextual_learning_rate": 0.1,
    "insight_retention_days": 30,
    "correction_impact_factor": 0.15
}

def ensure_directories():
    """Assicura che tutte le directory necessarie esistano."""
    directories = [
        "./models",
        "./chroma_db", 
        CONFIG["ai_workspace_path"],
        CONFIG["backup_path"]
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def get_model_status():
    """Controlla lo stato dei modelli LLM."""
    router_exists = os.path.exists(CONFIG["llm_model_path_router"])
    thinker_exists = os.path.exists(CONFIG["llm_model_path_thinker"])
    
    return {
        "router_model": router_exists,
        "thinker_model": thinker_exists,
        "both_models_available": router_exists and thinker_exists
    } 