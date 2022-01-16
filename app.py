# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'pred.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
        Home_Team = request.form['Home_Team']
        if Home_Team == 'Arsenal':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif Home_Team == 'Aston Villa':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif Home_Team == 'Bradford':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif Home_Team == 'Everton':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif Home_Team == 'Ipswich':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif Home_Team == 'Man City':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif Home_Team == 'Middlesbrough':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif Home_Team == 'Newcastle':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
         
            
        Away_Team = request.form['Away_Team']
        if Away_Team == 'Arsenal':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif Away_Team == 'Aston Villa':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif Away_Team == 'Bradford':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif Away_Team == 'Everton':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif Away_Team == 'Ipswich':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif Away_Team == 'Man City':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif Away_Team == 'Middlesbrough':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif Away_Team == 'Newcastle':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
            
        FTHG = float(request.form['FTHG'])
        HTP = float(request.form['HTP'])
        ATP = float(request.form['ATP'])
        HTGD = float(request.form['HTGD'])
        ATGD = float(request.form['ATGD'])
        
        temp_array = temp_array + [FTHG, HTP, ATP, HTGD, ATGD]
        
        data = np.array([temp_array])
        my_prediction = regressor.predict(data)[0]
        if my_prediction== "NH":
            res= Away_Team
        else:
            res= Home_Team

        
              
        return render_template('result.html', pred = res)



if __name__ == '__main__':
	app.run(debug=True)