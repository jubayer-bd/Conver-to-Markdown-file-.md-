# Convert File to Markdown with MarkItDown

This project contains a small Python script, `convert.py`, that uses [MarkItDown](https://github.com/microsoft/markitdown) to convert common document formats into Markdown.

## What `convert.py` Does

The script creates a `MarkItDown` object and then calls `convert()` on a few example files:

- `example.pdf`
- `example.docx`
- `example.pptx`

For each file, the returned result includes a `markdown` value, which is printed to the console.

In simple terms, the script:

1. Imports `MarkItDown`.
2. Creates a converter instance.
3. Passes a file path to `md.convert()`.
4. Prints the generated Markdown text.

## How It Works

MarkItDown reads the source document and extracts readable content into Markdown format. That means headings, paragraphs, lists, and other structured text can be represented in a way that is easier to reuse in plain text workflows.

The current `convert.py` file is a basic example, so the file names are hardcoded. In a real project, you would usually replace those example paths with files from your own system or add input handling so the script can convert different files dynamically.

## Why It Is Beneficial

Converting documents to Markdown is useful because Markdown is:

- lightweight and easy to read
- simple to store in version control
- compatible with many editors, note-taking tools, and documentation systems
- easy to reuse in scripts, websites, and knowledge bases

Using MarkItDown can save time when you need structured text from documents without manually copying and formatting the content.

## Where You Can Use It

This kind of conversion is helpful in several scenarios:

- documentation pipelines, where source files are turned into Markdown notes or docs
- knowledge management, where PDFs, Word files, or presentations are archived in a searchable text format
- content migration, when moving old documents into a Markdown-based system
- preprocessing for AI or search workflows, where clean text is easier to analyze
- note extraction, when you want to pull important text out of reports or slides

## Example Workflow

If you want to use the script with your own files, update the paths in `convert.py`:

```python
from markitdown import MarkItDown

md = MarkItDown()

result = md.convert("my-document.pdf")
print(result.markdown)
```

You can repeat that pattern for any supported file type.

## Installation

Install MarkItDown with only the extras you need for PDF, DOCX, and PPTX support:

```bash
pip install "markitdown[pdf, docx, pptx]"
```

If you only need some formats, you can remove the extras you do not use.

## Requirements

Before running the script, make sure:

- Python is installed
- the `markitdown` package is installed
- the input files exist at the paths you provide

## Running the Script

The comment at the bottom of `convert.py` suggests running it with Git Bash:

```bash
python convert.py
```

If the example files are not present, the script will fail when it tries to convert them. Replace the sample file names with real files before running it.

## Notes

- `convert.py` is currently a demonstration script, not a full app.
- It prints converted Markdown to the terminal instead of saving it to a file.
- You can extend it later to accept user input, batch process folders, or write output to `.md` files.
