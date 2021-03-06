
### 1 | Background

#### 1.1 | CELLS

Cells contain molecules which will reference to througout the notebook: **<mark style="background-color:#F1C40F;color:white;border-radius:5px;opacity:0.9">amino acids</mark>**, **<mark style="background-color:#F1C40F;color:white;border-radius:5px;opacity:0.9">nucleotides</mark>**, **<mark style="background-color:#F1C40F;color:white;border-radius:5px;opacity:0.9">proteins</mark>**

A **<mark style="background-color:#F1C40F;color:white;border-radius:5px;opacity:0.9">cell</mark>** is mostly composed of water:
> - A bacteria cell has a weight composition of roughly 70% water & 30% <b>chemical origin</b>, 
> - <b>7% -> small molecules</b> Inc. **<mark style="background-color:#F1C40F;color:white;border-radius:5px;opacity:0.9">amino acids</mark>** and **<mark style="background-color:#F1C40F;color:white;border-radius:5px;opacity:0.9">nucleotides</mark>**
> - 23% -> <b>macro molecules</b> (**<mark style="background-color:#F1C40F;color:white;border-radius:5px;opacity:0.9">proteins</mark>**,lipids,polysaccharides)

According to their internal structure, they can be divided into to major categories:

> - **<mark style="background-color:#F1C40F;color:white;border-radius:5px;opacity:0.9">Prokaryotic</mark>** cells : have no nucleus or internal membranes
> - **<mark style="background-color:#F1C40F;color:white;border-radius:5px;opacity:0.9">Eukaryotic</mark>** cells : which have a defined <b>nucleus</b>, <b>internal membranes</b> and functional elements called <b>organelles</b>.

- At a structural level, all cells are surrounded by a structure called cell <b>membrane</b> or <b>plasma membrane</b>. 
- This <b>membrane</b> is permeable to molecules that cells need to absorb from or excrete to the outside medium.
- Within the cell we find the <b>cytoplasm</b> (largely composed of water), which serves as the medium for the cell

#### 1.2 | DNA STRANDS

#### Complementary Strands

- DNA is a molecule composed of **two complementary strands** that form and stick together due to the connections established between the nucleotides in both strands
- This is made possible by due to the chemical phenomenon:
    - Where <code>Adenine (A)</code> bonds only with <code>Thymine (T)</code> nucleotides; as a result of **two hydrogen connections**
    - Similarly, <code>Guanine (G)</code> bonds only with <code>Cytosine (C)</code> nucleotides by **three hydrogen connections**

#### Reverse Complement

- This results in **two complementary** and **anti-parallel strands** (connected in opposite directions), if we know the nucleotide sequence in one of the strands, we can get the sequence in the opposite strand by taking the complement of its nucleotides, which are also read backwards, thus we have the **reverse complement** of the other strand
- It has become a **standard to describe the DNA though only one** of the strands, due to this **complementarity** using <b>[A,T,G,C]</b>
- The existence of these two strands is essential in order to **pass on genetic information** to new cells and **produce proteins**

#### 1.3 | SEQUENCE ALPHABETS

**<mark style="background-color:#323232;color:white;border-radius:5px;opacity:0.9">ABC (I/II)</mark>** **<mark style="background-color:#F1C40F;color:white;border-radius:5px;opacity:0.9">Nucleic Acids</mark>**

