---
theme: seriph
background: /images/cover.png
title: Field Data Collectins & Mobile GIS
class: text-center
transition: slide-left
mdc: true
duration: 60min
controls: true
presenter: false      
remote: false         
selectable: false     
monaco: false
info: false
drawings:
  enabled: false
contextMenu: false
colorSchema: light
themeConfig:
  primary: '#5d8392'
record: false
routerMode: hash
css: unocss
highlighter: shiki
download: "https://raw.githubusercontent.com/fmvaldezg/field_data_slides/main/slides.pdf"

---

<div class="overlay"></div>

<div class="content-wrapper">

# Mapping and Data Visualization 

<span class="text-3xl">with Python</span>

<div @click="$slidev.nav.next" class="mt-12 py-1 text-xs" hover:bg="white op-10">
  Press Space for next page <carbon:arrow-right />
</div>

</div>

<img 
  src="https://raw.githubusercontent.com/opengeos/leafmap/master/docs/assets/logo_rect.png" 
  class="absolute"
  style="left: 700px; top: 290px; width:130px; background-color: rgba(255, 255, 255, 0); padding: 10px; border-radius: 8px;"
  alt="leafmap logo"
/>

<img 
  src="https://miro.medium.com/v2/resize:fit:1400/0*XuBHZzSmxp8sKmHC.png" 
  class="absolute"
  style="left: 700px; top: 350px; width:130px; background-color: rgba(255, 255, 255, 0); padding: 10px; border-radius: 8px;"
  alt="folium logo"
/>

<img 
  src="/images/librarylogo.png" 
  class="absolute"
  style="left: 70px; top: 300px; width:300px; background-color: rgba(255, 255, 255, 0); padding: 10px; border-radius: 8px;"
  alt="OSM logo"
/>

<div class="abs-br m-6 text-xl">
  <a href="https://charlesstudy.temple.edu/calendar/workshops?&t=g&d=0000-00-00&cal%5B%5D=6197&ct%5B%5D=69157" target="_blank" class="slidev-icon-btn" title="Mapping Workshops at Temple University Libraries">
    <carbon:earth-filled />
  </a>
  <a href="https://library.temple.edu/services/support-for-gis-mapping" target="_blank" class="slidev-icon-btn" title="Temple University GIS Support">
    <carbon:information-filled />
  </a>
</div>

<style>
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
  z-index: 1;
  pointer-events: none;
}

.content-wrapper {
  position: relative;
  z-index: 2;
}

.abs-br {
  position: absolute !important;
  bottom: 0.5rem !important;
  right: 0.5rem !important;
  z-index: 10 !important;
}
</style>


---
transition: fade-out
---

# What is Leafmap?

Leafmap is a Python package for interactive mapping and geospatial analysis with minimal coding in Jupyter environments (Jupyter Notebook, JupyterLab, Google Colab). 

- **Easy** - simple API for creating interactive maps
- **Powerful** - built on top of ipyleaflet and folium
- **Flexible** - works in Jupyter notebooks and web apps

---
layout: two-cols
---

# Pre-requisites

