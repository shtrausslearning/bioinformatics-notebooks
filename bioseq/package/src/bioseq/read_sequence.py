from bioseq.sequence import SQ,SQRec
from re import sub, search

# NCBI identifiers
identifiers_dic = {'lcl':'local(nodb)','bbs':'GenInfo backbone seqid',
                   'bbm':'GenInfo backbone moltype','gim':'GenInfo import ID',
                   'gb':'GenBank','emb':'EMBL','pir':'PIR','sp':'SWISS-PROT',
                   'pat':'patent','pgp':'pre-grant patent','ref':'RefSeq',
                   'gnl':'general database reference','prf':'PRF','pdb':'PDB',
                   'gi':'GenInfo integrated database','dbj':'DDBJ'}

# FASTA formats
FASTA_dic = {'fa':'generic','fasta':'generic','fna':'nucleic acid',
             'ffn':'nucleotide of gene regions','faa':'amino acid',
             'frn':'non-coding RNA'}

# Class to read different files and store info only
class read_seq(SQRec,SQ):
    
    def __init__(self,name):
        self.name = name
        self.format = name.rsplit('.',1)[1]    
        if(self.format in FASTA_dic):      # if one of the fasta formats
            self.read_FASTA(self.name)

    # read FASTA format
    def read_FASTA(self,filename):

        tseq = None; self.lst_seq = []     # list of sequences
        thead = None; self.lst_header = [] # list of sequence identifications
        ff = FASTA_dic[filename.rsplit('.',1)[1]]
        print(ff)
        file = open(filename,'r')

        for line in file:
            if(search(">.*", line)): # get lines w/ >
                    if(tseq != None and thead != None and tseq != ""):
                        self.lst_seq.append(tseq)
                    thead = line; self.lst_header.append(line)              
                    tseq = ""
            else:
                if(tseq == None):
                    return None
                else: 
                    tseq += sub("\s","",line)

        if(tseq != None and thead != None and tseq != ""):
            self.lst_seq.append(tseq)
            
        print(f'READ -> FASTA [{ff}] | #SEQ: {len(self.lst_seq)}')
        file.close()
        
    # get read sequences
    def get_sq(self):
        lst_out = []
        if(len(self.lst_seq) > 1):
            for i in range(0,len(self.lst_seq)):
                lst_types = ['dna','rna','aa']
                for check in lst_types:
                    if(SQ(self.lst_seq[i],check).validate()):
                        lst_out.append(SQRec(seq=SQ(self.lst_seq[i],check),
                                       description=self.lst_header[i]))
            return lst_out
        else:
            lst_types = ['dna','rna','aa']
            for check in lst_types:
                if(SQ(self.lst_seq[0],check).validate()): # if valid sq
                    return SQRec(seq=SQ(self.lst_seq[0],check),
                                 description=self.lst_header[0])