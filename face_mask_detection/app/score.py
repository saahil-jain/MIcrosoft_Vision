from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array, array_to_img
from tensorflow.keras.models import load_model
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
    global faceNet, maskNet, args

    args = {
        "confidence" : 0.3,
        "input_dimensions" : 200
    }

    print("[INFO] loading faceNet model...")
    prototxtPath = os.path.sep.join(["Models","deploy.prototxt"])
    weightsPath = os.path.sep.join(["Models","res10_300x300_ssd_iter_140000.caffemodel"])
    faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

    print("[INFO] loading maskNet model...")
    maskNet_path = os.path.sep.join(["Models","maskNet_model.h5"])
    maskNet = load_model(maskNet_path)

@app.route("/predict", methods=["POST"])
def predict():
    frame = flask.request.json
    locs = []
    preds = []
    try:
        frame = preprocess(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
        faceNet.setInput(blob)
        detections = faceNet.forward()
        faces = []
        locs = []
        preds = []

        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > args["confidence"]:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                (startX, startY) = (max(0, startX-20), max(0, startY-20))
                (endX, endY) = (min(w - 1, endX+20), min(h - 1, endY+20))
                face = frame[startY:endY, startX:endX]
                try:
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)		
                    face = cv2.resize(face, (args["input_dimensions"], args["input_dimensions"]))	
                    face = img_to_array(face)
                    face = preprocess_input(face)
                except:
                    continue
                faces.append(face)
                (startX, startY, endX, endY) = map(int, [startX, startY, endX, endY])
                locs.append((startX, startY, endX, endY))
        if len(faces) > 0:
            faces = np.array(faces, dtype="float32")
            preds = maskNet.predict(faces, batch_size=32)
        predictions = []
        for prediction in preds:
            a,b = prediction
            a = float(a)
            b = float(b)
            predictions.append((a,b))
        mask_data = json.dumps({'locs': locs, 'predictions':predictions})
        return mask_data
        # return (locs, predictions)

    except Exception as e:
        error = str(e)
        mask_data = json.dumps({'locs': locs, 'predictions':preds})
        return mask_data
        # return (locs, preds)
        # return error

if __name__ == "__main__":
    init_predictor()
    app.run(host='0.0.0.0', port = 5000)