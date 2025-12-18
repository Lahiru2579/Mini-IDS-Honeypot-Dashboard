from flask import Flask, render_template
from scapy.all import sniff, IP, TCP
from threading import Thread
from datetime import datetime
from honeypot import start_honeypot

app = Flask(__name__)
alerts = []


def add_alert(alert):
    # Insert at index 0 so the newest alerts appear at the top of the table
    alerts.insert(0, alert)


def detect_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        if packet[TCP].dport in [22, 23, 3389, 2000, 443]:
            add_alert({
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "src": packet[IP].src,
                "dst": packet[IP].dst,
                "port": packet[TCP].dport,
                "type": "NETWORK"
            })


def start_sniffing():
    # Replace the iface string with your actual interface ID if necessary
    iface = r" interface ID Here"
    sniff(iface=iface, prn=detect_packet, store=False)


@app.route("/")
def dashboard():
    return render_template("dashboard.html", alerts=alerts)


if __name__ == "__main__":
    # Start Honeypot Thread
    Thread(target=start_honeypot, args=(add_alert,), daemon=True).start()
    # Start IDS Sniffer Thread
    Thread(target=start_sniffing, daemon=True).start()
    # run with use_reloader=False to prevent double-binding the Honeypot port
    app.run(debug=True, use_reloader=False)
