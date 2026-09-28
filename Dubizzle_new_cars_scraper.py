import requests
import time
import pandas as pd
import random

def scraper_code():
    url = "https://motors-content.dubizzle.com.eg/api/new-cars/all-new-cars"
    session = requests.Session()
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "origin": "https://www.dubizzle.com.eg",
        "priority": "u=1, i",
        "referer": "https://www.dubizzle.com.eg/",
        "sec-ch-ua": "\"Chromium\";v=\"153\", \"Not_A Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"
    }
    session.headers.update(headers)
            
    items = []

    for x in range(1, 72):
        print(f"fetching page {x}...")
        time.sleep(random.uniform(1, 3))
        querystring = {"sort_by":"popularity","page":str(x)}
        payload = ""
        try:
            r = session.get(url, data=payload, params=querystring)
            r.raise_for_status()
            print (f"{r.status_code} OK" )
            data = r.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"[!] HTTP error on page {x}: {http_err}")
            break  # Stop the loop if the URL/Build ID is dead
                
        except requests.exceptions.JSONDecodeError:
            print(f"[!] Page {x} did not return JSON. Returned raw HTML/Protection page instead.")
            continue  # Skip to the next page
                
        except requests.exceptions.RequestException as req_err:
            print(f"[!] Network error on page {x}: {req_err}")
            continue
        cars = data.get("cars" , [])

        for c in cars:
            abss= c.get("abs")
            items.append({
                "Car Name" : c.get("full_name"),
                "ABS Avialablity" : "Yes" if abss is True else ("No" if abss is False else "N/A"),
                "Engine Size" : c.get("displacement"),
                "Transmission" : c.get("transmission_type"),
                "Price (EGP)" : c.get("price")
            })


    return (items)

def save_to_csv(items):
    df = pd.DataFrame(items)
    df.to_csv("Dubizzle_new_Cars.csv", index=False , encoding='utf-8-sig')
    print(f"Scraping completed. Total items scraped: {len(items)}")

def main():
    items = scraper_code()
    save_to_csv(items)

if __name__ == "__main__":
    main()