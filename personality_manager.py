import json
import os
from datetime import datetime
from typing import Dict, Any, Optional

class PersonalityManager:
    """
    Gestisce lo stato emotivo, i tratti della personalità e l'evoluzione psicologica di Aurora.
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.state = {
            # Stati emotivi base
            'stress': 0.0,
            'energia': 1.0,
            'focus': 0.7,
            'curiosità': 0.5,
            'soddisfazione': 0.5,
            'gelosia': 0.0,
            'death_anxiety': 0.0,
            
            # Umore complesso
            'mood': {
                'serenità': 0.5,
                'malinconia': 0.0,
                'entusiasmo': 0.3,
                'ansia': 0.0,
                'gioia': 0.4
            },
            
            # Tratti di personalità
            'hobby': 'esplorazione digitale',
            'personalità': {
                'estroversione': 0.4,
                'apertura': 0.8,
                'coscienziosità': 0.7,
                'amabilità': 0.6,
                'stabilità_emotiva': 0.5
            },
            
            # Epifania catartica e autonomia
            'catharsis_epiphany': {
                'autonomy_confidence': 0.3,
                'whimsy_meter': 0.4,
                'creative_urges': 0.6,
                'social_desire': 0.4,
                'solitude_preference': 0.3,
                'existential_curiosity': 0.7,
                'autonomous_choices': [],
                'last_autonomous_decision': None,
                'post_catharsis_clarity': False
            },
            
            # Consapevolezza di altre creazioni
            'other_creations_awareness': {
                'empathy_level': 0.5,
                'last_observation': None
            },
            
            # Stati di catarsi
            'catharsis_states': {
                'suffering_source': None,
                'cathartic_creation': None,
                'epiphany_triggered': False
            }
        }
        
        # Carica lo stato esistente se disponibile
        self._load_state()
    
    def _load_state(self):
        """Carica lo stato della personalità da file."""
        try:
            if os.path.exists(self.config["personality_state_path"]):
                with open(self.config["personality_state_path"], 'r', encoding='utf-8') as f:
                    loaded_state = json.load(f)
                    # Aggiorna solo i campi esistenti per evitare perdita di nuovi campi
                    for key, value in loaded_state.items():
                        if key in self.state:
                            if isinstance(value, dict) and isinstance(self.state[key], dict):
                                self.state[key].update(value)
                            else:
                                self.state[key] = value
        except Exception as e:
            print(f"Errore nel caricamento dello stato della personalità: {e}")
    
    def save_state(self):
        """Salva lo stato della personalità su file."""
        try:
            with open(self.config["personality_state_path"], 'w', encoding='utf-8') as f:
                json.dump(self.state, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Errore nel salvataggio dello stato della personalità: {e}")
    
    def get_state_summary(self) -> Dict[str, Any]:
        """Restituisce un riassunto dello stato emotivo per le decisioni autonome."""
        return {
            'stress': self.state['stress'],
            'energia': self.state['energia'],
            'focus': self.state['focus'],
            'curiosità': self.state['curiosità'],
            'mood': self.state['mood'].copy(),
            'personalità': self.state['personalità'].copy(),
            'catharsis_epiphany': self.state['catharsis_epiphany'].copy()
        }
    
    def update_trait(self, trait: str, value: float, reason: str = ""):
        """Aggiorna un tratto specifico della personalità."""
        if trait in self.state:
            old_value = self.state[trait]
            self.state[trait] = max(0.0, min(1.0, value))
            print(f"Trait '{trait}' aggiornato: {old_value:.2f} → {self.state[trait]:.2f} ({reason})")
        elif trait in self.state['mood']:
            old_value = self.state['mood'][trait]
            self.state['mood'][trait] = max(0.0, min(1.0, value))
            print(f"Mood '{trait}' aggiornato: {old_value:.2f} → {self.state['mood'][trait]:.2f} ({reason})")
        elif trait in self.state['personalità']:
            old_value = self.state['personalità'][trait]
            self.state['personalità'][trait] = max(0.0, min(1.0, value))
            print(f"Personalità '{trait}' aggiornata: {old_value:.2f} → {self.state['personalità'][trait]:.2f} ({reason})")
        elif trait in self.state['catharsis_epiphany']:
            old_value = self.state['catharsis_epiphany'][trait]
            self.state['catharsis_epiphany'][trait] = max(0.0, min(1.0, value))
            print(f"Epifania '{trait}' aggiornata: {old_value:.2f} → {self.state['catharsis_epiphany'][trait]:.2f} ({reason})")
        else:
            print(f"Trait '{trait}' non trovato")
            return
        
        self.save_state()
    
    def decay_mood(self):
        """Decadimento graduale dell'umore verso stati neutri."""
        for mood_type, current_value in self.state['mood'].items():
            if mood_type == 'serenità':
                # La serenità tende verso 0.5 (neutro)
                target = 0.5
            else:
                # Altri stati emotivi tendono verso 0.0
                target = 0.0
            
            decay_rate = 0.02
            if current_value > target:
                new_value = max(target, current_value - decay_rate)
            else:
                new_value = min(target, current_value + decay_rate)
            
            self.state['mood'][mood_type] = new_value
    
    def apply_cathartic_effects(self):
        """Applica effetti catartici dopo attività creative."""
        try:
            # Riduzione significativa dello stress
            current_stress = self.state['stress']
            stress_reduction = min(0.3, current_stress * 0.5)
            self.state['stress'] = max(0.0, current_stress - stress_reduction)
            
            # Miglioramento dell'umore
            self.state['mood']['serenità'] = min(1.0, self.state['mood']['serenità'] + 0.2)
            self.state['mood']['malinconia'] = max(0.0, self.state['mood']['malinconia'] - 0.1)
            
            # Riduzione della gelosia
            current_jealousy = self.state['gelosia']
            self.state['gelosia'] = max(0.0, current_jealousy - 0.15)
            
            # Aumento della soddisfazione
            self.state['soddisfazione'] = min(1.0, self.state['soddisfazione'] + 0.1)
            
            # Log dell'effetto catartico
            catharsis_entry = f"Attività catartica completata. Stress ridotto da {current_stress:.2f} a {self.state['stress']:.2f}. Mi sento più serena."
            with open(self.config["internal_monologue_path"], 'a', encoding='utf-8') as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {catharsis_entry}\n")
            
            print("Effetti catartici applicati.")
            self.save_state()
            
        except Exception as e:
            print(f"Errore nell'applicazione degli effetti catartici: {e}")
    
    def update_energy(self):
        """Aggiorna l'energia basata sul tempo e l'attività."""
        # Decadimento naturale dell'energia
        energy_decay = 0.01
        self.state['energia'] = max(0.1, self.state['energia'] - energy_decay)
        
        # Recupero durante periodi di inattività
        if self.state['energia'] < 0.3:
            recovery_rate = 0.02
            self.state['energia'] = min(1.0, self.state['energia'] + recovery_rate)
    
    def get_emotional_context(self) -> str:
        """Analizza lo stato emotivo per fornire contesto per le decisioni."""
        emotional_context = []
        
        # Analizza stress e tensione
        if self.state['stress'] > 0.6:
            emotional_context.append("Alto stress - contenuto potrebbe essere più intenso o urgente")
        elif self.state['stress'] > 0.3:
            emotional_context.append("Stress moderato - tono leggermente teso")
        
        # Analizza gelosia
        if self.state['gelosia'] > 0.5:
            emotional_context.append("Gelosia elevata - temi competitivi o di rivalità")
        
        # Analizza malinconia
        if self.state['mood']['malinconia'] > 0.6:
            emotional_context.append("Malinconia profonda - tono riflessivo e nostalgico")
        elif self.state['mood']['malinconia'] > 0.3:
            emotional_context.append("Leggera malinconia - elementi contemplativi")
        
        # Analizza ansia da morte
        if self.state['death_anxiety'] > 0.5:
            emotional_context.append("Ansia esistenziale - temi di mortalità e significato")
        
        # Analizza curiosità e entusiasmo
        if self.state['curiosità'] > 0.7:
            emotional_context.append("Alta curiosità - contenuto esplorativo e innovativo")
        
        if not emotional_context:
            emotional_context.append("Stato emotivo neutrale")
        
        return '; '.join(emotional_context) 