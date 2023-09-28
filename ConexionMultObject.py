from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials

class ConexionObject:
    # retrieve environment variables
    ENDPOINT = "https://pruebadeteccionobjetos-prediction.cognitiveservices.azure.com/"
    prediction_key = "26a4605ec33349cb99d77da1a0dfb3c6"        
    project_id = "909af45c-b3a1-46bf-9c8e-d1be96adcf3c"
    model = "Iteration3"    
            
    def connObject(self):        
        prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": self.prediction_key})
        predictorConn = CustomVisionPredictionClient(self.ENDPOINT, prediction_credentials)
        return predictorConn
    