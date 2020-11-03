import json
from data.data_dicts.contact import data as contact_data
from data.data_dicts.hours import data as hours_data
from data.data_dicts.about import data as about_data


if __name__ == "__main__":
    """Converts python dicts to json."""
    with open('json/contact.json', 'w', encoding='utf-8') as f:
        json.dump(contact_data, f, ensure_ascii=False, indent=4)

    with open('json/hours.json', 'w', encoding='utf-8') as f:
        json.dump(hours_data, f, ensure_ascii=False, indent=4)

    with open('json/about.json', 'w', encoding='utf-8') as f:
        json.dump(about_data, f, ensure_ascii=False, indent=4)
