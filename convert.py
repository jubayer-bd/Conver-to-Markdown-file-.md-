from markitdown import MarkItDown

md = MarkItDown()

# # Convert a PDF
pdf_result = md.convert("example.pdf")
print(pdf_result.markdown)

# Convert a DOCX
docx_result = md.convert("d:\Download\Germany_Study_Plan_12_Months.docx")
print(docx_result.markdown)

# Convert a PPTX
pptx_result = md.convert("example.pptx")
print(pptx_result.markdown)



# run on git bash python convert.py