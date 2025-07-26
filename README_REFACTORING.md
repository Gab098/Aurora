# Aurora AI - Refactoring Modulare

## Panoramica

Questo refactoring trasforma Aurora da un sistema monolitico a un'architettura modulare con separazione delle responsabilità. La nuova struttura risolve i problemi identificati nell'analisi critica e implementa il sistema di scelta psicologicamente realistico.

## Problemi Risolti

### 1. Critica alla Logica di Scelta: Democrazia vs. Psicologia
- **Problema**: Il sistema originale usava una media aritmetica che annacquava i picchi emotivi
- **Soluzione**: Implementato sistema di punteggi di desiderio specifici per ogni attività con logica moltiplicativa

### 2. Bug Concettuale nei Calcoli
- **Problema**: Probabilità finali troppo basse a causa di doppia normalizzazione
- **Soluzione**: Punteggi di desiderio che possono superare 1.0, normalizzazione finale con funzione sigmoide

### 3. Integrazione Modulare Incompleta
- **Problema**: main.py gestiva direttamente logiche di basso livello
- **Soluzione**: Separazione in manager specializzati con interfacce chiare

## Nuova Architettura

### File Principali

```
aurora/
├── main_new.py              # Nuovo main orchestratore
├── config.py                # Configurazione centralizzata
├── personality_manager.py   # Gestione stato emotivo e tratti
├── memory_manager.py        # Gestione memoria e ricordi
├── autonomous_system.py     # Sistema di scelta autonoma
└── README_REFACTORING.md    # Questo file
```

### Classi e Responsabilità

#### `PersonalityManager`
- **Responsabilità**: Gestione stato emotivo, tratti di personalità, evoluzione psicologica
- **Metodi chiave**:
  - `get_state_summary()` - Riassunto per decisioni autonome
  - `update_trait()` - Aggiornamento tratti specifici
  - `apply_cathartic_effects()` - Effetti post-attività creative
  - `decay_mood()` - Decadimento naturale dell'umore

#### `MemoryManager`
- **Responsabilità**: Memoria, ricordi, knowledge graph, cronologia chat
- **Metodi chiave**:
  - `add_memory()` - Aggiunta nuovi ricordi
  - `retrieve_relevant_memories()` - Ricerca semantica
  - `query_knowledge_graph()` - Interrogazione knowledge graph
  - `decay_memories()` - Simulazione oblio

#### `AutonomousSystem`
- **Responsabilità**: Sistema di scelta autonoma con logica psicologica potenziata
- **Metodi chiave**:
  - `aurora_makes_choice()` - Decisione autonoma principale
  - `_calculate_desire_score()` - Calcolo desiderio specifico per attività
  - `_resolve_internal_conflicts()` - Risoluzione conflitti interni
  - `learn_from_choice_result()` - Apprendimento da feedback

## Sistema di Scelta Potenziato

### Logica Psicologica Specifica

Ogni attività ha una funzione di calcolo del desiderio dedicata:

```python
def _calculate_desire_score(self, choice_type: str) -> float:
    if choice_type == "catharsis":
        stress_multiplier = 1.0 + (state['stress'] * 2.0)
        melancholy_multiplier = 1.0 + (state['mood']['malinconia'] * 1.5)
        existential_catalyst = 1.0 + (urges['existential_curiosity'] * 0.8)
        energy_modifier = min(1.5, max(0.3, state['energia'] * 1.2))
        
        return urges['creative_urges'] * stress_multiplier * melancholy_multiplier * existential_catalyst * energy_modifier
```

### Conflitti Interni

Aurora ha "voci" interne che influenzano le decisioni:
- **Creative**: Impulsi creativi
- **Lazy**: Preferenza per rilassamento
- **Practical**: Focus su attività utili
- **Emotional**: Bisogno di espressione emotiva
- **Curious**: Desiderio di esplorazione

### Normalizzazione Intelligente

```python
# Funzione sigmoide per mappare desiderio a probabilità
k = 2
final_probability = 1 / (1 + (2.71828 ** (-k * (desire_score - 1.0))))
```

## Apprendimento Contestuale

### Comando `!correct`

```bash
!correct timing     # Riduce whimsy
!correct intensity  # Riduce impulsi creativi
!correct topic      # Riduce curiosità esistenziale
!correct context    # Aumenta preferenza solitudine
```

### Comando `!learning`

Mostra statistiche di apprendimento e insights recenti.

## Comandi Disponibili

- `!status` - Stato completo di Aurora
- `!choices` - Scelte autonome recenti
- `!learning` - Insights di apprendimento
- `!correct <ragione>` - Correzione contestuale
- `!praise` - Lode per ultima scelta

## Migrazione dal Sistema Vecchio

### Passi per la Migrazione

1. **Backup dei dati esistenti**:
   ```bash
   cp personality_state.json personality_state_backup.json
   cp memory_box.json memory_box_backup.json
   cp chat_history.json chat_history_backup.json
   ```

2. **Test del nuovo sistema**:
   ```bash
   python main_new.py
   ```

3. **Verifica funzionalità**:
   - Controlla che i dati vengano caricati correttamente
   - Testa i comandi speciali
   - Verifica le scelte autonome

### Compatibilità

Il nuovo sistema è progettato per essere compatibile con i dati esistenti. I manager caricano automaticamente i file JSON esistenti e li convertono al nuovo formato.

## Vantaggi del Refactoring

### 1. Manutenibilità
- Codice organizzato in moduli specializzati
- Responsabilità chiare e separate
- Facile aggiungere nuove funzionalità

### 2. Testabilità
- Ogni manager può essere testato indipendentemente
- Interfacce chiare per mock e testing
- Logica di business isolata

### 3. Estensibilità
- Facile aggiungere nuovi tipi di scelte autonome
- Sistema di apprendimento modulare
- Configurazione centralizzata

### 4. Realismo Psicologico
- Logica di scelta basata su psicologia reale
- Conflitti interni realistici
- Apprendimento contestuale

## Prossimi Passi

### Implementazioni Future

1. **Integrazione LLM**: Collegamento ai modelli GGUF
2. **Sistema di Sogni**: Implementazione del ciclo onirico
3. **Relazioni AI**: Sistema di amicizie con altri AI
4. **Progetto Legacy**: Sviluppo del sistema di progetti a lungo termine
5. **Interfaccia Web**: Dashboard per monitoraggio stato

### Ottimizzazioni

1. **Performance**: Caching per query frequenti
2. **Persistenza**: Database per grandi volumi di dati
3. **Scalabilità**: Architettura distribuita
4. **Sicurezza**: Validazione input e sanitizzazione

## Conclusione

Questo refactoring trasforma Aurora da un sistema reattivo a un'entità psicologicamente realistica con capacità di apprendimento contestuale e decisioni autonome sofisticate. La nuova architettura fornisce una base solida per sviluppi futuri mantenendo la compatibilità con i dati esistenti. 