1. Install Python:
   
   - Download from [python.org](https://www.python.org/downloads/)

2. Install required libraries

```bash
pip install leafmap geopandas pandas jupyterlab
```

3. Download the [workshop files](https://raw.githubusercontent.com/fmvaldezg/leafmap-slides2026/workshop_files.zip)

4. Launch and test Jupyter Lab
   
- navigate to the downloaded folder

```bash
cd Desktop/workshop-files
```

- Launch jupyter lab
   
```bash
jupyter lab
```

::right::

<img src="/images/prerequisites.png" style="height: 100%; width: 100%; object-fit: contain;" />


---

# Getting Started

```python {all|1|3|4}
import leafmap

m = leafmap.Map(center=[40, -100], zoom=4)
m
```

<div class="relative min-h-48">

<div v-click="[1,2]" class="absolute top-0 left-0 w-full">

#### Line 1: Importing the library

<div class="bg-gray-50 p-4 rounded-lg mb-4 border-l-4 border-green-200">
<div class="flex items-center mb-2">
</div>
<div class="font-mono text-green-600">import leafmap</div>
<div> brings all the code in the leafmap library to the environment</div>
</div>

</div>

<div v-click="[2,3]" class="absolute top-0 left-0 w-full">

#### Line 2: Setting a map

<div class="bg-gray-50 p-4 rounded-lg mb-4 border-l-4 border-green-200">
Set map center with lat,long coordinates
<div class="font-mono text-green-600">center=[40,-100]</div> Set zoom level (from 0 to 22)
<div class="font-mono text-green-600">zoom=4</div> 
</div>

</div>

<div v-click="3" class="absolute top-0 left-0 w-full">

#### Line 3: Return the "m" element (map)

<div class="bg-gray-50 p-4 rounded-lg mb-4 border-l-4 border-green-200">
<div class="font-mono text-green-600">m</div> Prints the results
</div>

</div>

</div>

---
layout: section
---

# leafmap's Unique Strengths

What leafmap does that nothing else does as easily

---

# What leafmap Does Best

<div class="overflow-auto">

| Strength | Why leafmap? |
|---|---|
| **Cloud-Optimized GeoTIFFs (COG)** | Stream satellite imagery directly from S3/cloud — no download |
| **Split-panel comparison** | Before/after view with a draggable divider — one method call |
| **WMS tile services** | Load live layers from government and research servers |
| **STAC catalog access** | Browse and visualize spatiotemporal asset catalogs |
| **Linked multi-panel maps** | Synchronized views for comparing multiple datasets |

</div>

> Open `leafmap_demo.ipynb` to follow along

---

# 1. Cloud-Optimized GeoTIFFs (COG)

A **COG** is a satellite image stored on a cloud server that lets you view any part of it without downloading the whole file.

```python {all|1-2|4-5|6}
url_after = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-09-13.tif"

m = leafmap.Map(center=[32.75, 22.63], zoom=13)
m.add_cog_layer(url_after, name="Libya — Post-flood (Sep 2023)")
m
```

<div class="relative min-h-36 mt-4">

<div v-click="[1,2]" class="absolute top-0 left-0 w-full">
<div class="bg-gray-50 p-4 rounded-lg border-l-4 border-blue-300">

**The URL points to a GeoTIFF on GitHub Releases (or any S3/HTTP server)**  
No `download_file()` call — leafmap streams it on the fly

</div>
</div>

<div v-click="[2,3]" class="absolute top-0 left-0 w-full">
<div class="bg-gray-50 p-4 rounded-lg border-l-4 border-blue-300">

**`add_cog_layer(url, name=...)`**  
One line to load a full satellite scene. Tiles load progressively as you zoom in.

</div>
</div>

<div v-click="3" class="absolute top-0 left-0 w-full">
<div class="bg-gray-50 p-4 rounded-lg border-l-4 border-blue-300">

**`m`** renders the interactive map inline in the notebook

</div>
</div>

</div>

---
layout: image
image: /images/step1.png
backgroundSize: contain
--- 

---

# 2. Split-Panel Comparison Map

`split_map()` creates a side-by-side view with a **draggable divider** — drag left/right to compare.

```python {all|1-2|4-12}
url_before = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-07-01.tif"
url_after  = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-09-13.tif"

m = leafmap.Map(center=[32.75, 22.63], zoom=13, height=500)
m.split_map(
    left_layer=url_before,
    right_layer=url_after,
    left_label="Before — July 2023",
    right_label="After — September 2023 (flooding)"
)
m
```

<div v-click class="mt-3 bg-gray-50 p-3 rounded-lg border-l-4 border-green-300 text-sm">

`split_map()` also works with **basemap names** — no COG URL needed:

```python
m.split_map(left_layer="Esri.WorldImagery", right_layer="CartoDB.Positron")
```

</div>

---
layout: image
image: /images/step2.png
backgroundSize: contain
--- 

---

# 3. WMS Tile Services

**WMS (Web Map Service)** is a standard protocol used by governments and research institutions to serve live map data. leafmap loads any WMS layer in two lines.

```python {all|1-2|4-10|11-12}
# NLCD 2021 Land Cover — live from the USGS/MRLC server
wms_url = "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2021_Land_Cover_L48/wms?"

m = leafmap.Map(center=[40, -100], zoom=4)
m.add_wms_layer(
    wms_url,
    layers="NLCD_2021_Land_Cover_L48",
    name="NLCD 2021 Land Cover",
    format="image/png",
    transparent=True
)
m.add_legend(builtin_legend="NLCD", title="Land Cover Type")
m
```

<div class="relative min-h-28 mt-2">

<div v-click="[1,2]" class="absolute top-0 left-0 w-full">
<div class="bg-gray-50 p-3 rounded-lg border-l-4 border-green-300 text-sm">
The WMS URL comes from the USGS MRLC server — no download, data is always current
</div>
</div>

<div v-click="[2,3]" class="absolute top-0 left-0 w-full">
<div class="bg-gray-50 p-3 rounded-lg border-l-4 border-green-300 text-sm">
<code>layers=</code> matches the layer name in the WMS server's capabilities document
</div>
</div>

<div v-click="3" class="absolute top-0 left-0 w-full">
<div class="bg-gray-50 p-3 rounded-lg border-l-4 border-green-300 text-sm">
<code>add_legend(builtin_legend="NLCD")</code> — leafmap ships with NLCD and other built-in legends
</div>
</div>

</div>

---
layout: image
image: /images/step3.png
backgroundSize: contain
--- 

---

# 4. Land Cover Change — WMS Split Map

leafmap has NLCD pre-configured as built-in basemap names. Combine with `split_map()` to show **20 years of land cover change** — no WMS setup needed.

```python
m = leafmap.Map(center=[36.1, -114.9], zoom=9, height=500)
m.split_map(
    left_layer="NLCD 2001 CONUS Land Cover",
    right_layer="NLCD 2021 CONUS Land Cover",
    left_label="2001",
    right_label="2021"
)
m.add_legend(builtin_legend="NLCD", title="Land Cover")
m
```

<div class="mt-4 grid grid-cols-2 gap-4 text-sm">
<div class="bg-gray-50 p-3 rounded-lg border-l-4 border-purple-300">

**Left panel — 2001**  
The landscape before rapid development around Las Vegas, NV

</div>
<div class="bg-gray-50 p-3 rounded-lg border-l-4 border-purple-300">

**Right panel — 2021**  
Urban sprawl visible as gray/developed land cover expanded

</div>
</div>

---
layout: image
image: /images/step4.png
backgroundSize: contain
--- 

---

# 5. STAC — SpatioTemporal Asset Catalog

**STAC** is a standard for organizing petabytes of satellite imagery. NASA, Microsoft Planetary Computer, and AWS all host STAC catalogs. leafmap loads a STAC item directly from a URL.

```python {all|1-4|6|8-11|13}
stac_url = (
    "https://canada-spot-ortho.s3.amazonaws.com/canada_spot_orthoimages/"
    "canada_spot5_orthoimages/S5_2007/S5_11055_6057_20070622/S5_11055_6057_20070622.json"
)

print("Available bands:", leafmap.stac_bands(stac_url))
# → ['pan', 'B1', 'B2', 'B3', 'B4']

m = leafmap.Map(center=[60.57, -110.55], zoom=10)
m.add_stac_layer(stac_url, bands=["B3","B2","B1"], name="True Color (RGB)", vmin=0, vmax=150)
m.add_stac_layer(stac_url, bands=["B4","B3","B2"], name="False Color (NIR)", shown=False)

m.add_layer_control()
m
```

<div v-click class="mt-3 bg-gray-50 p-3 rounded-lg border-l-4 border-blue-300 text-sm">

`shown=False` loads the layer but keeps it hidden — toggle it on via the layer control.  
False color (NIR) highlights vegetation in bright red.

</div>

---
layout: image
image: /images/step5.png
backgroundSize: contain
--- 

---

# 6. Linked Multi-Panel Maps

`leafmap.linked_maps()` creates multiple maps that are **synchronized** — pan or zoom one and all others follow.

```python
layers = [f"NLCD {year} CONUS Land Cover" for year in [2001, 2006, 2016, 2021]]
labels = [f"NLCD {year}" for year in [2001, 2006, 2016, 2021]]

leafmap.linked_maps(
    rows=2,
    cols=2,
    height="300px",
    layers=layers,
    labels=labels,
    center=[36.1, -115.2],
    zoom=9
)
```

<div class="mt-4 bg-amber-50 p-3 rounded-lg border-l-4 border-amber-400 text-sm">

Four NLCD snapshots in a 2×2 grid — zoom into any panel and the others jump to the same location.  
Great for teaching land cover change or comparing multiple scenarios.

</div>

---
layout: image
image: /images/step6.png
backgroundSize: contain
--- 

---

# leafmap vs Folium — When to Use Which

| Use case | leafmap | Folium |
|---|---|---|
| Satellite imagery (COG/STAC) | ✅ Best choice | ❌ Not supported |
| Before/after split map | ✅ One line | ⚠️ Complex setup |
| WMS tile services | ✅ Simple | ✅ Works |
| Linked synchronized maps | ✅ Built-in | ❌ Not supported |
| Vector data (points, polygons) | ⚠️ Works in notebook | ✅ Best choice |
| Choropleth maps | ⚠️ Works but quirky | ✅ Best choice |
| HTML export for web | ⚠️ Widget-based, fragile | ✅ Clean Leaflet.js |



---
layout: section
---

# Part 2: Folium Workshop

Philadelphia Public Art — Building an Interactive Web Map

--- 
layout: iframe
url: "https://fmvaldezg.codeberg.page/leafmap_folium_demo/map.html"
---

---
# What is Folium?

Folium is a Python library that generates **clean, standalone Leaflet.js HTML maps**.

```python
import folium

m = folium.Map(location=[39.952, -75.165], zoom_start=12)
m.save("map.html")   # → pure HTML, no Python server needed
```

<div class="mt-6 grid grid-cols-2 gap-4 text-sm">

<div class="bg-gray-50 p-4 rounded-lg border-l-4 border-orange-300">

**Strengths**
- Exports to self-contained HTML
- Works everywhere — GitHub Pages, email, CDN
- Clean Leaflet.js output
- Great for choropleths and vector data

</div>

<div class="bg-gray-50 p-4 rounded-lg border-l-4 border-orange-300">

**Workshop goal**
- Load 534 Philadelphia public artworks from a CSV
- Color points by decade
- Add click popups with artwork details
- Build a choropleth (artworks per neighborhood)
- Export to GitHub Pages

</div>

</div>

<div class="mt-4 text-sm text-gray-500">

> Open `philly_public_art_folium.ipynb` to follow along

</div>

---

# Step 1 — Create an Empty Map

```python {all|1|2}
m = folium.Map()
m
```

<div class="relative min-h-32 mt-4">

<div v-click="[1,2]" class="absolute top-0 left-0 w-full">
<div class="bg-gray-50 p-4 rounded-lg border-l-4 border-orange-300">

`folium.Map()` with no arguments creates a world map centered at `[0, 0]` with zoom 1.  
The map renders inline in the notebook.

</div>
</div>

<div v-click="2" class="absolute top-0 left-0 w-full">
<div class="bg-gray-50 p-4 rounded-lg border-l-4 border-orange-300">

`m` on its own line tells Jupyter to display the map widget.  
Unlike leafmap, `m` here is a pure HTML object — no widgets needed.

</div>
</div>

</div>

---

# Step 2 — Center, Zoom, and Basemap

```python {all|2|3|4}
m = folium.Map(
    location=[39.952, -75.165],   # Philadelphia center
    zoom_start=12,                # city-level zoom
    tiles="CartoDB Positron"      # clean light basemap
)
m
```

<div class="mt-4 text-sm">

**Common basemap options:**

| `tiles=` value | Style |
|---|---|
| `"OpenStreetMap"` | Detailed street map (default) |
| `"CartoDB Positron"` | Clean light — best for data visualization |
| `"CartoDB DarkMatter"` | Dark background |

</div>

<div v-click class="mt-4 bg-gray-50 p-3 rounded-lg border-l-4 border-green-300 text-sm">

**Try it:** Change `tiles=` to `"CartoDB DarkMatter"` and re-run. The basemap swaps instantly.

</div>

---
layout: image
image: /images/step22.png
backgroundSize: contain
--- 

---

# Step 3 — Load a GeoJSON Layer

```python {all|1-3|5-14}
neighborhoods_url = (
    "https://raw.githubusercontent.com/opendataphilly/open-geo-data/master/"
    "philadelphia-neighborhoods/philadelphia-neighborhoods.geojson"
)

m = folium.Map(location=[39.952, -75.165], zoom_start=12, tiles="CartoDB Positron")

folium.GeoJson(
    neighborhoods_url,
    name="Neighborhoods",
    style_function=lambda x: {
        "color": "#555555",
        "weight": 0.8,
        "fillOpacity": 0.0
    }
).add_to(m)
```

<div class="relative min-h-24 mt-2">

<div v-click="[1,2]" class="absolute top-0 left-0 w-full">
<div class="bg-gray-50 p-3 rounded-lg border-l-4 border-blue-300 text-sm">

Folium loads GeoJSON directly from a URL — 158 Philadelphia neighborhood boundaries from OpenDataPhilly.

</div>
</div>

<div v-click="2" class="absolute top-0 left-0 w-full">
<div class="bg-gray-50 p-3 rounded-lg border-l-4 border-blue-300 text-sm">

`style_function` is a lambda that returns a style dict for each feature.  
`fillOpacity: 0.0` shows only outlines — no fill color yet.

</div>
</div>

</div>

---
layout: image
image: /images/step23.png
backgroundSize: contain
--- 

---

# Step 4 — Load Point Data from CSV

```python {all|1-3|4-6}
art_df = pd.read_csv("philly_public_art.csv")
art_df = art_df.dropna(subset=["latitude", "longitude"])
art_df["year"] = pd.to_numeric(art_df["year"], errors="coerce")

for _, row in art_df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=4,
        color="#333333",
        fill=True,
        fill_color="#e8a320",
        fill_opacity=0.8
    ).add_to(m)
```

<div class="mt-4 grid grid-cols-2 gap-3 text-sm">
<div class="bg-gray-50 p-3 rounded-lg border-l-4 border-orange-300">

**Dataset:** 534 Philadelphia artworks  
Columns: `title`, `artist`, `year`, `type`, `latitude`, `longitude`  
Year range: 1400 – 2024

</div>
<div class="bg-gray-50 p-3 rounded-lg border-l-4 border-orange-300">

**`CircleMarker`** draws a fixed-pixel circle at a lat/lon.  
Unlike `Marker` (pin icon), it scales well with many points.

</div>
</div>

---
layout: image
image: /images/step24.png
backgroundSize: contain
--- 

---

# Step 5 — Color Points by Decade

In Folium, coloring by attribute is simple: compute the color in Python, pass it to `fill_color`.

```python {all|1-7|9-10|12}
DECADE_COLORS = {
    1980: "#fd8d3c",   # Mural Arts program founded
    1990: "#e6550d",
    2000: "#a63603",
    2010: "#8856a7",
    2020: "#810f7c",
}

def get_decade_color(year):
    ...   # compute decade, look up in DECADE_COLORS

art_df["color"] = art_df["year"].apply(get_decade_color)

for _, row in art_df.iterrows():
    folium.CircleMarker(..., fill_color=row["color"], ...).add_to(m)
```

<div v-click class="mt-3 bg-amber-50 p-3 rounded-lg border-l-4 border-amber-400 text-sm">

**Why 1980?** Philadelphia's Mural Arts Program launched in 1984, sparking a wave of public art. The orange/red colors highlight this era.

</div>

---
layout: image
image: /images/step25.png
backgroundSize: contain
--- 

---

# Step 6 — Add Popups and Tooltips

```python {all|1-9|10-13}
for _, row in art_df.iterrows():
    popup_html = f"""
        <div style="font-family: Arial; font-size: 12px; width: 180px;">
            <b style="color: #3d0059;">{row['title']}</b><br>
            <span style="color: #555;">{artist}</span><br>
            <span style="color: #888;">{year}</span>
        </div>
    """
    folium.CircleMarker(
        ...,
        popup=folium.Popup(popup_html, max_width=200),
        tooltip=row["title"]
    ).add_to(m)
```

<div class="mt-3 grid grid-cols-2 gap-2 text-sm">
<div class="bg-gray-50 p-2 rounded-lg border-l-4 border-purple-300">

**`popup`** — HTML shown on **click**.  
`folium.Popup(html, max_width=...)` wraps the string.

</div>
<div class="bg-gray-50 p-2 rounded-lg border-l-4 border-purple-300">

**`tooltip`** — plain text on **hover**.  
Keep it short — just the artwork title.

</div>
</div>

---
layout: image
image: /images/step26.png
backgroundSize: contain
--- 

---

# Step 7 — Choropleth Map

A **choropleth** colors geographic areas by a numeric value. We count artworks per neighborhood using a **spatial join**.

```python {all|1-3|5-13}
# Spatial join — count artworks per neighborhood
art_gdf = gpd.GeoDataFrame(art_df, geometry=gpd.points_from_xy(art_df["longitude"], art_df["latitude"]), crs="EPSG:4326")
art_counts = gpd.sjoin(art_gdf, neighborhoods, how="left", predicate="within").groupby("MAPNAME").size().reset_index(name="artwork_count")

# Choropleth layer
folium.Choropleth(
    geo_data=neighborhoods_with_art,
    data=neighborhoods_with_art,
    columns=["MAPNAME", "artwork_count"],
    key_on="feature.properties.MAPNAME",
    fill_color="YlOrRd",
    fill_opacity=0.75,
    legend_name="Artworks per Neighborhood"
).add_to(m)
```

<div v-click class="mt-3 bg-gray-50 p-3 rounded-lg border-l-4 border-red-300 text-sm">

**Top neighborhoods:** East Park (76), University City (64), Logan Square (52)

</div>

---
layout: image
image: /images/step27.png
backgroundSize: contain
--- 

---

# Step 8 — Final Polished Map

Combine all layers into one map with a **title**, **decade legend**, and **layer control**.

```python
m_final = folium.Map(location=[39.952, -75.165], zoom_start=12, tiles="CartoDB Positron")

# 1. Choropleth base
folium.Choropleth(...).add_to(m_final)

# 2. Artwork points with popups (in a FeatureGroup for toggling)
art_layer = folium.FeatureGroup(name="Public Art (by decade)")
for _, row in art_df.iterrows():
    folium.CircleMarker(...).add_to(art_layer)
art_layer.add_to(m_final)

# 3. Custom HTML legend (bottom-left corner)
legend_html = """<div style="position:fixed; bottom:40px; left:10px; ...">...</div>"""
m_final.get_root().html.add_child(folium.Element(legend_html))

# 4. Layer toggle control
folium.LayerControl().add_to(m_final)
m_final
```
---
layout: image
image: /images/step28.png
backgroundSize: contain
--- 

---

# Step 9 — Export to HTML

Folium generates pure Leaflet.js HTML — no widgets, no server, no dependencies.

```python
m_final.save("index.html")
```

<div class="mt-4 grid grid-cols-2 gap-3 text-sm">

<div class="bg-blue-50 p-3 rounded-lg border-l-4 border-blue-400">

**Preview locally**
```bash
python -m http.server 8000
```
Open `http://localhost:8000/index.html`

</div>

<div class="bg-green-50 p-3 rounded-lg border-l-4 border-green-400">

**Publish on GitHub Pages**
1. Create a new GitHub repository
2. Upload `index.html` to the root
3. Settings → Pages → Source → `main / root`
4. Live at `yourusername.github.io/yourrepo/`

</div>

</div>

<div class="mt-3 bg-gray-50 p-2 rounded-lg border-l-4 border-gray-400 text-sm">

Pure Leaflet.js HTML — no Python server needed. Share via link, email, or embed with `<iframe>`.

</div>

---

# Workshop Summary

| Step | Skill |
|------|-------|
| 1–2  | Create a map, set center, zoom, and basemap |
| 3    | Load a GeoJSON polygon layer from a URL |
| 4    | Load point data from a CSV file |
| 5    | Color points by a data attribute (decade) |
| 6    | Add HTML popups and hover tooltips |
| 7    | Spatial join + choropleth with `folium.Choropleth` |
| 8    | Combine layers, legend, title into a final map |
| 9    | Export to standalone HTML / GitHub Pages |


---
layout: center
class: text-center
---

# Learn More

**leafmap:** [leafmap.org](https://leafmap.org) · [Notebooks gallery](https://leafmap.org/notebooks/00_key_features/)

**Folium:** [python-visualization.github.io/folium](https://python-visualization.github.io/folium/)

**Data:** [OpenDataPhilly](https://opendataphilly.org) · [philart.net](https://www.philart.net)

**Standards:** [STAC specification](https://stacspec.org) · [Cloud-Optimized GeoTIFF](https://cogeo.org)

<br>

[GitHub](https://github.com/opengeos/leafmap) · [Report issues](https://github.com/anthropics/claude-code/issues)

--- 
layout: end
---

Contact us at:\
felipe.valdez@temple.edu \
<br>
Visit our guides:\
https://guides.temple.edu/gis-mapping

<style>
.slidev-layout.end {
  background: linear-gradient(135deg, rgb(164, 30, 53) 0%, rgb(149, 56, 71) 100%);
}
</style>