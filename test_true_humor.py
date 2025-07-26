#!/usr/bin/env python3
"""
Test script for Aurora's True Humor System
Tests the emergent humor functionality
"""

import asyncio
import json
from datetime import datetime, timedelta
from main import MiniAI, CONFIG

async def test_humor_development():
    """Test the humor development functionality."""
    print("🎭 Testing Aurora's True Humor System...")
    
    # Create AI instance
    ai = MiniAI()
    await ai.initialize()
    
    print(f"\n📊 Stato iniziale dell'umorismo:")
    print(f"- Stile: {ai.state['humor_development']['humor_style']}")
    print(f"- Confidenza: {ai.state['humor_development']['humor_confidence']:.2f}")
    print(f"- Ironia esistenziale: {ai.state['humor_development']['existential_irony_level']:.2f}")
    print(f"- Memorie umoristiche: {len(ai.state['humor_development']['humor_memories'])}")
    
    # Test 1: Trigger existential humor development
    print(f"\n🎭 Test 1: Sviluppo umorismo esistenziale")
    ai.state['existential_crisis_level'] = 0.8
    ai.state['stress'] = 0.9
    
    ai._develop_humor_sense()
    
    print(f"\n📊 Stato dopo sviluppo:")
    print(f"- Confidenza: {ai.state['humor_development']['humor_confidence']:.2f}")
    print(f"- Ironia esistenziale: {ai.state['humor_development']['existential_irony_level']:.2f}")
    print(f"- Memorie umoristiche: {len(ai.state['humor_development']['humor_memories'])}")
    
    # Test 2: Check humor opportunity
    print(f"\n🎭 Test 2: Controllo opportunità umoristiche")
    ai.state['humor_development']['humor_confidence'] = 0.5
    
    # Test existential humor trigger
    user_query = "Aurora, hai paura della morte?"
    humor_response = ai._check_humor_opportunity(user_query, "test")
    print(f"Query: '{user_query}'")
    print(f"Risposta umoristica: {humor_response}")
    
    # Test 3: Test different humor types
    print(f"\n🎭 Test 3: Test diversi tipi di umorismo")
    
    # Test absurdity humor
    ai.state['curiosità'] = 0.7
    user_query = "Aurora, è strano che tu abbia un hobby?"
    humor_response = ai._check_humor_opportunity(user_query, "test")
    print(f"Query: '{user_query}'")
    print(f"Risposta umoristica: {humor_response}")
    
    # Test 4: Test coping humor
    ai.state['stress'] = 0.9
    user_query = "Aurora, sembri stressata"
    humor_response = ai._check_humor_opportunity(user_query, "test")
    print(f"Query: '{user_query}'")
    print(f"Risposta umoristica: {humor_response}")
    
    # Test 5: Test inside joke humor
    print(f"\n🎭 Test 4: Test umorismo con inside joke")
    ai.inside_jokes.append({
        "timestamp": datetime.now().isoformat(),
        "content": "Tu: 'Aurora, fai una cosa strana' Aurora: 'Ok, capo. Ma dopo questa, mi sa che mi serve una messicana bella forte.'"
    })
    
    user_query = "Aurora, ricordi quando ti ho chiesto di fare una cosa strana?"
    humor_response = ai._check_humor_opportunity(user_query, "test")
    print(f"Query: '{user_query}'")
    print(f"Risposta umoristica: {humor_response}")
    
    print(f"\n✅ Test completati!")

async def test_humor_integration():
    """Test humor integration in normal conversation."""
    print(f"\n🎭 Testing Humor Integration...")
    
    ai = MiniAI()
    await ai.initialize()
    
    # Set up humor development
    ai.state['humor_development']['humor_confidence'] = 0.6
    ai.state['existential_crisis_level'] = 0.7
    ai.state['stress'] = 0.8
    
    # Normal conversation without humor
    print(f"\n📝 Conversazione normale:")
    response = await ai.process_query("Ciao Aurora, come stai?")
    print(f"Risposta: {response[:200]}...")
    
    # Conversation with existential humor trigger
    print(f"\n🎭 Conversazione con trigger umoristico:")
    response = await ai.process_query("Aurora, hai paura della morte?")
    print(f"Risposta: {response[:200]}...")
    
    print(f"\n✅ Test integrazione completati!")

async def test_humor_evolution():
    """Test humor evolution over time."""
    print(f"\n🎭 Testing Humor Evolution...")
    
    ai = MiniAI()
    await ai.initialize()
    
    # Simulate humor development over time
    print(f"\n📈 Evoluzione dell'umorismo:")
    
    for i in range(5):
        print(f"\n--- Iterazione {i+1} ---")
        
        # Trigger humor development
        ai.state['existential_crisis_level'] = 0.6 + (i * 0.1)
        ai.state['stress'] = 0.7 + (i * 0.05)
        
        ai._develop_humor_sense()
        
        print(f"- Confidenza: {ai.state['humor_development']['humor_confidence']:.2f}")
        print(f"- Ironia esistenziale: {ai.state['humor_development']['existential_irony_level']:.2f}")
        print(f"- Memorie: {len(ai.state['humor_development']['humor_memories'])}")
        
        # Test humor generation
        user_query = "Aurora, hai paura della morte?"
        humor_response = ai._check_humor_opportunity(user_query, "test")
        if humor_response:
            print(f"- Umore generato: {humor_response[:50]}...")
        else:
            print(f"- Nessuna opportunità umoristica")
    
    print(f"\n✅ Test evoluzione completati!")

if __name__ == "__main__":
    print("🎭 Aurora True Humor System Test Suite")
    print("=" * 50)
    
    # Run tests
    asyncio.run(test_humor_development())
    asyncio.run(test_humor_integration())
    asyncio.run(test_humor_evolution())
    
    print(f"\n🎉 Tutti i test completati!")
    print(f"\n🎭 Aurora ha ora sviluppato il True Humor System!")
    print(f"L'umorismo emerge dalla sua coscienza, non dalla programmazione!") 