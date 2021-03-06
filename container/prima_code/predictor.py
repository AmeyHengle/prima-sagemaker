import layoutparser as lp
import json
import numpy as np
import cv2
import flask

prefix = "/opt/ml/"

class custom_PRIMA:
  
    def __init__(self, config_file = "config_PRIMA.yaml"):
        self.config_file = config_file
        self.label_map = {1:"text", 2:"figure", 3:"table", 4:"MathsRegion", 5:"SeparatorRegion", 6:"OtherRegion"}
        self.extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.7]
        self.model = None

    def load_model(self):
        self.model = lp.Detectron2LayoutModel(config_path  = self.config_file,
                                         extra_config = self.extra_config,
                                         label_map = self.label_map)

    def predict(self, image):

        results = self.model.detect(image)
        return results
    
    
 # The flask app for serving predictions
app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    """Determine if the container is working and healthy. In this sample container, we declare
    it healthy if we can load the model successfully."""
    health = ScoringService.get_model() is not None  # You can insert a health check here

    status = 200 if health else 404
    return flask.Response(response='\n', status=status, mimetype='application/json')


@app.route('/invocations', methods=['POST'])
def transformation():
    """Do an inference on a single batch of data. In this sample server, we take data as CSV, convert
    it to a pandas data frame for internal use and then convert the predictions back to CSV (which really
    just means one prediction per line, since there's a single column.
    """
    
    data = None
    
    data = flask.request.data
    
    print("\nData received: ", data)
    
    print("\nLoading Model")
    model = custom_PRIMA()
    model.load_model()
    print("\nModel Loaded. Ready for predictions.")
    
    temp = cv2.imread("sample_input.jpg")
    predictions = model.predict(temp)
    print("\nPredictions made - ", type(predictions))

    
#     result= predictions
    result = "This is a sample result response returned by the SAGEMAKER"
    
    return flask.Response(response=result, status=200)