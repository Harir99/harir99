from pathlib import Path
import sys

pdf_path = Path(r"C:\Users\haree\OneDrive\Documents\Projects\harir99\Harir_Resume.pdf")
out_path = Path(r"C:\Users\haree\OneDrive\Documents\Projects\harir99\RESUME.txt")

if not pdf_path.exists():
    print(f"PDF not found at {pdf_path}")
    sys.exit(2)

# Try pypdf (modern), fall back to PyPDF2 if available
try:
    from pypdf import PdfReader as Reader
except Exception:
    try:
        from PyPDF2 import PdfReader as Reader
    except Exception:
        print("Neither 'pypdf' nor 'PyPDF2' is installed. Please install pypdf (python -m pip install pypdf)")
        sys.exit(3)

reader = Reader(str(pdf_path))
texts = []
for i, page in enumerate(reader.pages):
    try:
        t = page.extract_text()
    except Exception as e:
        t = None
    if t:
        texts.append(t)
    else:
        texts.append(f"[Page {i+1} contains no extractable text or extraction failed]")

out_path.write_text("\n\n".join(texts), encoding="utf-8")
print(f"Extracted text written to: {out_path}")
