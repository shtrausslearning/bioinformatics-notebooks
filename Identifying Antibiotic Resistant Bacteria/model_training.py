''' Standard Cross Validation '''
# models defined as turble of ('name',class instance')

# define models used for testing
models = []
n_est = 10

models.append(('LDA', LinearDiscriminantAnalysis())) 
models.append(('KNN', KNeighborsClassifier()))  
models.append(('NB', GaussianNB()))
models.append(('SVC',SVC()))
models.append(('TREE', DecisionTreeClassifier())) # Supervised Model
models.append(('GBM', GradientBoostingClassifier(n_estimators=n_est)))
models.append(('XGB',XGBClassifier(n_estimators=n_est,verbosity = 0)))
models.append(('CAT',CatBoostClassifier(silent=True,n_estimators=n_est)))
models.append(('RF', RandomForestClassifier(n_estimators=n_est)))

# Get case; (Dataset Feature Class)
case = get_unitigs()
case.get_case('cip_sr')

# Standard KFOLD evaluation initialisation
eval1 = class_eval(data=case, # input the case class
                   nfold = 4, # 4 fold kfold
                   models=models) # global models tuple list)

# Evaluate kfold using selected models 
eval1.cv(type_id='kfold')  # standard kfold evaluation

# Plot Training Results
eval1.fold_plot()  # plot kfold results

# If tree based methods used; get feature importance
crit_unitigs = fi(data=eval1,sort_by='CB')
crit_unitigs.get()

''' Grid SearchCV Validation '''
# When we want to search for best model during each cross validation segment
# load only one model into models list

# Define Grid used in Cross Validation
params = {'n_estimators':[10,25,40],
         'learning_rate':[0.01,0.05,0.5]}

# Define Model (just the one) 
models = []
models.append(('CAT', CatBoostClassifier(silent=True,
                                         task_type="GPU"),params))

# Get Dataset Features
case2 = get_unitigs()
case2.get_case('cip_sr')

eval2 = class_eval(data=case,
                   models=models)
eval2.gscv()
