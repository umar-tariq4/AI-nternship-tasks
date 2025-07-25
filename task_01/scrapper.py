import requests
from bs4 import BeautifulSoup
import pandas as pd

websites = [
    "https://www.daraz.pk",
    "https://sehgalmotors.pk",
    "https://www.mega.pk",
    "https://www.foodpanda.pk",
    "https://www.goto.com.pk",
    "https://www.telemart.pk",
    "https://www.mistore.com",
    "https://audionic.co/",
    "https://www.khaadi.pk",
    "https://www.lamaretail.com",
    "https://www.libertybooks.com/",
    "https://priceoye.pk",
    "http://shophive.com/",
    "https://lootloonline.pk/",
    "http://homeshopping.pk/",
    "https://pk.sapphireonline.pk/",
    "https://royalwrist.pk/",
    "https://saamaan.pk/",
    "https://www.pakwheels.com/"
]


data = []

for url in websites:
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        
        title = soup.title.string.strip() if soup.title else "Unknown"
   
        title_lower = title.lower()
        if "electronics" in title_lower:
            store_type = "Electronics"
        elif "fashion" in title_lower:
            store_type = "Fashion"
        elif "grocery" in title_lower or "mart" in title_lower:
            store_type = "Groceries"
        else:
            store_type = "Mixed / General"

        data.append({
            "Name": title,
            "URL": url,
            "Store Type": store_type
        })

        print(f"[✓] Scraped: {title}")

    except Exception as e:
        print(f"[!] Error scraping {url}: {e}")
        data.append({
            "Name": "Failed to load",
            "URL": url,
            "Store Type": "Unknown"
        })


df = pd.DataFrame(data)
df.to_csv("ecommercesites_pakistan.csv", index=False)

print("\n✅ Scraping completed. CSV file saved as 'ecommercesites_pakistan.csv'")
