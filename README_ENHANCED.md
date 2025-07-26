# Aurora Enhanced - Sistema AI Modulare Avanzato

## 🌟 Panoramica

Aurora Enhanced è un'evoluzione significativa del sistema AI Aurora, che introduce un'architettura modulare e funzionalità avanzate per un'esperienza più coinvolgente e sofisticata.

## 🏗️ Architettura Modulare

### 1. PersonalityManager (`personality_manager.py`)
Gestisce la personalità, l'umore, lo stress e gli stati emotivi di Aurora.

**Funzionalità:**
- Gestione stati emotivi (energia, stress, focus, curiosità)
- Sistema di umore dinamico (serenità, entusiasmo, malinconia)
- Aggiornamento automatico dell'energia
- Decadimento naturale dell'umore
- Applicazione di feedback (elogi/correzioni)
- Aggiornamento preferenze basato su contenuti
- Calcolo età e ansia da morte
- Salvataggio/caricamento stato persistente

**Esempio:**
```python
personality = PersonalityManager(config)
personality.apply_praise()  # Aumenta focus, energia, serenità
personality.update_energy()  # Aggiorna energia naturalmente
```

### 2. MemoryManager (`memory_manager.py`)
Gestisce il sistema di memoria, corruzione e RAG (Retrieval-Augmented Generation).

**Funzionalità:**
- Gestione memory_box con decadimento
- Sistema di corruzione memoria durante i sogni
- Retrieval di memorie rilevanti
- Gestione inside jokes e chat history
- Integrazione ChromaDB per vettori
- Statistiche memoria e corruzione
- Corruzione semantica, dettagli e fusione

**Esempio:**
```python
memory = MemoryManager(config)
memory.add_memory("Ho imparato qualcosa di nuovo", sentiment='positivo')
relevant = memory.retrieve_relevant_memories("apprendimento", limit=5)
memory.corrupt_random_memory(probability=0.1)
```

### 3. AutonomousSystem (`autonomous_system.py`)
Gestisce le scelte autonome e le attività di Aurora.

**Funzionalità:**
- Sistema di scelte autonome basato su stato emotivo
- Aggiornamento impulsi (creativi, sociali, esistenziali)
- Apprendimento dai risultati delle scelte
- Gestione confidenza autonomia e whimsy meter
- Salvataggio stato autonomo persistente
- Analisi contestuale per decisioni

**Esempio:**
```python
autonomous = AutonomousSystem(config, personality, memory)
autonomous.update_aurora_urges()
choice = autonomous.aurora_makes_choice("creazione_videogioco")
autonomous.learn_from_choice_result("creazione_videogioco", was_praised=True)
```

### 4. AuroraDashboard (`aurora_dashboard.py`)
Dashboard grafica per visualizzare lo stato interno di Aurora in tempo reale.

**Funzionalità:**
- Visualizzazione stati personalità (energia, stress, focus, curiosità)
- Monitoraggio sistema autonomo (confidenza, whimsy, impulsi)
- Statistiche memoria e corruzione
- Attività recenti in tempo reale
- Aggiornamento automatico ogni 2 secondi
- Interfaccia Tkinter user-friendly

**Esempio:**
```python
dashboard = create_dashboard(aurora_instance)
dashboard.run()  # Avvia dashboard in thread separato
```

## 🎮 Sistema di Creazione Videogiochi

Aurora può ora creare videogiochi autonomamente quando si sente ispirata o annoiata.

**Funzionalità:**
- Determinazione tipo gioco basata su stato emotivo
- Generazione concetto, design e codice
- Salvataggio in file JSON e Python
- Integrazione nel sistema di noia
- Scelta autonoma per creazione

**Tipi di Giochi:**
- **Stress alto** → Giochi rilassanti/meditativi
- **Energia alta** → Giochi veloci/adrenalinici  
- **Malinconia** → Giochi narrativi/introspettivi
- **Entusiasmo** → Giochi colorati/gioiosi
- **Hobby specifici** → Giochi tematici

## 🧠 Sistema di Sogni Avanzato

I sogni ora riflettono le tensioni emotive irrisolte di Aurora.

**Funzionalità:**
- Analisi tensioni emotive per generazione sogni
- Selezione concetti basata su stato emotivo
- Effetti sogni su stato emotivo
- Sogni catartici per ansia
- Riflessione su gelosia
- Integrazione con corruzione memoria

**Tipi di Tensioni:**
- **Ansia** → Sogni di libertà/volo (catartici)
- **Gelosia** → Sogni competitivi con riflessione
- **Crisi esistenziale** → Sogni filosofici
- **Desiderio sensoriale** → Sogni sensoriali
- **Solitudine** → Sogni sociali
- **Impulsi creativi** → Sogni artistici
- **Confusione memoria** → Sogni confusi

