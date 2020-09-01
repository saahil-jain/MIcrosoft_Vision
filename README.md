# Microsoft_Vision



# Computer Vision to Enfore Social Distancing Measures

These are developed containerized computer vision models for the detection of people violating health protocols. These models could be deployed on edge devices. These edge devices could either be drones or just a regular camera connected to a micro-computer

We built two computer vision models for the following problems:	

* ## Proximity Sensing and Social Distancing :
    To detect if people within the field of view are maintaining appropriate distance between each other.
* ## Mask Compliance
    To detect if people within the field of view are wearing a face mask.

# Steps to Run Proximity detection model

* ## Prerequisites :
Download Docker on the system, iF you want to run server as a container.
When in the vision_models/proximity_detection directory,
Enter the following line into the terminal
pip install requirements.txt

* ## Run Server as a Container
Once Docker is up and running,
Open terminal in the vision_models/proximity_detection directory.
Enter the following line into the terminal
docker container run -p 5001:5001 proximity_detector

* ## Run Server as a Preocess
WOpen terminal in the vision_models/proximity_detection/app directory.
Enter the following line into the terminal
python score.py

* ## Run Client as a Preocess
Open terminal in the vision_models/proximity_detection directory.
Enter the following line into the terminal
python eval.py

# Steps to Run Face Mask detection model

* ## Prerequisites
 Download Docker on the system, iF you want to run server as a container.
When in the vision_models/face_mask_detection directory,
Enter the following line into the terminal
pip install requirements.txt

* ## Run Server as a Container
Once Docker is up and running,
Open terminal in the vision_models/face_mask_detection directory.
Enter the following line into the terminal
docker container run -p 5000:5000 mask_detector

* ## Run Server as a Preocess
WOpen terminal in the vision_models/face_mask_detection/app directory.
Enter the following line into the terminal
python score.py

* ## Run Client as a Preocess
Open terminal in the vision_models/face_mask_detection directory.
Enter the following line into the terminal
python eval.py

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
