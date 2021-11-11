## "sequence.py" methods

<code>freq</code>
- description: count frequency of each base in the biological sequence <br>
- arguments: **compare**: <code>SQ</code> object

<code>count_purines</code>
- description: count purines  <code>A&G</code> sum & pyrimidines <code>C&T</code>
- arguments: **compare**: <code>SQ</code> object

<code>groupfreq</code>
- description: count di/tri nucleotide base frequencies
- arguments: **compare**: list of <code>SQ</code> objects

<code>gc</code>
- description: GC base concentration 
- arguments: **compare**: list of <code>SQ</code> objects

<code>info</code> 
- description: view sequence & sequence type information

<code>abc</code>
- description: view base character used in input sequence type

<code>validate</code>
- description: check if the sequence is valid

<code>transcription</code>
- description: change sequence type from DNA to RNA

<code>reverse_comp</code>
- description: get the reverse complement of the current DNA strand

<code>get_protein</code>
- description: get the list of putative proteins that start /w M & end with gap, sorted by size
- arguments: **min_size**: minimum size of putative protein 

<code>find_pattern</code>
- description: find specified pattern within the sequence (if it exists)
- arguments: **pattern**: string form of pattern, **search_id**: type of search (first,all,overlap)
