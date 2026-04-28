import socket
from utils.logger import save_log


def check_http(host):

    print(f"\nComprobando HTTP en {host}...\n")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        result = s.connect_ex((host, 80))

        if result == 0:
            status = "activo"
            print("[+] HTTP activo")
        else:
            status = "no accesible"
            print("[-] HTTP no accesible")

        s.close()

        save_log("http", {
            "host": host,
            "status": status
        })

    except Exception as e:
        print("Error HTTP:", str(e))