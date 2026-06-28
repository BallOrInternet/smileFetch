#!/usr/bin/env python3
import os
import platform
import time
import subprocess
import datetime
from rich.console import Console
from rich.live import Live
from rich.table import Table

console = Console()

def clean_hardware_string(text):
    if not text:
        return "Unknown"
    # Убираем стандартный мусор из процессоров
    for trash in ["(R)", "(TM)", "CPU", "@", "Processor", "Core"]:
        text = text.replace(trash, "")
    # Очищаем от длинных заводских названий видеокарт AMD/NVIDIA
    if "Advanced Micro Devices" in text or "AMD/ATI" in text:
        if "[" in text and "]" in text:
            # Вытаскиваем чистое коммерческое название из квадратных скобок (например, Radeon RX 6700 XT)
            text = text.split("[")[-1].split("]")[0].replace("Radeon", "").strip()
            text = f"AMD Radeon {text}"
    elif "NVIDIA" in text:
        if "[" in text and "]" in text:
            text = text.split("[")[-1].split("]")[0].strip()
            text = f"NVIDIA {text}"
            
    # Убираем двойные пробелы, которые могли остаться после удаления слов
    return " ".join(text.split()).strip()

os.system('clear')
def get_logo(logo_name):
    logo_name = str(logo_name).lower().strip()
    logo_cachy_old = [
        r"    /,,,,...../           ",
        r"   /,,,.,,,../   ()       ",
        r"  /,,,,../                ",
        r" /,,,.../     /'\         ",
        r"/,...../      \,/         ",
        r"\,,,,,,\\            _    ",
        r" \,,....\\          / \   ",
        r"  \...,..\\         \_/   ",
        r"   \..,,,,,,,,,,,,/       ",
        r"    \,,........,,/        "
    ]

    logo_mint_old = [
        r" ____________________     ",
        r"|                    \    ",
        r"|_  |   ___________   |   ",
        r"  | |  /  __   __  \  |   ",
        r"  | |  | |  | |  | |  |   ",
        r"  | |  | |  | |  | |  |   ",
        r"  | |  | |  | |  | |  |   ",
        r"  | |  \_/  \_/  | |  |   ",
        r"  | \____________/_/  |   ",               
        r"  \___________________/   "
    ]

    logo_default_old = [
        r"    .-----.       ",
        r"   |(') (')|      ",
        r"   |       |      ",
        r"   |  :_/  |      ",
        r"  //      \ \     ",
        r" (|        | )    ",
        r" |           |    ",
        r"/'\_  ___ _/`\    ",
        r"|   \    /    |   ",
        r"\____)  (____/    "
    ]

    logo_cachy = [
        r"    [bold blue]/,,,,[/][bold green]...../[/]           ",
        r"   [bold blue]/,,,[/][bold green]..[/][bold blue],,[/][bold green]../[/]   [bold cyan]()[/]       ",
        r"  [bold blue]/,,,,[/][bold green]../[/]                ",
        r" [bold blue]/,,,[/][bold green].../[/]     [bold cyan]/'\\[/]         ",
        r"[bold blue]/,[/][bold green]...../[/]      [bold cyan]\,/[/]         ",
        r"[bold blue]\,,,,,,\\\\[/]             [bold cyan]_[/]   ",
        r" [bold blue]\,,[/][bold green]....\\\\[/]           [bold cyan]/ \\[/]  ",
        r"  [bold green]\...[/][bold blue],[/][bold green]..\\\\[/]          [bold cyan]\_/[/]  ",
        r"   [bold green]\..[/][bold blue],,,,,,,,,,,,/[/]       ",
        r"    [bold green]\\[/][bold blue],,[/][bold green]........[/][bold blue],,/[/]        "
    ]

    logo_mint = [
        r"[bold green] ____________________     [/]",
        r"[bold green]|                    \    [/]",
        r"[bold green]|_  [/][bold white]|   ___________[/][bold green]   |[/]   ",
        r"[bold green]  | [/][bold white]|  /  __   __  \\[/][bold green]  |[/]   ",
        r"[bold green]  | [/][bold white]|  | |  | |  | |[/][bold green]  |[/]   ",
        r"[bold green]  | [/][bold white]|  | |  | |  | |[/][bold green]  |[/]   ",
        r"[bold green]  | [/][bold white]|  | |  | |  | |[/][bold green]  |[/]   ",
        r"[bold green]  | [/][bold white]|  \_/  \_/  | |[/][bold green]  |[/]   ",
        r"[bold green]  | [/][bold white]\____________/_/[/][bold green]  |[/]   ",               
        r"[bold green]  \___________________/   [/]"
    ]

    logo_default = [
        r"[bold black]    .-----.       [/]",
        r"[bold black]   |([/][bold white]'[/][bold black]) ([/][bold white]'[/][bold black])|[/]      ",
        r"[bold black]   |       |      [/]",
        r"[bold black]   |  [/][bold yellow]:_/[/]  [bold black]|[/]      ",
        r"[bold black]  /[/][bold white]/      \\[/] [bold black]\     [/]",
        r"[bold black] ([/][bold white]|        |[/] [bold black])    [/]",
        r"[bold black] |           |    [/]",
        r"[bold yellow]/'\_[/][bold black]  ___ [/][bold yellow]_/`\    [/]",
        r"[bold yellow]|   \    /    |   [/]",
        r"[bold yellow]\____)  (____/    [/]"
    ]

    logo_arch = [
        r"         /\\          ",
        r"        /  \\         ",
        r"       /    \\        ",
        r"      /      \\       ",
        r"     /        \\      ",
        r"    /   .--.   \\     ",
        r"   /   |    |   \\    ",
        r"  /    ;    ;    \\   ",
        r" /   _,|    |,_   \\  ",
        r"/,.-'          '-.,\\ "
    ]

    pop_os = [
        r"         , - ~ ~ ~ -,         "
        r"     , '             ',     "
        r"   ,                    ,   "
        r"  ,                      ,  "
        r" ,                        , "
        r" ,                        , "
        r" ,                        , "
        r"  ,                       ,  "
        r"   ,                     ,   "
        r"     ,                 ,'    "
        r"       ' - , _ _ _ ,  '       "
    ]

    logo_manjaro = [
        r" ____________   _____      ",
        r"|            | |     |     ",
        r"|     _______| |     |     ",
        r"|    |  _____  |     |     ",
        r"|    | |     | |     |     ",
        r"|    | |     | |     |     ",
        r"|    | |     | |     |     ",
        r"|    | |     | |     |     ",
        r"|    | |     | |     |     ",
        r"|____| |_____| |_____|     "
    ]

    logo_debian = [
        r"      ,--.          ",
        r"    ./     '        ",
        r"   /                ",
        r"  /                  ",
        r" |                 ",
        r" |                  ",
        r"  \                 ",
        r"   \.                ",
        r"     \.             ",
        r"      '-.._            "
    ]

    if "cachy_old" in logo_name:
        return logo_cachy_old, "bold cyan"
    elif "default_old" in logo_name:
        return logo_default_old, "bold white"
    elif "mint_old" in logo_name:
        return logo_mint_old, "bold green"
    elif "cachy" in logo_name:
        return logo_cachy, "none"
    elif "arch" in logo_name:
        return logo_arch, "bold blue"
    elif "mint" in logo_name:
        return logo_mint, "none"
    elif "manjaro" in logo_name:
        return logo_manjaro, "bold green"
    else:
        return logo_default, "none"


