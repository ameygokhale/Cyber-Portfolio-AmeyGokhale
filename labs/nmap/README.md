# Nmap Scanning Guide (macOS)

This README provides a clear and structured explanation of how to install **Nmap** on a Mac, along with demonstrations of essential Nmap commands. The results shown here come from practical scans run against **scanme.nmap.org**, the official public Nmap test target.

>  **Important:** Only scan hosts you own or have explicit permission to test. `scanme.nmap.org` is safe to use for learning.

---

## Installing Nmap on macOS (Apple M3)

### **1. Install Homebrew (if not installed)**

Homebrew is the easiest way to install Nmap.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After installation, add Homebrew to your PATH if prompted.

### **2. Install Nmap**

```bash
brew install nmap
```

### **3. Verify Installation**

```bash
nmap --version
```

You should see output confirming the installed version.

---

## Commands Used in This Project

Below are all the commands demonstrated, along with screenshots and explanations.

---

## ### 1. `nmap scanme.nmap.org`

A **default scan**. Nmap scans the most common 1,000 ports.

**Purpose:** Quick overview of open ports.

**Screenshot:**  
![Default Scan](images/nmapscanmenmaporg.png)

---

## ### 2. `nmap -O scanme.nmap.org`

Enables **OS detection**.

**Purpose:** Attempts to identify the remote operating system.  
*May fail if network distance is too large (as seen in the scan).*

**Screenshot:**  
![OS Detection](images/nmapO.png)

---

## ### 3. `nmap -p 80 scanme.nmap.org`

Scans a **specific port**.

**Purpose:** Faster, more targeted scanning.

**Screenshot:**  
![Port 80 Scan](images/nmapp80.png)

---

## ### 4. `nmap -p 1-1000 scanme.nmap.org`

Scans ports **1 through 1000**.

**Purpose:** Discover more services while keeping scan time reasonable.

**Screenshot:**  
![Port Range Scan](images/nmapp1-1000.png)

---

## ### 5. `nmap -sV scanme.nmap.org`

Runs **service/version detection**.

**Purpose:** Identifies software running on open ports (e.g., Apache, OpenSSH).

**Screenshot:**  
![Service Version Scan](images/nmapsV.png)

---

## ### 6. `nmap -A scanme.nmap.org`

The **aggressive scan**.

Includes:
- `-O` OS detection  
- `-sV` service/version detection  
- Default scripts  
- Traceroute  

**Purpose:** Most detailed single-command scan.

**Screenshot:**  
![Aggressive Scan](images/nampA.png)

---

## ### 7. `nmap -p- scanme.nmap.org`

Scans **all 65,535 ports**.

**Purpose:** Full coverage of every TCP port.  
Useful for catching services not shown in the default top 1000-port scan.

**Screenshot:**  
![All Ports Scan](images/nmappall.png)

---

##  Summary Table

| Command         | Description                                        |
| --------------- | -------------------------------------------------- |
| `nmap <target>` | Default top 1000 port scan                         |
| `-O`            | OS detection                                       |
| `-p <port>`     | Scan specific port                                 |
| `-p 1-1000`     | Scan a port range                                  |
| `-p-`           | Scan all ports (1–65535)                           |
| `-sV`           | Service & version detection                        |
| `-A`            | Aggressive scan (OS, version, scripts, traceroute) |

---
