import markdown
import pdfkit

# Set the correct path to wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")  # Adjust based on OS

def convert_markdown_to_pdf(md_file, pdf_file):
    # Read Markdown file
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Inline CSS for styling (White background & black text)
    css_styles = """
    <style>
        body {
            background-color: white;
            color: black;
            font-family: Arial, sans-serif;
            font-size: 14px;
            padding: 20px;
        }
    </style>
    """

    # Wrap HTML with styling
    html = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>Markdown PDF</title>
        {css_styles}
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Convert HTML to PDF
    pdfkit.from_string(html, pdf_file, configuration=config)

# Example usage
convert_markdown_to_pdf("front-end.md", "front-end.pdf")
