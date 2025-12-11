# Smart Plug Security Audit: A Comprehensive IoT Cybersecurity Case Study  

## Abstract  
This project presents a detailed case study on the cybersecurity assessment of a **Wi-Fi–enabled Smart Plug**, a common consumer IoT device that allows remote control and energy monitoring of electronic appliances.  
The objective of this research is to **analyze the security posture** of the device using real-world assessment methodologies including **Threat Modeling, Firmware Analysis, Network Traffic Inspection**, and **Software Bill of Materials (SBOM) Evaluation**.  

The results demonstrate how vulnerabilities in embedded systems can compromise both device integrity and user privacy, and how structured mitigation strategies can significantly reduce cyber risk.

---

## 1. Introduction  
Smart plugs are integral components of modern smart homes. Despite their convenience, these devices often lack robust security controls, making them attractive targets for cyberattacks.  

This study focuses on a commercial Wi-Fi smart plug that:  
- Connects to cloud servers via **SOAP over HTTP**  
- Interacts with companion smartphone apps for remote operation  
- Interfaces with microcontrollers, Wi-Fi modules, and RF transceivers  

By applying standard **embedded security testing techniques**, this project identifies and evaluates the device’s security weaknesses and proposes remediation measures following industry best practices such as **OWASP IoT Top 10** and **NIST SP 800-183**.

---

## 2. System Overview  

### 2.1 Product Architecture  
The Smart Plug system consists of both hardware and software components working in tandem:  

- **Microcontroller (MCU)** – Core control logic  
- **Wi-Fi Module** – Wireless communication interface  
- **RF Transceiver** – Local signal communication  
- **Flash Memory** – Stores firmware image  
- **Electrical Relay** – Switches power to the connected appliance  
- **Smartphone App** – User interface for remote operations  

### 2.2 Data Flow Diagram (DFD)  

![Data Flow Diagram](images/dfd.png)  
*Figure 1. Smart Plug Data Flow Diagram showing data exchange between internal components and external entities.*  

This DFD represents the data exchange between the smart plug, user interface, and backend systems, including the trust boundaries considered during the threat modeling process.  

---

## 3. Methodology  

### 3.1 Threat Modeling  
Threat modeling was conducted using the **Microsoft Threat Modeling Tool** based on the DFD above.  
- Total identified threats: **149**  
- Prioritized for testing: **28** high-impact threats  
- Categories: Spoofing, Tampering, Information Disclosure, Denial of Service, Elevation of Privilege  

### 3.2 Testing Procedures  
The following testing methodologies were employed:  
1. **Disassembly & Hardware Inspection** – Examined UART, I2C, and Debug interfaces.  
2. **Network Analysis (Wireshark)** – Monitored communication patterns; identified plaintext SOAP messages.  
3. **Firmware Analysis** – Extracted and examined unencrypted firmware for backdoors and hardcoded credentials.  
4. **Fuzz Testing** – Injected malformed packets to evaluate input validation.  
5. **Penetration Testing Simulation** – Evaluated exploit feasibility based on real-world attacker capabilities.  

### 3.3 Tools Used  
| Tool | Purpose |
|------|----------|
| Wireshark | Network traffic inspection |
| USB-to-Serial Adapter | UART communication analysis |
| Logic Analyzer | Signal monitoring |
| Firmware Extractor | Binary extraction |
| Microsoft Threat Modeling Tool | Threat analysis |
| Python Scripts | Automation of packet replay and fuzzing |

---

## 4. Findings and Results  

### 4.1 Key Vulnerabilities Identified  
| ID | Vulnerability | Risk | Evidence | Recommended Mitigation |
|----|----------------|------|-----------|------------------------|
| V-01 | Plaintext SOAP over HTTP | High | Wireshark captures show unencrypted data | Enforce HTTPS/TLS communication |
| V-02 | Unencrypted firmware image | High | Firmware readable via debug port | Sign and encrypt firmware |
| V-03 | Authentication bypass | High | Protocol bypass sequence found | Implement token-based authentication |
| V-04 | Exposed UART debug | Medium | Debug interface active on production board | Disable UART in production firmware |
| V-05 | Incomplete SBOM | Medium | Missing third-party component disclosure | Maintain and publish complete SBOM |

### 4.2 Hardware Inspection  

![Smart Plug PCB](images/pcb.png)  
*Figure 2. Internal hardware layout of the Smart Plug under test, showing key debug interfaces and MCU connections.*

### 4.3 Software Bill of Materials  

![SBOM Visualization](images/sbom.png)  
*Figure 3. Extracted Software Bill of Materials listing third-party components and dependencies.*

A detailed tabular SBOM is available in [`sbom.md`](sbom.md).

---

## 5. Discussion  
The findings indicate that the Smart Plug’s architecture prioritizes functionality and affordability over security.  
Major risks include **plaintext communication**, **unencrypted firmware**, and **incomplete component documentation**, all of which can be exploited for device takeover or data interception.  

Applying **secure design principles**—encryption, authentication, and regular patching—can significantly enhance the device’s resilience.  

---

## 6. Recommendations  

### 6.1 For Developers and Manufacturers  
- Implement **firmware encryption and signing**.  
- Adopt **secure boot mechanisms** to prevent tampered firmware.  
- Enforce **token-based authentication** between app and device.  
- Regularly update security advisories and patches.  
- Maintain an up-to-date **Software Bill of Materials (SBOM)**.

### 6.2 For End Users  
- Always update the device firmware and app.  
- Use strong, unique passwords for smart home networks.  
- Employ **VPNs** or isolated IoT networks.  
- Disable unnecessary device features (e.g., debug modes).  

---

## 7. Future Work  
- Perform hardware-level fault injection and side-channel analysis.  
- Automate SBOM generation and integrate with vulnerability scanning pipelines.  
- Conduct a comparative security study across multiple IoT device models.  
- Extend post-market surveillance for long-term device monitoring.

---

## 8. References  
1. OWASP IoT Top 10 (2024). *Open Web Application Security Project.*  
2. NIST SP 800-183: *Networks of ‘Things’.*  
3. MITRE CVE Database. *Common Vulnerabilities and Exposures.*  
4. Microsoft Threat Modeling Tool Documentation.  
5. Wireshark User Guide.  

---

📘 *This repository forms part of a comprehensive final-year academic project on IoT security, combining research-based methodologies with real-world testing approaches. The work aims to demonstrate the importance of proactive security assessment for embedded consumer devices.*
