from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time

# retrieve environment variables
ENDPOINT = "https://senacalidavidsebastian-prediction.cognitiveservices.azure.com/"
prediction_key = "b1e81542f271448db4f31264b66a46d4"
prediction_resource_id = "/subscriptions/5cffd501-9ba1-475a-b35b-fee1679a66a1/resourceGroups/SENAsoftDavid_Sebastian/providers/Microsoft.CognitiveServices/accounts/SenaCaliDavidSebastian-Prediction"

# Now there is a trained endpoint that can be used to make a prediction
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
project_id = "45ab08a3-bc97-4680-8496-48e561d2be37"


"""
img = "https://static.fundacion-affinity.org/cdn/farfuture/PVbbIC-0M9y4fPbbCsdvAD8bcjjtbFc0NSP3lRwlWcE/mtime:1643275542/sites/default/files/los-10-sonidos-principales-del-perro.jpg"

results = predictor.classify_image_url(project_id, "classifyModel",img)



for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))
"""

        
      
with open("C:/Users/Aprendiz/Desktop/SENASoft/Patos/pato_40.jpg", "rb") as image_contents:
    results = predictor.classify_image(project_id, "classifyModel", image_contents.read())

for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))# Now there is a trained endpoint that can be used to make a prediction


"""
    # Display the results.
    
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

with open(os.path.join (base_image_location, "Test/test_image.jpg"), "rb") as image_contents:
    results = predictor.classify_image(
        project.id, publish_iteration_name, image_contents.read())

    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))



"""
