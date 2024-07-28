import requests
from bs4 import BeautifulSoup

def fetch_proxies(url):
    """
    Fetches proxies from the given URL.

    Args:
    url (str): The URL to fetch proxies from.

    Returns:
    list: A list of proxies in the form of "IP:Port".
    """
    proxies = []
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch proxies from {url}")
        return proxies
    
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    if not table:
        print(f"No table found on the proxy list page at {url}")
        return proxies
    
    rows = table.find_all('tr')
    for row in rows[1:]:  # Skip header row
        columns = row.find_all('td')
        if len(columns) > 1:
            ip = columns[0].get_text(strip=True)
            port = columns[1].get_text(strip=True)
            proxies.append(f"{ip}:{port}")
    
    return proxies

if __name__ == "__main__":
    # Example URL of a public proxy list
    url = "https://www.sslproxies.org/"
    proxies = fetch_proxies(url)

    if proxies:
        print("Fetched proxies:")
        for proxy in proxies:
            print(proxy)
    else:
        print("No proxies found.")
#dev.omori