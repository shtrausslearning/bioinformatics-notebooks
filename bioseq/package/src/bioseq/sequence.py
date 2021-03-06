import plotly.express as px
import plotly.graph_objects as go
from collections import Counter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Mapping Dictionary
def dic_map(map_id='codon',tid=None):
	
	# Codon / Amino Acid Conversion
	if(map_id is 'codon'):
		tc = {
			"GCT":"A", "GCC":"A", "GCA":"A","GCG":"A",
			"TGT":"C", "TGC":"C","GAT":"D","GAC":"D",   
			"GAA":"E", "GAG":"E","TTT":"F","TTC":"F",   
			"GGT":"G", "GGC":"G","GGA":"G","GGG":"G",
			"CAT":"H", "CAC":"H","ATA":"I","ATT":"I", "ATC":"I",  
			"AAA":"K", "AAG":"K","TTA":"L","TTG":"L", "CTT":"L",  
			"CTC":"L", "CTA":"L","CTG":"L","ATG":"M",
			"AAT":"N", "AAC":"N","CCT":"P","CCC":"P", "CCA":"P", "CCG":"P",
			"CAA":"Q", "CAG":"Q","CGT":"R","CGC":"R", "CGA":"R",
			"CGG":"R", "AGA":"R","AGG":"R","TCT":"S", "TCC":"S", "TCA":"S",
			"TCG":"S", "AGT":"S","AGC":"S","ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
			"GTT":"V", "GTC":"V","GTA":"V","GTG":"V","TGG":"W",
			"TAT":"Y", "TAC":"Y","TAA":"_","TAG":"_","TGA":"_"
			}
	
	# IUPAC Amino Acids
	elif(map_id is 'iupac_amino'):
		tc   = {'A':'Alanine','C':'Cysteine','D':'Aspartic Acid','E':'Glutamic Acid',
				'F':'Phenylalanine','G':'Glycine','H':'Histidine','I':'Isoleucine',
				'L':'Lysine','M':'Methionine','N':'Asparagine','P':'Proline',
				'Q':'Glutamine','R':'Arginine','S':'Serine','T':'Threonine',
				'V':'Valine','W':'Tryptophan','Y':'Tryosine','_':'Gap'}
	   
	# IUPAC nuceotides
	elif(map_id is 'iupac_nucleotide'):
		tc  = {'A':'Adenine','C':'Cytosine','G':'Guanine','T':'Thymine',
			   'U':'Uracil'}
	
	if tid in tc: 
	  return tc[tid]
	else: 
	  return None