> - Among <b>molecules with a biological role</b>, we can find **<span style='color:#F1C40F'>nucleic acids</span>**
> - Nucleic acids encode and express the genetic code that is kept within the cell
- There are two major types of **<span style='color:#F1C40F'>nucleic acids</span>**: 
> - **<span style='color:#F1C40F'>Deoxyribo Nucleic Acid (DNA)</span>**
> - **<span style='color:#F1C40F'>Ribonucleic Acid (RNA)</span>** (Obtainable via transcription)
- DNA contains the information necessary to build a cell, and keep it functioning. 
- In <b>eukaryotic</b> cells, DNA will be found in the nucleus, whilst in the <b>prokaryotic</b> cells, it will be found in the cytoplasm. 
- <b>IUPAC</b> defines the full list of nucleotides as shown in the table below, with <b>A,T,G,C</b> being the main four:
- Another type of nucleotide list often used is **[IUB Ambiguity Codes](http://biocorp.ca/IUB.php)**, which we use later in the notebook as well

**<mark style="background-color:#323232;color:white;border-radius:5px;opacity:0.9">ABC (II/II)</mark>** **<mark style="background-color:#F1C40F;color:white;border-radius:5px;opacity:0.9">Amino Acids</mark>**

**<span style='color:#F1C40F'>Amino acids</span>**:
> The **building blocks of proteins**, which are macromolecules that perform most of the functions inside a cell

Proteins have a **broad range of functions**, spanning from **catalytic** to **structural functions**:

- <code>Enzymes</code> : Type of abundant proteins that promote chemical reactions & convert some molecules into other types of molecules required for the functioning of the cell
- <code>Carbohydrates</code> : Serve as energy storage, both for immediate and long term energy demands
- <code>Lipids</code> : Part of the plasma membrane, doing signaling and energy storage

The cell also contains other components of varying complexity. Of importance: 
- <b>Mitochondria</b> & the <b>Chloroplasts</b> : Organelles involved in the production of energy. 
- <b>Ribosomes</b> : Large and complex molecules composed of a mixture of genetic material, req. to assemble proteins and play a central role in the flow of genetic information

#### 1.4 | BIOLOGICAL SEQUENCES

- A **biological sequence** represents a single, continuous molecules of **nucleic acid (nucleotide)** or **amino acids**
- Subsequently we can also **compare multiple sequences** based on some form of alignment methodology, so that's what this notebook is about
    
**<code>Sequence Alignment Introduction</code>** | **[Data Mining Trends and Research Frontiers](https://www.sciencedirect.com/topics/computer-science/biological-sequence)**

- Sequence alignment is based on the fact that all living organisms are related by evolution 
- This implies that the nucleotide (DNA, RNA) and protein sequences of species that are closer to each other in evolution should exhibit more similarities    
- An alignment is the process of lining up sequences to achieve a maximal identity level, which also expresses the degree of similarity between sequences
- Two sequences are homologous if they share a common ancestor. The **degree of similarity** obtained by sequence alignment can be useful in determining the possibility of homology between two sequences
- Such an alignment also helps determine the relative positions of multiple species in an evolution tree, which is called a <code>phylogenetic</code> tree

#### 1.5 | BIOLOGICAL SEQUENCE EXAMPLES

- In notebook **[Biological Sequence Operations](https://www.kaggle.com/shtrausslearning/biological-sequence-operations)**, we looked at how to read biological sequence files, here are two examples of what they might look like:
    - An example of a <code>Nucleotide</code> Sequence <code>NC_005816.1</code>

```
ref|NC_005816.1|:4343-4780 pesticin immunity protein [Yersinia pestis biovar Microtus str. 91001]
> ATGGGAGGGGGAATGATCTCAAAGTTATTTTGCTTGGCTCTCATATTTTTATCATCAAGTGGCCTTGCAG
AAAAAAACACATATACAGCAAAAGACATCTTGCAAAACCTAGAATTAAATACCTTTGGCAATTCATTGTC
TCATGGCATCTATGGGAAACAGACAACCTTCAAGCAAACCGAGTTTACAAATATTAAAAGCAACACCAAA
AAACACATTGCACTTATCAATAAAGACAACTCATGGATGATATCATTAAAAATACTAGGAATTAAGAGAG
ATGAGTATACTGTCTGTTTTGAAGATTTCTCTCTAATAAGACCGCCAACATATGTAGCCATACATCCTCT
ACTTATAAAAAAAGTAAAATCTGGAAACTTTATAGTAGTGAAAGAAATAAAGAAATCTATCCCTGGTTGC
ACTGTATATTATCATTAA
```

- An example of an **<mark style="background-color:#F1C40F;color:white;border-radius:5px;opacity:0.9">Amino Acid</mark>** Sequence:

```
gi|7525080|ref|NP_051037.1| ribosomal protein S12 [Arabidopsis thaliana]
> MPTIKQLIRNTRQPIRNVTKSPALRGCPQRRGTCTRVYTITPKKPNSALRKVARVRLTSGFEITAYIPGI
GHNLQEHSVVLVRGGRVKDLPGVRYHIVRGTLDAVGVKDRQQGRSKYGVKKPK
```

#### 1.6 | HOMOLOGY & SIMILARITY

- Some key terms in **biological sequence alignment** : <code>Homology</code> & <code>similarity</code>
- First things first, we have two sequences, <code>DNA</code> sequences to be exact (here they are from file <code>NC_005816.1</code>):

#### Select two sequences

<code>Sequence #1</code>

```
ref|NC_005816.1|:c8360-8088 hypothetical protein YP_pPCP10 [Yersinia pestis biovar Microtus str. 91001]

> TTGGCTGATTTGAAAAAGCTACAGGTTTACGGACCTGAGTTACCCAGGCCATATGCCGATACCGTGAAAG
GTTCTCGGTACAAAAATATGAAAGAGCTTCGCGTTCAGTTTTCTGGCCGTCCGATAAGAGCCTTTTATGC
GTTCGATCCGATTCGTCGGGCTATCGTTCTTTGTGCAGGAGATAAAAGTAATGATAAGCGGTTTTATGAA
AAACTGGTGCGTATAGCTGAGGATGAATTTACAGCACATCTGAACACACTGGAGAGCAAGTAA
```

<code>Sequence #2</code>

```
ref|NC_005816.1|:c8088-7789 putative transcriptional regulator [Yersinia pestis biovar Microtus str. 91001]

> ATGAGAACATTAGATGAGGTGATTGCCAGTCGTTCACCTGAAAGCCAGACACGAATTAAAGAAATGGCAG
ATGAGATGATTCTTGAGGTCGGCTTGCAGATGATGCGTGAAGAACTCCAGTTATCACAAAAACAAGTTGC
TGAGGCGATGGGTATAAGCCAGCCAGCAGTAACAAAGCTGGAGCAGCGCGGAAATGATTTAAAGCTGGCG
ACGTTAAAGCGTTACGTTGAAGCAATGGGAGGCAAATTAAGCTTGGATGTTGAGCTTCCTACAGGAAGGA
GAGTAGCGTTCCATGTCTAA
```

#### <b><span style='color:#F1C40F'>How to tell if two sequences are homologous?</span></b>

**<code>HOMOLOGOUS</code>** | **[Wikipedia](https://en.wikipedia.org/wiki/Homology_(biology))**
- Similar biological structures or sequences in different taxa are <code>homologous</code> if they are derived from a common ancestor
- Thus, two sequences are said to be <code>homologous</code>, if they are both derived from a **common ancestral sequence**

#### How similar are these sequences?

If we wanted to know how **closely they are related**, we could **make some assumptions** about their relation to one another:
- We are assuming that there exists an ancestry relation between the two sequences, which is based on this <code>sequence similarity</code>
- We can **generate a hypothesis** about the biological function of a sequence we are exploring, based on its <code>similarity</code> to another sequence, which already has a determined function
- Sequences that display a significant **degree of similarity** have a high probability of being <code>homologous</code>, **sharing similar functions**
- Two sequences that have a high order of similarity -> have a high probability of being <code>homologous</code>
- There doesn't seem to exist a point, at which this becomes a certainty & thus requires experimental verification
- The **higher the degree of similarity**, the more confident we can be that **two sequences are homologous** & thus share similar functions

#### Biological mutations

So what stops us from just placing two sequences next to eachother & comparing them; there exist some factors that do add an extra level of complication to our similarity assumption:

- Biological **<mark style="background-color:#F1C40F;color:white;border-radius:5px;opacity:0.9">mutations</mark>** signifcantly complicate the process of what may seem quite a straightforward task
- **<mark style="background-color:#F1C40F;color:white;border-radius:5px;opacity:0.9">Insertions</mark>** & **<mark style="background-color:#F1C40F;color:white;border-radius:5px;opacity:0.9">deletions</mark>**, as well as **<span style='color:#F1C40F'>changes in multiple nucleotides</span>** due to these mutations can make the comparison of sequences more complex

<code>MUTATIONS</code> | **[GENOME.GOV](https://www.genome.gov/genetics-glossary/Mutation)**

- A <code>mutation</code> is a change in a DNA sequence
- <code>Mutations</code> can result from DNA copying mistakes made during cell division, exposure to ionizing radiation, exposure to chemicals called mutagens, or infection by viruses
- Germ line mutations occur in the eggs and sperm and can be passed on to offspring, while somatic mutations occur in body cells and are not passed on

<code>INSERTIONS</code> & <code>DELETIONS</code> | **[NATURE](https://www.nature.com/scitable/topicpage/dna-is-constantly-changing-through-the-process-6524898/)**
      
- <code>Insertions</code> and <code>deletions</code> are two other types of mutations that can affect cells at the gene level
An insertion mutation occurs when an extra nucleotide is added to the DNA strand during replication
This can happen when the replicating strand "slips," or wrinkles, which allows the extra nucleotide to be incorporated
- <b>Strand slippage</b> can also lead to deletion mutations.
- A deletion mutation occurs when a wrinkle forms on the DNA template strand and subsequently causes a nucleotide <br>
to be omitted from the replicated strand. <br>

### 1 | Substitution Matrix

```python

'''

####################################################################

# Substitution Matrix Class
# Class for storing the substitution matrix, reading & making

# Attributes:
- abc
- subm 

# Methods:
- __getitem__ - obtain the score from the substitution matrix
- score_pair - obtain the score from the substitution matrix
- head - show the first few entries in the substitution matrix 
- read - read a substitution matrix file
- make - create a simple hit/miss substitution matrix

####################################################################

'''

class SUBM:
    
    # Constructor & class operation
    def __init__(self):
        self.abc = ""        # characters
        self.subm = {}       # Substitution matrix mapping
        
    # get score pair class operation
    def __getitem__(self, ij):
        i,j = ij
        return self.score_pair(i, j)
    
    # get specific score of a pair
    def score_pair(self,c1,c2):
        if(c1 not in self.abc or c2 not in self.abc):
            return None
        return self.subm[c1+c2]
    
    # show first n number of pairs 
    def head(self,n=5):
        return list(islice(self.subm.items(),n))
    
    # Read Substitution Matrix from file (.mat)
    # Format includes separation by tabs
    
    def read(self,name):
        
        # Read the code
        file = open(name, "r")
        abc = file.readline().split('\t')
        
        self.abc = ""
        for i in range(0, len(abc)): 
            self.abc += abc[i][0]
        for i in range(0,len(abc)):
            line = file.readline();
            abc = line.split('\t');
            for j in range(0, len(abc)):
                k = self.abc[i]+self.abc[j]
                self.subm[k] = int(abc[j])
        file.close()
        
    # Create Substitution Matrix
    # requires match & mismatch score & alphabet
    # A constant match, mismatch score is used
    
    def make(self,code,match,missmatch):
        self.abc = code
        for values in itertools.product(code,code):
            c1 = values[0]; c2 = values[1]
            if (c1 == c2):
                self.subm[c1+c2] = match
            else:
                self.subm[c1+c2] = missmatch

```
