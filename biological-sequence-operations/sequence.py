import plotly.express as px
import plotly.graph_objects as go
from collections import Counter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from re import finditer,search

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
			"CTC":"L", "CTA":"L","CTG":"L",
			"ATG":"M", # starting codon
			"AAT":"N", "AAC":"N","CCT":"P","CCC":"P", "CCA":"P", "CCG":"P",
			"CAA":"Q", "CAG":"Q","CGT":"R","CGC":"R", "CGA":"R",
			"CGG":"R", "AGA":"R","AGG":"R","TCT":"S", "TCC":"S", "TCA":"S",
			"TCG":"S", "AGT":"S","AGC":"S","ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
			"GTT":"V", "GTC":"V","GTA":"V","GTG":"V","TGG":"W",
			"TAT":"Y", "TAC":"Y",
			"TAA":"_","TAG":"_","TGA":"_" # ending codon
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
	
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from re import finditer

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
					
		#####################################################
					
		# General Methods
		# info - show sequence information
		# abc - show sequence base alphabet
		# validate - check if the sequence contains no errors
					
		#####################################################
		@staticmethod
		def colored(lseq):
			
				bcolors = {'A': '\033[92m','C': '\033[94m','G':'\033[93m',
						'T': '\033[91m','U': '\033[91m','reset': '\033[0;0m'}
				tmpStr = ""
				for nuc in lseq:
						if nuc in bcolors:
								tmpStr += bcolors[nuc] + nuc
						else:
								tmpStr += bcolors['reset'] + nuc
				return tmpStr + '\033[0;0m'
	
		def info(self):
				if(self.seq_type is 'dna' or self.seq_type is 'rna'):
						print (f"SEQ: {self.colored(self.seq)}" + \
										" "+ f"TYPE: {self.seq_type}")
				else:
						print (f"SEQ: {self.seq}" +" " + \
										f"TYPE: {self.seq_type}")
					
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
			
		#####################################################
			
		# Counting
		# freq - count bases in sequence
		# count_purines - count purines & pyrimidines
		# groupfreq - count grouped bases
			
		#####################################################
			
		# Frequency of Symbols 
		def freq(self,compare=None,
									show_id='perc', # perc/count
									fheight=None,fwidth=None): # figure size
			
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
																textposition='outside',
																name='SEQ1'))
			
				if(compare is not None):
						perc = [round(x / len(compare),3) for x in [*c_all2.values()]]
						if(show_id is 'perc'):
								show1 = lst2; show2 = perc
						elif(show_id is 'count'):
								show1 = lst2; show2 = [*c_all2.values()]
							
						fig.add_trace(go.Bar(y=show1,x=show2,
																	marker_color='rgb(55, 83, 109)',
																	orientation='h',text=show2,
																	textposition='outside',
																	name='SEQ2'))
					
				fig.update_layout(template='plotly_white',height=fheight,width=fwidth,
													title=f'<b>{self.seq_type.upper()} SEQUENCE CONTENT</b>',
													font=dict(family='sans-serif',size=12),
													margin=dict(l=40, r=40, t=50, b=10));
				fig.show()
			
		# count purines & pyrimidines in sequence 
		def count_purines(self,compare=None):
			
				purines1 = self.seq.count("A") + self.seq.count("G")
				pyrimidines1 = self.seq.count("C") + self.seq.count("T")
				print(f"purines: {purines1}/{len(self.seq)}")
				print(f"pyrimidines: {pyrimidines1}/{len(self.seq)}") 
			
				if(compare is not None):
						purines2 = compare.seq.count("A") + \
														compare.seq.count("G")
						pyrimidines2 = compare.seq.count("C") + \
														compare.seq.count("T")
						print(f"purines: {purines2}/{len(compare.seq)}")
						print(f"pyrimidines: {pyrimidines2}/{len(compare.seq)}")
						return (purines1,pyrimidines1),(purines2,pyrimidines2)
				else:
						return (purines1,pyrimidines1)
			
		# Count frequency of grouped nucleotides
		def groupfreq(self,count_id='di',compare=None,fsize=(10,4)):
			
				if(count_id is 'di'):
						lst_count_id = ['AA','AC','AG','AT',
														'CA','CC','CG','CT',
														'GA','GC','GG','GT',
														'TA','TC','TG','TT']
				elif(count_id is 'tri'):
						lst_count_id = ['AAA','AAC','AAG','AAT','ACA','ACC','ACG',
														'ACT','AGA','AGC','AGG','AGT','ATA','ATC',
														'ATG','ATT''CAA','CAC','CAG','CAT','CCA',
														'CCC','CCG','CCT','CGA','CGC','CGG','CGT',
														'CTA','CTC','CTG','CTT','GAA','GAC','GAG',
														'GAT','GCA','GCC','GCG','GCT','GGA','GGC',
														'GGG','GGT','GTA','GTC','GTG','GTT','TAA',
														'TAC','TAG','TAT','TCA','TCC','TCG','TCT',
														'TGA','TGC','TGG','TGT','TTA','TTC','TTG',
														'TTT']
					
				if(self.seq_type is 'dna'):
					
						lst_c = []
						for i in lst_count_id:
								lst_c.append(self.seq.count(i))
							
						df = pd.DataFrame(data=lst_c,
															index=lst_count_id).T
						df.index = ['main']
					
						if(compare is not None):
							
								ii=-1
								for seq in compare: # cycle through all SQ
							
										ii+=1;lst_c = []
										for jj in lst_count_id:
												lst_c.append(compare[ii].seq.count(jj))
											
										ldf = pd.DataFrame(data=lst_c,
																				index=lst_count_id).T
										ldf.index = [f'sequence{ii}']
										df = pd.concat([df,ldf],axis=0)
							
						plt.figure(figsize=fsize)
						ax = sns.heatmap(df,annot=True,cbar=False)
						plt.yticks(rotation=90) 
					
				else:
						print('input must be dna type')
					
		# Return % GC Nucleotides (+Comparison list of sq)
		def gc(self,compare=None):
			
				if (self.seq_type == "dna" or self.seq_type == "rna"):
						ii = 0
						for s in self.seq:
								if(s in "GCgc"):
										ii += 1
						if(compare is None):
								val = round(ii / len(self.seq),4)
								return val
					
				if(compare is not None):
						lst_cg = []
						lst_cg.append(round(ii / len(self.seq),4))
					
				if(compare is not None):
						for i in compare:
								if (i.seq_type == "dna" or i.seq_type == "rna"):
										ii = 0
										for s in i.seq:
												if(s in "GCgc"):
														ii += 1
										lst_cg.append(round(ii/len(i.seq),4))
								else:
										lst_cg.append(-1)
									
						return lst_cg
			
		#####################################################
			
		# Complementary DNA Strands
			# reverse_comp - reverse complement strand of input DNA
			
		#####################################################
			
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
	
		#####################################################
	
		# Decoding of instructions for making proteins from DNA
		# transcription (DNA -> RNA)
		# get_protein (RNA -> AA chains containing proteins)
	
		#####################################################
	
		# Transcription 
		def transcription(self):
				if (self.seq_type == "dna"):
						return SQ(self.seq.replace("T","U"), "rna")
				else:
						return None
			
		# Translate 
		@staticmethod
		def translate(seq,p0=0):
				seq_aa = ""
				for pos in range(p0,len(seq)-2,3):
						cod = seq[pos:pos+3]
						seq_aa += dic_map(map_id='codon',tid=cod)
				return seq_aa
	
		'''Get All Possible open reading frames (ORF)'''
		# store all possible collections of amino acid 
		# groups in all 6 frames
		def frames(self):
				res = []
				for i in range(0,3):
						res.append(self.translate(self.seq,i))
				rc = self.reverse_comp()
				for i in range(0,3):
						res.append(self.translate(rc,i)) 
				return res
	
		''' Computes all possible proteins in an aa sequence in RF '''
		# using the knowledge that it starts with M and ends with _, 
		# filter out rule breaking ORFs
		# aa_seq -> full converted amino acid sequence
	
		@staticmethod
		def all_proteins_RF(aa_seq):
			
				current_prot = []
				proteins = []
				for aa in aa_seq:
					
						# stopping gap
						if(aa == "_"):
								if(current_prot):
										for p in current_prot:
												proteins.append(p)
										current_prot = []
									
						# not stopping gap
						else:
							
								# starting amino acid
								if(aa == "M"):
										current_prot.append("")
								for i in range(len(current_prot)):
										current_prot[i] += aa
									
				return proteins
	
		'''Computes all possible putative proteins for all ORF'''
		# and sort them based on size
		def get_protein(self,min_size=0):
			
				# order 
				def insert_prot_ord (prot, lst_prot):
						i = 0
						while(i < len(lst_prot) and len(prot)<len(lst_prot[i])):
								i += 1
						lst_prot.insert(i, prot)
					
				rfs = self.frames()  # get all ORF conversions
				res = []
				for rf in rfs:
						# return only protein cases
						prots = self.all_proteins_RF(rf) 
						# additionally sort based on protein size
						for p in prots: 
								if(len(p) > min_size): 
										insert_prot_ord(p, res)
				return res
	
		#####################################################
	
		# Finding Patterns in Sequence
			# find_pattern - find index(ies) of particular pattern 
	
		#####################################################
	
		# Prosite Pattern Lines
		# - Standard IUPAC amino acid used to as bases in pattern, separated by -
		# - x -> any amino acid acceptable
		# - [] -> ambiguity represented by list, any aa in that list acceptable
		# - {} -> ambiguity represented by list, any aa other than in {} accepted
		# - repetition of pattern element shown below:
		#   x(3) -> x-x-x, x(2,4) -> to x-x or x-x-x or x-x-x-x
	
		@staticmethod
		def prosite_process(rex):
				# adjust prosite to RE format
				rex = rex.replace("(","{")
				rex = rex.replace(")","}")
				rex = rex.replace("x",".")
				rex = rex.replace("-","")
				return rex
	
		def find_pattern(self,pattern,  #  sequence of interest
													find_id='first', # first,all,overlap
													search_id=None,
													verbose=True): # None,prosite
			
				if(find_id is 'first'):
					
						if(search_id is 'prosite'):
								pattern = self.prosite_process(pattern)
							
						# General search as well
						re_search = search(pattern,self.seq)
						if (re_search != None):
								if(verbose):
										print(f"showing first for {pattern}")
								result = re_search.span()[0]
								return result
						else:
								if(verbose):
										print(f'no matches for {pattern} found')
									
				elif(find_id is 'all'):
					
						if(search_id is 'prosite'):
								pattern = self.prosite_process(pattern)
							
						re_search = finditer(pattern,self.seq)
						result = []
						for x in re_search:
								result.append(x.span()[0])
							
						if(len(result) is not 0):
								if(verbose):
										print(f"found {len(result)} matches")
								return result
						else:
								if(verbose):
										print(f'no matches for {pattern} found')
									
				elif(find_id is 'overlap'):
					
						if(search_id is 'prosite'):
								pattern = self.prosite_process(pattern)
						mos = finditer("(?="+pattern+")",self.seq)
						result = []
						for x in mos:
								result.append(x.span()[0])
							
						if(len(result) is not 0):
								if(verbose):
										print(f"found {len(result)} matches")
								return result
						else:
								if(verbose):
										print(f'no matches for {pattern} found')
				else:
						print('first,all,overlap options')
					
		#####################################################
					
		# Cutting the Sequence
			# cut_pattern - cut sequence based on particular pattern
					
		#####################################################
					
		# converts IUB ambiguity code into RE
		# returns cut position of a restriction enzyme 
		# (in IUB code) in a sequence
					
		@staticmethod
		def divide_loc(enzyme, sequence):
			
				def iubrex(IUB):   
					
						# main 4 bases
						# purine, pyrimidine, amino
						# keto, strong, weak
						# not A, not C, not G, not T
						#  not T, any 
					
						dic = {"A":"A", "C":"C", "G":"G", "T":"T", 
										# Additional Cases
										"R":"[GA]", "Y":"[CT]", "M":"[AC]", 
										"K":"[GT]", "S":"[GC]", "W": "[AT]",
										"B":"[CGT]", "D":"[AGT]", "H":"[ACT]",
										"V":"[ACG]", "N":"[ACGT]"}
					
						site = IUB.replace("|","")
						rex = ""
					
						for c in site:
								rex += dic[c]
						return rex
			
				regexp = iubrex(enzyme) # convert pattern to IUB format
				matches = finditer(regexp, sequence)
				locs = []
				for match in matches:
					locs.append(match.start() + enzyme.find("|"))
					
				return locs # indicies of cuts
	
		# determines subsequences resulting from a sequence 
		# cut in a list of positions
		def cut_pattern(self,cut_pattern):
			
				res = []
				positions = self.divide_loc(cut_pattern,self.seq)
				positions.insert(0,0)
				positions.append(len(self.seq))
				for i in range(len(positions)-1):
						res.append(self.seq[positions[i]:positions[i+1]])
				return res
	
		# Function for when you want to prepare DNA sequence 
		# feature for ML applications
		def dnaseq_features(self,start=0,n_segs=101,seq_name=None):
			
				print(f"Input Sequence Length: {len(self.seq)}")
				remaind = len(self.seq)%n_segs
				if(remaind is not 0):
						last_id = len(self.seq) - remaind
				print(f"# Bases cut-off: {int(remaind)}")
			
				upd_seq = self.seq[start:last_id]
			
				print(f"Updated sequence length: {len(upd_seq)}")
				print(f"# Segments: {int(len(upd_seq)/n_segs)} created")
				if(seq_name is None):
						seq_name = 'seq'
					
				# store sequence subsets in a dictionary
				dic_seq = {}
				for i in range(0,3):
						a = int(i*n_segs) ; b = int(i*n_segs)+n_segs 
						identifier = f"{seq_name}_{a}:{b}"
						dic_seq[identifier] = upd_seq[a:b]
					
				lst_seq = dic_seq.values()
				index = list(dic_seq.keys())
			
				# One hot encode
			
				ii=-1
				for data in lst_seq:
					
						ii+=1; abc = 'acgt'.upper()
					
						char_to_int = dict((c, i) for i, c in enumerate(abc))
						int_enc = [char_to_int[char] for char in data]
					
						ohe = []
						for value in int_enc:
								base = [0 for _ in range(len(abc))]
								base[value] = 1
								ohe.append(base)
						np_mat = np.array(ohe)
						np_mat = np.expand_dims(np_mat,axis=0)
					
						if(ii is not 0):
								matrix = np.concatenate([np_mat,matrix],axis=0)
						else:
								matrix = np_mat
							
				return matrix,index

# Singular Sequence Class + Additional Information
# works in the same way as SQ
	
class SQRec(SQ):
	
		def __init__(self,seq=None,id=None,
							name=None,description=None):
			
				self.seq = seq.seq # String
				self.SQ = seq
				self.seq_type = seq.seq_type
				self.id = id  # sequence identifier (eg locus tag)
				self.name = name   # name of sequence
				self.description = description
				self.annotations = {}
			
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
					
		# method to add annotation to the current detailed sequence
		def add_annotation(self,inSQRec):
				lseq = inSQRec.seq  # local SQ
				lid = inSQRec.id
				ldesc = inSQRec.description
				
				# find the subsequence in the main sequence
				idx = self.SQ.find_pattern(pattern=str(lseq),
							   find_id='all',
							   search_id='standard',
							   verbose=False)
				
				# for each matching index
				for i in idx:
					ln = len(lseq)
					self.annotations[f'sq_{i}:{i+ln}'] = f"{lid}_{ldesc}"
					
