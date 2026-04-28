import socket
from utils.logger import save_log


def dns_lookup(domain):

    print(f"\nResolviendo {domain}...\n")

    try:
        ip = socket.gethostbyname(domain)

        print(f"[+] IP: {ip}")

        save_log("dns", {
            "domain": domain,
            "ip": ip
        })

    except Exception as e:
        print("[-] Error DNS:", str(e))

        save_log("dns", {
            "domain": domain,
            "error": str(e)
        })