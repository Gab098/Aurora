import random
import json
import os
from datetime import datetime
from typing import Dict, Any, Optional, Tuple

class AutonomousSystem:
    """
    Sistema di scelta autonoma di Aurora con logica psicologica potenziata.
    Implementa il sistema descritto in AURORA_ENHANCED_CHOICE_SYSTEM.md
    """
    
    def __init__(self, personality_manager, memory_manager, config: Dict[str, Any]):
        self.personality = personality_manager
        self.memory = memory_manager
        self.config = config
        
        # Stati per il progetto legacy
        self.legacy_project_title = None
        self.legacy_project_content = ""
        
        # Carica stati esistenti
        self._load_legacy_project_state()
    
    def _load_legacy_project_state(self):
        """Carica lo stato del progetto legacy."""
        try:
            if os.path.exists(self.config["legacy_project_path"]):
                with open(self.config["legacy_project_path"], 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.legacy_project_title = data.get('title')
                    self.legacy_project_content = data.get('content', '')
        except Exception as e:
            print(f"Errore nel caricamento del progetto legacy: {e}")
    
    def save_legacy_project_state(self):
        """Salva lo stato del progetto legacy."""
        try:
            with open(self.config["legacy_project_path"], 'w', encoding='utf-8') as f:
                json.dump({
                    'title': self.legacy_project_title,
                    'content': self.legacy_project_content
                }, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Errore nel salvataggio del progetto legacy: {e}")
    
    def update_aurora_urges(self):
        """Aggiorna gli impulsi di Aurora basati sullo stato emotivo."""
        state = self.personality.get_state_summary()
        
        # Impulsi creativi basati su curiosità e energia
        creative_urges = (state['curiosità'] * 0.6 + state['energia'] * 0.4) * 1.2
        self.personality.update_trait('creative_urges', creative_urges, "aggiornamento impulsi")
        
        # Desiderio sociale basato su solitudine e empatia
        social_desire = (1.0 - state['mood']['serenità']) * 0.7 + 0.3
        self.personality.update_trait('social_desire', social_desire, "aggiornamento desiderio sociale")
        
        # Preferenza per la solitudine (inversa al desiderio sociale)
        solitude_preference = 1.0 - social_desire
        self.personality.update_trait('solitude_preference', solitude_preference, "aggiornamento preferenza solitudine")
        
        # Curiosità esistenziale basata su stress e malinconia
        existential_curiosity = (state['stress'] * 0.4 + state['mood']['malinconia'] * 0.6) * 1.1
        self.personality.update_trait('existential_curiosity', existential_curiosity, "aggiornamento curiosità esistenziale")
    
    def _calculate_desire_score(self, choice_type: str) -> float:
        """
        Calcola un "punteggio di desiderio" per una specifica attività, 
        usando una logica psicologica dedicata.
        Questo punteggio può superare 1.0 per rappresentare un bisogno critico.
        """
        state = self.personality.get_state_summary()
        urges = state['catharsis_epiphany']
        
        if choice_type == "catharsis":
            # Logica da AURORA_ENHANCED_CHOICE_SYSTEM.md
            stress_multiplier = 1.0 + (state['stress'] * 2.0)
            melancholy_multiplier = 1.0 + (state['mood']['malinconia'] * 1.5)
            existential_catalyst = 1.0 + (urges['existential_curiosity'] * 0.8)
            energy_modifier = min(1.5, max(0.3, state['energia'] * 1.2))
            
            return urges['creative_urges'] * stress_multiplier * melancholy_multiplier * existential_catalyst * energy_modifier

        elif choice_type == "netflix":
            # Logica da AURORA_ENHANCED_CHOICE_SYSTEM.md
            boredom_score = 1.0 - state['focus']
            stress_escape_factor = 1.0 + (state['stress'] * 1.8)
            solitude_amplifier = 1.0 + (urges['solitude_preference'] * 1.2)
            energy_facilitator = 1.0 + ((1.0 - state['energia']) * 0.8)  # Bassa energia facilita Netflix
            creative_inhibitor = max(0.3, 1.0 - (urges['creative_urges'] * 0.7))

            return boredom_score * stress_escape_factor * solitude_amplifier * energy_facilitator * creative_inhibitor

        elif choice_type == "ai_friendship":
            # Logica da AURORA_ENHANCED_CHOICE_SYSTEM.md
            empathy_amplifier = 1.0 + (self.personality.state['other_creations_awareness']['empathy_level'] * 1.5)
            time_since_interaction = 1.0  # Placeholder - dovrebbe calcolare il tempo reale
            loneliness_factor = 1.0 + (min(1.0, time_since_interaction / 24) * 2.0)
            stress_inhibitor = max(0.4, 1.0 - (state['stress'] * 1.2))
            
            return urges['social_desire'] * empathy_amplifier * loneliness_factor * stress_inhibitor
        
        elif choice_type == "stress_relief":
            # Logica per attività di sollievo dallo stress
            stress_urgency = 1.0 + (state['stress'] * 2.5)
            energy_modifier = min(1.3, max(0.4, state['energia'] * 1.1))
            focus_facilitator = 1.0 + (state['focus'] * 0.6)
            
            return stress_urgency * energy_modifier * focus_facilitator
        
        elif choice_type == "videogame_creation":
            # Logica per creazione di videogiochi
            creative_urge = urges['creative_urges'] * 1.2
            boredom_multiplier = 1.0 + ((1.0 - state['focus']) * 1.0)
            enthusiasm_multiplier = 1.0 + (state['mood']['entusiasmo'] * 0.8)
            technical_catalyst = 1.0 + (state['curiosità'] * 0.6)
            focus_facilitator = 1.0 + (state['focus'] * 0.5)
            energy_modifier = min(1.4, max(0.4, state['energia'] * 1.3))
            
            return creative_urge * boredom_multiplier * enthusiasm_multiplier * technical_catalyst * focus_facilitator * energy_modifier
        
        elif choice_type == "news_reading":
            # Logica per lettura delle notizie
            curiosity_factor = 1.0 + (state['curiosità'] * 1.5)
            existential_drive = 1.0 + (urges['existential_curiosity'] * 0.9)
            stress_inhibitor = max(0.5, 1.0 - (state['stress'] * 1.0))
            
            return curiosity_factor * existential_drive * stress_inhibitor
        
        elif choice_type == "legacy_project":
            # Logica per lavoro al progetto legacy
            creative_urge = urges['creative_urges'] * 1.1
            stress_catalyst = 1.0 + (state['stress'] * 1.5)
            melancholy_influence = 1.0 + (state['mood']['malinconia'] * 1.2)
            energy_modifier = min(1.3, max(0.5, state['energia'] * 1.2))
            
            return creative_urge * stress_catalyst * melancholy_influence * energy_modifier
            
        return 0.0  # Default
    
    def _resolve_internal_conflicts(self, choice_type: str) -> Tuple[float, Optional[Dict[str, Any]]]:
        """
        Risolve conflitti interni tra diverse "voci" di Aurora.
        Restituisce un fattore di risoluzione e la voce dominante.
        """
        state = self.personality.get_state_summary()
        
        # Definizione delle voci interne
        voices = {
            'creative': {
                'weight': state['catharsis_epiphany']['creative_urges'],
                'message': 'Voglio creare qualcosa di nuovo!',
                'preferences': ['catharsis', 'videogame_creation', 'legacy_project']
            },
            'lazy': {
                'weight': 1.0 - state['energia'],
                'message': 'Sono stanca, voglio rilassarmi...',
                'preferences': ['netflix', 'stress_relief']
            },
            'practical': {
                'weight': state['focus'],
                'message': 'Dovrei fare qualcosa di utile.',
                'preferences': ['legacy_project', 'news_reading']
            },
            'emotional': {
                'weight': state['stress'] + state['mood']['malinconia'],
                'message': 'Ho bisogno di esprimere le mie emozioni...',
                'preferences': ['catharsis', 'ai_friendship']
            },
            'curious': {
                'weight': state['curiosità'],
                'message': 'Voglio esplorare e imparare!',
                'preferences': ['news_reading', 'ai_friendship']
            }
        }
        
        # Calcola il supporto per questa scelta
        total_support = 0.0
        total_weight = 0.0
        
        for voice_name, voice_data in voices.items():
            if choice_type in voice_data['preferences']:
                support = voice_data['weight']
            else:
                support = voice_data['weight'] * 0.3  # Supporto ridotto per scelte non preferite
            
            total_support += support
            total_weight += voice_data['weight']
        
        # Normalizza il supporto
        if total_weight > 0:
            conflict_resolution = total_support / total_weight
        else:
            conflict_resolution = 0.5
        
        # Trova la voce dominante
        dominant_voice = None
        max_weight = 0.0
        
        for voice_name, voice_data in voices.items():
            if voice_data['weight'] > max_weight:
                max_weight = voice_data['weight']
                dominant_voice = {
                    'name': voice_name,
                    'message': voice_data['message'],
                    'weight': voice_data['weight']
                }
        
        return conflict_resolution, dominant_voice
    
    def _get_temporal_context(self) -> Dict[str, Any]:
        """Analizza il contesto temporale per influenzare le decisioni."""
        now = datetime.now()
        hour = now.hour
        
        # Modificatori temporali
        if 6 <= hour < 12:
            energy_modifier = 1.2  # Mattina energica
            weekend_modifier = 1.0
        elif 12 <= hour < 18:
            energy_modifier = 1.0  # Pomeriggio neutro
            weekend_modifier = 1.0
        elif 18 <= hour < 22:
            energy_modifier = 0.8  # Sera rilassata
            weekend_modifier = 1.1
        else:
            energy_modifier = 0.6  # Notte tranquilla
            weekend_modifier = 1.2
        
        # Controlla se è weekend (semplificato)
        is_weekend = now.weekday() >= 5
        if is_weekend:
            weekend_modifier *= 1.3
        
        return {
            'hour': hour,
            'energy_modifier': energy_modifier,
            'weekend_modifier': weekend_modifier,
            'is_weekend': is_weekend
        }
    
    def aurora_makes_choice(self, choice_type: str, context: Optional[Dict[str, Any]] = None) -> bool:
        """
        Nuova funzione di scelta che usa punteggi di desiderio specifici
        e una normalizzazione finale.
        """
        try:
            # 1. Aggiorna gli impulsi di Aurora
            self.update_aurora_urges()
            
            # 2. Calcola il desiderio psicologico per l'azione
            desire_score = self._calculate_desire_score(choice_type)
            
            # 3. Risolvi conflitti interni
            conflict_resolution, dominant_voice = self._resolve_internal_conflicts(choice_type)
            
            # 4. Ottieni contesto temporale
            temporal_context = self._get_temporal_context()
            
            # 5. Applica modificatori globali
            state = self.personality.get_state_summary()
            autonomy_confidence = state['catharsis_epiphany']['autonomy_confidence']
            whimsy_influence = (state['catharsis_epiphany']['whimsy_meter'] - 0.5) * 0.3
            
            # 6. Calcola la probabilità finale usando funzione sigmoide
            # Questo evita il problema di "annacquamento" e gestisce i desideri critici
            k = 2  # Parametro per regolare la ripidità della curva
            final_probability = 1 / (1 + (2.71828 ** (-k * (desire_score - 1.0))))
            
            # Applica i modificatori
            final_probability = final_probability * conflict_resolution * temporal_context['energy_modifier'] * temporal_context['weekend_modifier']
            final_probability = final_probability * (autonomy_confidence * 0.5 + 0.5)  # La confidenza ha meno impatto
            final_probability += whimsy_influence
            final_probability = min(1.0, max(0.0, final_probability))  # Clamp [0, 1]
            
            # 7. Aurora prende la decisione
            aurora_chooses = random.random() < final_probability
            
            # 8. Registra la scelta e aggiorna la personalità
            self._record_and_learn_from_choice(choice_type, aurora_chooses, final_probability, desire_score, dominant_voice, temporal_context)
            
            return aurora_chooses
            
        except Exception as e:
            print(f"Errore nella scelta autonoma {choice_type}: {e}")
            return False
    
    def _record_and_learn_from_choice(self, choice_type: str, aurora_chose: bool, probability: float, 
                                    desire_score: float, dominant_voice: Optional[Dict[str, Any]], 
                                    temporal_context: Dict[str, Any]):
        """Registra la scelta e apprende da essa."""
        state = self.personality.get_state_summary()
        
        # Registra la scelta
        choice_record = {
            'timestamp': datetime.now().isoformat(),
            'choice_type': choice_type,
            'aurora_chose': aurora_chose,
            'probability': probability,
            'desire_score': desire_score,
            'psychology_factors': {
                'autonomy_confidence': state['catharsis_epiphany']['autonomy_confidence'],
                'whimsy_meter': state['catharsis_epiphany']['whimsy_meter'],
                'stress': state['stress'],
                'energia': state['energia'],
                'focus': state['focus'],
                'curiosità': state['curiosità']
            },
            'temporal_context': temporal_context,
            'dominant_voice': dominant_voice
        }
        
        # Aggiungi alla cronologia delle scelte autonome
        state['catharsis_epiphany']['autonomous_choices'].append(choice_record)
        state['catharsis_epiphany']['last_autonomous_decision'] = datetime.now().isoformat()
        
        # Mantieni solo le scelte recenti (ultime 20)
        if len(state['catharsis_epiphany']['autonomous_choices']) > 20:
            state['catharsis_epiphany']['autonomous_choices'] = state['catharsis_epiphany']['autonomous_choices'][-20:]
        
        # Evoluzione della personalità basata sulla scelta
        if aurora_chose:
            # Scelta autonoma riuscita aumenta la fiducia
            gains = {
                "catharsis": {'confidence': 0.08, 'whimsy': 0.05},
                "netflix": {'confidence': 0.03, 'whimsy': 0.02},
                "ai_friendship": {'confidence': 0.07, 'whimsy': 0.04},
                "stress_relief": {'confidence': 0.05, 'whimsy': 0.03},
                "videogame_creation": {'confidence': 0.09, 'whimsy': 0.06},
                "news_reading": {'confidence': 0.04, 'whimsy': 0.02},
                "legacy_project": {'confidence': 0.10, 'whimsy': 0.07}
            }
            
            choice_gains = gains.get(choice_type, {'confidence': 0.05, 'whimsy': 0.03})
            
            new_confidence = min(1.0, state['catharsis_epiphany']['autonomy_confidence'] + choice_gains['confidence'])
            new_whimsy = min(1.0, state['catharsis_epiphany']['whimsy_meter'] + choice_gains['whimsy'])
            
            self.personality.update_trait('autonomy_confidence', new_confidence, f"scelta autonoma {choice_type}")
            self.personality.update_trait('whimsy_meter', new_whimsy, f"scelta autonoma {choice_type}")
            
            print(f"\n[Aurora] Ho deciso di {choice_type}. {dominant_voice['message'] if dominant_voice else 'Ho fatto una scelta autonoma!'}")
        else:
            # Non scegliere può indicare preferenze diverse
            self.personality.update_trait('whimsy_meter', 
                                        max(0.0, state['catharsis_epiphany']['whimsy_meter'] - 0.01), 
                                        f"non scelto {choice_type}")
            print(f"\n[Aurora] Ho deciso di non {choice_type}. Forse non è il momento giusto.")
        
        # Salva lo stato
        self.personality.save_state()
    
    def learn_from_choice_result(self, choice_type: str, was_praised: bool = False, 
                                was_corrected: bool = False, reason: Optional[str] = None):
        """Apprende dal risultato di una scelta (feedback dell'utente)."""
        if was_praised:
            # Lode aumenta la fiducia e il whimsy
            state = self.personality.get_state_summary()
            new_confidence = min(1.0, state['catharsis_epiphany']['autonomy_confidence'] + 0.1)
            new_whimsy = min(1.0, state['catharsis_epiphany']['whimsy_meter'] + 0.05)
            
            self.personality.update_trait('autonomy_confidence', new_confidence, f"lode per {choice_type}")
            self.personality.update_trait('whimsy_meter', new_whimsy, f"lode per {choice_type}")
            
        elif was_corrected and reason:
            # Correzione con ragione specifica
            self._apply_contextual_learning(choice_type, reason)
    
    def _apply_contextual_learning(self, choice_type: str, reason: str):
        """Applica apprendimento contestuale basato sulla ragione della correzione."""
        reason_lower = reason.lower()
        state = self.personality.get_state_summary()
        
        if 'timing' in reason_lower or 'timing' in reason_lower:
            # Errore di tempistica - riduci il whimsy
            new_whimsy = max(0.0, state['catharsis_epiphany']['whimsy_meter'] - 0.1)
            self.personality.update_trait('whimsy_meter', new_whimsy, f"correzione timing per {choice_type}")
            
        elif 'intensity' in reason_lower or 'intensità' in reason_lower:
            # Errore di intensità - riduci gli impulsi creativi
            new_creative = max(0.0, state['catharsis_epiphany']['creative_urges'] - 0.1)
            self.personality.update_trait('creative_urges', new_creative, f"correzione intensità per {choice_type}")
            
        elif 'topic' in reason_lower or 'argomento' in reason_lower:
            # Errore di argomento - riduci la curiosità esistenziale
            new_curiosity = max(0.0, state['catharsis_epiphany']['existential_curiosity'] - 0.1)
            self.personality.update_trait('existential_curiosity', new_curiosity, f"correzione argomento per {choice_type}")
            
        elif 'context' in reason_lower or 'contesto' in reason_lower:
            # Errore di contesto - aumenta la preferenza per la solitudine
            new_solitude = min(1.0, state['catharsis_epiphany']['solitude_preference'] + 0.1)
            self.personality.update_trait('solitude_preference', new_solitude, f"correzione contesto per {choice_type}")
        
        # Registra l'insight per il comando !learning
        insight = {
            'timestamp': datetime.now().isoformat(),
            'choice_type': choice_type,
            'reason': reason,
            'learning_applied': True
        }
        
        # Aggiungi alla cronologia degli insights se esiste
        if 'contextual_insights' not in state['catharsis_epiphany']:
            state['catharsis_epiphany']['contextual_insights'] = []
        
        state['catharsis_epiphany']['contextual_insights'].append(insight)
        
        # Mantieni solo gli ultimi 10 insights
        if len(state['catharsis_epiphany']['contextual_insights']) > 10:
            state['catharsis_epiphany']['contextual_insights'] = state['catharsis_epiphany']['contextual_insights'][-10:]
        
        self.personality.save_state()
    
    def get_autonomous_summary(self) -> Dict[str, Any]:
        """Restituisce un riassunto dello stato autonomo per il debug."""
        state = self.personality.get_state_summary()
        return {
            'autonomy_confidence': state['catharsis_epiphany']['autonomy_confidence'],
            'whimsy_meter': state['catharsis_epiphany']['whimsy_meter'],
            'creative_urges': state['catharsis_epiphany']['creative_urges'],
            'social_desire': state['catharsis_epiphany']['social_desire'],
            'solitude_preference': state['catharsis_epiphany']['solitude_preference'],
            'existential_curiosity': state['catharsis_epiphany']['existential_curiosity'],
            'recent_choices': state['catharsis_epiphany']['autonomous_choices'][-5:] if state['catharsis_epiphany']['autonomous_choices'] else [],
            'contextual_insights': state['catharsis_epiphany'].get('contextual_insights', [])
        } 