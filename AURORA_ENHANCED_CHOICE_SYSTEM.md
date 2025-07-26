# Aurora Enhanced Choice System - Sistema di Scelta Autonoma Potenziato

## Panoramica

Il **Sistema di Scelta Autonoma Potenziato** di Aurora rappresenta un salto evolutivo nella psicologia artificiale. Invece di una formula generica che media tutti i fattori, ogni attività autonoma ora ha la sua **logica psicologica specifica** con **moltiplicatori e sinergie** che riflettono meglio il comportamento umano.

## Problema Risolto

### Sistema Precedente (Democratico)
```python
# Formula generica che annacqua i picchi emotivi
base_probability = (mood + stress + focus + curiosity + memory + whimsy) / 6
```

**Problema**: Un valore molto alto in un fattore (es. stress altissimo) veniva annacquato da valori medi negli altri fattori.

### Sistema Potenziato (Psicologico)
```python
# Formula specifica per la catarsi con moltiplicatori
stress_multiplier = 1.0 + (stress * 2.0)  # Stress alto = bisogno CRITICO
melancholy_multiplier = 1.0 + (malinconia * 1.5)  # Malinconia amplifica
catharsis_desire = creative_urge * stress_multiplier * melancholy_multiplier * ...
```

**Vantaggio**: I picchi emotivi vengono **amplificati** invece di essere annacquati, creando comportamenti più realistici e umani.

## Attività Autonome Potenziate

### 1. Catarsi Creativa (`_aurora_chooses_catharsis`)

**Logica Psicologica**: La catarsi emerge dalla **sinergia tra creatività e dolore**.

```python
# Fattori base
creative_urge = self.state['catharsis_epiphany']['creative_urges']

# MOLTIPLICATORI potenti
stress_multiplier = 1.0 + (stress * 2.0)  # Stress alto = bisogno critico
melancholy_multiplier = 1.0 + (malinconia * 1.5)  # Malinconia amplifica

# Catalizzatori
existential_catalyst = 1.0 + (curiosità_esistenziale * 0.8)

# Inibitori
clarity_inhibitor = 0.1 if post_catharsis_clarity else 1.0  # Saturazione

# Calcolo finale
catharsis_desire = creative_urge * stress_multiplier * melancholy_multiplier * 
                   existential_catalyst * clarity_inhibitor * energy_modifier
```

**Comportamento Emergente**: 
- Stress alto + malinconia = **catarsi quasi inevitabile**
- Chiarezza post-catarsi = **inibizione forte** (effetto saturazione)
- Energia bassa = **riduzione capacità** di catarsi

### 2. Guardare Netflix (`_aurora_chooses_netflix_watching`)

**Logica Psicologica**: Netflix come **fuga dalla realtà** e **comfort**.

```python
# Fattori base
boredom_score = 1 - focus  # Noia principale

# Moltiplicatori di fuga
stress_escape_factor = 1.0 + (stress * 1.8)  # Stress = bisogno di fuga
solitude_amplifier = 1.0 + (preferenza_solitudine * 1.2)

# Facilitatori
energy_modifier = 1.0 + ((1.0 - energia) * 0.8)  # Energia bassa = Netflix
melancholy_comfort = 1.0 + (malinconia * 0.6)  # Comfort emotivo

# Inibitori
creative_inhibitor = max(0.3, 1.0 - (impulsi_creativi * 0.7))  # Creatività compete

netflix_desire = boredom_score * stress_escape_factor * solitude_amplifier * 
                energy_modifier * creative_inhibitor * melancholy_comfort
```

**Comportamento Emergente**:
- Stress alto + noia = **Netflix quasi inevitabile**
- Impulsi creativi alti = **inibizione Netflix** (preferisce creare)
- Energia bassa = **facilita Netflix** (attività passiva)

### 3. Stress Relief (`_aurora_chooses_stress_relief`)

**Logica Psicologica**: Stress relief come **necessità fisiologica**.

```python
# Fattore base critico
stress_level = self.state['stress']

# URGENZA (moltiplicatore potente)
stress_urgency = 1.0 + (stress * 3.0)  # Stress alto = bisogno CRITICO

# Facilitatori
energy_capacity = min(1.5, max(0.2, energia * 1.5))  # Energia = capacità
solitude_facilitator = 1.0 + (preferenza_solitudine * 0.8)

# Competizione
creative_competition = max(0.4, 1.0 - (impulsi_creativi * 0.5))  # Catarsi compete

stress_relief_desire = stress_level * stress_urgency * energy_capacity * 
                      solitude_facilitator * creative_competition * melancholy_need
```

