# docker image build -t saahilbjain/proximity_detector . 
# docker container run -d -p 5001:5001 saahilbjain/proximity_detector
# docker push saahilbjain/proximity_detector
docker container run -p 5001:5001 saahilbjain/proximity_detector
python3 eval.py