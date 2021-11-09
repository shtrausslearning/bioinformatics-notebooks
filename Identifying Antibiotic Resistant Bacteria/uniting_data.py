''' Align Metadata Target values w/ Unitig File & Compile Feature Matrix '''
# class for reading and storing unitig feature matrix data

class get_unitigs:
    
    def __init__(self,verbose=True):
        self.df = pd.read_csv('../input/gono-unitigs/metadata.csv', index_col=0)
        self.meta_names = self.df.columns 
        self.target_name = None
        self.verbose = verbose
    
    # Get Unitig Feature matrix & Target Vector
    
    def get_case(self,phenotype=None):
    
        self.target_name = phenotype
        _metadata = self.df
        if(self.verbose):
            print(f'Target Antibiotic: {self.target_name}')
            print(f'Metadata df: {_metadata.shape}')
        
        # remove those that don't contain target values
        _metadata = _metadata.dropna(subset=[phenotype])
        self.metadata = _metadata.copy()
        
        if(self.verbose):
            print(f'Metadata df after na() removal {_metadata.shape}')
        _metadata = _metadata[phenotype] # choose target variable 
        
        prefix = '../input/gono-unitigs/'
        suffix = '_gwas_filtered_unitigs.Rtab'
        
        if(self.verbose):
            print('\nCombining Metadata & Unitigs')
        
        # unitig feature matrix for phenotype
        tdf = pd.read_csv(prefix + phenotype + suffix, sep=" ", 
                          index_col=0, low_memory=False)
        # align column data w/ metadata df (pattern_id = sample_idd)
        tdf = tdf.T 
        # keep only common rows, ie. that have resistence measure]
        tdf = tdf[tdf.index.isin(_metadata.index)] 
        
        train = tdf
        target = _metadata[_metadata.index.isin(tdf.index)]

        self.X = pd.concat([train,target],axis=1)
        if(self.verbose):
            print(f'Unitig Matrix (+target): {self.X.shape}')
            
    ''' unitig visual '''
    
    def toabr(self):
        
        self.X_names = self.X.columns.tolist()
        temp_names = self.X_names.copy()
        
        unitigs = self.X_names.copy()
        del unitigs[-1]

        lst_abr = []
        ii=-1
        for unitig in range(0,len(unitigs)):
            ii+=1;lst_abr.append(f'u{ii}')
        lst_abr.append(self.target_name)
        self.X.columns = lst_abr
        self.dicabr = dict(zip(lst_abr,self.X_names))
        
    def touni(self):
        self.X.columns = self.X_names
        
case = get_unitigs()
case.get_case('cfx_sr')
