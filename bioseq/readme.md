
### bioseq package 
![](https://camo.githubusercontent.com/d38e6cc39779250a2835bf8ed3a72d10dbe3b05fa6527baa3f6f1e8e8bd056bf/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f64652d507974686f6e2d696e666f726d6174696f6e616c3f7374796c653d666c6174266c6f676f3d707974686f6e266c6f676f436f6c6f723d776869746526636f6c6f723d326262633861) ![](https://badgen.net/badge/status/WIP/orange) 

- Compilation of various bioinformatics related operation classes in <code>wheeler</code> format
- Stored in <code>pypi</code> format to make it easier to call commonly used functions in notebooks w/o pasting entire code
- Wheeler package located @[bioinformatics](https://www.kaggle.com/shtrausslearning/bioinformatics) dataset /whl_packages/ on Kaggle
- Package Name (or similar): <code>bioseq-0.0.1-py3-none-any.whl</code>

#### "bioseq" package content:
- <code>sequence</code> - single sequence <code>SQ()</code> storage class & methods
- <code>read_sequence</code> - read FASTA format (single/multiple sequence) & store in <code>SQ()</code> format
- <code>sequence_alignment</code> - pairwise & multiple sequence alignment & <code>bokeh</code> sequence visualisation, alignment storage, substitution matrix storage
- <code>biopython_blast</code> - Biopython incorporates a good NCBI query module, so a class for result interpretation & visualisation /w Bokeh only

#### <code>sequence</code> methods:

- <code>freq</code> <br>
- description: count frequency of each base in the biological sequence <br>
- arguments: **compare**: <code>SQ</code> object

- <code>count_purines</code> <br>
- description: count purines  <code>A</code> & <code>G</code> sums & pyrimidines <code>C</code> & <code>T</code>
