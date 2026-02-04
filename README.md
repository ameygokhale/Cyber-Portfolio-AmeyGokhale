<div align="center">

# Cybersecurity Portfolio
### Amey Gokhale
**Security Engineer | Cloud Security | SOC Operations | Digital Forensics**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/amey-gokhale)
[![Email](https://img.shields.io/badge/Email-Contact_Me-red?style=for-the-badge&logo=gmail)](mailto:ameygokhale1@gmail.com)

---

### Portfolio Overview
This repository documents my **hands-on security engineering work**.
It moves beyond theory into **practical execution**, featuring end-to-end assessments, custom tool development, and cloud security implementations.

**Core Domains:**
`Cloud Security (AWS/Azure)` • `SOC & SIEM` • `Digital Forensics` • `IoT Security` • `Penetration Testing`

<br>

![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazon-aws&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-007FFF?style=flat&logo=microsoft-azure&logoColor=white)
![Splunk](https://img.shields.io/badge/Splunk-000000?style=flat&logo=splunk&logoColor=white)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=flat&logo=burpsuite&logoColor=white)
![Metasploit](https://img.shields.io/badge/Metasploit-333333?style=flat&logo=metasploit&logoColor=white)
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=flat&logo=wireshark&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=flat&logo=kalilinux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

</div>

---

# Featured Major Projects
*Complex, end-to-end engineering and assessment projects.*

### 1. [Smart Plug Security Assessment](Projects/Smart%20Plug%20Security%20Audi/README.md)
**Domain:** IoT Security & Hardware Hacking
A complete black-box security assessment of a Wi-Fi-enabled Smart Plug.
* **Techniques:** UART debugging, Firmware extraction, Logic Analyzer testing, Network traffic interception.
* **Outcome:** Identified vulnerabilities in communication protocols and firmware logic; produced a full threat model.
* **Tools:** `Wireshark` `UART` `Logic Analyzer` `Microsoft Threat Modeling Tool`

### 2. [Adaptive Web Application Firewall (Adaptive WAF)](https://github.com/ameygokhale/adaptive-waf)
**Domain:** DevSecOps & Application Security
Designed an adaptive WAF that moves beyond static signatures by using behavioral analysis.
* **Key Feature:** Integrates Machine Learning to detect anomaly-based attacks that bypass traditional rules.
* **Outcome:** Reduced false positives and improved detection of "low-and-slow" attacks.
* **Tools:** `Python` `ModSecurity` `Machine Learning` `Traffic Analysis`

### 3. [IoT Deleted Data Recovery Forensic Framework](Projects/IoT_Deleted_Data_Recovery/README.md)
**Domain:** Digital Forensics
A forensic investigation project focusing on recovering deleted artifacts from IoT storage media.
* **Techniques:** File carving, hash-based integrity verification, and metadata extraction.
* **Outcome:** Successfully recovered deleted data using signature-based recovery (Foremost).
* **Tools:** `Autopsy` `Foremost` `dd` `Volatility`

### 4. [AegisMind – AI-Driven SOC Monitoring](https://github.com/Mosshead-marimo/AegisMind)
**Domain:** SOC Automation & AI
A real-time monitoring system using AI to map behavioral anomalies to MITRE ATT&CK tactics.
* **Outcome:** Simulates modern SOC tooling to detect insider threats and abnormal system behavior.

---

# Cloud Security Labs
*Infrastructure-as-Code auditing, logging, and defense.*

### AWS Security
| Lab | Focus Area | Tech Stack |
| :--- | :--- | :--- |
| **[AWS CloudTrail Log Hunting](labs/AWS_CloudTrail_Log_Hunting/README.md)** | Event Correlation & IR | `CloudTrail` `Athena` |
| **[AWS GuardDuty Alert Triage](labs/AWS_GuardDuty_Alert_Triage/README.md)** | Threat Detection | `GuardDuty` `AWS Security Hub` |
| **[AWS IAM Investigation](labs/AWS_IAM_Investigation/README.md)** | Privilege Escalation | `IAM` `Policy Simulator` |
| **[S3 Bucket Attack & Defense](labs/AWS_S3_Bucket_Attack_&_Defense/README.md)** | Cloud Pentesting | `S3` `AWS CLI` |

### Azure Security
| Lab | Focus Area | Tech Stack |
| :--- | :--- | :--- |
| **[Defender for Cloud](labs/Azure_Defender_for_Cloud/README.md)** | CSPM & Posture Mgmt | `Defender` `Azure Portal` |
| **[Log Analytics & KQL](labs/Azure_Log_Analytics_&_KQL/README.md)** | SIEM Querying | `KQL` `Sentinel` |

---

# SOC & Threat Intelligence
*Log analysis, SIEM operations, and malware triage.*

| Lab | Focus & Methodology | Tools Used |
| :--- | :--- | :--- |
| **[Splunk SIEM Lab](labs/Splunk/README.md)** | Log ingestion, dashboards, correlation searches | `Splunk Enterprise` |
| **[KQL Query Design](labs/KQL/README.md)** | Writing queries for threat hunting | `KQL` `Sentinel` |
| **[Malware Analysis](labs/Virustotal/README.md)** | Hash analysis and EICAR testing | `VirusTotal` |
| **[Phishing Analysis](labs/Urlscan.io/README.md)** | URL reputation and scan analysis | `urlscan.io` `AbuseIPDB` |

---

# Offensive Security & Network
*Red Teaming, Network Exploitation, and Web Security.*

| Lab | Description | Tools |
| :--- | :--- | :--- |
| **[Web App Pentesting](labs/dvwa-sqli/README.md)** | SQL Injection, XSS, and Burp Suite workflows | `Burp Suite` `SQLMap` |
| **[MITM & Spoofing](labs/MITM-attack-bettercap/README.md)** | ARP/DNS Spoofing and traffic interception | `Bettercap` `Wireshark` |
| **[Password Attacks](labs/Hydra/README.md)** | Brute-force and Hash cracking | `Hydra` `John the Ripper` |
| **[Network Scanning](labs/nmap/README.md)** | Service enumeration and OS detection | `Nmap` `Netcat` |

---

# Digital Forensics & Malware
*Artifact analysis and reverse engineering.*

| Lab | Scope | Tools |
| :--- | :--- | :--- |
| **[Memory Forensics](labs/Volatility3/README.md)** | RAM analysis to find injected processes | `Volatility3` |
| **[Disk Forensics](labs/Autopsy/README.md)** | File system analysis and recovery | `Autopsy` |
| **[Reverse Engineering](labs/ghidra/README.md)** | Analyzing malware binaries (ELF/PE) | `Ghidra` |
| **[Email Forensics](labs/Phishinganalysis/README.md)** | Header analysis and attachment parsing | `ripmime` `oletools` |

---

# Network Engineering
*Fundamental networking protocols and infrastructure.*

| Lab | Topic | Tags |
| :--- | :--- | :--- |
| [Switching & Routing](labs/vlans/README.md) | VLANs, STP, Inter-VLAN Routing | `Cisco IOS` |
| [Protocols](labs/dhcp-dns/README.md) | DHCP, DNS, OSPF, RIPv2 | `Packet Tracer` |
| [Traffic Analysis](labs/wireshark/README.md) | Packet flow analysis (TCP/UDP handshake) | `Wireshark` |

---

<div align="center">

> ⚠️ **Ethical Notice**
> All work in this portfolio was performed in **isolated, intentionally vulnerable environments** (labs) or on hardware/systems I explicitly own. This portfolio documents defensive and educational security practices and does **not** promote unauthorized access.

</div>
