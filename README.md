# 🕸️ Website to PDF Scraper (PDFKit Version)

This project is a command-line tool that allows you to **scrape a website and all its internal pages**, then save the cleaned content as a **single PDF file**.

Built using:
- `requests` and `BeautifulSoup` for HTML scraping
- `pdfkit` + `wkhtmltopdf` for PDF generation (Windows-friendly)

---

## ✅ Features

- Scrapes all internal pages of the provided website
- Cleans layout: removes scripts, navigation bars, headers, footers, etc.
- Merges all pages into one neat PDF file with page breaks

---

## 📦 Requirements

### 1. Python Packages

Install Python requirements using:

```bash
pip install -r requirements.txt
```

This will install:
- `requests` – for HTTP requests
- `beautifulsoup4` – for HTML parsing
- `pdfkit` – to convert HTML to PDF

### 2. Install wkhtmltopdf (for PDFKit)

You **must** install the `wkhtmltopdf` binary separately:

👉 [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)

1. Download the **Windows installer** and install it (e.g., to `C:\Program Files\wkhtmltopdf`)
2. Add its `bin` folder to your **System PATH**:

   ```
   C:\Program Files\wkhtmltopdf\bin
   ```

3. Test it's working:

```bash
wkhtmltopdf --version
```

---

## 🚀 How to Use

### 1. Clone or extract this repo

If you downloaded the ZIP, extract it and `cd` into the folder:

```bash
cd website-to-pdf-scraper
```

### 2. Run the scraper with a website URL:

```bash
python main.py https://javascript.info/
```

This will:
- Crawl all internal pages from `https://javascript.info/`
- Clean each page's content
- Generate a PDF called `website_output.pdf` in the same folder

---

## 🧪 Example Output

If run on `https://javascript.info/`, you'll get:

```
website_output.pdf
├── Page 1: JavaScript Overview
├── Page 2: Code Editors
├── Page 3: Syntax & Basic Constructs
└── ...
```

Each page from the site will be separated by a page break.

---

## 💡 Tips

- This scraper only follows **internal links** (within the same domain).
- If a site uses heavy JavaScript for rendering content, consider using Selenium instead.
- You can increase the crawl delay if the site blocks you.

---
