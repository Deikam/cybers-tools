import platform
import os
from utils.logger import save_log


def ping(ip):

    print(f"\nPing a {ip}...\n")

    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"

    response = os.system(f"ping {param} {ip}")

    status = "activo" if response == 0 else "sin respuesta"

    if status == "activo":
        print("[+] Host activo")
    else:
        print("[-] Sin respuesta")

    save_log("ping", {
        "ip": ip,
        "status": status
    })