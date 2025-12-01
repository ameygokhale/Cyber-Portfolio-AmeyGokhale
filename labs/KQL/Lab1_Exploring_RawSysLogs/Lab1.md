# Lab 1 – Exploring RawSysLogs (KQL)  
Baseline Log Analysis for SOC Investigations

---


# 🎯 Objective  
This lab teaches foundational KQL log analysis skills similar to Microsoft Sentinel operations:

- Explore event logs  
- Identify frequent event types  
- Drill down into specific event names  
- Group by host  
- Build time-based trends  
- Prepare data for detection engineering  

Dataset used: **help.SampleLogs.RawSysLogs**

---

# Step-by-Step Guide

---

## Step 1 — Baseline: View First 20 Logs  
**Where to click:**  
- Click inside the KQL editor  
- Paste the query  
- Click **Run**  

```kql
RawSysLogs
| take 20
```

Screenshot: `screenshots/step1.png`

---

## Step 2 — Count All Event Types  
This shows which events occur most often.

**Where to click:**  
- Replace previous query  
- Click **Run**  

```kql
RawSysLogs
| summarize CountByName = count() by name
| sort by CountByName desc
```

Screenshot: `screenshots/step2.png`

---

## Step 3 — Investigate One Specific Event Type  
Pick any event name from Step 2 results (e.g. `"sqlserver_schedulers"`).

Replace YOUR_EVENT_NAME_HERE.

**Where to click:**  
- Edit the query  
- Click **Run**  

```kql
RawSysLogs
| where name == "YOUR_EVENT_NAME_HERE"
| project timestamp, name, tags
| sort by timestamp desc
```

Screenshot: `screenshots/step3.png`

---

## Step 4 — Identify Noisy Hosts for That Event  
Shows which hosts generate the most events of that type.

```kql
RawSysLogs
| where name == "YOUR_EVENT_NAME_HERE"
| extend host = tostring(tags["host"])
| summarize EventCount = count() by host
| sort by EventCount desc
```

Screenshot: `screenshots/step4.png`

---

## Step 5 — Timeline Analysis (10-Minute Buckets)  
Use time binning like a SOC analyst.

```kql
RawSysLogs
| where name == "YOUR_EVENT_NAME_HERE"
| extend host = tostring(tags["host"])
| summarize EventCount = count() by host, bin(timestamp, 10m)
| sort by timestamp asc, host
```

Screenshot: `screenshots/step5.png`

---

## Overall Findings

### **Most Frequent Event Type**
✔ **sqlserver_performance**  
753M+ events

### **Event Type Analyzed**
✔ **sqlserver_schedulers**

### **Most Active Host**
✔ **adx‑vm**

### **Timeline Behavior**
- Regular, stable 10‑minute intervals  
- No anomalies, spikes, or gaps  
- Indicates predictable telemetry ingestion