# Class for Sequence Operations 
class SQ: 
	
	# Constructor
	def __init__ (self, seq=None, seq_type = "dna"): 
		self.seq = seq.upper()
		self.seq_type = seq_type

	@staticmethod
	def dict_sum(dictlist):
		outdic = {}
		for d in dictlist:
			for k in d.keys():
				outdic[k] = 0
		for d in dictlist:
			for k in d.keys():
				outdic[k]+=d[k]
		return outdic
		  
	# class instance operations
	def __len__(self):
		return len(self.seq)
	def __getitem__(self, n):
		return self.seq[n]
	def __getslice__(self, i, j):
		return self.seq[i:j]
	def __str__(self):
		return self.seq
	def __add__(self,other):
		if(self.seq_type == other.seq_type):
			return SQ(self.seq + other.seq,seq_type=self.seq_type)
		else:
			print('sequences must of be same type')
	
	# Frequency of Sybols 
	def freq(self,compare=None,show_id='perc',fheight=None,fwidth=None):
		
		if(compare is not None):
			if(self.seq_type != compare.seq_type):
				print('sequences are not of same type')
				return None
			
		c1 = dict(Counter(self.seq))  # abc counter for s1
		if(compare is not None):
			c2 = dict(Counter(compare))  # abc counter for s2
			
		abc = list(self.abc())
		count = Counter(abc)
		abc_c = dict(Counter({x:0 for x in count}))
		
		c_all1 = self.dict_sum([c1,abc_c])
		if(compare is not None):
			c_all2 = self.dict_sum([c2,abc_c])    

		lst = []
		for i in c_all1.keys():
		   if(self.seq_type == 'dna' or self.seq_type == 'rna'):
			   lst.append(dic_map('iupac_nucleotide',i))
		   elif(self.seq_type == 'aa'):
			   lst.append(dic_map('iupac_amino',i))
				
		if(compare is not None):
			lst2 = []
			for i in c_all2.keys():
			   if(self.seq_type == 'dna' or self.seq_type == 'rna'):
				   lst2.append(dic_map('iupac_nucleotide',i))
			   elif(self.seq_type == 'aa'):
				   lst2.append(dic_map('iupac_amino',i))
		  
		perc = [round(x / len(self.seq),3) for x in [*c_all1.values()]]
		if(show_id is 'perc'):
			show1 = lst; show2 = perc
		elif(show_id is 'count'):
			show1 = lst; show2 = [*c_all1.values()]
		fig = go.Figure(go.Bar(y=show1,x=show2,
							   marker_color='rgb(26, 118, 255)',
							   orientation='h',text=show2,
							   textposition='outside',name='SEQ1'))
		if(compare is not None):
			perc = [round(x / len(compare),3) for x in [*c_all2.values()]]
			if(show_id is 'perc'):
				show1 = lst2; show2 = perc
			elif(show_id is 'count'):
				show1 = lst2; show2 = [*c_all2.values()]
			fig.add_trace(go.Bar(y=show1,x=show2,marker_color='rgb(55, 83, 109)',
								 orientation='h',text=show2,
								 textposition='outside',name='SEQ2'))
		fig.update_layout(template='plotly_white',height=fheight,width=fwidth,
						 title=f'<b>{self.seq_type.upper()} SEQUENCE CONTENT</b>',
						 font=dict(family='sans-serif',size=12),
						 margin=dict(l=40, r=40, t=50, b=10))
		fig.show()

	# count purines & pyrimidines
	def count_purines(self,compare=None):

		purines1 = self.seq.count("A") + self.seq.count("G")
		pyrimidines1 = self.seq.count("C") + self.seq.count("T")
		print(f"purines: {purines1}/{len(self.seq)}")
		print(f"pyrimidines: {pyrimidines1}/{len(self.seq)}") 

		if(compare is not None):
			purines2 = compare.seq.count("A") + compare.seq.count("G")
			pyrimidines2 = compare.seq.count("C") + compare.seq.count("T")
			print(f"purines: {purines2}/{len(compare.seq)}")
			print(f"pyrimidines: {pyrimidines2}/{len(compare.seq)}")
			return (purines1,pyrimidines1),(purines2,pyrimidines2)
		else:
			return (purines1,pyrimidines1)

	# Count frequency of grouped nucleotides
	def groupfreq(self,count_id='di',compare=None):

		if(count_id is 'di'):
			lst_count_id = ['AA','AC','AG','AT',
							'CA','CC','CG','CT',
							'GA','GC','GG','GT',
							'TA','TC','TG','TT']
		elif(count_id is 'tri'):
			lst_count_id = ['AAA','AAC','AAG','AAT','ACA','ACC','ACG','ACT',
							'AGA','AGC','AGG','AGT','ATA','ATC','ATG','ATT'
							'CAA','CAC','CAG','CAT','CCA','CCC','CCG','CCT',
							'CGA','CGC','CGG','CGT','CTA','CTC','CTG','CTT',
							'GAA','GAC','GAG','GAT','GCA','GCC','GCG','GCT',
							'GGA','GGC','GGG','GGT','GTA','GTC','GTG','GTT',
							'TAA','TAC','TAG','TAT','TCA','TCC','TCG','TCT',
							'TGA','TGC','TGG','TGT','TTA','TTC','TTG','TTT']

		if(self.seq_type is 'dna'):

			lst_count = []
			for i in lst_count_id:
				lst_count.append(self.seq.count(i))

			df = pd.DataFrame(data=lst_count,index=lst_count_id).T
			df.index = ['main']

			if(compare is not None):

				ii=-1
				for seq in compare: # cycle through all SQ
			
					ii+=1;lst_count = []
					for jj in lst_count_id:
						lst_count.append(compare[ii].seq.count(jj))

					ldf = pd.DataFrame(data=lst_count,index=lst_count_id).T
					ldf.index = [f'sequence{ii}']
					df = pd.concat([df,ldf],axis=0)

			plt.figure(figsize=(15,8))
			ax = sns.heatmap(df)

		else:
			print('input must be dna type')


	# Return % GC Nucleotides (+Comparison list of sq)
	def gc(self,lst=None):
		
		if (self.seq_type == "dna" or self.seq_type == "rna"):
			ii = 0
			for s in self.seq:
				if(s in "GCgc"):
					ii += 1
			if(lst is None):
				val = round(ii / len(self.seq),4)
				return val
		
		if(lst is not None):
			lst_cg = []
			lst_cg.append(round(ii / len(self.seq),4))
		
		if(lst is not None):
			for i in lst:
				if (i.seq_type == "dna" or i.seq_type == "rna"):
					ii = 0
					for s in i.seq:
						if(s in "GCgc"):
							ii += 1
					lst_cg.append(round(ii / len(i.seq),4))
				else:
					lst_cg.append(-1)
					
			return lst_cg
					
	def info(self):
		if(self.seq_type is 'dna' or self.seq_type is 'rna'):
			print (f"SEQ: {self.colored(self.seq)}" +" "+ f"TYPE: {self.seq_type}")
		else:
			print (f"SEQ: {self.seq}" +" "+ f"TYPE: {self.seq_type}")
		
	# Get ABC
	def abc(self):
		if(self.seq_type=="dna"): 
		  return "ACGT"
		elif(self.seq_type=="rna"):
		  return "ACGU"
		elif (self.seq_type=="aa"): 
		  return "ACDEFGHIKLMNPQRSTVWY"
		else: 
		  return None
		
	# Check Validity
	def validate(self,verbose=False):
		alp = self.abc()
		res = True; i = 0
		while (res and i < len(self.seq)):
			if self.seq[i] not in alp: 
				res = False
			else: i += 1
		if(res):
			if(verbose):
				print(f'{self.seq_type} is valid')
			return res
		else:
			if(verbose):
				print(f'{self.seq_type} is invalid')
			return res
		
	# Transcription 
	def transcription(self):
		if (self.seq_type == "dna"):
			return SQ(self.seq.replace("T","U"), "rna")
		else:
			return None
	
	# Reverse Complement
	def reverse_comp(self):
		
		if (self.seq_type != "dna"): 
			print('input not DNA')
			return None
	
		lst_seq = ['A','T','G','C']
		lst_comp = ['T','A','C','G']
			
		comp = ''
		for char in self.seq:
			ii=-1
			for c in lst_seq:
				ii+=1
				if(char == c ):
					comp = lst_comp[ii] + comp
			
		return SQ(comp, "dna")
		
	# Translate 
	@staticmethod
	def translate(seq,p0=0):
		seq_aa = ""
		for pos in range(p0,len(seq)-2,3):
			cod = seq[pos:pos+3]
			seq_aa += dic_map(map_id='codon',tid=cod)
		return seq_aa
	
	'''Get All Possible open reading frames (ORF)'''
	# store all possible collections of amino acid groups in all 6 frames
	def frames(self):
		res = []
		for i in range(0,3):
			res.append(self.translate(self.seq,i))
		rc = self.reverse_comp()
		for i in range(0,3):
			res.append(self.translate(rc,i)) 
		return res
	
	'''Computes all possible proteins in an amino acid sequence in reading frame '''
	# using the knowledge that it starts with M and ends with _, 
	# filter out rule breaking ORFs
	@staticmethod
	def all_proteins_RF(aa_seq):
		# aa_seq -> converted ORF
		current_prot = []
		proteins = []
		for aa in aa_seq:
			if(aa == "_"):
				if current_prot:
					for p in current_prot:
						proteins.append(p)
					current_prot = []
			else:
				if(aa == "M"):
					current_prot.append("")
				for i in range(len(current_prot)):
					current_prot[i] += aa
		return proteins
	
	'''Computes all possible proteins for all ORF'''
	# and sort them based on size
	def ORF_protein(self, mins = 0):
		
		# order 
		def insert_prot_ord (prot, list_prots):
			i = 0
			while i < len(list_prots) and len(prot) < len(list_prots[i]):        
				i += 1
			list_prots.insert(i, prot)
		
		rfs = self.frames()  # get all ORF conversions
		res = []
		for rf in rfs:
			prots = self.all_proteins_RF(rf) # return only protein cases
			# additionally sort based on protein size
			for p in prots: 
				if(len(p) > mins): 
					insert_prot_ord(p, res)
		return res
	
	@staticmethod
	def colored(lseq):

		bcolors = {
			'A': '\033[92m',
			'C': '\033[94m',
			'G': '\033[93m',
			'T': '\033[91m',
			'U': '\033[91m',
			'reset': '\033[0;0m'
		}
		
		tmpStr = ""
		for nuc in lseq:
			if nuc in bcolors:
				tmpStr += bcolors[nuc] + nuc
			else:
				tmpStr += bcolors['reset'] + nuc
			
		return tmpStr + '\033[0;0m'

class SQRec(SQ):
    
    def __init__(self,seq=None,
                 id=None,name=None,description=None):
        self.seq = seq # SQ class
        self.id = id  # sequence identifier (eg locus tag)
        self.name = name   # name of sequence
        self.description = description 