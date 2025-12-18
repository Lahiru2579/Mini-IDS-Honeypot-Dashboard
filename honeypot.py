import socket
import time  # Added to prevent crash in the main loop
from datetime import datetime


def start_honeypot(push_alert, port=2222):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", port))
    s.listen(5)

    print(f"🍯 Honeypot active on port {port}...")

    while True:
        conn, addr = s.accept()

        # This sends data directly to the IDS dashboard's alert list
        push_alert({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "src": addr[0],
            "dst": "HONEYPOT_SERVICE",
            "port": port,
            "type": "HONEYPOT"
        })

        conn.close()