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

# ⚠️Disclaimer⚠️ 

Injection_Recon is a security testing tool developed for educational purposes and ethical hacking only. The software is intended to help security researchers, penetration testers, and developers identify vulnerabilities in web applications such as SQL Injection and Cross-Site Scripting (XSS) in a controlled and legal environment. By using this tool, you agree to the following terms:

1. Authorized Use Only: You must have explicit permission from the website owner or organization before running any scans. Testing websites without consent is considered illegal and may lead to criminal charges, civil penalties, or both. Injection_Recon must never be used on unauthorized targets.

2. Legal Responsibility: The author, contributors, and distributors of Injection_Recon are not responsible for any misuse, damage, data loss, or legal consequences arising from the use of this software. Users assume full responsibility for their actions when deploying this tool.

3. Data Protection: Injection_Recon does not store or transmit sensitive data outside your system intentionally. However, scanning production websites may expose user data inadvertently. Users must ensure they comply with data protection laws applicable in their jurisdiction.

4. No Guarantees: Injection_Recon is provided “as-is” without any warranties. The tool may not detect all vulnerabilities, and false positives or false negatives may occur. Use it as a supplementary aid in security testing, not as a replacement for professional audits.

5. Ethical Conduct: Users should adhere to ethical hacking principles. Only use the tool to identify and report vulnerabilities responsibly, preferably following coordinated disclosure guidelines. Never exploit vulnerabilities for personal gain, unauthorized access, or malicious purposes.

6. Educational Purpose: The primary goal of Injection_Recon is to educate and train aspiring ethical hackers, security enthusiasts, and developers to understand web vulnerabilities and their impact.

By proceeding to use Injection_Recon, you acknowledge and accept these terms. Unauthorized use or abuse may have serious legal consequences. Always obtain written permission before testing any system.

Author: Dinesh Rimal
Project Name: Injection_Recon
GitHub: https://github.com/yourusername/Injection_Recon

