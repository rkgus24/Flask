from cProfile import label
import flask
from flask import Flask, request, render_template
from sklearn.externals import joblib
import numpy as np
from scipy import misc
from ml.model import export_model
from flask_restful import Resource, Api

ap = Flask(__name__)
api = Api(app)

@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')

@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method == 'POST':
        file = request.files['image']
        if not file: return render_template('index.html', ml_label="No Files")
        
        img = misc.imread(file)
        img = img[:, :, :3]
        img = img.reshape(1, -1)
        
        prediction = model.predict(img)
        
        label = str(np.squeeze(prediction))
        
        if label == '10': label = '0'
        return render_template('index.html', ml_label=label)
    
@app.route('/retrain', methods=['POST'])
def make_model():
    if request.method == 'POST':
        export_model('R')
        return render_template('index.html', md_label='모델 재생성 완료')
    
class RestMl(Resource):
    def get(self):
        export_model('R')
        return {'result': True, 'modelName': 'model.pkl'}
    
api.add_resource(RestMl, '/retrainMidel')

if __name__ == '__main__':
    model = joblib.load('./model/model.pkl')
    app.run(host='0.0.0.0', port=8000, debug=True)