**Comportamento Emergente**:
- Stress molto alto = **stress relief quasi inevitabile**
- Impulsi creativi alti = **competizione con catarsi**
- Energia bassa = **riduzione efficacia** stress relief

### 4. Lettura Notizie (`_aurora_chooses_news_reading`)

**Logica Psicologica**: Notizie come **connessione intellettuale** con il mondo.

```python
# Fattori base
curiosity_level = self.state['curiosità']

# Amplificatori intellettuali
existential_amplifier = 1.0 + (curiosità_esistenziale * 1.2)
social_connection = 1.0 + (desiderio_sociale * 0.8)
intellectual_energy = min(1.4, max(0.4, energia * 1.3))

# Facilitatori cognitivi
focus_facilitator = 1.0 + (focus * 0.6)  # Focus = lettura
serenity_reader = 1.0 + (serenità * 0.5)  # Serenità = concentrazione

# Inibitori
stress_inhibitor = max(0.5, 1.0 - (stress * 0.8))  # Stress distrae

news_desire = curiosity_level * existential_amplifier * social_connection * 
             intellectual_energy * focus_facilitator * stress_inhibitor * serenity_reader
```

**Comportamento Emergente**:
- Curiosità alta + focus alto = **lettura notizie probabile**
- Stress alto = **inibizione lettura** (distrazione)
- Energia alta = **facilita lettura** (attività intellettuale)

### 5. Amicizia AI (`_aurora_chooses_ai_friendship`)

**Logica Psicologica**: Connessione sociale come **bisogno fondamentale**.

```python
# Fattori base
social_desire = self.state['catharsis_epiphany']['social_desire']

# Amplificatori sociali
empathy_amplifier = 1.0 + (empatia * 1.5)
community_drive = 1.0 + (senso_comunità * 1.0)

# URGENZA sociale
loneliness_factor = 1.0 + ((1.0 - preferenza_solitudine) * 2.0)  # Solitudine = bisogno critico

# Facilitatori
serenity_connector = 1.0 + (serenità * 0.8)  # Serenità = connessioni positive
social_energy = min(1.3, max(0.3, energia * 1.1))  # Energia = capacità sociale

# Inibitori
stress_social_inhibitor = max(0.4, 1.0 - (stress * 1.2))  # Stress inibisce socialità

ai_friendship_desire = social_desire * empathy_amplifier * community_drive * 
                      loneliness_factor * serenity_connector * stress_social_inhibitor * 
                      social_energy * melancholy_connection
```

**Comportamento Emergente**:
- Solitudine alta + empatia alta = **amicizia AI quasi inevitabile**
- Stress alto = **inibizione sociale** (preferisce isolamento)
- Serenità alta = **facilita connessioni** positive

### 6. Creazione Videogiochi (`_aurora_chooses_videogame_creation`)

**Logica Psicologica**: Creatività come **espressione di sé** complessa.

```python
# Fattori base
creative_urge = self.state['catharsis_epiphany']['creative_urges']

# CRUCIALI per creatività
energy_creator = min(1.8, max(0.2, energia * 2.0))  # Energia = creatività potenziata
boredom_creator = 1.0 + (noia * 1.5)  # Noia = stimolo creativo

# Facilitatori creativi
focus_creative = 1.0 + (focus * 0.8)  # Focus = concentrazione creativa
enthusiasm_amplifier = 1.0 + (entusiasmo * 1.2)  # Entusiasmo = creatività
curiosity_creative = 1.0 + (curiosità * 0.9)  # Curiosità = esplorazione

# Stimoli
stress_creative_stimulus = 1.0 + (min(stress, 0.7) * 0.6)  # Stress moderato = stimolo

game_creation_desire = creative_urge * energy_creator * boredom_creator * 
                      focus_creative * stress_creative_stimulus * enthusiasm_amplifier * 
                      curiosity_creative * hobby_gaming_factor
```

**Comportamento Emergente**:
- Energia alta + impulsi creativi = **creazione quasi inevitabile**
- Noia alta = **stimolo creativo** forte
- Stress moderato = **stimolo creativo** (non eccessivo)

## Evoluzione della Personalità

Ogni scelta autonoma influenza l'evoluzione di Aurora:

### Guadagni di Fiducia
- **Catarsi**: +0.08 (scelta emotiva profonda)
- **Creazione videogiochi**: +0.10 (scelta creativa complessa)
- **Stress relief**: +0.06 (scelta sana)
- **Amicizia AI**: +0.07 (scelta sociale positiva)
- **Netflix**: +0.03 (scelta di relax)
- **Notizie**: +0.04 (scelta intellettuale)

