import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pathlib import Path
from tqdm import tqdm


def write_markdown(file_name, list_entry_sep):

    # Extract unique categories and sort them
    unique_categories = sorted(df["Category"].unique())

    # Create a dictionary for markdown link names
    markdown_links = {
        category: category.lower().replace(" ", "-") for category in unique_categories
    }

    # Initialize Markdown document with the Table of Contents
    markdown_toc = "## Table of Contents:\n"
    for category, link in markdown_links.items():
        markdown_toc += f"- [{category}](#{link})\n"

    with open(file_name, "w") as file:

        file.write(markdown_toc)
        file.write("\n")
        file.write("___\n")
        file.write("<br>\n")

        # Append each category and its papers
        for category, link_name in markdown_links.items():
            file.write(f'\n<a name="{link_name}"></a>\n# {category}\n')
            # Filter the DataFrame for the current category
            category_df = df[df["Category"] == category]
            for index, row in category_df.iterrows():
                shortname = "".join(
                    filter(
                        str.isalnum,
                        f"{row['Authors'].split()[0]}{row['Year']}{row['Title'].split()[0]}",
                    )
                ).lower()

                paper_links = []
                for column_name, link_text in [
                    ("📄 Paper", "PDF"),
                    ("🌐 Project Page", "Project Page"),
                    ("💻 Code", "Code"),
                    ("🎥 Presentation", "Presentation"),
                ]:
                    link = row[column_name]
                    if pd.notnull(link):
                        paper_links.append(f"[{link_text}]({link})")
                links_str = ", ".join(paper_links)

                file.write(f"- <a name=\"{shortname}\"></a>{row['Authors']},")
                file.write(list_entry_sep)
                file.write(f"*[{row['Title']}]({row['📄 Paper']})*,")
                file.write(list_entry_sep)
                file.write(
                    f"{int(row['Year']) if pd.notnull(row['Year']) else ''}, {links_str}"
                )
                file.write("\n")


a3dgs_gsheet_url = "https://docs.google.com/spreadsheets/d/1k9KcnI3DUb6BioFOQ_zg_0pUrOdL6n7oZ1N7nYUDbBE/edit?usp=sharing"
csv_export_url = a3dgs_gsheet_url.replace("/edit?usp=sharing", "/export?format=csv")

df = pd.read_csv(csv_export_url)

write_markdown("awesome_3dgs_papers_3line.md", "  \n  ")
write_markdown("awesome_3dgs_papers.md", " ")
