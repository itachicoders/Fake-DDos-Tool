import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import time
import random
import re

# Функция для имитации DDoS-атаки
def simulate_ddos(target, duration, update_progress):
    total_steps = 100
    for step in range(total_steps):
        time.sleep(duration / total_steps)
        ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        update_progress(step + 1, f"Отправка пакета с IP: {ip} на {target}")
    update_progress(total_steps, "Атака завершена успешно!")

# Функция запуска атаки
def start_attack():
    target = target_entry.get()
    duration = float(duration_entry.get())
    progress_bar['value'] = 0
    log_text.delete('1.0', tk.END)
    status_var.set("Атака начата...")
    
    def update_progress(step, message):
        progress_bar['value'] = step
        log_text.insert(tk.END, message + "\n")
        log_text.see(tk.END)
        window.update_idletasks()
        if step == 100:
            status_var.set("Атака завершена успешно!")
    
    threading.Thread(target=simulate_ddos, args=(target, duration, update_progress)).start()

def validate_input(input_str):
    return re.match("^[a-zA-Z0-9.]*$", input_str) is not None

def validate_inputs(input_str):
    return re.match("^\d*$", input_str) is not None

window = tk.Tk()
window.title("DDoS Tool")
window.geometry("600x450")
window.configure(bg="black")

# Изменения стилей
style = ttk.Style()
style.theme_use('clam')
style.configure('Hacker.TLabel', foreground='lime', background='black', font=('Courier New', 10))
style.configure('Hacker.TButton', foreground='lime', background='black', font=('Courier New', 10))
style.configure('Hacker.TEntry', foreground='lime', background='black', font=('Courier New', 10))
style.configure('Hacker.Horizontal.TProgressbar', troughcolor='black', bordercolor='black', background='green')

input_frame = ttk.Frame(window, padding="10", style='Hacker.TLabel')
input_frame.pack(padx=10, pady=10, fill='x')

target_label = ttk.Label(input_frame, text="Цель атаки:", style='Hacker.TLabel')
target_label.grid(row=0, column=0, padx=(0, 10), sticky="w")

validate_cmd = window.register(validate_input)
validate_cmds = window.register(validate_inputs)
target_entry = ttk.Entry(input_frame, validate="key", validatecommand=(validate_cmd, '%S'), font=('Courier New', 10))
target_entry.grid(row=0, column=1, sticky="ew")

duration_label = ttk.Label(input_frame, text="Продолжительность (сек):", style='Hacker.TLabel')
duration_label.grid(row=1, column=0, padx=(0, 10), pady=(10, 0), sticky="w")

duration_entry = ttk.Entry(input_frame, validate="key", validatecommand=(validate_cmds, '%S'), font=('Courier New', 10))
duration_entry.grid(row=1, column=1, sticky="ew", pady=(10, 0))

attack_button = ttk.Button(window, text="Начать атаку", command=start_attack, style='Hacker.TButton')
attack_button.pack(pady=10)

progress_bar = ttk.Progressbar(window, orient='horizontal', length=400, mode='determinate', style='Hacker.Horizontal.TProgressbar')
progress_bar.pack(padx=10, fill='x')

log_text = scrolledtext.ScrolledText(window, height=10, width=60, bg="black", fg="lime", insertbackground="lime", font=('Courier New', 10))
log_text.pack(padx=10, pady=5, fill='both', expand=True)

status_var = tk.StringVar()
status_var.set("Готово к началу атаки...")
status_bar = ttk.Label(window, textvariable=status_var, relief=tk.SUNKEN, anchor="w", style='Hacker.TLabel')
status_bar.pack(side='bottom', fill='x')

window.mainloop()