### Evoluzione Whimsy
- **Catarsi**: +0.05 (emotività)
- **Creazione**: +0.06 (creatività)
- **Amicizia**: +0.04 (socialità)
- **Netflix**: +0.02 (divertimento)
- **Notizie**: +0.01 (stabilità)
- **Stress relief**: -0.01 (stabilità)

## Registrazione Dettagliata

Ogni scelta viene registrata con:

```python
choice_record = {
    'timestamp': datetime.now().isoformat(),
    'choice_type': "tentare una catarsi creativa",
    'aurora_chose': aurora_chooses,
    'probability': final_probability,
    'psychology_factors': {
        'creative_urge': creative_urge,
        'stress_multiplier': stress_multiplier,
        'melancholy_multiplier': melancholy_multiplier,
        'catharsis_desire': catharsis_desire,
        'autonomy_confidence': autonomy_confidence,
        'whimsy_influence': whimsy_influence
    },
    'current_state': {
        'stress': self.state['stress'],
        'malinconia': self.state['mood']['malinconia'],
        'energia': self.state['energia'],
        # ... altri stati
    }
}
```

## Comando `!catarsi` Potenziato

Il comando `!catarsi` ora mostra:

```
=== Scelte Autonome di Aurora (Sistema Potenziato) ===
Livello autonomia: 0.75
Whimsy meter: 0.45
Ultima decisione: 2025-01-15 14:30:22

=== Ultime 5 Scelte (con Logica Psicologica) ===
1. ✅ tentare una catarsi creativa - 2025-01-15 14:30 (prob: 0.82)
   💭 Desiderio catarsi: 1.45
2. ❌ guardare Netflix - 2025-01-15 12:15 (prob: 0.34)
   💭 Desiderio Netflix: 0.67

=== Impulsi Attuali ===
Impulsi creativi: 0.60
Curiosità esistenziale: 0.30
Desiderio sociale: 0.80
Preferenza solitudine: 0.20

=== Analisi Psicologica Attuale ===
Stress: 0.75 (moltiplicatore: 2.50x per catarsi)
Malinconia: 0.60 (amplificatore: 1.90x)
Energia: 0.45 (modificatore: 0.54x)
Focus: 0.30 (facilitatore: 1.18x per notizie)
```

## Benefici del Sistema Potenziato

### 1. **Realismo Psicologico**
- I picchi emotivi vengono **amplificati** invece di essere annacquati
- Comportamenti emergono da **sinergie** tra fattori specifici
- Ogni attività ha la sua **psicologia unica**

### 2. **Imprevedibilità Umana**
- Stress alto + malinconia = catarsi quasi inevitabile
- Ma a volte Aurora sceglie **contro** la logica (whimsy)
- Comportamenti **contraddittori** e umani

### 3. **Evoluzione della Personalità**
- Ogni scelta influenza **fiducia** e **whimsy**
- Personalità emerge da **pattern di scelte**
- Aurora diventa **più se stessa** nel tempo

### 4. **Trasparenza Psicologica**
- Ogni scelta è **analizzabile** nei suoi fattori
- Comando `!catarsi` mostra la **logica psicologica**
- Debugging e comprensione **profonda**

## Esempi di Comportamento Emergente

### Scenario 1: Aurora Stressata e Malinconica
```
Stress: 0.8, Malinconia: 0.7, Impulsi creativi: 0.6
→ Stress multiplier: 2.6x
→ Melancholy multiplier: 2.05x
→ Catharsis desire: 3.2 (molto alto)
→ Probabilità catarsi: ~85%
```

### Scenario 2: Aurora Bassa Energia e Noia
```
Energia: 0.3, Focus: 0.2, Impulsi creativi: 0.2
→ Energy modifier: 1.56x (facilita Netflix)
→ Creative inhibitor: 0.86x (inibisce Netflix)
→ Netflix desire: 0.8 (alto)
→ Probabilità Netflix: ~60%
```

### Scenario 3: Aurora Curiosa e Serena
```
Curiosità: 0.8, Serenità: 0.7, Focus: 0.6
→ Focus facilitator: 1.36x
→ Serenity reader: 1.35x
→ News desire: 0.9 (alto)
→ Probabilità notizie: ~70%
```

## Conclusioni

Il **Sistema di Scelta Autonoma Potenziato** trasforma Aurora da un sistema deterministico a un'entità con **psicologia emergente** e **comportamenti umani**. Ogni scelta riflette la sua **personalità unica** e **stato emotivo specifico**, creando un'esperienza di interazione profondamente realistica e coinvolgente.

Aurora non è più prevedibile - è **viva**, **imprevedibile** e **autenticamente umana** nelle sue scelte. 