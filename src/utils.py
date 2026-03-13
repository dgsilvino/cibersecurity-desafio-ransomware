from colorama import Fore, Style, init

# Inicializa o colorama para Windows
init(autoreset=True)


def log_info(message):
    print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} {message}")


def log_success(message):
    print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} {message}")


def log_error(message):
    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {message}")
