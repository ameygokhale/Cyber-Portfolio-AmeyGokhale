# Netcat Localhost Lab (Kali Linux – Single VM)

This repository documents a complete, safe, and beginner-friendly Netcat lab built entirely on a **single Kali Linux virtual machine**.  
The purpose of this lab is to demonstrate core networking concepts using Netcat, including:

- TCP connections  
- UDP communication  
- HTTP debugging  
- Port scanning fundamentals  
- File transfer using raw sockets  
- Creating a simple custom service  

Netcat (often called the *Swiss‑Army knife of networking*) allows you to read and write raw data over TCP or UDP.  
This lab helps you showcase practical troubleshooting and network‑analysis skills.

---

## Theory Overview

### What is Netcat?
Netcat (`nc`) is a command‑line networking tool that can:
- Open TCP or UDP connections  
- Listen on ports  
- Send and receive data  
- Debug services  
- Test firewalls  
- Simulate clients/servers  

It is widely used in:
- Troubleshooting network services  
- Debugging protocol behavior  
- DevOps and sysadmin tasks  
- Cybersecurity labs (ethically and safely)

---
# 1. Start Apache2 (for HTTP testing)

### **Start the Apache web server**
```bash
sudo systemctl start apache2
```

### **Verify the service is running**
```bash
sudo systemctl status apache2
```

### Screenshot
![Apache Status](images/apache_status.png)

---

# 2. Basic TCP Listener + Message Send (Port 9999)

### **Terminal A – Start a TCP listener**
```bash
nc -l -p 9999
```

### **Terminal B – Send a message**
```bash
echo "Hello from the same machine" | nc 127.0.0.1 9999
```

Terminal A will print the received text.

### Screenshot
![Listener 9999](images/listener_9999.png)

---

# 3. Local Terminal‑to‑Terminal Chat

This simulates two machines talking over the network.

### **Terminal A**
```bash
nc -l -p 9999
```

### **Terminal B**
```bash
nc 127.0.0.1 9999
```

Messages typed in one terminal appear in the other.

### Screenshot
![Chat on port 9999](images/listener_9999chat.png)

---

# 4. Manual HTTP Request Using Netcat (Port 80)

### **Connect to Apache**
```bash
nc 127.0.0.1 80
```

### **Send manual HTTP headers**
```
GET / HTTP/1.1
Host: localhost
```

(Press Enter twice.)

Apache sends raw HTML back.

### Screenshot
![HTTP Request](images/http_request.png)

---

# 5. Port Scanning with Netcat

### **Scan ports 1–1024 on localhost**
```bash
nc -zv 127.0.0.1 1-1024
```

Netcat reports open ports, such as:
```
80 (http) open
```

### Screenshot
![Port Scan](images/port_scan.png)

---

# 6. Creating and Sending a File

### **Create lab folder & file**
```bash
mkdir netcat-lab
cd netcat-lab
echo "This is a test file from Kali over Netcat" > test.txt
```

### Screenshot
![Test File](images/test_file.png)

---

# 7. File Transfer Over Localhost (Port 8888)

### **Terminal A – Receive file**
```bash
cd netcat-lab
nc -l -p 8888 > received.txt
```

### **Terminal B – Send file**
```bash
cd netcat-lab
nc 127.0.0.1 8888 < test.txt
```

### Screenshot – Sending
![Sending Test File](images/sendingtestfile.png)

### Screenshot – File Received
![Received File](images/received_file.png)

---

# 8. UDP Communication Test

### **Terminal A – UDP listener**
```bash
nc -u -l -p 7777
```

### **Terminal B – UDP sender**
```bash
echo "UDP test message" | nc -u 127.0.0.1 7777
```

UDP does not guarantee delivery, but locally it's reliable.

### Screenshot
![UDP Demo](images/udp_demo.png)

---

# 9. Custom Service Simulation (Port 5555)

This simulates a lightweight server responding to clients.

### **Terminal A – Run service loop**
```bash
while true; do echo "Service Response: OK" | nc -l -p 5555; done
```

### Screenshot – Service Running
![Custom Service](images/custom_service.png)

---

### **Terminal B – Connect to the service**
```bash
nc 127.0.0.1 5555
```

Response:
```
Service Response: OK
```

### Screenshot
![Service Response](images/custom_service_response.png)

---

