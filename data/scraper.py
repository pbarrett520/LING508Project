# This has issues accurately retrieving data from some webpages, likely because I think some have slight variations in the HTML structure than the one I based this script on.
import requests
from bs4 import BeautifulSoup


def extract_section_content(soup, section_id):
    """Extracts content under a given section ID from the soup."""
    section = soup.find("span", {"id": section_id})
    content = []
    if section:
        for sibling in section.find_parent().find_next_siblings():
            if sibling.name and sibling.name.startswith('h'):
                break
            content.append(str(sibling))
    return "\n".join(content)


def extract_romanizations_from_section(section_content): # I wanted to select the non- IPA romanizations to make the app more accessible, but it seems sometimes it grabs IPA anyways?
    """Extracts romanizations from a given section content."""
    soup_section = BeautifulSoup(section_content, "html.parser")
    romanizations = {}
    dialect_specs = {
        "Mandarin": ("a", "span"),
        "Cantonese": ("a", "span"),
        "Hakka": ("a", "span"),
        "Wu": ("a", "span"),
        "Xiang": ("a", "span"),
        "Min Nan": ("a", "span"),
        "Jin": ("a", "span"),
        "Gan": ("a", "span")
    }
    for dialect, (tag_name, next_tag_name) in dialect_specs.items():
        dialect_section = soup_section.find(lambda tag: tag.name == tag_name and dialect in tag.get_text())
        if dialect_section:
            romanization_tag = dialect_section.find_next(next_tag_name, class_=lambda x: x != "IPA")
            if romanization_tag:
                romanizations[dialect] = romanization_tag.get_text(strip=True)
    return romanizations


def save_to_file_no_blanks(filename, data):
    """Saves the scraped pronunciations to a text file without blank entries."""
    with open(filename, 'w', encoding='utf-8') as file:
        for char, pronunciations in data.items():
            if pronunciations:
                file.write(f"{char}:\n")
                for dialect, pronunciation in pronunciations.items():
                    file.write(f"  {dialect}: {pronunciation}\n")
                file.write("\n")


# Begin scraping
all_pronunciations = {}
start_unicode = 0x4E00  # Let's just iterate through characters by their unicode encodings. Frequency may be arguably a better criteria, but this was more convenient.
current_char = start_unicode

while len(all_pronunciations) < 50: # Let's arbitratily grab 50 and see what we get
    char = chr(current_char)
    url = f"https://en.wiktionary.org/wiki/{char}"
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, "html.parser")

    content_pronunciation_1 = extract_section_content(soup, "Pronunciation_1") # Wikitionary has two tables with romanizations, for some reason.
    content_pronunciation_2 = extract_section_content(soup, "Pronunciation_2")

    romanizations_from_p1 = extract_romanizations_from_section(content_pronunciation_1)
    romanizations_from_p2 = extract_romanizations_from_section(content_pronunciation_2)

    combined_romanizations = {**romanizations_from_p1, **romanizations_from_p2}

    # Only add to the dictionary if we have valid pronunciations
    if combined_romanizations and len(combined_romanizations) == 8: # Make sure we have all 8 desired dialects, otherwise throw it out. Need to debug more to find out why all 8 aren't consistently returned.
        all_pronunciations[char] = combined_romanizations

    current_char += 1

# Save the results to a text file
save_to_file_no_blanks("pronunciations1.txt", all_pronunciations)

# This script has some issues. It's hard to fully debug because that would require downloading lots of html files to test on locally and wikitionary "locks me out" after x amount of requests in a certain time span.