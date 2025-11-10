# Data Flow Diagram (DFD) and System Architecture Analysis  
### Case Study: Wi-Fi Smart Plug Security Evaluation  

---

## 1. Introduction  
This document provides a detailed explanation of the **Data Flow Diagram (DFD)** constructed during the threat modeling phase of the Wi-Fi Smart Plug security assessment.  

The DFD is a key component of the project’s **Microsoft Threat Modeling Tool** analysis and visually represents the interaction between system entities, data flows, processes, and external actors.  

By understanding each data flow and trust boundary, this analysis supports the identification of security threats under the **STRIDE** framework (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege).  

---

## 2. Data Flow Diagram  

![Data Flow Diagram](images/dfd.png)  
*Figure 1. Smart Plug Data Flow Diagram representing communication between core system components and external interfaces.*

---

## 3. DFD Components and Data Stores  

| ID | Component | Type | Description | Security Consideration |
|----|------------|------|-------------|------------------------|
| **P1** | Microcontroller (MCU) | Process | Executes control logic for device operations. | Must validate all incoming commands and manage secure boot. |
| **P2** | Wi-Fi Module | Process | Handles network communication with the smartphone app and cloud. | Should use encrypted transport (TLS) and validate endpoints. |
| **P3** | RF Transceiver | Process | Enables local wireless control from remote button or RF remote. | Should include input validation to prevent replay attacks. |
| **D1** | Flash Memory | Data Store | Stores firmware binary and configuration data. | Must ensure firmware encryption and integrity protection. |
| **E1** | Smartphone App | External Entity | Provides user interface for controlling the smart plug. | Must authenticate and communicate securely with the device. |
| **E2** | Cloud Server | External Entity | Manages remote commands, telemetry, and updates. | Should use strong authentication and enforce HTTPS communication. |
| **I1** | UART Debug Interface | External Interface | Used during development and testing for firmware flashing. | Must be disabled in production builds to prevent local exploitation. |

---

## 4. Data Flows  

| Flow ID | Source | Destination | Description | Trust Boundary | Potential Threat |
|----------|----------|-------------|--------------|----------------|------------------|
| **DF1** | Smartphone App | Smart Plug (Wi-Fi) | User sends control commands (ON/OFF, scheduling). | External → Internal | Spoofing, Tampering, Replay |
| **DF2** | Smart Plug | Cloud Server | Device transmits telemetry and status updates. | Internal → Cloud | Information Disclosure |
| **DF3** | Cloud Server | Smart Plug | Sends update notifications or firmware packages. | Cloud → Internal | Firmware Tampering |
| **DF4** | RF Remote | Smart Plug | Local wireless control commands. | External → Internal | Unauthorized access |
| **DF5** | Smart Plug | Flash Memory | Writes firmware and configuration data. | Internal | Firmware corruption risk |
| **DF6** | UART Debug | MCU | Developer access for debugging. | Internal (Dev Boundary) | Privilege escalation, firmware dump |
| **DF7** | Smartphone App | Cloud Server | Account and device registration API calls. | External | Data leakage, session hijacking |

---

## 5. Trust Boundaries  

| Boundary ID | Description | Risk | Mitigation |
|--------------|-------------|------|-------------|
| **TB1** | Between smartphone app and smart plug (local Wi-Fi network) | High | Use mutual TLS authentication, secure API tokens |
| **TB2** | Between smart plug and cloud infrastructure | High | Encrypt data in transit using HTTPS/TLS |
| **TB3** | Between developer interfaces (UART/I2C) and production firmware | Medium | Disable debug ports and enforce access controls |
| **TB4** | Between firmware and flash memory | Medium | Implement secure boot and signed firmware validation |

The DFD identifies four main trust boundaries where data transitions between entities with differing security contexts. These points are the primary focus for **threat modeling** and **penetration testing** activities.  

---

## 6. STRIDE-Based Threat Analysis Summary  

| STRIDE Category | Example in System | Risk | Mitigation |
|------------------|------------------|------|-------------|
| **Spoofing** | Fake app impersonating the legitimate client | High | Use mutual authentication with unique device certificates |
| **Tampering** | Firmware modified before or during update | High | Implement firmware signing and integrity checks |
| **Repudiation** | Lack of event logging | Medium | Maintain secure, timestamped device logs |
| **Information Disclosure** | SOAP over HTTP leaks user data | High | Transition to HTTPS/TLS communication |
| **Denial of Service (DoS)** | Packet flooding or replay attack | Medium | Implement rate limiting and message sequencing |
| **Elevation of Privilege** | UART debug access exploited | High | Disable debug in production, enforce access control |

---

## 7. Observations  
- The device exhibits **multiple critical data flows crossing trust boundaries without encryption**.  
- Developer-facing interfaces (e.g., UART, I2C) remain accessible, increasing physical attack surface.  
- The use of **SOAP over HTTP** represents a legacy protocol risk, not aligned with modern IoT security standards.  

These weaknesses were mapped back to vulnerabilities **V-01 through V-05** in the [Vulnerability Assessment Report](vulnerability_assessment.md).  

---

## 8. Recommendations  
1. **Secure Communications:** Replace SOAP over HTTP with TLS-protected RESTful APIs.  
2. **Boundary Hardening:** Authenticate all inter-boundary data flows.  
3. **Interface Lockdown:** Remove or disable all debug interfaces post-development.  
4. **Firmware Protection:** Enforce integrity verification during boot.  
5. **Logging and Monitoring:** Maintain audit logs for device actions crossing boundaries.  

---

## 9. Conclusion  
The Data Flow Diagram provides a comprehensive view of how data moves within the smart plug ecosystem and reveals where critical security controls must be applied.  

By identifying trust boundaries and mapping STRIDE threats, this DFD serves as the foundation for both the **threat modeling** and **vulnerability assessment** conducted during this project.  

Future iterations of the system should integrate **secure-by-design principles** to minimize cross-boundary risks and ensure long-term IoT device integrity.  

---

📘 *This DFD explanation forms part of the Smart Plug IoT Security Case Study, serving as a technical reference for system architecture and threat modeling documentation.*
