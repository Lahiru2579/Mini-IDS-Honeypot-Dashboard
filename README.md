# 🚨 Mini IDS & Honeypot Dashboard

Welcome to my **Castle Guard** system! This project is a network security tool that watches for "sneaky people" (hackers) trying to enter my computer through backdoors.

## 🏰 How it Works
This project uses three main parts working together:

* **The Trap (Honeypot):** A fake "treasure chest" on port 2222. If anyone touches it, an alarm goes off!
* **The Guard (IDS Sniffer):** Uses `Scapy` to watch network traffic for people trying to use suspicious doors like SSH (22) or Telnet (23).
* **The Command Center (Dashboard):** A web page built with `Flask` that shows all alerts in real-time with cool colors!

## 🛠️ Tools Used
* **Python:** The main language used to write the logic.
* **Flask:** To create the web dashboard.
* **Scapy:** To sniff the network packets like a digital bloodhound.
* **HTML/CSS:** To make the dashboard look like a professional security screen.

## 🚀 How to Run
1. Make sure you have Python installed.
2. Install the needs: `pip install flask scapy`
3. Create a test.py and run this.
   from scapy.all import get_if_list, get_if_addr

   for iface in get_if_list():
    try:
        print(iface, "->", get_if_addr(iface))
    except:
        pass
4. Get the interface ID
   #A real IP like 192.168.x.x or 10.x.x.x
5. Please add the **interface ID Here** that I mentioned to the files `dashboard_ids.py` and `honeypot.py`.
6. Run the dashboard (as Administrator/Sudo):
   ```bash
   python dashboard_ids.py
