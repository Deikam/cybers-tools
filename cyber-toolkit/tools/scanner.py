import socket
import time
from concurrent.futures import ThreadPoolExecutor
from utils.logger import save_log


def check_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.25)

        if s.connect_ex((ip, port)) == 0:
            s.close()
            return port

        s.close()
    except:
        return None


def scan(ip, start, end):

    print(f"\nEscaneando {ip} ({start}-{end})...\n")

    open_ports = []
    total = end - start + 1
    checked = 0

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=120) as executor:
        results = executor.map(lambda p: check_port(ip, p), range(start, end + 1))

        for r in results:
            checked += 1

            # porcentaje
            percent = (checked / total) * 100

            # progreso visual simple
            if checked % 200 == 0 or checked == total:
                elapsed = time.time() - start_time
                speed = checked / elapsed if elapsed > 0 else 0
                remaining = (total - checked) / speed if speed > 0 else 0

                print(f"\n[{percent:.1f}%] Escaneados {checked}/{total}")
                print(f"Velocidad: {speed:.0f} puertos/s")
                print(f"ETA: {remaining:.1f} seg\n")

            if r is not None:
                print(f"[+] Puerto abierto: {r}")
                open_ports.append(r)

    elapsed_total = time.time() - start_time

    save_log("scanner", {
        "ip": ip,
        "range": f"{start}-{end}",
        "open_ports": open_ports,
        "total_checked": total,
        "found": len(open_ports),
        "time_seconds": round(elapsed_total, 2)
    })

    print("\n======================")
    print(" ESCANEO COMPLETADO")
    print("======================")
    print(f"Puertos abiertos: {len(open_ports)}")
    print(f"Tiempo: {elapsed_total:.2f}s\n")