def get_info():
    info = {}

    # 1 # кто вообще сидит (user)
    try:
        user = os.getlogin()
    except:
        user = os.environ.get('USER', 'user')

    info['user'] = f"{user}@{platform.node()}"

    # 2 # на каком диструбутиве (OS)
    info['os'] = "Linux"
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
    try:
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("ID_LIKE="):
                    info['base_os'] = line.split('=')[1].strip().replace('"', '').capitalize()
    except:
        pass

    # 9 # Возраст системы
    try:
        import datetime
        date_str = None

        if os.path.exists("/var/log/pacman.log"):
            cmd = "head -n 1 /var/log/pacman.log | awk -F'[][]' '{print $2}'"
            birth_raw = subprocess.check_output(cmd, shell=True).decode().strip()
            date_str = birth_raw[:10] 

        elif os.path.exists("/etc/timezone"):
            install_time = os.path.getctime("/etc/timezone")
            install_date = datetime.datetime.fromtimestamp(install_time)
            date_str = install_date.strftime("%Y-%m-%d")

        elif os.path.exists("/var/log/dpkg.log"):
            cmd = "head -n 1 /var/log/dpkg.log | awk '{print $1}'"
            date_str = subprocess.check_output(cmd, shell=True).decode().strip()

        if date_str:
            install_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            now = datetime.datetime.now()
            diff = now - install_date
            days = diff.days
            info['sys_age'] = f"{days} days (since {date_str})"
        else:
            raise Exception()
    except:
        info['sys_age'] = "Unknown"

    return info

def make_layout(forced_logo = None, minimal = False):

    data = get_info()
    logo_target = forced_logo if forced_logo else data['os']
    logo, logo_color = get_logo(logo_target)

    # Если флаг вызван, очищаем строки железа, иначе оставляем как есть
    display_cpu = clean_hardware_string(data['cpu']) if minimal else data['cpu']
    display_gpu = clean_hardware_string(data['gpu']) if minimal else data['gpu']

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
        f"[bold cyan]CPU:[/bold cyan]       {display_cpu}", # Используем новые переменные
        f"[bold cyan]GPU:[/bold cyan]       {display_gpu}", # вместо data['cpu'] и data['gpu']
        f"[bold cyan]RAM:[/bold cyan]       {data['ram']}",
        "",           
        f"           {palette}"
    ]

    output_lines = []
    max_lines = max(len(logo), len(right_side))

    for i in range(max_lines):
        if i < len(logo):
            if logo_color == "none":
                l_part = logo[i]
            else:
                l_part = f"[{logo_color}]{logo[i]}[/{logo_color}]"
        else:
            fallback_width = len(logo[0]) if logo else 23
            l_part = " " * fallback_width
            
        r_part = right_side[i] if i < len(right_side) else " "
        output_lines.append(f"{l_part}   {r_part}")

    return "\n".join(output_lines)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="smileFetch — A customizable real-time system fetch utility."
    )
    
    parser.add_argument(
        '-s', '--static', 
        action='store_true', 
        help='Print system info once and exit (no real-time loop)'
    )
    parser.add_argument(
        '-n', '--no-color', 
        action='store_true', 
        help='Disable colored output'
    )

    parser.add_argument(
        '-l', '--logo', 
        type=str, 
        default=None,
        help='Force display a specific logo (e.g., arch, mint, cachy, cachy_old, manjaro)'
    )

    parser.add_argument(
        '-m', '--minimal', 
        action='store_true', 
        help='Clean and shorten CPU and GPU strings for a minimalist look'
    )


    args = parser.parse_args()

    if args.no_color:
        console = Console(color_system=None)

    os.system('clear')

    if args.static:
        console.print(make_layout(forced_logo=args.logo, minimal=args.minimal))
    else:
        try:
            with Live(make_layout(forced_logo=args.logo, minimal=args.minimal), console=console, refresh_per_second=1) as live:
                while True:
                    time.sleep(1)
                    live.update(make_layout(forced_logo=args.logo, minimal=args.minimal))
        except KeyboardInterrupt:
            print("")
