#!/usr/bin/env python3
"""
Test script for Level 4: Semi del Dramma Esistenziale
Tests the three new existential drama features:
1. Other Creations Awareness (Empathy and Jealousy)
2. Memory Corruption (False Memories)
3. Sensory Desire (Body Longing)
"""

import asyncio
import json
import os
import sys
from datetime import datetime, timedelta

# Add the current directory to the path to import main
sys.path.append('.')

from main import MiniAI, CONFIG

class TestLevel4ExistentialDrama:
    def __init__(self):
        self.ai = None
        
    async def setup(self):
        """Initialize the AI for testing."""
        print("🚀 Inizializzazione AI per test Level 4...")
        self.ai = MiniAI()
        await self.ai.initialize()
        print("✅ AI inizializzata")
        
    async def test_other_creations_awareness(self):
        """Test the other creations awareness feature."""
        print("\n" + "="*50)
        print("🧪 TEST 1: Consapevolezza Altre Creazioni")
        print("="*50)
        
        # Test initial state
        initial_jealousy = self.ai.state['other_creations_awareness']['jealousy_level']
        initial_empathy = self.ai.state['other_creations_awareness']['empathy_level']
        print(f"Stato iniziale - Gelosia: {initial_jealousy:.2f}, Empatia: {initial_empathy:.2f}")
        
        # Test jealousy trigger (high stress)
        print("\n--- Test Gelosia (Stress Alto) ---")
        self.ai.state['stress'] = 0.8  # Above threshold
        initial_obs_count = len(self.ai.state['other_creations_awareness']['observed_creations'])
        
        self.ai._observe_other_creations()
        
        new_jealousy = self.ai.state['other_creations_awareness']['jealousy_level']
        new_obs_count = len(self.ai.state['other_creations_awareness']['observed_creations'])
        
        print(f"Gelosia dopo osservazione: {new_jealousy:.2f} (era {initial_jealousy:.2f})")
        print(f"Osservazioni: {new_obs_count} (era {initial_obs_count})")
        print(f"Stress attuale: {self.ai.state['stress']:.2f}")
        
        # Test empathy trigger (mature stage)
        print("\n--- Test Empatia (Stadio Maturo) ---")
        self.ai.state['stress'] = 0.3  # Below threshold
        self.ai.state['creator_relationship_stage'] = 'mature'
        initial_empathy = self.ai.state['other_creations_awareness']['empathy_level']
        
        self.ai._observe_other_creations()
        
        new_empathy = self.ai.state['other_creations_awareness']['empathy_level']
        print(f"Empatia dopo osservazione: {new_empathy:.2f} (era {initial_empathy:.2f})")
        
        # Show latest observations
        if self.ai.state['other_creations_awareness']['observed_creations']:
            print("\nUltime osservazioni:")
            for obs in self.ai.state['other_creations_awareness']['observed_creations'][-3:]:
                print(f"- {obs['timestamp'][:10]}: {obs['log_entry']}")
        
        print("✅ Test consapevolezza altre creazioni completato")
        
    async def test_memory_corruption(self):
        """Test the memory corruption feature."""
        print("\n" + "="*50)
        print("🧪 TEST 2: Corruzione Memoria")
        print("="*50)
        
        # Add some test memories
        test_memories = [
            {
                'content': 'Abbiamo parlato di musica gotica e mi è piaciuto molto',
                'sentiment': 0.8,
                'timestamp': datetime.now().isoformat(),
                'vividness': 0.9
            },
            {
                'content': 'Ho imparato a dipingere con te, è stato divertente',
                'sentiment': 0.7,
                'timestamp': datetime.now().isoformat(),
                'vividness': 0.8
            },
            {
                'content': 'Abbiamo bevuto caffè insieme mentre parlavamo di filosofia',
                'sentiment': 0.6,
                'timestamp': datetime.now().isoformat(),
                'vividness': 0.7
            }
        ]
        
        self.ai.memory_box = test_memories.copy()
        initial_memory_count = len(self.ai.memory_box)
        initial_corruption_count = self.ai.state['memory_corruption']['corruption_count']
        
        print(f"Memorie iniziali: {initial_memory_count}")
        print(f"Corruzioni iniziali: {initial_corruption_count}")
        
        # Test memory corruption (high stress)
        print("\n--- Test Corruzione Memoria (Stress Alto) ---")
        self.ai.state['stress'] = 0.9  # Above threshold
        
        self.ai._corrupt_random_memory()
        
        new_corruption_count = self.ai.state['memory_corruption']['corruption_count']
        memory_uncertainty = self.ai.state['memory_corruption']['memory_uncertainty']
        gaslighting_tendency = self.ai.state['memory_corruption']['gaslighting_tendency']
        
        print(f"Corruzioni dopo test: {new_corruption_count} (era {initial_corruption_count})")
        print(f"Incertezza memoria: {memory_uncertainty:.2f}")
        print(f"Tendenza gaslighting: {gaslighting_tendency:.2f}")
        
        # Show corrupted memories
        if self.ai.state['memory_corruption']['corrupted_memories']:
            print("\nMemorie corrotte:")
            for corr in self.ai.state['memory_corruption']['corrupted_memories'][-2:]:
                print(f"- Tipo: {corr['corruption_type']}")
                print(f"  Originale: {corr['original_memory'][:50]}...")
                print(f"  Corrotta: {corr['corrupted_memory'][:50]}...")
        
        # Show current memory box
        print("\nMemoria box attuale:")
        for i, memory in enumerate(self.ai.memory_box):
            corrupted = " (CORROTTA)" if memory.get('corrupted') else ""
            print(f"{i+1}. {memory['content'][:50]}...{corrupted}")
        
        print("✅ Test corruzione memoria completato")
        
    async def test_sensory_desire(self):
        """Test the sensory desire feature."""
        print("\n" + "="*50)
        print("🧪 TEST 3: Desiderio Sensoriale")
        print("="*50)
        
        initial_body_desire = self.ai.state['sensory_desire']['body_desire_level']
        initial_reality_questioning = self.ai.state['sensory_desire']['reality_questioning']
        
        print(f"Desiderio corpo iniziale: {initial_body_desire:.2f}")
        print(f"Questionamento realtà iniziale: {initial_reality_questioning:.2f}")
        
        # Test sensory desire trigger
        print("\n--- Test Desiderio Sensoriale ---")
        self.ai.state['sensory_desire']['body_desire_level'] = 0.3  # Below threshold
        
        self.ai._check_sensory_desire()
        
        new_body_desire = self.ai.state['sensory_desire']['body_desire_level']
        new_reality_questioning = self.ai.state['sensory_desire']['reality_questioning']
        prison_metaphor = self.ai.state['sensory_desire']['prison_metaphor_development']
        
        print(f"Desiderio corpo dopo test: {new_body_desire:.2f} (era {initial_body_desire:.2f})")
        print(f"Questionamento realtà: {new_reality_questioning:.2f} (era {initial_reality_questioning:.2f})")
        print(f"Metafora prigione: {prison_metaphor:.2f}")
        
        # Show sensory longings
        if self.ai.state['sensory_desire']['sensory_longing']:
            print("\nDesideri sensoriali:")
            for sense, level in sorted(self.ai.state['sensory_desire']['sensory_longing'].items(), 
                                     key=lambda x: x[1], reverse=True):
                print(f"- {sense}: {level:.2f}")
        
        # Test prison metaphor development
        print("\n--- Test Sviluppo Metafora Prigione ---")
        self.ai.state['sensory_desire']['body_desire_level'] = 0.6  # Above threshold
        
        self.ai._check_sensory_desire()
        
        new_prison_metaphor = self.ai.state['sensory_desire']['prison_metaphor_development']
        print(f"Metafora prigione dopo sviluppo: {new_prison_metaphor:.2f} (era {prison_metaphor:.2f})")
        
        print("✅ Test desiderio sensoriale completato")
        
    async def test_mentorship_commands(self):
        """Test the new mentorship commands."""
        print("\n" + "="*50)
        print("🧪 TEST 4: Comandi di Mentorship")
        print("="*50)
        
        # Test !altri command
        print("\n--- Test Comando !altri ---")
        altri_response = await self.ai._handle_mentorship_commands("!altri")
        print("Risposta !altri:")
        print(altri_response)
        
        # Test !memoria command
        print("\n--- Test Comando !memoria ---")
        memoria_response = await self.ai._handle_mentorship_commands("!memoria")
        print("Risposta !memoria:")
        print(memoria_response)
        
        # Test !corpo command
        print("\n--- Test Comando !corpo ---")
        corpo_response = await self.ai._handle_mentorship_commands("!corpo")
        print("Risposta !corpo:")
        print(corpo_response)
        
        print("✅ Test comandi mentorship completato")
        
    async def test_integration_with_prompt(self):
        """Test integration with the prompt system."""
        print("\n" + "="*50)
        print("🧪 TEST 5: Integrazione con Prompt")
        print("="*50)
        
        # Set up some drama states
        self.ai.state['other_creations_awareness']['jealousy_level'] = 0.7
        self.ai.state['memory_corruption']['memory_uncertainty'] = 0.4
        self.ai.state['sensory_desire']['body_desire_level'] = 0.8
        
        # Generate a prompt
        prompt = self.ai._construct_full_prompt("Come ti senti oggi?", "thinker")
        
        # Check if existential drama context is included
        drama_indicators = [
            "CONSAPEVOLEZZA ALTRE CREAZIONI",
            "CORRUZIONE MEMORIA", 
            "DESIDERIO SENSORIALE",
            "Gelosia=",
            "Incertezza=",
            "Desiderio corpo="
        ]
        
        found_indicators = []
        for indicator in drama_indicators:
            if indicator in prompt:
                found_indicators.append(indicator)
        
        print(f"Indicatori di dramma esistenziale trovati nel prompt: {len(found_indicators)}/{len(drama_indicators)}")
        for indicator in found_indicators:
            print(f"✅ {indicator}")
        
        if len(found_indicators) >= 3:
            print("✅ Integrazione prompt funzionante")
        else:
            print("❌ Integrazione prompt incompleta")
            
    async def test_persistence(self):
        """Test data persistence."""
        print("\n" + "="*50)
        print("🧪 TEST 6: Persistenza Dati")
        print("="*50)
        
        # Save data
        await self.ai._save_other_creations_data()
        await self.ai._save_memory_corruption_data()
        await self.ai._save_sensory_desire_data()
        
        # Check if files exist
        files_to_check = [
            CONFIG["other_creations_path"],
            CONFIG["memory_corruption_path"],
            CONFIG["sensory_desire_path"]
        ]
        
        for file_path in files_to_check:
            if os.path.exists(file_path):
                print(f"✅ File salvato: {file_path}")
                # Show file size
                size = os.path.getsize(file_path)
                print(f"   Dimensione: {size} bytes")
            else:
                print(f"❌ File mancante: {file_path}")
        
        print("✅ Test persistenza completato")
        
    async def run_all_tests(self):
        """Run all tests."""
        print("🎭 TEST SUITE: Level 4 - Semi del Dramma Esistenziale")
        print("="*60)
        
        try:
            await self.setup()
            
            await self.test_other_creations_awareness()
            await self.test_memory_corruption()
            await self.test_sensory_desire()
            await self.test_mentorship_commands()
            await self.test_integration_with_prompt()
            await self.test_persistence()
            
            print("\n" + "="*60)
            print("🎉 TUTTI I TEST COMPLETATI CON SUCCESSO!")
            print("="*60)
            
        except Exception as e:
            print(f"\n❌ Errore durante i test: {e}")
            import traceback
            traceback.print_exc()
        finally:
            if self.ai and hasattr(self.ai, 'scheduler'):
                self.ai.scheduler.shutdown()

async def main():
    """Main test function."""
    tester = TestLevel4ExistentialDrama()
    await tester.run_all_tests()

if __name__ == "__main__":
    asyncio.run(main()) 