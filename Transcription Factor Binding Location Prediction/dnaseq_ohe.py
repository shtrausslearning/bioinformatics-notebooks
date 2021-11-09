''' One-Hot-Encoding of DNA sequence '''
# used to create dna segment sequence features, similar to input data in notebook

import numpy as np

# Test Sequence you want to OHE for ML problems
seq = 'ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGA' +\
			'TCTGTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTC' + \
			'GGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAACTAATTACTGTCGTTGAC' +\
			'AGGACACGAGTAACTCGTCTATCTTCTGCAGGCTGCTTACGGT'  + \
			'TTCGTCCGTGTTGCAGCCGATCATCAGCACATCTAGGTTTCGTCCGGGTGTGACCGA' +\
			'AAGGTAAGATGGAGAGCCTTGTCCCTGGTTTCAACGAGAAAA' + \
			'CACACGTCCAACTCAGTTTGCCTGTTTTACAGGTTCGCGACGTGCTCGTAC'
			
# Function for when you want to prepare DNA sequence feature for ML applications
def dnaseq_features(seq,start=0,n_segs=101,seq_name=None):
	
		print(f"Input Sequence Length: {len(seq)}")
		remaind = len(seq)%n_segs
		if(remaind is not 0):
				last_id = len(seq) - remaind
		print(f"# Bases cut-off: {int(remaind)}")
	
		upd_seq = seq[start:last_id]
	
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

dna_ohe_feat,dna_ohe_index = dnaseq_features(seq)
print(f'\n{type(dna_ohe_feat)}')
print(f'DNA OHE features: {dna_ohe_feat.shape}')
print(f'Index: {dna_ohe_index[:10]}')
