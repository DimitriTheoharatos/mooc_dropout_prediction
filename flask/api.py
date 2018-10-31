from sklearn.externals import joblib
import numpy as np



def get_prob(age, subject, gender, education):
	log_model = joblib.load('../models/log_flask_model.pkl')
	columns = np.array(['>=70', '60s', '50s', '40s', '30s', '25_to_30',
       '20_to_25', 'under_20', 'cs', 'social', 'mechanics', 'electrical',
       'bio', 'public_health', 'gender_f', 'gender_m', "LoE_DI_Bachelor's",
       'LoE_DI_Doctorate', 'LoE_DI_Less than Secondary', "LoE_DI_Master's",
       'LoE_DI_Secondary'])

	#initialize a numpy array of all zeroes
	input_features = np.zeros(len(columns))

	#find the indices where the user input is the same as the column
	age_index = np.where(columns == age)[0][0]
	subject_index = np.where(columns == subject)[0][0]
	gender_index = np.where(columns == gender)[0][0]
	education_index = np.where(columns == education)[0][0]

	#encode our inputs with matching indices
	input_features[age_index] = 1
	input_features[subject_index] = 1
	input_features[gender_index] = 1
	input_features[education_index] = 1

	return round(log_model.predict_proba(input_features.reshape(1,-1))[0][1], 3)



	
