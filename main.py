
import tkinter as tk
from pynput import keyboard

class KeystrokeVisualizer:
    def __init__(self):
        # GUI Setup
        self.root = tk.Tk()
        self.root.title("Keystroke Visualizer")
        self.root.geometry("300x100+10+10") # Position oben links
        self.root.overrideredirect(True) # Fensterrahmen entfernen
        self.root.attributes("-alpha", 0.8) # Transparenz
        self.root.attributes("-topmost", True) # Immer im Vordergrund
        self.key_text = ""
        self.key_counter = 1

        self.old_key = ""
        self.key_meta = ""

        self.label = tk.Label(self.root, text="Drücke Tasten...", font=("Arial", 24), fg="white", bg="black")
        self.label.pack(expand=True, fill='both')

        self.lblCounter = tk.Label(self.root, text="", font=("Arial", 24), fg="white", bg="black")
        self.lblCounter.pack(expand=True, fill='both')

        # Pynput Listener
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
    
        # GUI Hauptschleife
        self.root.mainloop()

    def on_press(self, key):
        try:
            if key.char == self.old_key:
                self.key_counter += 1
                self.old_key = key.char
            else:
                self.old_key = key.char
                self.key_text = f"{self.key_meta}  {key.char}"
                self.key_counter = 1
        except AttributeError:
            self.key_meta = f"{key.name}"
        
        self.label.after(0, self.update_label, self.key_text)
        self.lblCounter.after(0, self.update_lblCounter, f"x{self.key_counter}")

    def on_release(self, key):
        self.key_meta = f""
        

        # Beenden mit ESC
        if key == keyboard.Key.esc:
            self.root.quit()

    def update_label(self, text):
        self.label.config(text=text)

    def update_lblCounter(self, text):
        self.lblCounter.config(text=text)


if __name__ == "__main__":
    KeystrokeVisualizer()
