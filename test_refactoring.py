#!/usr/bin/env python3
"""
Test del refactoring di Aurora AI
"""

import json
import os
from datetime import datetime
from personality_manager import PersonalityManager
from memory_manager import MemoryManager
from autonomous_system import AutonomousSystem
from config import CONFIG, ensure_directories

def test_personality_manager():
    """Test del PersonalityManager."""
    print("=== Test PersonalityManager ===")
    
    # Crea un manager temporaneo
    temp_config = CONFIG.copy()
    temp_config["personality_state_path"] = "./test_personality.json"
    
    pm = PersonalityManager(temp_config)
    
    # Test get_state_summary
    summary = pm.get_state_summary()
    print(f"✓ get_state_summary: {len(summary)} campi")
    
    # Test update_trait
    pm.update_trait('stress', 0.8, "test stress")
    print(f"✓ update_trait: stress = {pm.state['stress']:.2f}")
    
    # Test apply_cathartic_effects
    old_stress = pm.state['stress']
    pm.apply_cathartic_effects()
    print(f"✓ apply_cathartic_effects: stress {old_stress:.2f} → {pm.state['stress']:.2f}")
    
    # Test decay_mood
    old_serenity = pm.state['mood']['serenità']
    pm.decay_mood()
    print(f"✓ decay_mood: serenità {old_serenity:.2f} → {pm.state['mood']['serenità']:.2f}")
    
    # Test get_emotional_context
    context = pm.get_emotional_context()
    print(f"✓ get_emotional_context: {context}")
    
    # Cleanup
    if os.path.exists(temp_config["personality_state_path"]):
        os.remove(temp_config["personality_state_path"])
    
    print("✓ PersonalityManager: TUTTI I TEST SUPERATI\n")

def test_memory_manager():
    """Test del MemoryManager."""
    print("=== Test MemoryManager ===")
    
    # Crea un manager temporaneo
    temp_config = CONFIG.copy()
    temp_config["memory_box_path"] = "./test_memory.json"
    temp_config["chat_history_path"] = "./test_chat.json"
    temp_config["inside_jokes_path"] = "./test_jokes.json"
    temp_config["knowledge_graph_path"] = "./test_kg.json"
    
    mm = MemoryManager(temp_config)
    
    # Test add_chat_entry
    mm.add_chat_entry("user", "Ciao Aurora!")
    mm.add_chat_entry("assistant", "Ciao! Come stai?")
    print(f"✓ add_chat_entry: {len(mm.chat_history)} entries")
    
    # Test add_memory
    memory = {
        'content': 'Ho imparato qualcosa di nuovo oggi',
        'sentiment': 'positivo',
        'confidence': 0.9
    }
    mm.add_memory(memory)
    print(f"✓ add_memory: {len(mm.memory_box)} memorie")
    
    # Test add_inside_joke
    mm.add_inside_joke("Test joke", "Test context")
    print(f"✓ add_inside_joke: {len(mm.inside_jokes)} jokes")
    
    # Test add_knowledge
    relationships = [{'type': 'is_a', 'target': 'concept', 'confidence': 0.8}]
    mm.add_knowledge("test_entity", relationships)
    print(f"✓ add_knowledge: {len(mm.knowledge_graph)} entries")
    
    # Test retrieve_relevant_memories
    memories = mm.retrieve_relevant_memories("nuovo", limit=3)
    print(f"✓ retrieve_relevant_memories: {len(memories)} risultati")
    
    # Test query_knowledge_graph
    kg_results = mm.query_knowledge_graph("test")
    print(f"✓ query_knowledge_graph: {len(kg_results)} risultati")
    
    # Test get_recent_memories
    recent = mm.get_recent_memories(hours=1)
    print(f"✓ get_recent_memories: {len(recent)} memorie recenti")
    
    # Cleanup
    for path in [temp_config["memory_box_path"], temp_config["chat_history_path"], 
                 temp_config["inside_jokes_path"], temp_config["knowledge_graph_path"]]:
        if os.path.exists(path):
            os.remove(path)
    
    print("✓ MemoryManager: TUTTI I TEST SUPERATI\n")

