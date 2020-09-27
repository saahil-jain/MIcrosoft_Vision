# docker image build -t saahilbjain/mask_detector . 
# docker container run -d -p 5000:5000 saahilbjain/mask_detector
# docker push saahilbjain/mask_detector

docker container run -p 5000:5000 saahilbjain/mask_detector
python3 eval.py