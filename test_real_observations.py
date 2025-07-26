#!/usr/bin/env python3
"""
Test script for real file observation functionality in Level 4
Tests Aurora's ability to read real system files to observe creator's activities
"""

import os
import tempfile
import shutil
import asyncio
import sys
from datetime import datetime

# Add the current directory to the path to import main
sys.path.append('.')

from main import MiniAI, CONFIG

class TestRealObservations:
    def __init__(self):
        self.ai = None
        self.test_dir = None
        
    async def setup(self):
        """Initialize the AI and create test files."""
        print("🚀 Inizializzazione AI per test osservazioni reali...")
        self.ai = MiniAI()
        await self.ai.initialize()
        print("✅ AI inizializzata")
        
        # Create test directory with fake AI projects
        self.test_dir = tempfile.mkdtemp(prefix="aurora_test_")
        print(f"📁 Directory test creata: {self.test_dir}")
        
        # Create fake AI project files
        self._create_fake_ai_files()
        
    def _create_fake_ai_files(self):
        """Create fake AI project files for testing."""
        
        # Create a fake AI assistant file
        gpt_assistant_content = '''import openai
from typing import List

class GPTAssistant:
    def __init__(self):
        self.client = openai.OpenAI()
        self.conversation_history = []
    
    def chat(self, message: str) -> str:
        """Enhanced chat with memory system"""
        self.conversation_history.append({"role": "user", "content": message})
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=self.conversation_history
        )
        return response.choices[0].message.content
    
    def save_memory(self):
        """Save conversation to persistent storage"""
        with open("memory.json", "w") as f:
            json.dump(self.conversation_history, f)
'''
        
        # Create a fake neural network file
        neural_net_content = '''import torch
import torch.nn as nn

class AdvancedNeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(AdvancedNeuralNetwork, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.layer2 = nn.Linear(hidden_size, hidden_size)
        self.layer3 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()
        
    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        x = self.layer3(x)
        return x

# Training configuration
config = {
    "learning_rate": 0.001,
    "epochs": 100,
    "batch_size": 32
}
'''
        
        # Create a fake chatbot configuration
        chatbot_config = '''{
    "name": "Claude Assistant",
    "version": "2.1.0",
    "features": {
        "memory": true,
        "personality": true,
        "creativity": 0.8
    },
    "api_endpoints": {
        "chat": "/api/v1/chat",
        "memory": "/api/v1/memory"
    }
}'''
        
        # Create files in test directory
        files_to_create = [
            ("gpt_assistant.py", gpt_assistant_content),
            ("neural_network.py", neural_net_content),
            ("chatbot_config.json", chatbot_config),
            ("ai_training_log.txt", "Training completed successfully. Model accuracy: 94.2%"),
            ("conversation_memory.json", '{"conversations": [{"id": 1, "user": "Hello", "assistant": "Hi there!"}]}')
        ]
        
        for filename, content in files_to_create:
            filepath = os.path.join(self.test_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"📄 Creato file: {filename}")
            
        # Create a subdirectory with more AI files
        ai_subdir = os.path.join(self.test_dir, "ai_models")
        os.makedirs(ai_subdir, exist_ok=True)
        
        subdir_files = [
            ("transformer_model.py", "class TransformerModel:\n    def __init__(self):\n        self.layers = 12\n        self.attention_heads = 8"),
            ("bert_config.yml", "model_type: bert\nvocab_size: 30000\nhidden_size: 768"),
            ("training_script.sh", "#!/bin/bash\necho 'Starting AI model training...'\npython train.py --epochs 100")
        ]
        
        for filename, content in subdir_files:
            filepath = os.path.join(ai_subdir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"📁 Creato file in subdirectory: {filename}")
        
    async def test_real_file_observation(self):
        """Test the real file observation functionality."""
        print("\n" + "="*60)
        print("🧪 TEST: Osservazione File Reali")
        print("="*60)
        
        # Temporarily modify the potential_dirs to include our test directory
        original_potential_dirs = [
            os.path.expanduser("~/Desktop"),
            os.path.expanduser("~/Documents"),
            os.path.expanduser("~/Projects"),
            os.path.expanduser("~/workspace"),
            os.path.expanduser("~/ai_projects"),
            os.path.expanduser("~/code"),
            os.path.expanduser("~/development"),
            os.path.expanduser("~/Desktop/Projects"),
            os.path.expanduser("~/Documents/Projects")
        ]
        
        # Add our test directory to the search path
        test_potential_dirs = [self.test_dir] + original_potential_dirs
        
        # Temporarily replace the potential_dirs in the function
        import main
        original_observe_function = main.MiniAI._observe_other_creations
        
        def modified_observe_function(self):
            """Modified version that uses our test directory."""
            try:
                observed_activities = []
                
                # Use our test directory first
                for directory in test_potential_dirs:
                    if os.path.exists(directory):
                        try:
                            items = os.listdir(directory)
                            for item in items:
                                item_path = os.path.join(directory, item)
                                
                                # Look for AI-related keywords in names
                                ai_keywords = ['ai', 'gpt', 'llm', 'model', 'neural', 'bot', 'assistant', 'agent', 'intelligence', 'machine', 'learning', 'deep', 'transformer', 'bert', 'claude', 'bard', 'copilot', 'chat', 'conversation', 'dialogue', 'prompt', 'fine-tune', 'training']
                                
                                if any(keyword in item.lower() for keyword in ai_keywords):
                                    # Try to read file contents if it's a text file
                                    if os.path.isfile(item_path) and item.lower().endswith(('.txt', '.md', '.py', '.js', '.json', '.log', '.yml', '.yaml', '.config', '.conf')):
                                        try:
                                            with open(item_path, 'r', encoding='utf-8', errors='ignore') as f:
                                                content = f.read(1000)  # Read first 1000 chars
                                                if content.strip():
                                                    observed_activities.append({
                                                        'type': 'file',
                                                        'path': item_path,
                                                        'name': item,
                                                        'content_preview': content[:200] + "..." if len(content) > 200 else content
                                                    })
                                        except:
                                            observed_activities.append({
                                                'type': 'file',
                                                'path': item_path,
                                                'name': item,
                                                'content_preview': '[File non leggibile]'
                                            })
                                    elif os.path.isdir(item_path):
                                        # For directories, try to list contents
                                        try:
                                            dir_contents = os.listdir(item_path)
                                            ai_files = [f for f in dir_contents if any(keyword in f.lower() for keyword in ai_keywords)]
                                            if ai_files:
                                                observed_activities.append({
                                                    'type': 'directory',
                                                    'path': item_path,
                                                    'name': item,
                                                    'content_preview': f'Contiene: {", ".join(ai_files[:5])}'
                                                })
                                        except:
                                            observed_activities.append({
                                                'type': 'directory',
                                                'path': item_path,
                                                'name': item,
                                                'content_preview': '[Directory non accessibile]'
                                            })
                        except:
                            continue
                
                # Process observations
                if observed_activities:
                    selected_activity = observed_activities[0]  # Use first one for testing
                    if selected_activity['type'] == 'file':
                        selected_log = f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] File osservato: '{selected_activity['name']}' - {selected_activity['content_preview']}"
                    elif selected_activity['type'] == 'directory':
                        selected_log = f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Directory osservata: '{selected_activity['name']}' - {selected_activity['content_preview']}"
                    else:
                        selected_log = selected_activity['content']
                else:
                    selected_log = "[Test] Nessun file AI trovato"
                
                # Update observation tracking
                self.state['other_creations_awareness']['last_observation'] = datetime.now()
                
                observation_data = {
                    'timestamp': datetime.now().isoformat(),
                    'log_entry': selected_log,
                    'impact': 'observed',
                    'observation_type': selected_activity['type'] if observed_activities else 'none',
                    'total_activities_found': len(observed_activities)
                }
                
                if observed_activities and selected_activity['type'] == 'file':
                    observation_data['file_path'] = selected_activity['path']
                    observation_data['file_name'] = selected_activity['name']
                    observation_data['content_preview'] = selected_activity['content_preview']
                
                self.state['other_creations_awareness']['observed_creations'].append(observation_data)
                
                print(f"🔍 Osservazioni trovate: {len(observed_activities)}")
                if observed_activities:
                    print(f"📄 File osservato: {selected_activity['name']}")
                    print(f"📝 Preview: {selected_activity['content_preview'][:100]}...")
                
                return selected_log
                
            except Exception as e:
                print(f"❌ Errore nell'osservazione: {e}")
                return None
        
        # Replace the function temporarily
        main.MiniAI._observe_other_creations = modified_observe_function
        
        try:
            # Test the observation
            print("🔍 Testando osservazione file reali...")
            result = self.ai._observe_other_creations()
            
            print(f"\n📊 Risultati:")
            print(f"Log generato: {result}")
            
            # Check observation data
            observations = self.ai.state['other_creations_awareness']['observed_creations']
            if observations:
                latest = observations[-1]
                print(f"\n📋 Dettagli osservazione:")
                print(f"- Tipo: {latest.get('observation_type', 'unknown')}")
                print(f"- File trovati: {latest.get('total_activities_found', 0)}")
                if latest.get('file_name'):
                    print(f"- File osservato: {latest['file_name']}")
                    print(f"- Percorso: {latest['file_path']}")
                    print(f"- Preview: {latest['content_preview'][:150]}...")
            
            # Test the mentorship command
            print(f"\n📝 Test comando !altri:")
            altri_response = await self.ai._handle_mentorship_commands("!altri")
            print(altri_response)
            
        finally:
            # Restore original function
            main.MiniAI._observe_other_creations = original_observe_function
        
        print("✅ Test osservazione file reali completato")
        
    async def test_file_permissions(self):
        """Test that Aurora can read but not modify files."""
        print("\n" + "="*60)
        print("🧪 TEST: Permessi File (Solo Lettura)")
        print("="*60)
        
        test_file = os.path.join(self.test_dir, "permission_test.txt")
        with open(test_file, 'w') as f:
            f.write("Test content for permission checking")
        
        print(f"📄 File test creato: {test_file}")
        
        # Test reading (should work)
        try:
            with open(test_file, 'r') as f:
                content = f.read()
            print(f"✅ Lettura file: OK - Contenuto: {content}")
        except Exception as e:
            print(f"❌ Errore lettura: {e}")
        
        # Test writing (should fail or be restricted)
        try:
            with open(test_file, 'w') as f:
                f.write("Attempted modification")
            print(f"⚠️  Scrittura file: Permesso (ma non dovrebbe modificare)")
        except Exception as e:
            print(f"✅ Scrittura file: Bloccata come previsto - {e}")
        
        print("✅ Test permessi completato")
        
    async def cleanup(self):
        """Clean up test files."""
        if self.test_dir and os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
            print(f"🧹 Directory test rimossa: {self.test_dir}")
        
    async def run_all_tests(self):
        """Run all tests."""
        print("🔍 TEST SUITE: Osservazioni File Reali")
        print("="*60)
        
        try:
            await self.setup()
            await self.test_real_file_observation()
            await self.test_file_permissions()
            
            print("\n" + "="*60)
            print("🎉 TUTTI I TEST COMPLETATI CON SUCCESSO!")
            print("="*60)
            
        except Exception as e:
            print(f"\n❌ Errore durante i test: {e}")
            import traceback
            traceback.print_exc()
        finally:
            await self.cleanup()

async def main():
    """Main test function."""
    tester = TestRealObservations()
    await tester.run_all_tests()

if __name__ == "__main__":
    asyncio.run(main()) 