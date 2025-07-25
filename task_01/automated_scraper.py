from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import time

# 🧠 Function to guess store type from the text
def guess_store_type(text):
    text = text.lower()
    if any(word in text for word in ["fashion", "clothing", "apparel", "wear", "boutique", "dress", "shoes"]):
        return "Clothing/Fashion"
    elif any(word in text for word in ["tech", "gadget", "mobile", "laptop", "electronics", "gear", "accessory", "earpods"]):
        return "Technology"
    elif any(word in text for word in ["book", "library", "novel", "read"]):
        return "Books"
    elif any(word in text for word in ["furniture", "sofa", "home", "interior"]):
        return "Home/Furniture"
    elif any(word in text for word in ["grocery", "mart", "food", "snacks"]):
        return "Grocery/Food"
    else:
        return "General E-commerce"

# 🚀 Setup headless Chrome
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

# 🌐 Target URL
url = 'https://clarity.pk/ecommerce/list-online-marketplaces-ecommerce-stores-pakistan/'
driver.get(url)

# ⏳ Wait for JS to render
time.sleep(5)

# 🥣 Get page source and parse it
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# 📦 Extract data
rows = []
for link in soup.find_all('a'):
    href = link.get('href')
    text = link.get_text(strip=True)

    # Make sure it's a valid business link
    if href and 'http' in href and text:
        store_type = guess_store_type(text)  # 🤖 Guess category
        rows.append([text, href, store_type])

# 📁 Save to CSV
with open('clarity_links_with_categories.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Business Name', 'URL', 'Store Type'])
    writer.writerows(rows)

print(f"✅ Extracted {len(rows)} links with categories into 'clarity_links_with_categories.csv'")
