#  smileFetch

Smilefetch is a program very similar to Fastfetch, but it uses a smaller version of the logo, remade from Fastfetch and containing only the necessary information (at least for me). It also updates in real time without flickering.

I'll soon be remaking art for all major distributions.

##  One-Line Installation

To install smileFetch on any major Linux distribution, just open your terminal and paste this command:

`curl -sL "https://raw.githubusercontent.com/BallOrInternet/smileFetch/refs/heads/main/install.sh" | bash`

##  How to Use

Once the installation is complete, you can run the program from any directory in your terminal by simply typing:

`smilefetch`

### ⚙️ Available Flags

You can customize the output using these command-line arguments:

* `smilefetch -s` or `smilefetch --static` — Print system info once and exit (no real-time loop). Perfect for adding to your `.bashrc`.
* `smilefetch -l <name>` or `smilefetch --logo <name>` — Force display a specific logo. Supported names: `arch`, `mint`, `cachy`. (e.g., `smilefetch -l mint`)
* `smilefetch -n` or `smilefetch --no-color` — Disable colored output (black and white mode).
* `smilefetch -h` or `smilefetch --help` — Show the automated help menu with all options.

To stop the real-time update and close the program, just press `Ctrl + C`.
##  Requirements
- Python 3
- \`rich\` library (the installer installs it automatically using your system package manager)
