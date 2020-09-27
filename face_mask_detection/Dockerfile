FROM python:3.7

COPY app /app
# Set the working directory
WORKDIR /app

RUN pip install -U pip
RUN pip install numpy==1.18.2 opencv-python-headless==4.2.0.32 json5==0.9.3 imutils==0.5.3 Flask==1.1.2
RUN pip install tensorflow==2.0.0
# Expose the port
EXPOSE 5000
# Run the flask server for the endpoints
CMD python -u score.py