# Dubizzle Egypt New Cars Scraper

Scrapes brand-new car listings, prices, and specifications directly from Dubizzle Egypt (motors section).

### How it works
The script queries Dubizzle's internal backend REST API (`/api/new-cars/all-new-cars`) page by page. It utilizes a `requests.Session` configured with full browser headers and randomized request throttling (`time.sleep`) to prevent rate limits.

### Data Collected
- Car Full Name
- ABS Availability (Yes/No)
- Engine Displacement
- Transmission Type
- Price (EGP)

### Requirements
```bash
pip install requests pandas
```
### Running the script
```bash
python Dubizzle_new_cars_scraper.py
```
### Output
Outputs the vehicle listings to Dubizzle_new_Cars.csv encoded in utf-8-sig.
