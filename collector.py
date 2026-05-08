import requests

def get_malicious_ip():
    url = "https://otx.alienvault.com/api/v1/indicators/IPv4/general"

    try:
        response = requests.get(url)
        return response.status_code
    except Exception as e:
        return str(e)