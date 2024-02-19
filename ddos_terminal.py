from rich.console import Console
from rich.progress import track
from time import sleep
import random

console = Console()

def simulate_ddos(target, duration):
    console.print(f"[bold magenta]Начало имитации DDoS-атаки на {target}[/bold magenta]")
    
    for step in track(range(100), description="[bold green]Прогресс атаки...[/]"):
        sleep(duration / 100.0)  # Имитация задержки
        if step % 10 == 0:  # Имитация логов атаки
            ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            console.log(f"[bold red]Отправка пакета[/] с IP: {ip} на {target}")
    
    console.print("[bold green]Атака завершена успешно![/]")

if __name__ == "__main__":
    target = console.input("[bold cyan]Введите цель атаки (например, 177.183.33.97): [/]")
    duration = float(console.input("[bold cyan]Введите продолжительность атаки в секундах (например, 5): [/]"))
    simulate_ddos(target, duration)
