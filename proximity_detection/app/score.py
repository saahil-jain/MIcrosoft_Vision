from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array, array_to_img
from tensorflow.keras.models import load_model
from scipy.spatial import distance as dist
import numpy as np
import json
import cv2
import os

import flask
app = flask.Flask(__name__)

def preprocess(input_data_json):
    # convert the JSON data into the tensor input
    return np.array(json.loads(input_data_json)['data']).astype('float32')

def init_predictor():
    global MobileNetSSD, args

    args = {
        "confidence" : 0.1,
        "boundary" : 0,
        "min_distance" : 75
    }

    print("[INFO] loading model...")
    prototxtPath = os.path.sep.join(["Models","MobileNetSSD_deploy.prototxt"])
    weightsPath = os.path.sep.join(["Models","MobileNetSSD_deploy.caffemodel"])
    MobileNetSSD = cv2.dnn.readNet(weightsPath, prototxtPath)
  

@app.route("/predict", methods=["POST"])
def predict():
    frame = flask.request.json
    people = []
    violate = []
    try:
        # frame = flask.request.json
        frame = preprocess(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
        # pass the blob through the network and obtain the detections and
        # predictions
        MobileNetSSD.setInput(blob)
        detections = MobileNetSSD.forward()
        # loop over the detections
        people = []
        for i in np.arange(0, detections.shape[2]):
            idx = int(detections[0, 0, i, 1])
            if (idx==15):
                confidence = detections[0, 0, i, 2]
                if confidence > args["confidence"]:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    (startX, startY) = (max(0, startX-args["boundary"]), max(0, startY-args["boundary"]))
                    (endX, endY) = (min(w - 1, endX+args["boundary"]), min(h - 1, endY+args["boundary"]))
                    centroidX = int((startX + endX)/2)
                    centroidY = int((startY + endY)/2)
                    height = (endY-startY)
                    width = (endX-startX)
                    (startX, startY, endX, endY) = map(int, [startX, startY, endX, endY])
                    confidence = int(confidence)
                    person = (confidence,(startX, startY, endX, endY), (centroidX, centroidY))
                    people.append(person)
        # print(len(people))

        violate = set()
        if len(people) >= 2:
            centroids = np.array([r[2] for r in people])
            D = dist.cdist(centroids, centroids, metric="euclidean")
            for i in range(0, D.shape[0]):
                for j in range(i + 1, D.shape[1]):
                    if D[i, j] < args["min_distance"]:
                        violate.add(i)
                        violate.add(j)
        violate = list(violate)
        mask_data = json.dumps({'people': people, 'violate':violate})
        return mask_data
        # return((people,violate))

    except Exception as e:
        error = str(e)
        mask_data = json.dumps({'people': people, 'violate':violate})
        return mask_data
        # return((people,violate))
        # return error

if __name__ == "__main__":
    init_predictor()
    app.run(host='0.0.0.0', port = 5001)
