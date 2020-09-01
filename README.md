# Hospital of the Future - Monitoring Social Distancing 


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Downloading Docker](#downloading-docker)
  * [Proximity Detection Model](#proximity-detection-model)
    * [Prerequisites](#prerequisites)
    * [Steps to Train Proximity Detection Model](#steps-to-train-proximity-detection-model)
        * [Setting Up Data](#setting-up-data)
        * [Training](#training)
    * [Steps to Run Proximity Detection Model](#steps-to-run-proximity-detection-model)
        * [Run Server as a Container](#run-server-as-a-container)
        * [Run Server as a Process](#run-server-as-a-process)
        * [Run Client as a Preocess](#run-client-as-a-preocess)
  * [Face Mask Detection Model](#face-mask-detection-model)
    * [Prerequisites](#prerequisites)
    * [Steps to Train Face Mask Detection Model](#steps-to-train-face-mask-detection-model)
        * [Setting Up Data](#setting-up-data)
        * [Training](#training)
    * [Steps to Run Face Mask Detection Model](#steps-to-run-face-mask-detection-model)
        * [Run Server as a Container](#run-server-as-a-container)
        * [Run Server as a Process](#run-server-as-a-process)
        * [Run Client as a Preocess](#run-client-as-a-preocess)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)


## About The Project
These are developed containerized computer vision models for the detection of people violating health protocols.
We built two computer vision models for the following problems:	
* #### Proximity Sensing and Social Distancing :
    To detect if people within the field of view are maintaining appropriate distance between each other.
* #### Mask Compliance
    To detect if people within the field of view are wearing a face mask.


<!-- GETTING STARTED -->
## Getting Started
* ### Downloading Docker
    [Download](https://www.docker.com/products/docker-desktop) Docker on the system, if you want to run models in a container.

* ### Proximity Detection Model
    * #### Prerequisites :
        When in the vision_models/proximity_detection directory,
        Enter the following line into the terminal -
        ```
            pip install requirements.txt
        ```
    * #### Steps to Train Proximity Detection Model
        * #### Setting Up Data :
            When in the vision_models/proximity_detection directory,
            Enter the following line into the terminal -
            ```
                pip install requirements.txt
            ```
        * #### Training :
            When in the vision_models/proximity_detection directory,
            Enter the following line into the terminal -
            ```
                pip install requirements.txt
            ```
    * #### Steps to Run Proximity Detection Model
        * #### Run Server as a Container
            Once Docker is up and running,
            Open terminal in the vision_models/proximity_detection directory.
            Enter the following line into the terminal -
            ```
                docker container run -p 5001:5001 proximity_detector
            ```
        * #### Run Server as a Process
            Open terminal in the vision_models/proximity_detection/app directory.
            Enter the following line into the terminal -
            ```
                python score.py
            ```
        * #### Run Client as a Preocess
            Open terminal in the vision_models/proximity_detection directory.
            Enter the following line into the terminal -
            ```
                python eval.py
            ```

* ### Face Mask Detection Model
    * #### Prerequisites
        When in the vision_models/face_mask_detection directory,
        Enter the following line into the terminal -
        ```
            pip install requirements.txt
        ```
    * #### Steps to Train Face Mask Detection Model
        * #### Setting Up Data :
            When in the vision_models/proximity_detection directory,
            Enter the following line into the terminal -
            ```
                pip install requirements.txt
            ```
        * #### Training
            When in the vision_models/face_mask_detection directory,
            Enter the following line into the terminal -
            ```
                python train.py
            ```
    * #### Steps to Run Face Mask Detection Model
        * #### Run Server as a Container
            Once Docker is up and running,
            Open terminal in the vision_models/face_mask_detection directory.
            Enter the following line into the terminal -
            ```
                docker container run -p 5000:5000 mask_detector
            ```
        * #### Run Server as a Process
            Open terminal in the vision_models/face_mask_detection/app directory.
            Enter the following line into the terminal -
            ```
                python score.py
            ```
        * #### Run Client as a Preocess
            Open terminal in the vision_models/face_mask_detection directory.
            Enter the following line into the terminal -
            ```
                python eval.py
            ```

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
