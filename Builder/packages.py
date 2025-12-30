from utils.schemes import DistributionPackages, PackageInfo, Packages

BASE = Packages(
    pacman=DistributionPackages(
        common=[  
            ##==> Base tools and daemons
            ###########################################
            "base-devel", "git", "networkmanager", "libnotify", "bluez", 
            "bluez-utils", "playerctl", "upower", "brightnessctl", 
            "udiskie", "xdg-desktop-portal-gtk", "xdg-desktop-portal",
            "mkinitcpio", "xorg-server-xvfb", "gobject-introspection",
            "power-profiles-daemon", "gvfs-mtp", "android-udev",
            "pacman-contrib", "sudo", "fakeroot", "uthash", "gzip", 
            "usbutils", "dpkg", "cmake", "clang", "gcc", "automake", 
            "make", "meson", "ninja",

            ##==> Audio
            ###########################################
            "pipewire-jack", "pipewire-alsa", "wireplumber", 
            "python-pyalsa", "pavucontrol", "pamixer", "pipewire", 
            "pipewire-pulse", "pipewire-audio", "sof-firmware",
            "gst-libav", "gst-plugins-base", "gst-plugins-good", 
            "gst-plugins-bad", "gst-plugins-ugly",
            
            ##==> CLI-Tools
            ###########################################
            "jq", "fastfetch", "lsd", "bat", "micro", "sudo",
            "btop", "yazi", "starship", "openssh", "sshfs", 
            "wget", "neovim", "tmux", "ffmpeg", "cliphist",
            "tree", "bash-completion", "parallel", "netcat", "mat2", 
            "ranger", "cowsay", "pyenv", "shellcheck", "lazygit", 
            "htop", "nmap", "reflector", "openvpn", 
            "networkmanager-openvpn", "wireguard-tools", "netctl",

            ##==> GUI 
            ###########################################
            "sddm", "plymouth", "firefox", "kitty", "blueman", "file-roller", "nemo", 
            "nemo-fileroller", "gvfs", "ffmpegthumbnailer", "imagemagick", 
            "vlc", "loupe", "qt5ct", "qt6ct", "qt5-graphicaleffects", 
            "qt5-svg", "qt5-multimedia", "qt5-quickcontrols2", "gst-plugins-good", 
            "redshift", "zenity", "polkit-gnome", "gnome-disk-utility", "rofimoji",
            "flameshot", "rofi", "qalculate-gtk", "dunst", "wmname", "clipnotify",
            "evince", "libreoffice-fresh", "timeshift",
            
            ##==> Archives & Files
            ###########################################
            "ark", "p7zip", "unrar", "zip", "unzip", "gparted",
            
            ##==> Development Tools
            ###########################################
            "python", "python-pip", "python-poetry", "python-virtualenv", 
            "python-pipx", "python-pytest", "python-black", "python-isort", 
            "python-flake8", "mypy", "python-pre-commit",
            "go", "go-tools", "golangci-lint", "nginx",
            "nodejs", "npm", "yarn", "typescript", "typescript-language-server",
            "dbeaver", "ansible", "kubectl", "helm",
            "postgresql", "postgresql-libs",
            
            ##==> Git Tools
            ###########################################
            "github-cli", "git-lfs", "git-delta", "tig",
            
            ##==> Fonts
            ###########################################
            "ttf-hack-nerd", "noto-fonts", "noto-fonts-cjk", 
            "noto-fonts-emoji", "noto-fonts-extra", "ttf-iosevka-nerd", 
            "ttf-jetbrains-mono", "ttf-jetbrains-mono-nerd", 
            "ttf-fira-code", "ttf-dejavu", "ttf-liberation",
        ],
        bspwm_packages=[
            "xorg-server", "bspwm", "sxhkd", "xorg-xinit", "xclip", "feh", 
            "wmname", "polybar", "xorg-xrandr", "xsettingsd", "clipnotify",
            "dunst", "xorg-xsetroot", "picom"
        ],
        hyprland_packages=[
            "hyprland", "waybar", "hyprlock", "swww", "wl-clipboard", 
            "xdg-desktop-portal-hyprland", "qt5-wayland", "qt6-wayland",
            "xdg-desktop-portal-wlr", "hypridle", "hyprpicker", "wlr-randr",
            "uwsm", "libnewt", "swaync", "wl-clip-persist", "cliphist",
        ]
    ),
    aur=DistributionPackages(
        common=[
            ##==> System
            ###########################################
            "meowrch-settings", "meowrch-tools", "update-grub",
            "grub-customizer", "downgrade", "vault", "gitflow-avh",
            "flutter", "docker-desktop", "lazydocker",

            ##==> GUI
            ###########################################
            "visual-studio-code-bin", "nemo-tags", "hotkeyhub-bin",
            "insomnia-bin", "zen-browser-bin", "yandex-browser",
            "drawio-desktop", "wireshark-qt", "gnome-calculator-gtk3",
            
            ##==> Customization: Themes, icons and cursors
            ###########################################
            "bibata-cursor-theme-bin", "tela-circle-icon-theme-dracula",
            "pawlette", "oomox", "papirus-icon-theme",
            
            ##==> CLI-Tools
            ###########################################
            "cava", "pokemon-colorscripts", "youtube-dl",
            
            ##==> Fonts
            ###########################################
            "ttf-meslo-nerd-font-powerlevel10k",
        ],
        bspwm_packages=["xkb-switch", "i3lock-color"],
        hyprland_packages=[
            "hyprprop", "grimblast-git", "mewline", "hyprpicker",
            "swaylock-effects-git", "wlr-randr-git", "grimblast-git"
        ]
    )
)

