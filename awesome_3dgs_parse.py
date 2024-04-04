import requests
import pandas as pd
import re

import pandas as pd
import re


def parse_markdown_to_csv(markdown_text):
    # Initialize variables
    category = ""
    year = ""
    data = []
    collecting_abstract = False
    abstract_lines = []
    start_parsing = False
    tag = ""

    # Split the text into lines for processing
    lines = markdown_text.split("\n")

    for line in lines:
        # Start parsing from the seminal paper introduction
        if "## Seminal Paper introducing 3D Gaussian Splatting:" in line:
            start_parsing = True
        if not start_parsing:
            continue  # Skip lines until the seminal paper section is reached

        # Stop parsing after the "Data" section
        if "## Data" in line:
            break

        # Detect new category or year
        if line.startswith("## "):
            # Check if the line indicates a year (presence of an integer followed by a colon)
            year_match = re.match(r"## (\d{4}):", line)
            if year_match:
                year = year_match.group(1)
            else:
                # If not a year, it's a category, respecting the <br> as a new category indicator
                category = line.strip("## ").strip().strip(":")
            continue

        # Process individual paper entries
        if line.startswith("###"):
            # Reset abstract collection for the new entry
            if collecting_abstract:
                abstract = " ".join(abstract_lines).strip()
                abstract_lines = []
                collecting_abstract = False

            title = line.split(" ", 2)[-1].strip()

            # Regular expression to find a tag in the title
            tag_pattern = re.compile(r"\[(.*?)\]")
            match = tag_pattern.search(title)

            if match:
                # Extract tag and remove it from the title
                tag = match.group(1)  # This captures the content within the brackets
                title = tag_pattern.sub(
                    "", title
                ).strip()  # Remove the tag from the title
            else:
                tag = ""

            continue  # Extract title and skip to next line

        if "**Authors**:" in line:
            authors = line.split("**Authors**:", 1)[-1].strip()
            continue  # Extract authors and skip to next line

        if "<details" in line:
            collecting_abstract = True
            continue

        if collecting_abstract:
            if "</details>" in line:
                collecting_abstract = False
                # Remove the initial tag from the first line of the abstract
                if abstract_lines:
                    # drop "<summary><b>Abstract</b></summary>"...
                    abstract_lines = abstract_lines[1:]
                abstract = " ".join(abstract_lines).strip()
                abstract_lines = []  # Reset for the next entry
            else:
                abstract_lines.append(line)
            continue

        # Assuming 'line' is the current line being processed

        # Define a dictionary for emoji to column name mapping
        emoji_to_column = {
            "📄": "📄 Paper",
            "🌐": "🌐 Project Page",
            "💻": "💻 Code",
            "🎥": "🎥 Presentation",
        }

        # Initialize a dictionary to hold link categories and their texts
        link_categories = {}

        has_category = False

        # Extract all links and their texts
        for emoji, column_name in emoji_to_column.items():
            if emoji in line:
                # Regular expression to extract URL and its text
                pattern = re.compile(r"\[" + re.escape(emoji) + r" (.*?)\]\((.*?)\)")
                match = pattern.search(line)
                if match:
                    link_text, link_url = match.groups()
                    link_categories[column_name] = link_url
                    link_categories[emoji + " Comment"] = link_text

                has_category = True

        if has_category:
            # Prepare data entry
            entry = {
                "Category": category,
                "Year": year,
                "Title": title,
                "Authors": authors,
                "Tag": tag,
                **link_categories,
                "Abstract": abstract,
            }
            data.append(entry)

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv("awesome_3dgs_papers.csv", index=False)


# Example usage
if __name__ == "__main__":
    # URL of the markdown file
    url = "https://raw.githubusercontent.com/MrNeRF/awesome-3D-gaussian-splatting/main/README.md"

    # Fetch the markdown content
    response = requests.get(url)
    if response.status_code == 200:
        markdown_text = response.text

        # Continue with parsing and saving to CSV
        df = parse_markdown_to_csv(markdown_text)
    else:
        print("Failed to fetch the markdown content.")

    # # Load markdown text from a file or any source
    # with open(
    #     "/Users/morgenstern/dev/GitHub/awesome-3D-gaussian-splatting/README.md",
    #     "r",
    #     encoding="utf-8",
    # ) as file:
    #     markdown_text = file.read()

    # # Parse and save to CSV
    # parse_markdown_to_csv(markdown_text)
