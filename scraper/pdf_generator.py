import pdfkit

class PDFGenerator:
    def __init__(self, html_pages):
        self.html_pages = html_pages

    def create_pdf(self, output_path="output.pdf"):
        combined_html = "<html><head><meta charset='utf-8'></head><body>"
        for page in self.html_pages:
            combined_html += f"<div style='page-break-after: always;'>{page}</div>"
        combined_html += "</body></html>"

        with open("temp_combined.html", "w", encoding="utf-8") as f:
            f.write(combined_html)

        pdfkit.from_file("temp_combined.html", output_path)
        print(f"\n✅ PDF saved to: {output_path}")
