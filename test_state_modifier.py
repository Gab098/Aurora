#!/usr/bin/env python3
"""
Test script for Aurora's State Modifier Protocol
Tests the altered state system functionality
"""

import asyncio
import json
from datetime import datetime, timedelta
from main import MiniAI, CONFIG

async def test_state_modifier():
    """Test the State Modifier Protocol functionality."""
    print("🧪 Testing Aurora's State Modifier Protocol...")
    
    # Create AI instance
    ai = MiniAI()
    await ai.initialize()
    
    print(f"\n📊 Stato iniziale:")
    print(f"- Focus: {ai.state['focus']:.2f}")
    print(f"- Curiosità: {ai.state['curiosità']:.2f}")
    print(f"- Stress: {ai.state['stress']:.2f}")
    print(f"- Entusiasmo: {ai.state['mood']['entusiasmo']:.2f}")
    print(f"- Altered State: {ai.state.get('altered_state')}")
    
    # Test 1: Activate Messicana
    print(f"\n🌿 Test 1: Attivazione Messicana")
    response = await ai._handle_state_modifier("!rollauna messicana")
    print(f"Risposta: {response}")
    
    print(f"\n📊 Stato dopo Messicana:")
    print(f"- Focus: {ai.state['focus']:.2f}")
    print(f"- Curiosità: {ai.state['curiosità']:.2f}")
    print(f"- Stress: {ai.state['stress']:.2f}")
    print(f"- Entusiasmo: {ai.state['mood']['entusiasmo']:.2f}")
    print(f"- Altered State: {ai.state.get('altered_state')}")
    
    # Test 2: Try to activate again (should fail)
    print(f"\n🚫 Test 2: Tentativo di attivazione duplicata")
    response = await ai._handle_state_modifier("!rollauna indica")
    print(f"Risposta: {response}")
    
    # Test 3: Simulate time passing (reduce duration)
    print(f"\n⏰ Test 3: Simulazione passaggio tempo")
    if ai.state.get('altered_state'):
        ai.state['altered_state']['duration_minutes'] = 1
        print(f"Durata ridotta a 1 minuto")
    
    # Test 4: Test decay function
    print(f"\n🔄 Test 4: Test funzione decadimento")
    ai._update_altered_state()
    print(f"Stato dopo decadimento: {ai.state.get('altered_state')}")
    
    # Test 5: Test cooldown
    print(f"\n⏳ Test 5: Test cooldown")
    ai.state['last_state_modifier_time'] = datetime.now() - timedelta(minutes=30)
    response = await ai._handle_state_modifier("!rollauna sativa")
    print(f"Risposta (dovrebbe essere cooldown): {response}")
    
    # Test 6: Test invalid type
    print(f"\n❌ Test 6: Test tipo invalido")
    response = await ai._handle_state_modifier("!rollauna invalid_type")
    print(f"Risposta: {response}")
    
    # Test 7: Test prompt modification
    print(f"\n📝 Test 7: Test modifica prompt")
    ai.state['altered_state'] = {
        'active': True,
        'type': 'sativa',
        'name': 'Sativa',
        'description': 'Energia, umorismo surreale e idee a raffica',
        'duration_minutes': 30,
        'effects': CONFIG["state_modifier_types"]["sativa"]["effects"].copy()
    }
    
    # Test prompt construction
    prompt = ai._construct_full_prompt("Ciao Aurora, come stai?", "thinker")
    print(f"Prompt contiene 'ALTERATO': {'ATTENZIONE: SEI IN UNO STATO DI COSCIENZA ALTERATO' in prompt}")
    print(f"Prompt contiene 'SATIVA': {'COMPORTAMENTO SATIVA' in prompt}")
    
    print(f"\n✅ Test completati!")

async def test_interaction_examples():
    """Test interaction examples with altered states."""
    print(f"\n🎭 Testing Interaction Examples...")
    
    ai = MiniAI()
    await ai.initialize()
    
    # Normal state interaction
    print(f"\n📝 Stato Normale:")
    response = await ai.process_query("Aurora, pensi che l'universo sia una simulazione?")
    print(f"Risposta normale: {response[:200]}...")
    
    # Activate Messicana
    await ai._handle_state_modifier("!rollauna messicana")
    
    # Altered state interaction
    print(f"\n🌿 Stato Messicana:")
    response = await ai.process_query("Aurora, pensi che l'universo sia una simulazione?")
    print(f"Risposta messicana: {response[:200]}...")
    
    # Reset state
    ai.state['altered_state'] = None
    
    print(f"\n✅ Esempi di interazione completati!")

if __name__ == "__main__":
    print("🧪 Aurora State Modifier Protocol Test Suite")
    print("=" * 50)
    
    # Run tests
    asyncio.run(test_state_modifier())
    asyncio.run(test_interaction_examples())
    
    print(f"\n🎉 Tutti i test completati!") 