DRIVERS = {
    "intel": Packages(
        pacman=DistributionPackages(
            common=[
                "lib32-mesa",
                "vulkan-intel",
                "lib32-vulkan-intel",
                "vulkan-icd-loader",
                "lib32-vulkan-icd-loader",
                "intel-media-driver",
                "libva-intel-driver",
                "xf86-video-intel",
            ]
        )
    ),
    "amd": Packages(
        pacman=DistributionPackages(
            common=[
                "lib32-mesa",
                "vulkan-radeon",
                "lib32-vulkan-radeon",
                "vulkan-icd-loader",
                "lib32-vulkan-icd-loader",
            ]
        )
    ),
    "nvidia": Packages(
        pacman=DistributionPackages(
            common=[
                "nvidia-dkms",
                "nvidia-utils",
                "lib32-nvidia-utils",
                "nvidia-settings",
                "vulkan-icd-loader",
                "lib32-vulkan-icd-loader",
                "lib32-opencl-nvidia",
                "opencl-nvidia",
                "libxnvctrl",
            ]
        )
    ),
}

CUSTOM = {
    "useful": {
        "timeshift": PackageInfo("A system restore utility for Linux", recommended=True)
    },
    "development": {
        "obsidian": PackageInfo("A powerful knowledge base that works on top of a local folder of plain text Markdown files", recommended=True, aur=True),
        "postgresql": PackageInfo("Sophisticated object-relational DBMS", recommended=True),
        "pgadmin4-desktop": PackageInfo("The desktop user interface for pgAdmin", aur=True, recommended=True),
        "redis": PackageInfo("An in-memory database that persists on disk")
    },
    "social_media": {
        "telegram-desktop": PackageInfo("Popular messenger", recommended=True, selected=True, aur=True),
        "discord": PackageInfo("Popular social platform", recommended=True, aur=True),
        "vesktop": PackageInfo("Custom Discord client", recommended=True, aur=True)
    },
    "games": {
        "steam": PackageInfo("The best launcher for games", recommended=True, selected=True), 
        "gamemode": PackageInfo("Game optimization tool", recommended=True, selected=True), 
        "mangohud": PackageInfo("Displays metrics in running games"),
        "portproton": PackageInfo("Launcher for Windows games with good optimization", recommended=True, aur=True)
    },
    "entertainment": {
        "yandex-music": PackageInfo("Personal recommendations, selections for any occasion and new music", aur=True, recommended=True),
        "spotify": PackageInfo("A proprietary music streaming service", aur=True, recommended=True)
    },
    "office": {
        "libreoffice-fresh": PackageInfo("Comprehensive office suite for word processing, spreadsheets, and presentations"),
        "onlyoffice-bin": PackageInfo("Office suite that allows collaborative editing of documents", aur=True, recommended=True),
        "evince": PackageInfo("Document viewer", selected=True, recommended=True)
    },
    "optional_tools": {
        "redis": PackageInfo("In-memory database", recommended=False),
        "mangohud": PackageInfo("Game overlay for monitoring", recommended=False),
    }
}