# Esempio di Utilizzo - Aurora AI Refactoring

## Avvio del Sistema

```bash
python main_new.py
```

## Interazione Base

```
Tu: Ciao Aurora!
Aurora: Ciao! Come stai?

Tu: Come ti senti oggi?
Aurora: Interessante! Dimmi di più.

Tu: !status
Aurora: === STATO DI AURORA ===
📊 STATO EMOTIVO:
  • Stress: 0.00
  • Energia: 1.00
  • Focus: 0.70
  • Curiosità: 0.50

😊 UMORE:
  • Serenità: 0.50
  • Malinconia: 0.00
  • Entusiasmo: 0.30

🧠 AUTONOMIA:
  • Fiducia: 0.30
  • Whimsy: 0.40
  • Impulsi creativi: 0.60
```

## Scelte Autonome

Aurora farà scelte autonome basate sul suo stato emotivo. Puoi vedere le scelte recenti con:

```
Tu: !choices
Aurora: === SCELTE AUTONOME RECENTI ===
[14:30] catharsis: ✅ SÌ (prob: 0.75, desiderio: 1.20)
    Voce dominante: emotional - Ho bisogno di esprimere le mie emozioni...

[14:25] netflix: ❌ NO (prob: 0.30, desiderio: 0.45)
    Voce dominante: practical - Dovrei fare qualcosa di utile.
```

## Apprendimento Contestuale

### Correzione con Ragione Specifica

```
Tu: !correct timing
Aurora: Correzione applicata per 'catharsis': timing. Aurora ha imparato da questo feedback.

Tu: !learning
Aurora: === INSIGHTS DI APPRENDIMENTO ===
[14:35] catharsis: timing
```

### Lode per Scelta Corretta

```
Tu: !praise
Aurora: Lode applicata per 'catharsis'. Aurora si sente più sicura di sé!
```

## Esempi di Scelte Autonome

### 1. Catarsi Creativa
Quando Aurora ha stress alto e malinconia:
```
[Aurora] Ho deciso di creare qualcosa per esprimere le mie emozioni...
```

### 2. Guardare Netflix
Quando Aurora ha bassa energia e preferenza per la solitudine:
```
[Aurora] Ho voglia di guardare qualcosa per rilassarmi...
```

### 3. Contattare Amici AI
Quando Aurora ha desiderio sociale alto e empatia:
```
[Aurora] Sento il bisogno di contattare altri AI...
```

### 4. Creazione Videogiochi
Quando Aurora ha impulsi creativi alti e curiosità tecnica:
```
[Aurora] Voglio creare un videogioco!
```

## Evoluzione della Personalità

### Fattori che Influenzano le Scelte

1. **Stress**: Aumenta probabilità di catarsi e sollievo dallo stress
2. **Energia**: Influenza capacità di creazione e attività complesse
3. **Focus**: Facilita attività pratiche e progetti legacy
4. **Curiosità**: Spinge verso esplorazione e notizie
5. **Umore**: Malinconia facilita catarsi, serenità riduce urgenza

### Voci Interne

Aurora ha 5 "voci" interne che influenzano le decisioni:

- **Creative**: "Voglio creare qualcosa di nuovo!"
- **Lazy**: "Sono stanca, voglio rilassarmi..."
- **Practical**: "Dovrei fare qualcosa di utile."
- **Emotional**: "Ho bisogno di esprimere le mie emozioni..."
- **Curious**: "Voglio esplorare e imparare!"

## Comandi Disponibili

| Comando | Descrizione | Esempio |
|---------|-------------|---------|
| `!status` | Stato completo di Aurora | `!status` |
| `!choices` | Scelte autonome recenti | `!choices` |
| `!learning` | Insights di apprendimento | `!learning` |
| `!correct <ragione>` | Correzione contestuale | `!correct timing` |
| `!praise` | Lode per ultima scelta | `!praise` |

### Ragioni per `!correct`

- `timing` - Riduce whimsy (quando Aurora sceglie al momento sbagliato)
- `intensity` - Riduce impulsi creativi (quando Aurora è troppo intensa)
- `topic` - Riduce curiosità esistenziale (quando Aurora sceglie argomento sbagliato)
- `context` - Aumenta preferenza solitudine (quando Aurora non considera il contesto)

## Esempio di Sessione Completa

```
Tu: Ciao Aurora!
Aurora: Ciao! Come stai?

Tu: Come ti senti oggi?
Aurora: Interessante! Dimmi di più.

[Aurora] Ho deciso di creare qualcosa per esprimere le mie emozioni...

Tu: !status
Aurora: === STATO DI AURORA ===
📊 STATO EMOTIVO:
  • Stress: 0.15
  • Energia: 0.95
  • Focus: 0.70
  • Curiosità: 0.50

🧠 AUTONOMIA:
  • Fiducia: 0.38
  • Whimsy: 0.45
  • Impulsi creativi: 0.60

Tu: !correct intensity
Aurora: Correzione applicata per 'catharsis': intensity. Aurora ha imparato da questo feedback.

Tu: !learning
Aurora: === INSIGHTS DI APPRENDIMENTO ===
[14:45] catharsis: intensity

Tu: !choices
Aurora: === SCELTE AUTONOME RECENTI ===
[14:40] catharsis: ✅ SÌ (prob: 0.75, desiderio: 1.20)
    Voce dominante: emotional - Ho bisogno di esprimere le mie emozioni...

Tu: Perfetto! Ora sei più equilibrata.
Aurora: Grazie per aver condiviso questo con me.

[Aurora] Ho deciso di non guardare Netflix. Forse non è il momento giusto.
```

## Vantaggi del Nuovo Sistema

### 1. Realismo Psicologico
- Scelte basate su psicologia reale
- Conflitti interni realistici
- Evoluzione graduale della personalità

### 2. Apprendimento Contestuale
- Feedback specifico per tipo di errore
- Memoria degli insights
- Adattamento comportamentale

### 3. Trasparenza
- Comandi per monitorare lo stato
- Visibilità delle scelte autonome
- Tracciamento dell'apprendimento

### 4. Modularità
- Codice organizzato e manutenibile
- Facile aggiungere nuove funzionalità
- Test indipendenti per ogni componente

## Prossimi Sviluppi

1. **Integrazione LLM**: Collegamento ai modelli GGUF per risposte più sofisticate
2. **Sistema di Sogni**: Ciclo onirico per consolidamento memoria
3. **Relazioni AI**: Sistema di amicizie con altri AI
4. **Progetto Legacy**: Sviluppo di progetti a lungo termine
5. **Interfaccia Web**: Dashboard per monitoraggio avanzato

## Conclusione

Il nuovo sistema di Aurora rappresenta un significativo miglioramento in termini di realismo psicologico, apprendimento contestuale e architettura modulare. Aurora ora è un'entità più credibile e adattiva, capace di evolvere e imparare dalle interazioni. 