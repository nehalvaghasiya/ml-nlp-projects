

# CO2 emission prediction
## Table of Content

- Demo
- Overview
- Technical Aspect
- Run
- Deployement on Virtual machine provided by google-collab with the help of flask-ngrok
- Directory Tree
- Bug / Feature Request
- Technologies Used
- Team
- Credits

## Demo
![alt text](image.jpg)

## Overview
- This is a simple Linear regresion model. The [trained model](https://www.example.com) takes three parameters (Engine size, number of cylinders, fuel comsumption) as input and predict the co2 emissions(g/km) based on that.

## Technical Aspect
- This project is divided into two part:

> 1. Training a Linear regression model.
> 2. Building and hosting a Flask web app on Virtual machine provided by google-collab with the help of flask-ngrok.


## Deployement on Virtual machine provided by google-collab with the help of flask-ngrok
- Google Colab provides a VM(virtual machine) so we cannot access the localhost(all it does it route it to our local machine’s localhost) as we do on our local machine when running a local web server. What we can do is expose it to a public URL using ngrok. Here comes the Python library flask-ngrok.
- install flask-ngrok in google-collab and import run_with_ngrok. That's it.

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
├── requirements.txt
├── Procfile
├── README.md
└── co2_model.pkl
````



## Bug / Feature Request
- If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/nehalvaghasiya/Data-Science-Portfolio/issues/new) by including your search query and the expected result.
- If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/nehalvaghasiya/Data-Science-Portfolio/issues/new). Please include sample queries and their corresponding results.

## Technologies Used
![1200px-Scikit_learn_logo_small svg](https://user-images.githubusercontent.com/78668871/116827827-753acb00-ab9b-11eb-93fb-0aadf41d4ba8.png)
