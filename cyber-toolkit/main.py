from colorama import init, Fore, Style
init()

import os
import json

from tools.scanner import scan
from tools.ping import ping
from tools.dns import dns_lookup
from tools.http_check import check_http


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print(Fore.CYAN + "\n======================")
    print("   CYBER TOOLKIT PRO")
    print("======================\n" + Style.RESET_ALL)


def menu():
    print(Fore.YELLOW + "1. Port Scanner")
    print("2. Ping Tool")
    print("3. DNS Lookup")
    print("4. HTTP Check")
    print("5. Ver historial")
    print("0. Salir" + Style.RESET_ALL)


def scanner():
    ip = input(Fore.GREEN + "\nIP objetivo: " + Style.RESET_ALL).strip()

    while True:
        print("\nModo de escaneo:")
        print("1. Rápido (1-100)")
        print("2. Normal (1-1024)")
        print("3. Profundo (1-5000)")

        m = input("Modo: ").strip()

        if m == "1":
            scan(ip, 1, 100)
            break
        elif m == "2":
            scan(ip, 1, 1024)
            break
        elif m == "3":
            scan(ip, 1, 5000)
            break
        else:
            print(Fore.RED + "Modo inválido, intenta otra vez" + Style.RESET_ALL)


def show_history():

    path = os.path.join("reports", "history.json")

    if not os.path.exists(path):
        print(Fore.RED + "\nNo hay historial todavía.\n" + Style.RESET_ALL)
        input("Enter para continuar...")
        return

    with open(path, "r") as f:
        history = json.load(f)

    print(Fore.CYAN + "\n===== HISTORIAL (últimas 10 ejecuciones) =====\n" + Style.RESET_ALL)

    for entry in history[-10:]:
        print(f"{Fore.YELLOW}[{entry['timestamp']}] {entry['tool']}{Style.RESET_ALL}")
        print(f"  {entry['data']}\n")

    input("Enter para continuar...")


def run():
    while True:
        clear()
        banner()
        menu()

        op = input(Fore.GREEN + "\nOpción: " + Style.RESET_ALL).strip()

        if op == "0":
            print(Fore.CYAN + "Saliendo..." + Style.RESET_ALL)
            break

        elif op == "1":
            scanner()

        elif op == "2":
            ip = input("IP objetivo: ").strip()
            ping(ip)

        elif op == "3":
            domain = input("Dominio: ").strip()
            dns_lookup(domain)

        elif op == "4":
            host = input("Host: ").strip()
            check_http(host)

        elif op == "5":
            show_history()

        else:
            print(Fore.RED + "Opción inválida" + Style.RESET_ALL)
            input("Enter para continuar...")


if __name__ == "__main__":
    run()