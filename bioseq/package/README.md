# bioseq

- Compilation of various bioinformatics related operation classes in <code>wheeler</code> format
- Stored in <code>pypi</code> format to make it easier to call commonly used functions in notebooks w/o pasting entire code
- Wheeler package located @[bioinformatics](https://www.kaggle.com/shtrausslearning/bioinformatics) dataset /whl_packages/ on Kaggle
- Package Name (or similar): <code>bioseq-0.0.1-py3-none-any.whl</code>

#### "bioseq" package content:
- <code>sequence</code> - single sequence <code>SQ()</code> storage class & methods
- <code>read_sequence</code> - read FASTA format (single/multiple sequence) & store in <code>SQ()</code> format
- <code>sequence_alignment</code> - pairwise & multiple sequence alignment & <code>bokeh</code> sequence visualisation, alignment storage, substitution matrix storage
- <code>biopython_blast</code> - Biopython incorporates a good NCBI query module, so a class for result interpretation & visualisation /w Bokeh only
