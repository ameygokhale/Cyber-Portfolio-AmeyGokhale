# Azure KQL SOC Analysis Labs  
Hands-On Security Investigations, Threat Hunting & Detection Engineering with Kusto Query Language (KQL)

This repository contains a complete set of **Microsoft Sentinel–style SOC labs**, built using **Azure Data Explorer’s free Logs dataset**.  
All labs use **KQL**, the same language used in Microsoft Sentinel, Microsoft Defender, and Azure Monitor.

The goal of this project is to demonstrate practical skills in:

- Log analysis  
- Threat hunting  
- Anomaly detection  
- Query optimization  
- Detection engineering  
- SOC investigation documentation  

---



# 🧪 **Lab 1 – Exploring RawSysLogs (Baseline Analysis)**

**Objective:**  
Learn essential KQL techniques used in Microsoft Sentinel:

- `take`, `where`, `sort`, `project`
- Counting events
- Grouping by host
- Building timelines with `bin()`

---

# 🕵️ **Lab 2 – Threat Hunting: Rare vs. Common Events**

Learn how to compare global vs. host-specific behavior to detect anomalies.

---

# 🚨 Detection Engineering (Microsoft Sentinel Style)

Includes two analytic rule templates:

- `detect_high_rate_by_host.kql`
- `detect_rare_event_on_host.kql`

---

# 🛠 How to Run the Labs

1. Visit: https://dataexplorer.azure.com/publicfreecluster  
2. Choose **Logs Data**  
3. Use database: **help.SampleLogs**  
4. Table: **RawSysLogs**  
5. Copy queries from labs into the editor.

---
