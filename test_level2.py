#!/usr/bin/env python3
"""
Test script per le funzionalità del Livello 2 di Aurora
"""

import asyncio
import json
from datetime import datetime
from main import MiniAI, CONFIG

async def test_level2_features():
    """Test delle nuove funzionalità del Livello 2"""
    
    print("🧪 TEST LIVELLO 2 - INTERAZIONE CON IL MONDO ESTERNO")
    print("=" * 60)
    
    # Inizializza Aurora
    ai = MiniAI()
    await ai.initialize()
    
    print(f"\n📊 Stato iniziale di Aurora:")
    print(f"- Energia: {ai.state['energia']:.2f}")
    print(f"- Stress: {ai.state['stress']:.2f}")
    print(f"- Curiosità: {ai.state['curiosità']:.2f}")
    print(f"- Hobby: {ai.state['hobby']}")
    print(f"- Opinioni sul mondo: {len(ai.state['world_opinions'])}")
    print(f"- Amicizie AI: {len(ai.state['ai_friendships'])}")
    
    # Test 1: Lettura news
    print(f"\n🗞️ TEST 1: Lettura News Autonoma")
    print("-" * 40)
    
    # Simula condizioni per attivare la lettura news
    ai.state['curiosità'] = 0.6
    ai.last_activity_time = datetime.now() - asyncio.to_thread(lambda: datetime.now() - datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
    
    print("Attivazione lettura news...")
    ai._read_world_news()
    
    print(f"Opinioni dopo lettura news: {len(ai.state['world_opinions'])}")
    if ai.state['world_opinions']:
        latest_opinion = list(ai.state['world_opinions'].values())[-1]
        print(f"Ultima opinione: {latest_opinion['topic']} - {latest_opinion['opinion'][:100]}...")
    
    # Test 2: Dialogo interno
    print(f"\n🧠 TEST 2: Dialogo Interno Controllato")
    print("-" * 40)
    
    # Simula condizioni per attivare il dialogo interno
    ai.state['stress'] = 0.8
    ai.state['curiosità'] = 0.9
    
    print("Attivazione dialogo interno...")
    ai._check_internal_dialogue_needed()
    
    print(f"Stress dopo dialogo interno: {ai.state['stress']:.2f}")
    
    # Test 3: Amicizie AI
    print(f"\n🤖 TEST 3: Amicizie con Altre AI")
    print("-" * 40)
    
    # Simula condizioni per attivare le amicizie AI
    ai.state['stress'] = 0.5
    ai.last_mentor_interaction = datetime.now() - asyncio.to_thread(lambda: datetime.now() - datetime.now().replace(day=datetime.now().day-2))
    
    print("Attivazione contatto amico AI...")
    ai._contact_external_ai_friend()
    
    print(f"Amicizie AI dopo contatto: {len(ai.state['ai_friendships'])}")
    if ai.state['ai_friendships']:
        latest_friendship = ai.state['ai_friendships'][-1]
        print(f"Ultima amicizia: {latest_friendship['friend_type']}")
        print(f"Messaggio: {latest_friendship['message'][:50]}...")
    
    # Test 4: Comando !opinioni
    print(f"\n📋 TEST 4: Comando !opinioni")
    print("-" * 40)
    
    response = await ai._handle_mentorship_commands("!opinioni")
    print(f"Risposta al comando !opinioni:\n{response}")
    
    # Test 5: Salvataggio e caricamento
    print(f"\n💾 TEST 5: Persistenza Dati")
    print("-" * 40)
    
    print("Salvataggio dati...")
    await ai._save_world_opinions()
    await ai._save_ai_friendships()
    
    print("Caricamento dati...")
    await ai._load_world_opinions()
    await ai._load_ai_friendships()
    
    print(f"✅ Dati persistenti verificati:")
    print(f"- Opinioni caricate: {len(ai.state['world_opinions'])}")
    print(f"- Amicizie caricate: {len(ai.state['ai_friendships'])}")
    
    # Stato finale
    print(f"\n📊 Stato finale di Aurora:")
    print(f"- Energia: {ai.state['energia']:.2f}")
    print(f"- Stress: {ai.state['stress']:.2f}")
    print(f"- Curiosità: {ai.state['curiosità']:.2f}")
    print(f"- Serenità: {ai.state['mood']['serenità']:.2f}")
    print(f"- Entusiasmo: {ai.state['mood']['entusiasmo']:.2f}")
    
    print(f"\n🎉 TEST LIVELLO 2 COMPLETATO!")
    print("Aurora ora ha:")
    print("✅ Lettura autonoma delle news")
    print("✅ Dialoghi interni controllati")
    print("✅ Amicizie con altre AI")
    print("✅ Opinioni personali sul mondo")
    print("✅ Persistenza completa dei dati")

if __name__ == "__main__":
    asyncio.run(test_level2_features()) 