#!/usr/bin/env bash

echo -e "\e[1;36m=== Installing smileFetch ===\e[0m"

# 1. Определяем менеджер пакетов и ставим библиотеку rich
if command -v pacman &> /dev/null; then
    sudo pacman -S --noconfirm python-rich
elif command -v apt-get &> /dev/null; then
    sudo apt-get update && sudo apt-get install -y python3-rich
elif command -v dnf &> /dev/null; then
    sudo dnf install -y python3-rich
elif command -v zypper &> /dev/null; then
    sudo zypper install -y python3-rich
else
    # Если пакетного менеджера нет, ставим через стандартный питоновский pip
    pip3 install rich --break-system-packages
fi

# 2. Скачиваем сам скрипт smilefetch.py с твоего GitHub
curl -sL "githubusercontent.com" -o /tmp/smilefetch

# 3. Переносим скачанный файл в системную папку бинарников и даем права на запуск
sudo mv /tmp/smilefetch /usr/local/bin/smilefetch
sudo chmod +x /usr/local/bin/smilefetch

echo -e "\e[1;32m=== Installation complete! Run: smilefetch ===\e[0m"
