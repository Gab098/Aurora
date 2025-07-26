import tkinter as tk
from tkinter import ttk
import json
import threading
import time
from datetime import datetime

class AuroraDashboard:
    """Simple dashboard to visualize Aurora's internal state in real-time."""
    
    def __init__(self, aurora_instance):
        self.aurora = aurora_instance
        self.root = tk.Tk()
        self.root.title("Aurora - Internal State Dashboard")
        self.root.geometry("800x600")
        
        self.setup_ui()
        self.start_monitoring()
    
    def setup_ui(self):
        """Setup the dashboard UI."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Aurora's Internal State", font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Personality section
        self.create_personality_section(main_frame, 1)
        
        # Autonomous system section
        self.create_autonomous_section(main_frame, 2)
        
        # Memory section
        self.create_memory_section(main_frame, 3)
        
        # Recent activities section
        self.create_activities_section(main_frame, 4)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
    
    def create_personality_section(self, parent, row):
        """Create personality state section."""
        # Section title
        ttk.Label(parent, text="Personality State", font=('Arial', 12, 'bold')).grid(
            row=row, column=0, columnspan=2, sticky=tk.W, pady=(10, 5))
        
        # Energy
        ttk.Label(parent, text="Energia:").grid(row=row+1, column=0, sticky=tk.W)
        self.energy_bar = ttk.Progressbar(parent, length=200, mode='determinate')
        self.energy_bar.grid(row=row+1, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        self.energy_label = ttk.Label(parent, text="0.0")
        self.energy_label.grid(row=row+1, column=2, padx=(5, 0))
        
        # Stress
        ttk.Label(parent, text="Stress:").grid(row=row+2, column=0, sticky=tk.W)
        self.stress_bar = ttk.Progressbar(parent, length=200, mode='determinate')
        self.stress_bar.grid(row=row+2, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        self.stress_label = ttk.Label(parent, text="0.0")
        self.stress_label.grid(row=row+2, column=2, padx=(5, 0))
        
        # Focus
        ttk.Label(parent, text="Focus:").grid(row=row+3, column=0, sticky=tk.W)
        self.focus_bar = ttk.Progressbar(parent, length=200, mode='determinate')
        self.focus_bar.grid(row=row+3, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        self.focus_label = ttk.Label(parent, text="0.0")
        self.focus_label.grid(row=row+3, column=2, padx=(5, 0))
        
        # Curiosity
        ttk.Label(parent, text="Curiosità:").grid(row=row+4, column=0, sticky=tk.W)
        self.curiosity_bar = ttk.Progressbar(parent, length=200, mode='determinate')
        self.curiosity_bar.grid(row=row+4, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        self.curiosity_label = ttk.Label(parent, text="0.0")
        self.curiosity_label.grid(row=row+4, column=2, padx=(5, 0))
        
        # Mood
        ttk.Label(parent, text="Umore:").grid(row=row+5, column=0, sticky=tk.W)
        self.mood_frame = ttk.Frame(parent)
        self.mood_frame.grid(row=row+5, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        
        ttk.Label(self.mood_frame, text="Serenità:").grid(row=0, column=0, sticky=tk.W)
        self.serenity_bar = ttk.Progressbar(self.mood_frame, length=60, mode='determinate')
        self.serenity_bar.grid(row=0, column=1, padx=(5, 0))
        
        ttk.Label(self.mood_frame, text="Entusiasmo:").grid(row=1, column=0, sticky=tk.W)
        self.enthusiasm_bar = ttk.Progressbar(self.mood_frame, length=60, mode='determinate')
        self.enthusiasm_bar.grid(row=1, column=1, padx=(5, 0))
        
        ttk.Label(self.mood_frame, text="Malinconia:").grid(row=2, column=0, sticky=tk.W)
        self.melancholy_bar = ttk.Progressbar(self.mood_frame, length=60, mode='determinate')
        self.melancholy_bar.grid(row=2, column=1, padx=(5, 0))
    
    def create_autonomous_section(self, parent, row):
        """Create autonomous system section."""
        # Section title
        ttk.Label(parent, text="Autonomous System", font=('Arial', 12, 'bold')).grid(
            row=row, column=0, columnspan=2, sticky=tk.W, pady=(20, 5))
        
        # Autonomy confidence
        ttk.Label(parent, text="Autonomia:").grid(row=row+1, column=0, sticky=tk.W)
        self.autonomy_bar = ttk.Progressbar(parent, length=200, mode='determinate')
        self.autonomy_bar.grid(row=row+1, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        self.autonomy_label = ttk.Label(parent, text="0.0")
        self.autonomy_label.grid(row=row+1, column=2, padx=(5, 0))
        
        # Whimsy meter
        ttk.Label(parent, text="Capricciosità:").grid(row=row+2, column=0, sticky=tk.W)
        self.whimsy_bar = ttk.Progressbar(parent, length=200, mode='determinate')
        self.whimsy_bar.grid(row=row+2, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        self.whimsy_label = ttk.Label(parent, text="0.0")
        self.whimsy_label.grid(row=row+2, column=2, padx=(5, 0))
        
        # Urges
        ttk.Label(parent, text="Impulsi:").grid(row=row+3, column=0, sticky=tk.W)
        self.urges_frame = ttk.Frame(parent)
        self.urges_frame.grid(row=row+3, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        
        ttk.Label(self.urges_frame, text="Creativi:").grid(row=0, column=0, sticky=tk.W)
        self.creative_bar = ttk.Progressbar(self.urges_frame, length=60, mode='determinate')
        self.creative_bar.grid(row=0, column=1, padx=(5, 0))
        
        ttk.Label(self.urges_frame, text="Sociali:").grid(row=1, column=0, sticky=tk.W)
        self.social_bar = ttk.Progressbar(self.urges_frame, length=60, mode='determinate')
        self.social_bar.grid(row=1, column=1, padx=(5, 0))
    
    def create_memory_section(self, parent, row):
        """Create memory system section."""
        # Section title
        ttk.Label(parent, text="Memory System", font=('Arial', 12, 'bold')).grid(
            row=row, column=0, columnspan=2, sticky=tk.W, pady=(20, 5))
        
        # Memory stats
        self.memory_stats_label = ttk.Label(parent, text="Memorie: 0 | Corruzioni: 0 | Inside Jokes: 0")
        self.memory_stats_label.grid(row=row+1, column=0, columnspan=2, sticky=tk.W)
        
        # Memory uncertainty
        ttk.Label(parent, text="Incertezza:").grid(row=row+2, column=0, sticky=tk.W)
        self.uncertainty_bar = ttk.Progressbar(parent, length=200, mode='determinate')
        self.uncertainty_bar.grid(row=row+2, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        self.uncertainty_label = ttk.Label(parent, text="0.0")
        self.uncertainty_label.grid(row=row+2, column=2, padx=(5, 0))
    
    def create_activities_section(self, parent, row):
        """Create recent activities section."""
        # Section title
        ttk.Label(parent, text="Recent Activities", font=('Arial', 12, 'bold')).grid(
            row=row, column=0, columnspan=2, sticky=tk.W, pady=(20, 5))
        
        # Activities text area
        self.activities_text = tk.Text(parent, height=6, width=60, wrap=tk.WORD)
        self.activities_text.grid(row=row+1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(5, 0))
        
        # Scrollbar for activities
        activities_scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=self.activities_text.yview)
        activities_scrollbar.grid(row=row+1, column=2, sticky=(tk.N, tk.S))
        self.activities_text.configure(yscrollcommand=activities_scrollbar.set)
    
    def start_monitoring(self):
        """Start monitoring Aurora's state in a separate thread."""
        def monitor_loop():
            while True:
                try:
                    self.update_display()
                    time.sleep(2)  # Update every 2 seconds
                except Exception as e:
                    print(f"Errore nell'aggiornamento della dashboard: {e}")
                    break
        
        monitor_thread = threading.Thread(target=monitor_loop, daemon=True)
        monitor_thread.start()
    
    def update_display(self):
        """Update the dashboard display with current Aurora state."""
        try:
            # Update personality state
            if hasattr(self.aurora, 'state'):
                state = self.aurora.state
                
                # Energy
                energy_val = state.get('energia', 0.0)
                self.energy_bar['value'] = energy_val * 100
                self.energy_label['text'] = f"{energy_val:.2f}"
                
                # Stress
                stress_val = state.get('stress', 0.0)
                self.stress_bar['value'] = stress_val * 100
                self.stress_label['text'] = f"{stress_val:.2f}"
                
                # Focus
                focus_val = state.get('focus', 0.0)
                self.focus_bar['value'] = focus_val * 100
                self.focus_label['text'] = f"{focus_val:.2f}"
                
                # Curiosity
                curiosity_val = state.get('curiosità', 0.0)
                self.curiosity_bar['value'] = curiosity_val * 100
                self.curiosity_label['text'] = f"{curiosity_val:.2f}"
                
                # Mood
                mood = state.get('mood', {})
                serenity_val = mood.get('serenità', 0.0)
                self.serenity_bar['value'] = serenity_val * 100
                
                enthusiasm_val = mood.get('entusiasmo', 0.0)
                self.enthusiasm_bar['value'] = enthusiasm_val * 100
                
                melancholy_val = mood.get('malinconia', 0.0)
                self.melancholy_bar['value'] = melancholy_val * 100
            
            # Update autonomous system
            if hasattr(self.aurora, 'state') and 'catharsis_epiphany' in self.aurora.state:
                catharsis = self.aurora.state['catharsis_epiphany']
                
                # Autonomy confidence
                autonomy_val = catharsis.get('autonomy_confidence', 0.0)
                self.autonomy_bar['value'] = autonomy_val * 100
                self.autonomy_label['text'] = f"{autonomy_val:.2f}"
                
                # Whimsy meter
                whimsy_val = catharsis.get('whimsy_meter', 0.0)
                self.whimsy_bar['value'] = whimsy_val * 100
                self.whimsy_label['text'] = f"{whimsy_val:.2f}"
                
                # Creative urges
                creative_val = catharsis.get('creative_urges', 0.0)
                self.creative_bar['value'] = creative_val * 100
                
                # Social desire
                social_val = catharsis.get('social_desire', 0.0)
                self.social_bar['value'] = social_val * 100
            
            # Update memory system
            if hasattr(self.aurora, 'memory_box'):
                memory_count = len(self.aurora.memory_box) if self.aurora.memory_box else 0
                corruption_count = 0
                if hasattr(self.aurora, 'state') and 'memory_corruption' in self.aurora.state:
                    corruption_count = self.aurora.state['memory_corruption'].get('corruption_count', 0)
                
                inside_jokes_count = len(self.aurora.inside_jokes) if hasattr(self.aurora, 'inside_jokes') else 0
                
                self.memory_stats_label['text'] = f"Memorie: {memory_count} | Corruzioni: {corruption_count} | Inside Jokes: {inside_jokes_count}"
                
                # Memory uncertainty
                uncertainty_val = 0.0
                if hasattr(self.aurora, 'state') and 'memory_corruption' in self.aurora.state:
                    uncertainty_val = self.aurora.state['memory_corruption'].get('memory_uncertainty', 0.0)
                
                self.uncertainty_bar['value'] = uncertainty_val * 100
                self.uncertainty_label['text'] = f"{uncertainty_val:.2f}"
            
            # Update recent activities
            self.update_activities_display()
            
        except Exception as e:
            print(f"Errore nell'aggiornamento del display: {e}")
    
    def update_activities_display(self):
        """Update the recent activities display."""
        try:
            activities = []
            
            # Get recent autonomous choices
            if hasattr(self.aurora, 'state') and 'catharsis_epiphany' in self.aurora.state:
                catharsis = self.aurora.state['catharsis_epiphany']
                recent_choices = catharsis.get('autonomous_choices', [])[-3:]
                
                for choice in recent_choices:
                    timestamp = choice.get('timestamp', '')
                    choice_type = choice.get('choice_type', '')
                    aurora_chose = choice.get('aurora_chose', False)
                    
                    if timestamp:
                        try:
                            dt = datetime.fromisoformat(timestamp)
                            time_str = dt.strftime('%H:%M:%S')
                        except:
                            time_str = timestamp[:8]
                    else:
                        time_str = "N/A"
                    
                    status = "✅" if aurora_chose else "❌"
                    activities.append(f"{time_str} {status} {choice_type}")
            
            # Get recent memories
            if hasattr(self.aurora, 'memory_box') and self.aurora.memory_box:
                recent_memories = self.aurora.memory_box[-2:]
                for memory in recent_memories:
                    timestamp = memory.get('timestamp', '')
                    content = memory.get('content', '')[:50]
                    
                    if timestamp:
                        try:
                            dt = datetime.fromisoformat(timestamp)
                            time_str = dt.strftime('%H:%M:%S')
                        except:
                            time_str = timestamp[:8]
                    else:
                        time_str = "N/A"
                    
                    activities.append(f"{time_str} 💭 {content}...")
            
            # Update text area
            self.activities_text.delete(1.0, tk.END)
            for activity in activities:
                self.activities_text.insert(tk.END, activity + "\n")
            
        except Exception as e:
            print(f"Errore nell'aggiornamento delle attività: {e}")
    
    def run(self):
        """Start the dashboard."""
        self.root.mainloop()

def create_dashboard(aurora_instance):
    """Create and return a dashboard instance."""
    return AuroraDashboard(aurora_instance) 