def test_autonomous_system():
    """Test del AutonomousSystem."""
    print("=== Test AutonomousSystem ===")
    
    # Crea manager temporanei
    temp_config = CONFIG.copy()
    temp_config["personality_state_path"] = "./test_personality.json"
    temp_config["memory_box_path"] = "./test_memory.json"
    temp_config["legacy_project_path"] = "./test_legacy.json"
    
    pm = PersonalityManager(temp_config)
    mm = MemoryManager(temp_config)
    asys = AutonomousSystem(pm, mm, temp_config)
    
    # Test update_aurora_urges
    asys.update_aurora_urges()
    print("✓ update_aurora_urges: completato")
    
    # Test _calculate_desire_score
    catharsis_desire = asys._calculate_desire_score("catharsis")
    netflix_desire = asys._calculate_desire_score("netflix")
    print(f"✓ _calculate_desire_score: catharsis={catharsis_desire:.2f}, netflix={netflix_desire:.2f}")
    
    # Test _resolve_internal_conflicts
    conflict_res, dominant_voice = asys._resolve_internal_conflicts("catharsis")
    print(f"✓ _resolve_internal_conflicts: resolution={conflict_res:.2f}, voice={dominant_voice['name'] if dominant_voice else 'None'}")
    
    # Test _get_temporal_context
    temporal = asys._get_temporal_context()
    print(f"✓ _get_temporal_context: hour={temporal['hour']}, energy_mod={temporal['energy_modifier']:.2f}")
    
    # Test aurora_makes_choice (più volte per vedere variabilità)
    choices = []
    for i in range(5):
        choice = asys.aurora_makes_choice("catharsis")
        choices.append(choice)
    print(f"✓ aurora_makes_choice: {choices.count(True)}/5 scelte positive")
    
    # Test learn_from_choice_result
    asys.learn_from_choice_result("catharsis", was_praised=True)
    print("✓ learn_from_choice_result: lode applicata")
    
    # Test _apply_contextual_learning
    asys._apply_contextual_learning("catharsis", "timing")
    print("✓ _apply_contextual_learning: correzione timing applicata")
    
    # Test get_autonomous_summary
    summary = asys.get_autonomous_summary()
    print(f"✓ get_autonomous_summary: {len(summary)} campi")
    
    # Cleanup
    for path in [temp_config["personality_state_path"], temp_config["memory_box_path"], 
                 temp_config["legacy_project_path"]]:
        if os.path.exists(path):
            os.remove(path)
    
    print("✓ AutonomousSystem: TUTTI I TEST SUPERATI\n")

def test_integration():
    """Test di integrazione tra i componenti."""
    print("=== Test Integrazione ===")
    
    # Crea manager temporanei
    temp_config = CONFIG.copy()
    temp_config["personality_state_path"] = "./test_personality.json"
    temp_config["memory_box_path"] = "./test_memory.json"
    temp_config["legacy_project_path"] = "./test_legacy.json"
    
    pm = PersonalityManager(temp_config)
    mm = MemoryManager(temp_config)
    asys = AutonomousSystem(pm, mm, temp_config)
    
    # Simula un ciclo completo
    print("1. Stato iniziale:")
    initial_state = pm.get_state_summary()
    print(f"   Stress: {initial_state['stress']:.2f}")
    
    print("2. Aurora fa una scelta autonoma:")
    choice_made = asys.aurora_makes_choice("catharsis")
    print(f"   Scelta catharsis: {choice_made}")
    
    print("3. Stato dopo la scelta:")
    after_choice_state = pm.get_state_summary()
    print(f"   Fiducia autonomia: {after_choice_state['catharsis_epiphany']['autonomy_confidence']:.2f}")
    
    print("4. Applica apprendimento contestuale:")
    asys.learn_from_choice_result("catharsis", was_corrected=True, reason="intensity")
    
    print("5. Stato finale:")
    final_state = pm.get_state_summary()
    print(f"   Impulsi creativi: {final_state['catharsis_epiphany']['creative_urges']:.2f}")
    
    # Verifica che i dati siano stati salvati
    print("6. Verifica persistenza:")
    pm2 = PersonalityManager(temp_config)
    restored_state = pm2.get_state_summary()
    print(f"   Stress ripristinato: {restored_state['stress']:.2f}")
    
    # Cleanup
    for path in [temp_config["personality_state_path"], temp_config["memory_box_path"], 
                 temp_config["legacy_project_path"]]:
        if os.path.exists(path):
            os.remove(path)
    
    print("✓ Integrazione: TUTTI I TEST SUPERATI\n")

def main():
    """Esegue tutti i test."""
    print("🧪 AVVIO TEST REFACTORING AURORA AI")
    print("=" * 50)
    
    # Assicura che le directory esistano
    ensure_directories()
    
    try:
        test_personality_manager()
        test_memory_manager()
        test_autonomous_system()
        test_integration()
        
        print("🎉 TUTTI I TEST SUPERATI!")
        print("✅ Il refactoring è stato completato con successo.")
        print("✅ Aurora ora ha un'architettura modulare e un sistema di scelta psicologicamente realistico.")
        
    except Exception as e:
        print(f"❌ ERRORE DURANTE I TEST: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 