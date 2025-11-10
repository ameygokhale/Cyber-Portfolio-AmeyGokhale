# Bettercap Setup & ARP Spoofing 

This README walks through the steps to set up **bettercap** on Kali Linux and perform ARP spoofing (up to enabling ARP spoofing in full-duplex). All example screenshots included in this package have been **sanitized** to remove IPs, MACs and other sensitive on-screen data.

---

## Prerequisites
- Kali Linux (updated)
- VirtualBox (or any VM host) with the Kali VM powered on
- Internet connection to install packages

---

## Steps
1. **Find your system IP and default gateway**
   - In the Kali terminal, determine your IP address:
     ```bash
     ifconfig
     ```
2. **Get the ARP table/gateway MAC**
   - List cached ARP entries (example):
     ```bash
     arp -a
     ```
   - This will show IP ↔ MAC mappings (the package screenshots included here have been sanitized).

3. **Start your Kali VM**
   - Open VirtualBox and start the Kali VM (double-click or press the VM “Start” button).

4. **Open a terminal in Kali**

5. **Update Kali**
   - Open a terminal and run:
     ```bash
     sudo apt update
     ```

6. **Install required packages**
   - Install the tools and libraries needed to build and run bettercap:
     ```bash
     sudo apt install golang git build-essential libpcap-dev libusb-1.0-0-dev libnetfilter-queue-dev
     ```

7. **Install/compile Bettercap**
   - Use `go get` to fetch and install bettercap:
     ```bash
     go get -u github.com/bettercap/bettercap
     ```
   - (Depending on your `$GOPATH`/`$PATH` you may need to move the binary or adjust your PATH.)

8. **Find your system IP and default gateway**
   - Get the default gateway (on macOS the command is shown below; in Linux use `ip route`):
     ```bash
     # macOS example (for reference)
     route -n get default
     ```

9. **Start Bettercap**
   - Run bettercap with root privileges:
     ```bash
     sudo bettercap
     ```

10. **Enable network probing**
   - Inside the bettercap interactive prompt, enable net probing:
     ```
     net.probe on
     ```

11. **Show discovered hosts**
    - To list detected hosts and endpoints:
      ```
      net.show
      ```

12. **Enable ARP spoofing (full duplex)**
    - Configure ARP spoofing for full-duplex (attacks both target and gateway) and start:
      ```
      set arp.spoof.fullduplex true
      arp.spoof on
      ```

---

## Included files
- `README.md` — this file.
- Sanitized screenshots:
  - `sanitized_1.png`
  - `sanitized_2.png`
  - `sanitized_3.png`

> **Security note:** ARP spoofing is disruptive and can break network connectivity. Only perform ARP spoofing on networks and devices you own or have explicit permission to test.