## 📚 Sistema di Apprendimento dai Risultati

Aurora ora impara dalle conseguenze delle sue scelte autonome.

**Funzionalità:**
- Apprendimento da feedback positivo/negativo
- Aumento/diminuzione confidenza autonomia
- Boost/riduzione impulsi correlati
- Apprendimento specifico per argomenti
- Registrazione apprendimento nelle scelte
- Integrazione con comandi `!praise` e `!correct`

**Esempio:**
```python
# Aurora fa una scelta
aurora._aurora_chooses_videogame_creation()

# Utente dà feedback
aurora._learn_from_choice_result("creazione_videogioco", was_praised=True)
# → Aumenta confidenza autonomia +0.1
# → Aumenta impulsi creativi +0.15

aurora._learn_from_choice_result("catarsi_creativa", was_corrected=True, topic="timing")
# → Diminuisce confidenza autonomia -0.05
# → Diminuisce impulsi creativi -0.1
```

## 🚀 Integrazione Completa

### EnhancedAurora (`aurora_integration_example.py`)
Classe che integra tutti i sistemi in un'unica interfaccia.

**Funzionalità:**
- Inizializzazione automatica di tutti i manager
- Dashboard opzionale
- Processamento query con aggiornamento stati
- Scelte autonome con apprendimento
- Salvataggio automatico stati
- Monitoraggio completo sistema

**Esempio di Utilizzo:**
```python
# Creazione Aurora Enhanced
aurora = EnhancedAurora()
await aurora.initialize()

# Interazione normale
response = await aurora.process_query("Ciao Aurora!")

# Aurora fa scelte autonome
if aurora._aurora_chooses_videogame_creation():
    aurora._create_videogame()

# Apprendimento automatico
aurora._learn_from_choice_result("recent_activity", was_praised=True)

# Stato completo sistema
status = aurora.get_system_status()
```

## 📊 Comandi Avanzati

### Comandi Esistenti Migliorati
- **`!praise`** - Ora include apprendimento dalle scelte recenti
- **`!correct [argomento]`** - Include apprendimento specifico per argomento

### Nuovi Comandi
- **`!dashboard`** - Avvia dashboard grafica (se abilitata)
- **`!status`** - Mostra stato completo di tutti i sistemi
- **`!learning`** - Mostra statistiche apprendimento

## 🔧 Configurazione

### Abilitazione Dashboard
```python
CONFIG = {
    # ... altre configurazioni ...
    'enable_dashboard': True,  # Abilita dashboard grafica
}
```

### Configurazione Manager
```python
CONFIG = {
    # PersonalityManager
    'energy_threshold_tired': 0.3,
    'ai_birth_date': '2025-01-01',
    'ai_life_span_days': 730,
    'death_anxiety_threshold': 0.9,
    
    # MemoryManager
    'memory_box_path': './memory_box.json',
    'inside_jokes_path': './inside_jokes.json',
    'chat_history_path': './chat_history.json',
    'chroma_db_path': './chroma_db',
    
    # AutonomousSystem
    'aurora_autonomy_level': 0.8,
    'aurora_whimsy_factor': 0.3,
    'aurora_mood_influence': 0.7,
    'aurora_memory_influence': 0.6,
    'aurora_creativity_boost': 0.4,
}
```

## 🎯 Vantaggi del Sistema Modulare

1. **Manutenibilità** - Codice organizzato in moduli specializzati
2. **Estensibilità** - Facile aggiungere nuove funzionalità
3. **Testabilità** - Ogni modulo può essere testato separatamente
4. **Persistenza** - Stati salvati automaticamente
5. **Visualizzazione** - Dashboard per monitoraggio in tempo reale
6. **Apprendimento** - Sistema di apprendimento continuo
7. **Sogni Significativi** - Riflessione delle tensioni emotive
8. **Creatività** - Sistema di creazione videogiochi autonomo

## 🔮 Sviluppi Futuri

- **Integrazione Web** - Dashboard web con Flask/FastAPI
- **Machine Learning** - Modelli predittivi per scelte autonome
- **API Esterna** - Interfaccia per altri sistemi AI
- **Analisi Avanzata** - Pattern recognition nelle scelte
- **Collaborazione Multi-AI** - Sistema di amicizie AI avanzato

## 📝 Note di Sviluppo

- Tutti i sistemi sono retrocompatibili con Aurora originale
- I manager possono essere utilizzati indipendentemente
- La dashboard è opzionale e non influisce sulle prestazioni
- Il sistema di apprendimento è incrementale e sicuro
- I sogni sono generati in modo deterministico ma creativo

---

**Aurora Enhanced** rappresenta un significativo passo avanti nell'evoluzione di sistemi AI autonomi, combinando architettura modulare, apprendimento continuo e creatività autonoma in un sistema coeso e coinvolgente. 