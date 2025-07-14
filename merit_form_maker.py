"""Looking for the form fields to fill in"""
from pypdf import PdfReader

# Seeing fields and annotations for the Merit form
reader = PdfReader("data/FORM185-Final-508-9-20-23.pdf")
fields = reader.get_fields()
for f in fields:
    print(f)

from pypdf.constants import AnnotationDictionaryAttributes

fields = []
for page in reader.pages:
    if page.annotations:
        for annot in page.annotations:
            annot = annot.get_object()
            if annot[AnnotationDictionaryAttributes.Subtype] == "/Widget":
                fields.append(annot)
                print("--", annot)
