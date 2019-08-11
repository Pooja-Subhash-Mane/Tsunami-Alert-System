from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
import numpy as np
import array as ar

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	'''df= pd.read_csv("YoutubeSpamMergedData.csv")
	df_data = df[["CONTENT","CLASS"]]
	# Features and Labels
	df_x = df_data['CONTENT']
	df_y = df_data.CLASS
    # Extract Feature With CountVectorizer
	corpus = df_x
	cv = CountVectorizer()
	X = cv.fit_transform(corpus) # Fit the Data
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, df_y, test_size=0.33, random_state=42)
	#Naive Bayes Classifier
	from sklearn.naive_bayes import MultinomialNB
	clf = MultinomialNB()
	clf.fit(X_train,y_train)
	clf.score(X_test,y_test)
	#Alternative Usage of Saved Model
	 ytb_model = open("naivebayes_spam_model.pkl","rb")
	# clf = joblib.load(ytb_model)
	'''

	# df=pd.read_csv("S:/extra/SIH/tsunami/final SIH/Earthquake.csv",sep=',',header=0)
	# df=df.drop(['place','time','locationSource','magSource','magType','nst','gap','dmin','rms','net','id','updated','type','horizontalError','magNst','status','depthError','magError'], axis=1)
	
	# df['tsunami']=0
	# df.iloc[160, df.columns.get_loc('tsunami')] = 1
	# df.iloc[949, df.columns.get_loc('tsunami')] = 1
	# df.iloc[1268, df.columns.get_loc('tsunami')] = 1
	# df.iloc[1756, df.columns.get_loc('tsunami')] = 1
	# df.iloc[4711, df.columns.get_loc('tsunami')] = 1
	# df.iloc[4993, df.columns.get_loc('tsunami')] = 1
	# df.iloc[7230, df.columns.get_loc('tsunami')] = 1
	# df.iloc[7755, df.columns.get_loc('tsunami')] = 1
	# df.iloc[7799, df.columns.get_loc('tsunami')] = 1
	# df.iloc[8544, df.columns.get_loc('tsunami')] = 1
	# df.iloc[9070, df.columns.get_loc('tsunami')] = 1
	# df.iloc[9586, df.columns.get_loc('tsunami')] = 1
	# df.iloc[10049, df.columns.get_loc('tsunami')] = 1
	# df.iloc[10927, df.columns.get_loc('tsunami')] = 1
	# df.iloc[11382, df.columns.get_loc('tsunami')] = 1
	# df.iloc[11491, df.columns.get_loc('tsunami')] = 1
	# df.iloc[12871, df.columns.get_loc('tsunami')] = 1
	# df.iloc[13501, df.columns.get_loc('tsunami')] = 1
	# df.iloc[14033, df.columns.get_loc('tsunami')] = 1
	# df.iloc[14517, df.columns.get_loc('tsunami')] = 1
	# df.iloc[14608, df.columns.get_loc('tsunami')] = 1
	# df.iloc[14624, df.columns.get_loc('tsunami')] = 1


	# df_X=df[['latitude', 'longitude', 'mag', 'depth']]  # Features
	# df_y=df['tsunami']#target	
	# cv = CountVectorizer()
	# X = cv.fit_transform(df_X)
	ytb_model = open("/home/atharvakango/Desktop/Hack/theapp/data/random_forest.pkl","rb")
	clf = joblib.load(ytb_model)
	if request.method == 'POST':
		lng = request.form['lng']
		lat = request.form['lat']
		power = request.form['depth']
		depth = request.form['power']


		data= [[int(lng), int(lat), int(power), int(depth)]]
		# data[0]=lng;
		# data[1]=lat;
		# data[2]=power;
		# data[3]=depth;
		#data = [lng,lat,power,depth]
		#arr=np.array(data[lng,lat,power,depth])
		#vect = cv.transform(data).toarray()
		my_prediction = clf.predict(data)

	return render_template('result.html',prediction =my_prediction)



if __name__ == '__main__':
	app.run(debug=True)