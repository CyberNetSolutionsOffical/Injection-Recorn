# Injection-Recorn
# <img width="318" height="159" alt="Untitled" src="https://github.com/user-attachments/assets/aefd064d-3860-4b76-942c-653ed1aa9e6a" />

Injection_Recon** is a Multi-threaded Web Vulnerability Scanner designed for security researchers and ethical hackers to identify **SQL Injection** and **XSS vulnerabilities** in web applications quickly and efficiently.



# Features ✨

- Multi-threaded scanning for speed ⏱️
- Detects **SQL Injection** and **Cross-Site Scripting (XSS)** vulnerabilities
- Supports both GET and POST form submissions
- Auto-detection of SQL error messages
- Generates **JSON report** for analysis
- URL encoding for payloads
- Color-coded terminal output for easy identification
- Easy-to-use command-line interface

  # Help
  
<img width="635" height="623" alt="2025-09-13-041704_635x623_scrot" src="https://github.com/user-attachments/assets/5ce75003-9ff4-4b03-82d5-1505ce5966d0" />


# <img width="546" height="203" alt="2025-09-13-041617_546x203_scrot" src="https://github.com/user-attachments/assets/12d32dfc-c4fd-41e7-bd7e-bdc12b65be67" />


## Installation ⚡

1. Clone the repository:
     ```bash
   git clone https://github.com/yourusername/Injection_Recon.git
   cd Injection_Recon
     
# Install dependencies:
      pip install -r requirements.txt

# Usage 🛠️
     python3 inject-scan.py <url1> [url2 ...]

# Example:-
      python3 inject-scan.py https://example.com

<img width="1280" height="399" alt="2025-09-13-041635_1280x399_scrot" src="https://github.com/user-attachments/assets/b0453944-71c0-423f-8fa5-40b6d6545a61" />




- The scanner will find all forms in the target URLs.

- Test each input for SQL Injection and XSS.

- JSON report will be saved as vuln_report.json.

  

# Payloads Used ⚔️

XSS Payload: <script>alert('XSS')</script>
SQL Injection Payloads: Includes common payloads like:
' OR '1'='1' --
admin' --
1234 " AND 1=0 UNION ALL SELECT "admin", "81dc9bdb52d04dc20036dbd8313ed055
And many more…

# Requirements 📦
Python 3.8+
Requests
BeautifulSoup4
Tabulate

# Install dependencies with:
               pip install requests beautifulsoup4 tabulate


# Security Notice ⚠️

Use Injection_Recon only on websites you own or have explicit permission to test.
Unauthorized testing may be illegal and could result in serious consequences.

# Contribution 🤝
Contributions are welcome!
Please fork the repository, make changes, and submit a pull request.

License 📄

# MIT License

Author: Dinesh Rimal
Project Name: Injection_Recon
GitHub: https://github.com/yourusername/Injection_Recon

