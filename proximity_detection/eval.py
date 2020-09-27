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
# vs = VideoStream(1).start()
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
	mask_results = json.loads(requests.post('http://localhost:5001/predict',json = frame_data).text)
	people = mask_results["people"]
	violate = mask_results["violate"]

	# (locs, preds) = predict(frame_data)

	for (i, (prob, bbox, centroid)) in enumerate(people):
		(startX, startY, endX, endY) = bbox
		(cX, cY) = centroid
		color = (0, 255, 0)

		if i in violate:
			color = (0, 0, 255)
		cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
		cv2.circle(frame, (cX, cY), 5, color, 1)

	text = "Social Distancing Violations: {}".format(len(violate))
	cv2.putText(frame, text, (10, frame.shape[0] - 50),cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 0, 255), 2)
	text = "Number of people: {}".format(len(people))
	cv2.putText(frame, text, (10, frame.shape[0] - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 0, 255), 2)

	cv2.imshow("Video", frame)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs.stop()