#!/usr/bin/env python3
import os
import platform
import time
import subprocess
from rich.console import Console
from rich.live import Live
from rich.table import Table

console = Console()

os.system('clear')
def get_logo(os_name):
    os_name = os_name.lower()      
    logo_cachy = [
        "    /'''''''''''/         ",
        "   /'''''''''''/   /      ",
        "  /''''''/                ",
        " /''''''/        /        ",
        "/''''''/         //       ",
        "\\......\\\                 ",
        " \\......\\\            //  ",
        "  \\......\\\          //   ",
        "   \\............../       ",
        "    \\............/        "
    ]

    logo_arch = [
        "         /\\\          ",
        "        /  \\\         ",
        "       /    \\\        ",
        "      /  ()  \\\       ",
        "     /   ||   \\\      ",
        "    /   /  \\   \\\     ",
        "   /   /    \\   \\\    ",
        "  /   /_    _\\   \\\   ",
        " /   /  |  |  \\   \\\  ",
        "/___/   |__|   \\___\\\ "
    ]

    logo_mint = [
        " ____________________     ",
        "|                    \\    ",
        "|_  |   ___________   |   ",
        "  | |  /  __   __  \  |   ",
        "  | |  | |  | |  | |  |   ",
        "  | |  | |  | |  | |  |   ",
        "  | |  | |  | |  | |  |   ",
        "  | |  \_/  \_/  | |  |   ",
        "  | \____________/_/  |   ",               
        "  \\___________________/   "
    ]

    logo_default = [
        "    .-----.       ",
        "   |(') (')|      ",
        "   |       |      ",
        "   |  :_/  |      ",
        "  //      \ \     ",
        " (|        | )    ",
        " |           |    ",
        "/'\_  ___ _/`\    ",
        "|   \    /    |   ",
        "\____)  (____/    "
    ]

    if "cachy" in os_name:
        return logo_cachy, "bold cyan"
    elif "arch" in os_name:
        return logo_arch, "bold blue"
    elif "mint" in os_name:
        return logo_mint, "bold green"
    else:
        return logo_default, "bold white"


def get_info():
    info = {}

    # 1 # кто вообще сидит (user)
    try:
        user = os.getlogin()
    except:
        user = os.environ.get('USER', 'user')

    info['user'] = f"{user}@{platform.node()}"

    # 2 # на каком диструбутиве (OS)
    with open("/etc/os-release") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("PRETTY_NAME="):
                info['os'] = line.split('"')[1]

    # 3 # ядрышко (Kernel)
    info['kernel'] = platform.release()

    # 4 # штука которая всё считает типо калькулятор (CPU)
    with open("/proc/cpuinfo") as f:
        for line in f:
            if "model name" in line:
                info['cpu'] = line.split(":")[1].strip()
                break

    # 5 # дорагая оперативка (RAM)
    with open("/proc/meminfo") as f:
        mem_data = {}
        for line in f:
            parts = line.split(":")
            mem_data[parts[0]] = parts[1].strip().split(" ")[0]

        total = int(mem_data['MemTotal']) // 1024 # в мегабайтики
        free = int(mem_data['MemAvailable']) // 1024
        used = total - free
        info['ram'] = f"{used}MB / {total}MB"

    # 6 # сколько ты сидишь на линуксе не перезагружаясь (Uptime)
    with open("/proc/uptime") as f:
        uptime_seconds = float(f.readline().split()[0])
        hours = int(uptime_seconds // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        info['uptime'] = f"{hours}h {minutes}m"

    # 7 # тоже недешёвая видюха (GPU)
    try:
        gpu_cmd = "lspci | grep -E 'VGA|3D'"
        gpu_info = subprocess.check_output(gpu_cmd, shell = True).decode().strip()
        info['gpu'] = gpu_info.split(":")[2].strip()
    except:
        info['gpu'] = "Unknown"

    # 8 # (base)
    info['base_os'] = "Independent"
    with open("/etc/os-release") as f:
        for line in f:
            if line.startswith("ID_LIKE="):
                info['base_os'] = line.split('=')[1].strip().replace('"', '').capitalize()

    # 9 #
    try:
        import datetime
        # Вытаскиваем первую строчку лога, где записана самая первая установка пакета
        cmd = "head -n 1 /var/log/pacman.log | awk -F'[][]' '{print $2}'"
        birth_raw = subprocess.check_output(cmd, shell=True).decode().strip()
        
        # Строка выглядит так: '2024-10-15T14:23:10+0300' или '2024-10-15 14:23'
        # Берем только дату (первые 10 символов: ГГГГ-ММ-ДД)
        date_str = birth_raw[:10]
        
        install_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        now = datetime.datetime.now()
        
        diff = now - install_date
        days = diff.days
        
        info['sys_age'] = f"{days} days (since {date_str})"
    except:
        info['sys_age'] = "Unknown"

    return info

def make_layout():
    data = get_info()
    logo, logo_color = get_logo(data['os'])

    colors = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    palette = "".join([f"[{c}]███[/{c}]" for c in colors])

    right_side = [
        f"[bold green]{data['user']}[/bold green]",
        "-" * len(data['user']),
        f"[bold cyan]OS:[/bold cyan]        {data['os']}",
        f"[bold cyan]base OS:[/bold cyan]   {data['base_os']}",
        f"[bold cyan]Kernel:[/bold cyan]    {data['kernel']}",
        f"[bold cyan]Uptime:[/bold cyan]    {data['uptime']}",
        f"[bold cyan]Sys age:[/bold cyan]   {data['sys_age']}",
        f"[bold cyan]CPU:[/bold cyan]       {data['cpu']}",
        f"[bold cyan]GPU:[/bold cyan]       {data['gpu']}",
        f"[bold cyan]RAM:[/bold cyan]       {data['ram']}",
        "",           
        f"           {palette}"
    ]

    output_lines = []
    max_lines = max(len(logo), len(right_side))

    for i in range(max_lines):
        l_part = f"[{logo_color}]{logo[i]}[/{logo_color}]" if i < len(logo) else " " * 23
        r_part = right_side[i] if i < len(right_side) else " "
        output_lines.append(f"{l_part}   {r_part}")

    return "\n".join(output_lines)

if __name__ == "__main__":
    with Live(make_layout(), console = console, refresh_per_second = 1) as live:
        while True:
            time.sleep(1)
            live.update(make_layout())