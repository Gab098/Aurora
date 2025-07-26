#!/usr/bin/env python3
"""
Aurora Integration Example
==========================

This file demonstrates how to integrate all the new systems:
1. PersonalityManager
2. MemoryManager  
3. AutonomousSystem
4. AuroraDashboard
5. Enhanced Dream System
6. Learning from Choice Results

Usage:
    python aurora_integration_example.py
"""

import asyncio
import threading
from datetime import datetime

# Import the new manager classes
from personality_manager import PersonalityManager
from memory_manager import MemoryManager
from autonomous_system import AutonomousSystem
from aurora_dashboard import create_dashboard

# Import the main Aurora class
from main import MiniAI

class EnhancedAurora(MiniAI):
    """Enhanced Aurora with modular architecture."""
    
    def __init__(self):
        super().__init__()
        
        # Initialize the new manager systems
        self.personality_manager = PersonalityManager(self.config)
        self.memory_manager = MemoryManager(self.config)
        self.autonomous_system = AutonomousSystem(
            self.config, 
            self.personality_manager, 
            self.memory_manager
        )
        
        # Dashboard (optional)
        self.dashboard = None
        
    async def initialize(self):
        """Initialize the enhanced Aurora system."""
        print("🚀 Inizializzazione di Aurora Enhanced...")
        
        # Initialize base Aurora
        await super().initialize()
        
        # Initialize managers
        print("📊 Inizializzazione dei manager...")
        await self.personality_manager.save_state()
        await self.memory_manager.save_memory_box()
        await self.autonomous_system.save_state()
        
        # Start dashboard in separate thread (optional)
        if self.config.get('enable_dashboard', False):
            print("🖥️ Avvio dashboard...")
            self.dashboard = create_dashboard(self)
            dashboard_thread = threading.Thread(target=self.dashboard.run, daemon=True)
            dashboard_thread.start()
        
        print("✅ Aurora Enhanced inizializzata con successo!")
    
    async def process_query(self, user_query):
        """Enhanced query processing with learning integration."""
        # Update personality state
        self.personality_manager.update_activity_time()
        
        # Process query with base Aurora
        response = await super().process_query(user_query)
        
        # Update autonomous system urges
        self.autonomous_system.update_aurora_urges()
        
        # Save states
        await self.personality_manager.save_state()
        await self.autonomous_system.save_state()
        
        return response
    
    def _aurora_makes_choice(self, choice_type, context=None):
        """Enhanced choice making with learning."""
        # Use autonomous system for choice making
        choice_result = self.autonomous_system.aurora_makes_choice(choice_type, context)
        
        # Update personality state based on choice
        if choice_result:
            self.personality_manager.state['energia'] = max(0.0, 
                self.personality_manager.state['energia'] - 0.05)
        
        return choice_result
    
    def _learn_from_choice_result(self, choice_type, was_praised=False, was_corrected=False, topic=None):
        """Enhanced learning from choice results."""
        # Use autonomous system learning
        self.autonomous_system.learn_from_choice_result(choice_type, was_praised, was_corrected, topic)
        
        # Update personality based on feedback
        if was_praised:
            self.personality_manager.apply_praise()
        elif was_corrected:
            self.personality_manager.apply_correction(topic or "")
    
    async def _dream_cycle(self):
        """Enhanced dream cycle with emotional tension analysis."""
        # Use enhanced dream system from main.py
        await super()._dream_cycle()
        
        # Additional dream effects on personality
        if hasattr(self, '_apply_dream_effects'):
            # The dream effects are already applied in the main system
            pass
    
    def get_system_status(self):
        """Get comprehensive system status."""
        return {
            'personality': self.personality_manager.get_state_summary(),
            'memory': self.memory_manager.get_memory_stats(),
            'autonomous': self.autonomous_system.get_autonomous_summary(),
            'base_aurora': {
                'energia': self.state.get('energia', 0.0),
                'stress': self.state.get('stress', 0.0),
                'focus': self.state.get('focus', 0.0),
                'curiosità': self.state.get('curiosità', 0.0)
            }
        }

async def main():
    """Main function to run Aurora Enhanced."""
    print("🌟 Aurora Enhanced - Sistema Modulare Avanzato")
    print("=" * 50)
    
    # Create and initialize Aurora
    aurora = EnhancedAurora()
    await aurora.initialize()
    
    # Example interaction
    print("\n💬 Esempio di interazione:")
    response = await aurora.process_query("Ciao Aurora! Come stai oggi?")
    print(f"Aurora: {response}")
    
    # Show system status
    print("\n📊 Stato del Sistema:")
    status = aurora.get_system_status()
    for system, data in status.items():
        print(f"\n{system.upper()}:")
        for key, value in data.items():
            print(f"  {key}: {value}")
    
    # Example of Aurora making autonomous choices
    print("\n🤖 Scelte Autonome di Aurora:")
    if aurora._aurora_chooses_videogame_creation():
        print("Aurora ha deciso di creare un videogioco!")
        aurora._create_videogame()
    
    if aurora._aurora_chooses_catharsis():
        print("Aurora ha deciso di fare una catarsi creativa!")
        aurora._attempt_creative_catharsis()
    
    # Example of learning from feedback
    print("\n📚 Apprendimento dal Feedback:")
    aurora._learn_from_choice_result("creazione_videogioco", was_praised=True)
    aurora._learn_from_choice_result("catarsi_creativa", was_corrected=True, topic="timing")
    
    # Show updated status
    print("\n📊 Stato Aggiornato:")
    updated_status = aurora.get_system_status()
    print(f"Confidenza Autonomia: {updated_status['autonomous']['autonomy_confidence']:.2f}")
    print(f"Impulsi Creativi: {updated_status['autonomous']['creative_urges']:.2f}")
    
    print("\n✅ Aurora Enhanced funziona perfettamente!")

if __name__ == "__main__":
    asyncio.run(main()) 