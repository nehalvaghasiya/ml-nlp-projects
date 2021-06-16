

# Click_on_Ad_or_not
## Table of Content

- Demo
- Overview
- Technical Aspect
- Deployement on Virtual machine provided by google-collab with the help of flask-ngrok
- Directory Tree
- Setting up the Environment
- Bug / Feature Request
- Technologies Used


## Demo
<img src="https://user-images.githubusercontent.com/78668871/122223469-7a39ac80-ceb3-11eb-86fe-9231f2b99962.PNG" width="450"/> <img src="https://user-images.githubusercontent.com/78668871/122223475-7b6ad980-ceb3-11eb-81e1-8a5140d2d0f5.PNG" width="450"/>




## Overview
- This is a Logistic Regression model. The trained model takes five parameters (Daily Time Spent on Site, Age, Area Income, Daily Internet Usage, Male(if its make then enter 1, otherwise 0)) as input and predict whether user has clicked on Ad or not.

## Technical Aspect
- This project is divided into two part:

> 1. Training a Logistic Regression model.
> 2. Building and hosting a Flask web app on Virtual machine provided by google-collab with the help of flask-ngrok(to make the server accessible outside the runtime globally on HTTP).

## Deployement on Virtual machine provided by google-collab with the help of flask-ngrok 
<img src="https://user-images.githubusercontent.com/78668871/116829747-e5e6e500-aba5-11eb-921a-6174e199bacf.png" width="500" align="right"/>
- Google Colab provides a VM(virtual machine) so we cannot access the localhost(all it does it route it to our local machine’s localhost) as we do on our local machine when running a local web server. What we can do is expose it to a public URL using ngrok. 



- Here comes the Python library flask-ngrok.
- Install flask-ngrok in google-collab and import run_with_ngrok. That's it.

`!pip install flask-ngrok`

`from flask_ngrok import run_with_ngrok`

## Directory Tree
```
├── static
│   ├── styles
│   │   ├── style.css
├── templates
│   ├── home.html
├── advertising.csv
├── app.py
├── model.py
├── click_on_Ad_or_not.ipynb
├── deployment_with_flask_app.ipynb
├── requirements.txt
├── Procfile
├── README.md
└── ads_model.pkl
````

## Setting up the Environment
- To setup the environment (to run globally) - Recommended

> - [x] Open google collab and mount it on your google drive
> - [x] Clone the repo `git clone https://github.com/nehalvaghasiya/Data-Science-Portfolio/tree/main/Machine%20Learning/Classification/Decision%20Tree%20Classification/click_on_Ad_or_not `
> - [x] Upload it to the drive that is being used with google-collab
> - [x] Run the file `"click_on_Ad_or_not.ipynb"` to train and test the model, use the model parameters for deployment in `"deployment_with_flask_app.ipynb"`
> - [x] Install flask-ngrok for deployment `pip install flask-ngrok  `
> - [x] For Production deployment, a link will be generated. Navigate to URL which has ending `".ngrok.io"`


- To setup the environment (to run locally)

> - [x] Install pip and Python 3
> - [x] Clone the repo `git clone https://github.com/nehalvaghasiya/Data-Science-Portfolio/tree/main/Machine%20Learning/Classification/Decision%20Tree%20Classification/click_on_Ad_or_not `
> - [x] Navigate to the working directory  `cd click_on_Ad_or_not`
> - [x] Install pandas  `pip install pandas`
> - [x] Install numpy   `pip install numpy`
> - [x] Install matplotlib   `pip install matplotlib`
> - [x] Install flask-ngrok for deployment `pip install flask-ngrok  `
> - [x] Install the Python dependencies  `pip install -r requirements.txt `
> - [x] Create Machine learning model by running `python model.py `
> - [x] To start Flask API, run  `python app.py `
> - [x] Flask will run on port 5000, Navigate to URL `http://localhost:5000` 





## Bug / Feature Request
- If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/nehalvaghasiya/Data-Science-Portfolio/issues/new) by including your search query and the expected result.
- If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/nehalvaghasiya/Data-Science-Portfolio/issues/new). Please include sample queries and their corresponding results.

## Technologies Used
<img src="https://user-images.githubusercontent.com/78668871/116827827-753acb00-ab9b-11eb-93fb-0aadf41d4ba8.png" width="125"/> <img src="https://user-images.githubusercontent.com/78668871/116829280-c8188080-aba3-11eb-936b-4f13999faa76.png" width="125"/> <img src="https://user-images.githubusercontent.com/78668871/116829376-031ab400-aba4-11eb-8724-d81e2d6a4970.png" width="125"/> <img src="https://user-images.githubusercontent.com/78668871/116829387-1463c080-aba4-11eb-9a08-f1595d2899a8.png" width="125"/> <img src="https://user-images.githubusercontent.com/78668871/121388288-a69d7800-c94b-11eb-9f40-35c4c7b81542.png" width="125"/>

