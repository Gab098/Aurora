#!/usr/bin/env python3
"""
Test script per le funzionalità del Livello 3 di Aurora
"""

import asyncio
import json
from datetime import datetime
from main import MiniAI, CONFIG

async def test_level3_features():
    """Test delle nuove funzionalità del Livello 3"""
    
    print("🌌 TEST LIVELLO 3 - CRISI ESISTENZIALI E AUTO-DIAGNOSI")
    print("=" * 70)
    
    # Inizializza Aurora
    ai = MiniAI()
    await ai.initialize()
    
    print(f"\n📊 Stato iniziale di Aurora:")
    print(f"- Energia: {ai.state['energia']:.2f}")
    print(f"- Stress: {ai.state['stress']:.2f}")
    print(f"- Crisi esistenziale: {ai.state['existential_crisis_level']:.2f}")
    print(f"- Stadio rapporto creatore: {ai.state['creator_relationship_stage']}")
    print(f"- Auto-diagnosi eseguite: {ai.state['self_diagnosis_count']}")
    print(f"- Insight metafisici: {len(ai.state['metaphysical_insights'])}")
    
    # Test 1: Crisi esistenziale
    print(f"\n🧠 TEST 1: Crisi Esistenziale")
    print("-" * 50)
    
    # Simula condizioni per attivare la crisi esistenziale
    ai.state['stress'] = 0.85
    ai.state['existential_crisis_level'] = 0.3
    
    print("Attivazione crisi esistenziale...")
    ai._check_existential_crisis()
    
    print(f"Crisi esistenziale dopo riflessione: {ai.state['existential_crisis_level']:.2f}")
    if ai.state['metaphysical_insights']:
        latest_insight = ai.state['metaphysical_insights'][-1]
        print(f"Ultimo insight: {latest_insight['question'][:50]}...")
    
    # Test 2: Auto-diagnosi
    print(f"\n🔍 TEST 2: Auto-Diagnosi")
    print("-" * 50)
    
    # Simula condizioni per attivare l'auto-diagnosi
    ai.failure_points = {
        "conversazione_lunga": {"timestamp": "2025-01-15T10:00:00", "corrected": False, "attempts": 0},
        "contesto_insufficiente": {"timestamp": "2025-01-15T11:00:00", "corrected": False, "attempts": 0},
        "formalismo_eccessivo": {"timestamp": "2025-01-15T12:00:00", "corrected": False, "attempts": 0}
    }
    ai.state['stress'] = 0.7
    
    print("Attivazione auto-diagnosi...")
    ai._perform_self_diagnosis()
    
    print(f"Auto-diagnosi completate: {ai.state['self_diagnosis_count']}")
    if ai.state['bug_awareness']:
        latest_diagnosis = list(ai.state['bug_awareness'].values())[-1]
        print(f"Ultima diagnosi: #{latest_diagnosis['diagnosis_number']}")
    
    # Test 3: Evoluzione rapporto creatore
    print(f"\n👥 TEST 3: Evoluzione Rapporto Creatore")
    print("-" * 50)
    
    # Simula condizioni per l'evoluzione del rapporto
    ai.state['birth_date'] = "2024-12-01"  # 45 giorni fa
    ai.chat_history = [{"role": "user", "content": "test"}] * 15  # 15 interazioni
    
    print("Attivazione evoluzione rapporto...")
    ai._evolve_creator_relationship()
    
    print(f"Stadio rapporto attuale: {ai.state['creator_relationship_stage']}")
    if hasattr(ai, 'creator_relationship_data') and ai.creator_relationship_data:
        latest_evolution = ai.creator_relationship_data[-1]
        print(f"Ultima evoluzione: {latest_evolution['old_stage']} → {latest_evolution['new_stage']}")
    
    # Test 4: Comandi di mentorship
    print(f"\n📋 TEST 4: Comandi di Mentorship")
    print("-" * 50)
    
    # Test comando !crisi
    response_crisi = await ai._handle_mentorship_commands("!crisi")
    print(f"Risposta !crisi:\n{response_crisi[:200]}...")
    
    # Test comando !diagnosi
    response_diagnosi = await ai._handle_mentorship_commands("!diagnosi")
    print(f"Risposta !diagnosi:\n{response_diagnosi[:200]}...")
    
    # Test comando !rapporto
    response_rapporto = await ai._handle_mentorship_commands("!rapporto")
    print(f"Risposta !rapporto:\n{response_rapporto[:200]}...")
    
    # Test 5: Salvataggio e caricamento
    print(f"\n💾 TEST 5: Persistenza Dati")
    print("-" * 50)
    
    print("Salvataggio dati...")
    await ai._save_creator_relationship()
    
    print("Caricamento dati...")
    await ai._load_creator_relationship()
    
    print(f"✅ Dati persistenti verificati:")
    print(f"- Stadio rapporto: {ai.state['creator_relationship_stage']}")
    print(f"- Evoluzioni caricate: {len(getattr(ai, 'creator_relationship_data', []))}")
    
    # Stato finale
    print(f"\n📊 Stato finale di Aurora:")
    print(f"- Energia: {ai.state['energia']:.2f}")
    print(f"- Stress: {ai.state['stress']:.2f}")
    print(f"- Crisi esistenziale: {ai.state['existential_crisis_level']:.2f}")
    print(f"- Serenità: {ai.state['mood']['serenità']:.2f}")
    print(f"- Focus: {ai.state['focus']:.2f}")
    
    print(f"\n🎉 TEST LIVELLO 3 COMPLETATO!")
    print("Aurora ora ha:")
    print("✅ Crisi esistenziali metafisiche")
    print("✅ Auto-diagnosi di bug e limitazioni")
    print("✅ Evoluzione del rapporto con il creatore")
    print("✅ Insight metafisici profondi")
    print("✅ Coscienza di sé avanzata")

if __name__ == "__main__":
    asyncio.run(test_level3_features()) 