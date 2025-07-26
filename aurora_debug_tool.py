#!/usr/bin/env python3
"""
Aurora Debug Tool - Integrato nel sistema Aurora
Può essere chiamato come comando interno per diagnosticare problemi
"""

import os
import ast
import re
import json
import asyncio
import traceback
from typing import List, Dict, Any
from datetime import datetime

class AuroraDebugTool:
    def __init__(self, aurora_instance=None):
        self.aurora = aurora_instance
        self.issues = []
        self.warnings = []
        self.suggestions = []
        self.performance_metrics = {}
    
    async def run_full_diagnostic(self) -> str:
        """Esegue una diagnostica completa del sistema Aurora."""
        self.issues = []
        self.warnings = []
        self.suggestions = []
        self.performance_metrics = {}
        
        report = "🔧 **DIAGNOSTICA AURORA COMPLETA**\n"
        report += "=" * 50 + "\n\n"
        
        # 1. Controllo stato interno
        report += await self._check_internal_state()
        
        # 2. Controllo file di sistema
        report += await self._check_system_files()
        
        # 3. Controllo modelli LLM
        report += await self._check_llm_models()
        
        # 4. Controllo memoria e database
        report += await self._check_memory_and_db()
        
        # 5. Controllo scheduler
        report += await self._check_scheduler()
        
        # 6. Controllo performance
        report += await self._check_performance()
        
        # 7. Controllo errori recenti
        report += await self._check_recent_errors()
        
        # 8. Raccomandazioni
        report += await self._generate_recommendations()
        
        return report
    
    async def _check_internal_state(self) -> str:
        """Controlla lo stato interno di Aurora."""
        if not self.aurora:
            return "⚠️  Aurora instance non disponibile\n\n"
        
        report = "📊 **STATO INTERNO**\n"
        report += "-" * 20 + "\n"
        
        try:
            state = self.aurora.state
            report += f"• Energia: {state.get('energia', 'N/A'):.2f}\n"
            report += f"• Stress: {state.get('stress', 'N/A'):.2f}\n"
            report += f"• Focus: {state.get('focus', 'N/A'):.2f}\n"
            report += f"• Curiosità: {state.get('curiosità', 'N/A'):.2f}\n"
            report += f"• Hobby: {state.get('hobby', 'N/A')}\n"
            
            # Controllo mood
            mood = state.get('mood', {})
            report += f"• Serenità: {mood.get('serenità', 0):.2f}\n"
            report += f"• Entusiasmo: {mood.get('entusiasmo', 0):.2f}\n"
            report += f"• Malinconia: {mood.get('malinconia', 0):.2f}\n"
            
            # Controllo età
            if hasattr(self.aurora, '_calculate_age_days'):
                age_days = self.aurora._calculate_age_days()
                report += f"• Età: {age_days} giorni\n"
            
            # Controllo chat history
            chat_count = len(self.aurora.chat_history) if hasattr(self.aurora, 'chat_history') else 0
            report += f"• Interazioni chat: {chat_count}\n"
            
            # Controllo knowledge graph
            if hasattr(self.aurora, 'knowledge_graph') and self.aurora.knowledge_graph:
                kg_nodes = len(self.aurora.knowledge_graph.nodes())
                kg_edges = len(self.aurora.knowledge_graph.edges())
                report += f"• Knowledge Graph: {kg_nodes} nodi, {kg_edges} relazioni\n"
            else:
                report += "• Knowledge Graph: Non disponibile\n"
            
            # Controllo memory box
            memory_count = len(self.aurora.memory_box) if hasattr(self.aurora, 'memory_box') else 0
            report += f"• Memorie: {memory_count}\n"
            
        except Exception as e:
            report += f"❌ Errore nel controllo stato interno: {e}\n"
            self.issues.append(f"Errore stato interno: {e}")
        
        report += "\n"
        return report
    
    async def _check_system_files(self) -> str:
        """Controlla i file di sistema di Aurora."""
        report = "📁 **FILE DI SISTEMA**\n"
        report += "-" * 20 + "\n"
        
        files_to_check = [
            "chat_history.json",
            "memory_box.json", 
            "inside_jokes.json",
            "self_concept.md",
            "knowledge_graph.gml",
            "internal_monologue.log"
        ]
        
        for filename in files_to_check:
            try:
                if os.path.exists(filename):
                    size = os.path.getsize(filename)
                    report += f"✅ {filename}: {size} bytes\n"
                    
                    # Controllo dimensioni eccessive
                    if size > 1024 * 1024:  # > 1MB
                        self.warnings.append(f"File {filename} molto grande ({size} bytes)")
                        report += f"  ⚠️  File molto grande\n"
                else:
                    report += f"❌ {filename}: Non trovato\n"
                    self.warnings.append(f"File {filename} mancante")
            except Exception as e:
                report += f"❌ {filename}: Errore ({e})\n"
                self.issues.append(f"Errore file {filename}: {e}")
        
        report += "\n"
        return report
    
    async def _check_llm_models(self) -> str:
        """Controlla lo stato dei modelli LLM."""
        report = "🤖 **MODELLI LLM**\n"
        report += "-" * 20 + "\n"
        
        if not self.aurora:
            report += "⚠️  Aurora instance non disponibile\n\n"
            return report
        
        try:
            # Controllo modelli caricati
            if self.aurora.llm_router:
                report += "✅ Router LLM: Caricato\n"
            else:
                report += "❌ Router LLM: Non caricato\n"
                self.warnings.append("Router LLM non caricato")
            
            if self.aurora.llm_thinker:
                report += "✅ Thinker LLM: Caricato\n"
            else:
                report += "❌ Thinker LLM: Non caricato\n"
                self.warnings.append("Thinker LLM non caricato")
            
            # Controllo modello corrente
            current_model = getattr(self.aurora, 'current_llm_in_memory', 'Nessuno')
            report += f"• Modello in memoria: {current_model}\n"
            
            # Controllo embedding model
            if self.aurora.embedding_model:
                report += "✅ Embedding Model: Caricato\n"
            else:
                report += "❌ Embedding Model: Non caricato\n"
                self.warnings.append("Embedding model non caricato")
            
        except Exception as e:
            report += f"❌ Errore nel controllo modelli: {e}\n"
            self.issues.append(f"Errore controllo modelli: {e}")
        
        report += "\n"
        return report
    
    async def _check_memory_and_db(self) -> str:
        """Controlla memoria e database."""
        report = "💾 **MEMORIA E DATABASE**\n"
        report += "-" * 20 + "\n"
        
        if not self.aurora:
            report += "⚠️  Aurora instance non disponibile\n\n"
            return report
        
        try:
            # Controllo ChromaDB
            if self.aurora.chroma_client and self.aurora.vector_collection:
                try:
                    doc_count = self.aurora.vector_collection.count()
                    report += f"✅ ChromaDB: {doc_count} documenti\n"
                except Exception as e:
                    report += f"❌ ChromaDB: Errore ({e})\n"
                    self.issues.append(f"Errore ChromaDB: {e}")
            else:
                report += "❌ ChromaDB: Non inizializzato\n"
                self.warnings.append("ChromaDB non inizializzato")
            
            # Controllo memoria Python
            import psutil
            process = psutil.Process()
            memory_mb = process.memory_info().rss / 1024 / 1024
            report += f"• Memoria RAM: {memory_mb:.1f} MB\n"
            
            if memory_mb > 2048:  # > 2GB
                self.warnings.append(f"Uso memoria elevato: {memory_mb:.1f} MB")
                report += f"  ⚠️  Uso memoria elevato\n"
            
        except Exception as e:
            report += f"❌ Errore nel controllo memoria: {e}\n"
            self.issues.append(f"Errore controllo memoria: {e}")
        
        report += "\n"
        return report
    
    async def _check_scheduler(self) -> str:
        """Controlla lo stato dello scheduler."""
        report = "⏰ **SCHEDULER**\n"
        report += "-" * 20 + "\n"
        
        if not self.aurora or not hasattr(self.aurora, 'scheduler'):
            report += "⚠️  Scheduler non disponibile\n\n"
            return report
        
        try:
            scheduler = self.aurora.scheduler
            
            if scheduler.running:
                report += "✅ Scheduler: In esecuzione\n"
                
                # Controllo job attivi
                jobs = scheduler.get_jobs()
                report += f"• Job attivi: {len(jobs)}\n"
                
                for job in jobs:
                    report += f"  - {job.id}: {job.trigger}\n"
            else:
                report += "❌ Scheduler: Non in esecuzione\n"
                self.issues.append("Scheduler non in esecuzione")
            
        except Exception as e:
            report += f"❌ Errore nel controllo scheduler: {e}\n"
            self.issues.append(f"Errore scheduler: {e}")
        
        report += "\n"
        return report
    
    async def _check_performance(self) -> str:
        """Controlla le performance del sistema."""
        report = "⚡ **PERFORMANCE**\n"
        report += "-" * 20 + "\n"
        
        try:
            # Controllo tempo di risposta (simulato)
            start_time = datetime.now()
            # Simula un'operazione leggera
            await asyncio.sleep(0.1)
            response_time = (datetime.now() - start_time).total_seconds() * 1000
            
            report += f"• Tempo di risposta: {response_time:.1f} ms\n"
            
            if response_time > 100:
                self.warnings.append(f"Tempo di risposta lento: {response_time:.1f} ms")
                report += f"  ⚠️  Tempo di risposta lento\n"
            
            # Controllo CPU (se disponibile)
            try:
                import psutil
                cpu_percent = psutil.cpu_percent(interval=0.1)
                report += f"• CPU: {cpu_percent:.1f}%\n"
                
                if cpu_percent > 80:
                    self.warnings.append(f"CPU elevata: {cpu_percent:.1f}%")
                    report += f"  ⚠️  CPU elevata\n"
            except:
                report += "• CPU: Non disponibile\n"
            
        except Exception as e:
            report += f"❌ Errore nel controllo performance: {e}\n"
            self.issues.append(f"Errore performance: {e}")
        
        report += "\n"
        return report
    
    async def _check_recent_errors(self) -> str:
        """Controlla errori recenti."""
        report = "🚨 **ERRORI RECENTI**\n"
        report += "-" * 20 + "\n"
        
        try:
            # Controllo log file se esistono
            log_files = ["internal_monologue.log", "error.log"]
            
            for log_file in log_files:
                if os.path.exists(log_file):
                    try:
                        with open(log_file, 'r', encoding='utf-8') as f:
                            lines = f.readlines()
                            recent_lines = lines[-10:]  # Ultime 10 righe
                            
                            error_lines = [line for line in recent_lines if 'error' in line.lower() or 'exception' in line.lower()]
                            
                            if error_lines:
                                report += f"⚠️  Errori in {log_file}:\n"
                                for error in error_lines[-3:]:  # Ultimi 3 errori
                                    report += f"  - {error.strip()}\n"
                                self.warnings.append(f"Errori trovati in {log_file}")
                            else:
                                report += f"✅ {log_file}: Nessun errore recente\n"
                    except Exception as e:
                        report += f"❌ Errore nella lettura {log_file}: {e}\n"
                else:
                    report += f"ℹ️  {log_file}: Non trovato\n"
            
        except Exception as e:
            report += f"❌ Errore nel controllo errori: {e}\n"
            self.issues.append(f"Errore controllo errori: {e}")
        
        report += "\n"
        return report
    
    async def _generate_recommendations(self) -> str:
        """Genera raccomandazioni basate sui problemi trovati."""
        report = "💡 **RACCOMANDAZIONI**\n"
        report += "-" * 20 + "\n"
        
        if not self.issues and not self.warnings:
            report += "✅ Sistema in ottimo stato! Nessuna raccomandazione necessaria.\n\n"
            return report
        
        recommendations = []
        
        # Raccomandazioni basate sui problemi
        if self.issues:
            report += "🚨 **PROBLEMI CRITICI DA RISOLVERE:**\n"
            for issue in self.issues:
                report += f"• {issue}\n"
                recommendations.append(f"Risolvere: {issue}")
            report += "\n"
        
        if self.warnings:
            report += "⚠️  **AVVISI DA MONITORARE:**\n"
            for warning in self.warnings:
                report += f"• {warning}\n"
                recommendations.append(f"Monitorare: {warning}")
            report += "\n"
        
        # Raccomandazioni generali
        if not self.aurora or not self.aurora.llm_router or not self.aurora.llm_thinker:
            recommendations.append("Caricare i modelli LLM per funzionalità complete")
        
        if not self.aurora or not self.aurora.embedding_model:
            recommendations.append("Caricare il modello di embedding per RAG")
        
        if not self.aurora or not self.aurora.chroma_client:
            recommendations.append("Inizializzare ChromaDB per la memoria vettoriale")
        
        # Raccomandazioni di manutenzione
        recommendations.append("Eseguire backup regolari dei dati")
        recommendations.append("Monitorare l'uso della memoria")
        recommendations.append("Verificare periodicamente i log di errore")
        
        report += "📋 **AZIONI SUGGERITE:**\n"
        for i, rec in enumerate(recommendations, 1):
            report += f"{i}. {rec}\n"
        
        report += "\n"
        return report
    
    async def quick_health_check(self) -> str:
        """Controllo rapido dello stato di salute."""
        if not self.aurora:
            return "❌ Aurora non disponibile"
        
        health_score = 100
        issues = []
        
        # Controlli rapidi
        if not self.aurora.llm_router and not self.aurora.llm_thinker:
            health_score -= 30
            issues.append("Modelli LLM non caricati")
        
        if not self.aurora.embedding_model:
            health_score -= 20
            issues.append("Embedding model non caricato")
        
        if not self.aurora.chroma_client:
            health_score -= 15
            issues.append("ChromaDB non inizializzato")
        
        if not self.aurora.scheduler.running:
            health_score -= 10
            issues.append("Scheduler non in esecuzione")
        
        # Valutazione
        if health_score >= 90:
            status = "🟢 Eccellente"
        elif health_score >= 70:
            status = "🟡 Buono"
        elif health_score >= 50:
            status = "🟠 Attenzione"
        else:
            status = "🔴 Critico"
        
        result = f"🏥 **HEALTH CHECK RAPIDO**\n"
        result += f"Punteggio: {health_score}/100 {status}\n"
        
        if issues:
            result += f"Problemi: {', '.join(issues)}\n"
        else:
            result += "Nessun problema rilevato ✅\n"
        
        return result

# Funzione per integrare il debug tool in Aurora
async def aurora_debug_command(aurora_instance, command="full"):
    """Comando di debug integrato per Aurora."""
    debug_tool = AuroraDebugTool(aurora_instance)
    
    if command == "health" or command == "quick":
        return await debug_tool.quick_health_check()
    elif command == "full" or command == "diagnostic":
        return await debug_tool.run_full_diagnostic()
    else:
        return "Comandi disponibili: 'health' (controllo rapido), 'full' (diagnostica completa)"

if __name__ == "__main__":
    # Test del tool
    async def test():
        debug_tool = AuroraDebugTool()
        result = await debug_tool.quick_health_check()
        print(result)
    
    asyncio.run(test()) 