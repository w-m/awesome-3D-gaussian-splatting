import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pathlib import Path
from tqdm import tqdm


def sanitize_filename(filename):
    """Sanitize the filename to avoid illegal characters."""
    return "".join(
        [c for c in filename if c.isalpha() or c.isdigit() or c in " ._-"]
    ).rstrip()


def find_image_url(page_url):
    """Fetch the page and look for an image URL in the meta tags."""
    try:
        response = requests.get(page_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            image_tags = soup.find_all("meta", attrs={"property": "og:image"})
            if not image_tags:
                image_tags = soup.find_all("meta", attrs={"name": "twitter:image"})
            if image_tags:
                return urljoin(page_url, image_tags[0]["content"])
    except Exception as e:
        print(f"Failed to fetch or parse {page_url}: {e}")
    return None


a3dgs_gsheet_url = "https://docs.google.com/spreadsheets/d/1k9KcnI3DUb6BioFOQ_zg_0pUrOdL6n7oZ1N7nYUDbBE/edit?usp=sharing"
csv_export_url = a3dgs_gsheet_url.replace("/edit?usp=sharing", "/export?format=csv")

df = pd.read_csv(csv_export_url)

# Create a directory for downloaded images
images_dir = "3dgs_thumbs"
Path(images_dir).mkdir(parents=True, exist_ok=True)

# Prepare a summary list
summary = []

# Wrap your iteration with tqdm for a progress bar
for _, row in tqdm(df.iterrows(), total=df.shape[0], desc="Processing Papers"):
    title = row["Title"]
    project_page = row["🌐 Project Page"]
    if pd.notna(project_page):
        image_url = find_image_url(project_page)
        if image_url:
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                filename = sanitize_filename(title) + Path(image_url).suffix
                with open(os.path.join(images_dir, filename), "wb") as file:
                    file.write(image_response.content)
                summary.append(
                    {"Title": title, "Image Found": "Yes", "Filename": filename}
                )
            else:
                summary.append({"Title": title, "Image Found": "No"})
        else:
            summary.append({"Title": title, "Image Found": "No"})
    else:
        summary.append({"Title": title, "Image Found": "No"})

# Convert the summary to a DataFrame and save/export as needed
summary_df = pd.DataFrame(summary)
summary_df.to_csv("summary_table.csv", index=False)

# Print out a summary of the results
images_downloaded = summary_df["Image Found"].value_counts().get("Yes", 0)
print(f"Total images found and downloaded: {images_downloaded}")
