# OSINT Threat Intelligence Automation

## Objective
Collect malicious IPs and domains from OSINT sources.

## Tools
- Python
- MongoDB
- VirusTotal API
- AlienVault OTX API
- AbuseIPDB API

## Team Roles
Member 1 → Data collection  
Member 2 → Database  
Member 3 → Firewall  
Member 4 → GitHub + Documentation
**Install Dependencies**:Run 'pip install flask python-dotenv'.
**Configure API Keys**:Create a '.env' file and add your 'SHODAN_API_KEY' and 'VIRUSTOTAL_API_KEY'.
**Start the Server**: Run 'python main.py'.
**Access the Dashboard**:Open 'http://127.0.0.1:5000' in your browser.

## Documentation Links
- [Schema Desifn](schema.md)
- [API Usage Guide](api_usage.md)