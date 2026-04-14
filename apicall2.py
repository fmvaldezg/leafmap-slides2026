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
df.to_csv("philly_public_art.csv", index=False)
print(f"Saved philly_public_art.csv")
print(df.head())