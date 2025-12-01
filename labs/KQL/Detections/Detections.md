# Detection Engineering Templates (KQL)

This folder contains **Sentinel-style detection rules**.  
Add screenshots and modify queries based on your dataset.

---


## 🚨 Detection 1 — High Event Rate per Host

Use when a host generates an unusual burst of activity.

```kql
RawSysLogs
| where name == "YOUR_EVENT_NAME_HERE"
| extend host = tostring(tags["host"])
| summarize EventCount = count() by host, bin(timestamp, 10m)
| where EventCount > 100
```

---

## 🔍 Detection 2 — Rare Event on a Host (Global vs Local)

Flags events that are *normal globally* but *rare on a specific host*.

```kql
RawSysLogs
| extend host = tostring(tags["host"])
| summarize HostCount = count() by host, name
| join kind=inner (
    RawSysLogs
    | summarize GlobalCount = count() by name
) on name
| where host == "YOUR_HOST_HERE"
| where GlobalCount > 100 and HostCount < 3
```

---


