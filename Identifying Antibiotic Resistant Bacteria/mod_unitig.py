''' Feature Matrix Upsampling Modification (+Target) '''
# Model based approach to upsample minor class in target variable

class mod_unitigs():
    
    def __init__(self,unitigs):
        self.X = unitigs.X # input data class
        self.target_name = unitigs.target_name
        self.verbose = True

    ''' Downsampling Class 0 using .sample & recompile '''
    # If there's too much of the dominant class, just downsample
    
    def split_case(self,frac_id=0.5):
        
        X = self.train
        y = pd.Series(self.target,name=self.target_name)
        XX = pd.concat([X,y],axis=1)
        
        lst_temp = dict(tuple(XX.groupby(self.target_name))) # divide classes
        ratio = lst_temp[0].shape[0]/lst_temp[1].shape[0] # get class ratio
        
        # Sample approach for downsizing majority class
        X_red = lst_temp[0].sample(frac=frac_id)
        X_all = pd.concat([X_red,lst_temp[1]],axis=0)
        
        if(self.verbose):
            print(f'Class 0 : {lst_temp[0].shape}')
            print(f'Class 1 : {lst_temp[1].shape}')
            print(f'Class Ratio: {round(ratio,4)}')
            print(f'Reduced Training Matrix: {X_all.shape}')
        
        # Redefine .train, .targett
        self.target = X_all[self.target_name].copy()
        X_all.drop(self.target_name, inplace=True, axis=1)
        self.train = X_all
        
    ''' SMOTE UPSAMPLING '''
    # For unbalanced problems, synthetically/model new data
        
    def smote(self,smote_id = 'smotenc',
                   smote_strat=0.5,
                   k_neighbours=5):
        
        self.smote_id = smote_id
        self.smote_strat = smote_strat
        self.smote_nbr = k_neighbours
        
        y = self.X[self.target_name].copy()
        X = self.X.drop([self.target_name],axis=1).copy()
    
        # smote for contin, smotenc for category
        if(self.smote_id is 'smote'):
            model_id = SMOTE(sampling_strategy=self.smote_strat,
                             k_neighbors=self.smote_nbr)
        elif(self.smote_id is 'smotenc'):
            model_id = SMOTENC(sampling_strategy=self.smote_strat,
                               k_neighbors=self.smote_nbr,
                               categorical_features=[0,1])
        
        X_mod, y_mod = model_id.fit_resample(X,y)
        self.X = pd.concat([X_mod,y_mod],axis=1)
        
        if(self.verbose):
            print(f'\nSMOTE Upsampling: {self.X.shape}')
            print(f'Target Value Counts: \n{pd.Series(y_mod).value_counts()}')
        self.X = pd.concat([X_mod,y_mod],axis=1)
