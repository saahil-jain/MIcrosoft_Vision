from imutils.video import VideoStream
import numpy as np
import imutils
import time
import json
import cv2
import os

# from score import init_predictor, predict
import requests

print("[INFO] starting video stream...")
vs = VideoStream().start()
time.sleep(2.0)
# init_predictor()
while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	cols, rows, _ = frame.shape
	brightness = np.sum(frame) / (255 * cols * rows)
	ratio = brightness / 1.0
	if ratio < 1.0:
		frame = cv2.convertScaleAbs(frame, alpha = 1 / ratio, beta = 50)
	
	frame_data = frame
	frame_data = np.array(frame)
	frame_data = json.dumps({'data': frame_data.tolist()})
	# mask_results = json.loads(predict(frame_data))
	mask_results = json.loads(requests.post('http://localhost:5000/predict',json = frame_data).text)
	locs = mask_results["locs"]
	preds = mask_results["predictions"]

	# (locs, preds) = predict(frame_data)
	
	for (box, pred) in zip(locs, preds):
		(startX, startY, endX, endY) = box
		(mask, withoutMask) = pred

		label = "Mask" if mask > withoutMask else "No Mask"
		color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
		label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
		cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.50, color, 2)
		cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs.stop()