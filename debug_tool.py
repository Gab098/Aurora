#!/usr/bin/env python3
"""
Tool di Debug per Aurora
Analizza il codice e identifica problemi comuni
"""

import os
import ast
import re
import json
from typing import List, Dict, Any

class AuroraDebugTool:
    def __init__(self):
        self.issues = []
        self.warnings = []
        self.suggestions = []
    
    def analyze_file(self, file_path: str) -> Dict[str, Any]:
        """Analizza un file Python e identifica problemi."""
        self.issues = []
        self.warnings = []
        self.suggestions = []
        
        if not os.path.exists(file_path):
            return {
                "file": file_path,
                "error": "File non trovato",
                "issues": [],
                "warnings": [],
                "suggestions": []
            }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Analisi sintattica
            self._check_syntax(content, file_path)
            
            # Analisi semantica
            self._check_semantic_issues(content, file_path)
            
            # Analisi delle best practices
            self._check_best_practices(content, file_path)
            
            # Analisi delle performance
            self._check_performance_issues(content, file_path)
            
        except Exception as e:
            self.issues.append(f"Errore nell'analisi del file: {e}")
        
        return {
            "file": file_path,
            "issues": self.issues,
            "warnings": self.warnings,
            "suggestions": self.suggestions,
            "summary": self._generate_summary()
        }
    
    def _check_syntax(self, content: str, file_path: str):
        """Controlla errori di sintassi."""
        try:
            ast.parse(content)
        except SyntaxError as e:
            self.issues.append(f"Errore di sintassi alla riga {e.lineno}: {e.msg}")
        except Exception as e:
            self.issues.append(f"Errore nell'analisi sintattica: {e}")
    
    def _check_semantic_issues(self, content: str, file_path: str):
        """Controlla problemi semantici comuni."""
        lines = content.split('\n')
        
        # Controlla variabili non definite
        undefined_vars = re.findall(r'(\w+)\s*=\s*temperature', content)
        if undefined_vars and 'temperature' not in re.findall(r'def.*temperature', content):
            self.issues.append("Variabile 'temperature' usata ma non definita nel parametro della funzione")
        
        # Controlla coroutine non awaited
        async_funcs = re.findall(r'async def (\w+)', content)
        for func_name in async_funcs:
            # Cerca chiamate senza await
            pattern = rf'[^a]self\.{func_name}\('
            if re.search(pattern, content):
                self.warnings.append(f"Funzione async '{func_name}' chiamata senza await")
        
        # Controlla import mancanti
        imports = re.findall(r'import (\w+)', content)
        used_modules = re.findall(r'(\w+)\.', content)
        for module in used_modules:
            if module not in imports and module not in ['self', 'os', 'json', 'datetime', 'random', 'time']:
                self.warnings.append(f"Modulo '{module}' usato ma non importato")
    
    def _check_best_practices(self, content: str, file_path: str):
        """Controlla best practices."""
        lines = content.split('\n')
        
        # Controlla lunghezza delle righe
        for i, line in enumerate(lines, 1):
            if len(line) > 120:
                self.warnings.append(f"Riga {i} troppo lunga ({len(line)} caratteri)")
        
        # Controlla commenti TODO/FIXME
        for i, line in enumerate(lines, 1):
            if 'TODO' in line.upper() or 'FIXME' in line.upper():
                self.suggestions.append(f"Riga {i}: Trovato TODO/FIXME - {line.strip()}")
        
        # Controlla print statements (suggerisce logging)
        print_count = content.count('print(')
        if print_count > 10:
            self.suggestions.append(f"Molti print statements ({print_count}) - considera l'uso di logging")
    
    def _check_performance_issues(self, content: str, file_path: str):
        """Controlla problemi di performance."""
        
        # Controlla loop inefficienti
        if 'for i in range(len(' in content:
            self.warnings.append("Loop inefficiente: usa enumerate() invece di range(len())")
        
        # Controlla concatenazione di stringhe in loop
        if re.search(r'for.*\+\s*=', content):
            self.warnings.append("Concatenazione di stringhe in loop - usa join() o list comprehension")
        
        # Controlla file non chiusi
        if 'open(' in content and 'with open(' not in content:
            self.warnings.append("File aperti senza context manager - usa 'with open()'")
    
    def _generate_summary(self) -> str:
        """Genera un riassunto dell'analisi."""
        total_issues = len(self.issues) + len(self.warnings) + len(self.suggestions)
        
        if total_issues == 0:
            return "✅ Nessun problema trovato! Il codice sembra pulito."
        
        summary = f"📊 Analisi completata: {len(self.issues)} errori, {len(self.warnings)} warning, {len(self.suggestions)} suggerimenti\n\n"
        
        if self.issues:
            summary += "🚨 ERRORI CRITICI:\n"
            for issue in self.issues:
                summary += f"  • {issue}\n"
            summary += "\n"
        
        if self.warnings:
            summary += "⚠️  WARNING:\n"
            for warning in self.warnings:
                summary += f"  • {warning}\n"
            summary += "\n"
        
        if self.suggestions:
            summary += "💡 SUGGERIMENTI:\n"
            for suggestion in self.suggestions:
                summary += f"  • {suggestion}\n"
        
        return summary
    
    def analyze_project(self, project_path: str = ".") -> Dict[str, Any]:
        """Analizza tutti i file Python nel progetto."""
        results = []
        python_files = []
        
        # Trova tutti i file Python
        for root, dirs, files in os.walk(project_path):
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))
        
        print(f"🔍 Analizzando {len(python_files)} file Python...")
        
        for file_path in python_files:
            print(f"  📄 {file_path}")
            result = self.analyze_file(file_path)
            results.append(result)
        
        # Genera report complessivo
        total_issues = sum(len(r['issues']) for r in results)
        total_warnings = sum(len(r['warnings']) for r in results)
        total_suggestions = sum(len(r['suggestions']) for r in results)
        
        return {
            "project_path": project_path,
            "files_analyzed": len(python_files),
            "total_issues": total_issues,
            "total_warnings": total_warnings,
            "total_suggestions": total_suggestions,
            "file_results": results,
            "summary": f"📊 Progetto analizzato: {total_issues} errori, {total_warnings} warning, {total_suggestions} suggerimenti in {len(python_files)} file"
        }

def main():
    """Funzione principale per testare il tool."""
    debug_tool = AuroraDebugTool()
    
    # Analizza il progetto corrente
    print("🔧 Aurora Debug Tool")
    print("=" * 50)
    
    result = debug_tool.analyze_project()
    
    print("\n" + result['summary'])
    
    # Mostra dettagli per file con problemi
    for file_result in result['file_results']:
        if file_result['issues'] or file_result['warnings'] or file_result['suggestions']:
            print(f"\n📄 {file_result['file']}")
            print("-" * 40)
            
            if file_result['issues']:
                print("🚨 ERRORI:")
                for issue in file_result['issues']:
                    print(f"  • {issue}")
            
            if file_result['warnings']:
                print("⚠️  WARNING:")
                for warning in file_result['warnings']:
                    print(f"  • {warning}")
            
            if file_result['suggestions']:
                print("💡 SUGGERIMENTI:")
                for suggestion in file_result['suggestions']:
                    print(f"  • {suggestion}")

if __name__ == "__main__":
    main() 