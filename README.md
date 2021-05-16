# pdf\_scraper

**pdf\_ scraper** is a tool to find all pdf files in a folder and all of its
sub-folders, extract the text from each pdf files, remove punctuation and
stop-words from the text, and count the number of word occurrences in the text.
The most common keywords are stored for each pdf file together with the file
path. In the end, similar pdf files can be identified by comparison of the
keywords between files.

```console
$./pdf_scraper <path>
```

## Installing pdf\_scraper

pdf\_scraper is **not yet** available on PyPI, but I will do my best.

```console
$ python -m pip install pdf_scraper
```
