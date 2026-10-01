import sys
import os
import fitz  # PyMuPDF

def convert(pdf_path, out_dir, zoom=2.0):
    os.makedirs(out_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    base = os.path.splitext(os.path.basename(pdf_path))[0]
    mat = fitz.Matrix(zoom, zoom)
    written = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=mat)
        out = os.path.join(out_dir, f"{base}_p{i+1:02d}.png")
        pix.save(out)
        written.append(out)
    doc.close()
    return written

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    out_dir = sys.argv[2]
    files = convert(pdf_path, out_dir)
    print(f"Converted {len(files)} pages:")
    for f in files:
        print(f)
