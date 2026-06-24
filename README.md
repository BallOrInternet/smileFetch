<img width="901" height="276" alt="screenshot_2026-06-24_19-01-48" src="https://github.com/user-attachments/assets/68880246-655d-46b2-90fe-049c61511557" />


#  smileFetch

Smilefetch is a program very similar to Fastfetch, but it uses a smaller version of the logo, remade from Fastfetch and containing only the necessary information (at least for me). It also updates in real time without flickering.

I'll soon be remaking art for all major distributions.

##  One-Line Installation

To install smileFetch on any major Linux distribution, just open your terminal and paste this command:

`curl -sL "https://raw.githubusercontent.com/BallOrInternet/smileFetch/refs/heads/main/install.sh" | bash`

##  How to Use

Once the installation is complete, you can run the program from any directory in your terminal by simply typing:

`smilefetch`

<img width="847" height="250" alt="screenshot_2026-06-21_23-58-31" src="https://github.com/user-attachments/assets/b952c973-cd9c-4fac-b62d-545afae336cb" />

### 🎨 Supported Distro Logos
The program automatically detects your OS or lets you force change the logo using flags. Currently, the following custom-resized logos are built-in:
-  **Default Linux Tux** (for any unlisted distribution)
-  **Arch Linux** (work)
-  **Linux Mint** (work)
-  **CachyOS** (work)
-  **Manjaro Linux**

-  **CachyOS_old** 
-  **Linux Mint_old** 
-  **Default Linux Tux_old** 

<img width="814" height="248" alt="screenshot_2026-06-21_23-59-13" src="https://github.com/user-attachments/assets/110451b6-6b61-4a7c-b9c7-03bec0fdd31f" />

### Available Flags

You can customize the output using these command-line arguments:

* `smilefetch -s` or `smilefetch --static` — Print system info once and exit (no real-time loop). Perfect for adding to your `.bashrc`.
* `smilefetch -l <name>` or `smilefetch --logo <name>` — Force display a specific logo. Supported names: `arch`, `mint`, `cachy`. (e.g., `smilefetch -l mint`)
* `smilefetch -n` or `smilefetch --no-color` — Disable colored output (black and white mode).
* `smilefetch -h` or `smilefetch --help` — Show the automated help menu with all options.

To stop the real-time update and close the program, just press `Ctrl + C`.
##  Requirements
- Python 3
- \`rich\` library (the installer installs it automatically using your system package manager)

If you like this tool, please leave a star on GitHub!
