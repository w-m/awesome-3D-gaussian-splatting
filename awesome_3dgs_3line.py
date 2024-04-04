# Reformats the list from https://github.com/MrNeRF/awesome-3D-gaussian-splatting into a denser format
# See discussion: https://github.com/MrNeRF/awesome-3D-gaussian-splatting/issues/91

import pandas as pd

from awesome_3dgs_parse import parse_awesome_3dgs_md


def write_markdown(
    file_name, list_entry_sep, title_before_author=True, include_abstract=False
):

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
                for emoji, column_name, column_comment in [
                    ("📄", "📄 Paper", "📄 Comment"),
                    ("🌐", "🌐 Project Page", "🌐 Comment"),
                    ("💻", "💻 Code", "💻 Comment"),
                    ("🎥", "🎥 Presentation", "🎥 Comment"),
                ]:
                    link = row[column_name]
                    if pd.notnull(link) and not link == "":
                        paper_links.append(f"[{emoji} {row[column_comment]}]({link})")
                links_str = ", ".join(paper_links)

                file.write(f'- <a name="{shortname}"></a>')

                authors = f"{row['Authors']}"
                title = f"*[{row['Title']}]({row['📄 Paper']})*"

                if title_before_author:
                    file.write(f"{title},{list_entry_sep}{authors},{list_entry_sep}")
                else:
                    file.write(f"{authors},{list_entry_sep}{title},{list_entry_sep}")

                if pd.notnull(row["Tag"]) and not row["Tag"] == "":
                    file.write(f"{row['Tag']}, ")

                if pd.notnull(row["Year"]) and not row["Year"] == "":
                    file.write(f"{int(row['Year'])}, ")
                file.write(f"{links_str}")

                if (
                    include_abstract
                    and pd.notnull(row["Abstract"])
                    and not row["Abstract"] == ""
                ):
                    file.write(f"{list_entry_sep}")
                    file.write(
                        f"<details><summary>Abstract</summary>{row['Abstract']}</details>"
                    )

                file.write("\n")


df = parse_awesome_3dgs_md()

# three lines per paper
write_markdown(
    "awesome_3dgs_papers_3line.md", list_entry_sep="  \n  ", title_before_author=False
)

write_markdown(
    "awesome_3dgs_papers_full_abs.md",
    list_entry_sep="  \n  ",
    title_before_author=False,
    include_abstract=True,
)

# one line per paper (most dense)
write_markdown("awesome_3dgs_papers.md", list_entry_sep=" ", title_before_author=True)
