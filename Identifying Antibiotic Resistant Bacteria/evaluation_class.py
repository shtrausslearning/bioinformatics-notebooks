''' Evaluation Class '''
# Model evaluation class used in problem
# input -> feature matrix + target variable

# cross validation approaches
# gscv -> gridsearch cross validation (search for best hyperparameter combo)
# cv -> standard kfold cross validation (type_id -> 'skfold'/'kfold')

# fold_plot -> plot training/evaluation results
# col_trans -> change unitig name to abrev. & visa versa

# self.store_models -> stores resultant models from gscv/cv
# self.nfold -> number of cross validation folds in cv
# self.gsfold -> number of grid search cross validation folds

class class_eval:
    
    def __init__(self,data=None,models=None,nfold = 4, 
                 gsfold=3, verbose=True,
                 shuffle_id=False,random_state=22):

        self.shuffle = shuffle_id

        if(self.shuffle is False):
            self.rs = None
        else:
            self.rs = random_state # random state
        
        if(data is not None):
            X_all = data.X
            self.y = data.X[data.target_name].copy()
            self.X = data.X.drop([data.target_name],axis=1).copy()
        else:
            print('input case data')

        self.models = models # Tuple /w (name,model)
        self.nfold = nfold       # number of cross validation folds 
        self.gsfold = gsfold    # number of grid search folds in every fold
        self.target_name = data.target_name  # target name
        
    ''' Grid-Search Standard Kfold Cross Validation '''
    # For each fold, a grid search cv is applied to find best params
    
    def gscv(self,type_id='kfold'):
        
        self.store_models = {} # Store models of Kfolds
        self.dic_tr = {}
        self.dic_te = {}
        
        for model in self.models:
            
            if(type_id is 'skfold'):
                kfold = StratifiedKFold(n_splits=self.nfold,
                                        shuffle=self.shuffle,
                                        random_state=self.rs)
            elif(type_id is 'kfold'):
                kfold = KFold(n_splits=self.nfold,
                              shuffle=self.shuffle,
                              random_state=self.rs)
        
            lst_temp = []; lst_temp2 = []; kfold_id = -1
            for train_index, test_index in kfold.split(self.X,self.y):
    
                kfold_id+=1;print(f'\nkfold {kfold_id}')
                # split data into train/test sets
                X_train = self.X.iloc[train_index]
                y_train = self.y[train_index]
                X_test = self.X.iloc[test_index]
                y_test = self.y[test_index]

                # perform grid search to identify best hyper-parameters
                gs_clf = GridSearchCV(model[1],param_grid=model[2], 
                                      cv=self.gsfold, n_jobs=-1, 
                                      scoring='balanced_accuracy')
                
                # Train using the best model 
                gs_clf.fit(X_train, y_train)
                best_model = gs_clf.best_estimator_ # best cv model
                self.store_models[f'GS_{model[0]}_{kfold_id}'] = best_model
                
                # Predict using best model
                ym_tr = gs_clf.predict(X_train)
                ym_te = gs_clf.predict(X_test)
                score_tr = balanced_accuracy_score(y_train,ym_tr)
                score_te = balanced_accuracy_score(y_test,ym_te)
                lst_temp.append(score_tr); lst_temp2.append(score_te)
            
                print(f'Train Score: {round(score_tr,4)} - Test Score: {round(score_te,4)}')
                print('Best hyperparameters for this fold')
                print(gs_clf.best_params_)
                print(f"Test : Confusion matrix Fold {kfold_id}")
                print(confusion_matrix(y_test, ym_te))
                
            self.dic_tr[model[0]] = lst_temp
            self.dic_te[model[0]] = lst_temp2
            test_mean = round(sum(lst_temp2)/len(lst_temp2),4)
            print(f'\n {model[0]} - Test Mean Score: {test_mean}')
        
    '''K-Fold Cross Validation'''
    # w/ type_id option; statified used to make sure classes are balanced in folds
    
    def cv(self,type_id='kfold'):
        
        print(f'type_id set to: {type_id}')
        self.store_models = {} # Store models of Kfolds
        self.dic_tr = {}
        self.dic_te = {}
    
        # Cycle though all tuple model settings
        for model in self.models:
            
            t0 = time.time()
            if(type_id is 'skfold'):
                kfold = StratifiedKFold(n_splits=self.nfold,
                                        shuffle=self.shuffle,
                                        random_state=self.rs)
            elif(type_id is 'kfold'):
                kfold = KFold(n_splits=self.nfold,
                              shuffle=self.shuffle,
                              random_state=self.rs)
                
            lst_temp = []; lst_temp2 = []; kfold_id = -1
            for train_index, test_index in kfold.split(self.X,self.y):

                kfold_id+=1              
                # split data into train/test sets
                X_train = self.X.iloc[train_index]
                y_train = self.y[train_index]
                X_test = self.X.iloc[test_index]
                y_test = self.y[test_index]

                # Fit, Stopre & Predict Kfold models
                model[1].fit(X_train, y_train)
                self.store_models[f'{model[0]}_{kfold_id}'] = model[1]
                ym_tr = model[1].predict(X_train)
                ym_te = model[1].predict(X_test)
                
                score_tr = balanced_accuracy_score(y_train,ym_tr)
                score_te = balanced_accuracy_score(y_test,ym_te)
                lst_temp.append(score_tr); lst_temp2.append(score_te)

            self.dic_tr[model[0]] = lst_temp
            self.dic_te[model[0]] = lst_temp2
            test_mean = round(sum(lst_temp2)/len(lst_temp2),4)
            print(f'{model[0]} - Test Mean Score: {test_mean} - Total Time: {round(time.time() - t0,4)}')
            
    ''' unitig visual functions only '''
    
    def col_trans(self,sel_id=0):
        
        # unitig to abrev
        if(sel_id is 0):
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
            
        # abreb to unitig
        elif(sel_id is 1):
            self.X.columns = self.X_names
        
    ''' PLOT KFOLD RESULTS '''
    
    def fold_plot(self):
            
        df_tr = pd.DataFrame(self.dic_tr)
        df_te = pd.DataFrame(self.dic_te)

        # Make Plots
        fig,ax = plt.subplots(2,2,figsize=(14,6))
        sns.stripplot(data=df_tr, orient='h',linewidth=1,ax=ax[0,0])
        sns.heatmap(data=df_tr,annot=True,cbar=False,cmap="plasma_r",
                    vmax=1,vmin=0.5,ax=ax[0,1])
        sns.stripplot(data=df_te, orient='h',linewidth=1,ax=ax[1,0])
        sns.heatmap(data=df_te,annot=True,cbar=False,cmap="plasma_r",
                    vmax=1,vmin=0.5,fmt='.3g',ax=ax[1,1])
        ax[0,0].set_xlim([0.5,1.1]);ax[1,0].set_xlim([0.5,1.1])
        ax[0,0].set_title('train kfold') 
        ax[0,1].set_title('train kfold heatmap')
        ax[1,0].set_title('test kfold')
        ax[1,1].set_title('test kfold heatmap')
        sns.despine(bottom=True, left=True)
        plt.tight_layout()
