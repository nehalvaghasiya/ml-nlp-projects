
# CO2 emission prediction
## Table of Content

- Demo
- Overview
- Technical Aspect
- Deployement on Virtual machine provided by google-collab with the help of flask-ngrok
- Directory Tree
- Setting up the Environment
- Bug / Feature Request
- Technologies Used
- Team
- Credits

## Demo
<img src="https://user-images.githubusercontent.com/78668871/116970610-9513e100-acb8-11eb-8243-deed302aafdf.PNG" width="450"/> <img src="https://user-images.githubusercontent.com/78668871/116970609-947b4a80-acb8-11eb-8ef2-eba7d9c5262d.PNG" width="450"/>



## Overview
- This is a simple Linear regresion model. The trained model takes three parameters (Engine size, number of cylinders, fuel comsumption) as input and predict the co2 emissions(g/km) based on that.

## Technical Aspect
- This project is divided into two part:

> 1. Training a Linear regression model.
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
├── CO2 Emissions_Canada.csv
├── app.py
├── model.py
├── co2 emission linear regression.ipynb
├── deployment_with_flask_app.ipynb
├── requirements.txt
├── Procfile
├── README.md
└── co2_model.pkl
````

## Setting up the Environment
- To setup the environment (to run globally) - Recommended

> - [x] Open google collab and mount it on your google drive
> - [x] Clone the repo `git clone https://github.com/nehalvaghasiya/Data-Science-Portfolio/tree/main/Machine%20Learning/Regression/Linear%20Regression/CO2%20emission%20prediction `
> - [x] Upload it to the drive that is being used with google-collab
> - [x] Run the file `"co2 emission linear regression.ipynb"` to train and test the model, use the model parameters for deployment in `"deployment_with_flask_app.ipynb"`
> - [x] Install flask-ngrok for deployment `pip install flask-ngrok  `


-To setup the environment (to run locally)

> - [x] Install pip and Python 3
> - [x] Clone the repo `git clone https://github.com/nehalvaghasiya/Data-Science-Portfolio/tree/main/Machine%20Learning/Regression/Linear%20Regression/CO2%20emission%20prediction `
> - [x] Navigate to the working directory  `cd CO2 emission prediction`
> - [x] Install pandas  `pip install pandas`
> - [x] Install numpy   `pip install numpy`
> - [x] Install matplotlib   `pip install matplotlib`
> - [x] Install flask-ngrok for deployment `pip install flask-ngrok  `
> - [x] Install the Python dependencies  `pip install -r requirements.txt `





## Bug / Feature Request
- If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/nehalvaghasiya/Data-Science-Portfolio/issues/new) by including your search query and the expected result.
- If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/nehalvaghasiya/Data-Science-Portfolio/issues/new). Please include sample queries and their corresponding results.

## Technologies Used
<img src="https://user-images.githubusercontent.com/78668871/116827827-753acb00-ab9b-11eb-93fb-0aadf41d4ba8.png" width="125"/> <img src="https://user-images.githubusercontent.com/78668871/116829280-c8188080-aba3-11eb-936b-4f13999faa76.png" width="125"/> <img src="https://user-images.githubusercontent.com/78668871/116829376-031ab400-aba4-11eb-8724-d81e2d6a4970.png" width="125"/> <img src="https://user-images.githubusercontent.com/78668871/116829387-1463c080-aba4-11eb-9a08-f1595d2899a8.png" width="125"/>
