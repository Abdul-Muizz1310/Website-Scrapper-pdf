# 📚 JavaScript.info PDF Scraper — Individual Article PDFs

This Python project crawls all tutorial pages on [https://javascript.info](https://javascript.info), extracts **only the core content**
(`<div itemprop="articleBody">`), removes all distractions like navigation bars, comments, links, and images, and then saves **each page as a clean PDF**.

> ✅ Perfect for offline study, archiving, or printing

---

## 🚀 Features

- 🔎 Crawls every article on `https://javascript.info`
- 🧽 Removes:
  - Navigation bars
  - Comments
  - Images and icons
  - Hyperlinks (text is preserved)
- ✂️ Extracts only the main content (`articleBody`)
- 📄 Saves **one PDF per article**, using the URL path as the filename
- 🖨️ PDF preserves original styles using **Playwright browser rendering**

---

## 🧰 Project Structure

```
website-scraper-pdf/
├── output/                   # 📄 Individual PDF files go here
├── scraper/
│   ├── __init__.py
│   ├── crawler.py            # 🔗 Collects internal links
│   └── merger.py             # 🧽 Cleans & generates PDF per page
├── main.py                   # 🚀 Entry point
├── requirements.txt          # 📦 Dependencies
└── README.md                 # 📘 This file
```

---

## ⚙️ Prerequisites

- Python 3.8+
- Google Chrome (installed automatically via Playwright)

---

## 🔧 Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/reponame.git
cd reponame

# 2. Set up a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install Playwright browsers
playwright install
```

---

## 🧪 Run the Scraper

```bash
python main.py
```

Each page will:
- Load in a headless browser
- Be cleaned and simplified
- Be saved as a `.pdf` in the `output/` folder

---

## 🗂️ Example Output

| URL | Saved As |
|-----|----------|
| `https://javascript.info/` | `output/index.pdf` |
| `https://javascript.info/types` | `output/types.pdf` |
| `https://javascript.info/object/constructor` | `output/object_constructor.pdf` |

---

## 🔍 Customization Tips

Want to test with fewer pages?

Edit `main.py`:
```python
links = get_internal_links(base_url)
links = links[:10]  # Limit to first 10 pages
```

Want to exclude certain sections?

In `scraper/crawler.py`, add to `UNWANTED_SUBSTRINGS`:
```python
"/feedback", "/rss", ".xml", ".json"
```

---