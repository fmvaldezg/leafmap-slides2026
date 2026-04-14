import requests, json, pandas as pd, time

headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}

# Get the full list of art IDs
index_r = requests.get("https://www.philart.net/api/art.json", headers=headers)
index_data = index_r.json()
art_list = index_data["body"]["list"]

print(f"Total artworks in index: {len(art_list)}")

# Extract the URL for each artwork
art_urls = [item["links"][0]["href"] for item in art_list]
print(f"Sample URLs: {art_urls[:3]}")

# Fetch each artwork — this will take a few minutes
records = []
errors = 0

for i, url in enumerate(art_urls):
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            body = r.json().get("body", {})
            loc = body.get("location", {})
            years = body.get("years", [])
            artists = body.get("artists", [])

            records.append({
                "title":     body.get("title", {}).get("display", ""),
                "artist":    artists[0].get("name", "") if artists else "",
                "year":      years[0].get("year", "") if years else "",
                "type":      body.get("architecture", {}).get("description", "Mural/Public Art"),
                "latitude":  loc.get("latitude"),
                "longitude": loc.get("longitude"),
            })
        else:
            errors += 1
    except Exception as e:
        errors += 1

    # Progress update every 100 items
    if (i + 1) % 100 == 0:
        print(f"  {i+1}/{len(art_urls)} fetched — {len(records)} ok, {errors} errors")

    # Be polite to the server — small delay
    time.sleep(0.1)

print(f"\nDone: {len(records)} artworks, {errors} errors")

# Save to CSV
df = pd.DataFrame(records)

# Filter to murals and standalone public art only
df_murals = df[df["type"] == "Mural/Public Art"].copy()

# Drop rows missing coordinates
df_murals = df_murals.dropna(subset=["latitude", "longitude"])

# Save filtered version
df.to_csv("philly_public_art_all.csv", index=False)       # everything
df_murals.to_csv("philly_public_art.csv", index=False)    # murals only — used in workshop

print(f"Total artworks fetched : {len(df)}")
print(f"Mural/Public Art only  : {len(df_murals)}")
print(f"With coordinates       : {len(df_murals)}")
print(df_murals.head())