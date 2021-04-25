
# H1
## H2
### H3

**bold text**

*italicized text*

> blockquote
> 
- First item
- Second item
- Third item

[title](https://www.example.com)

![alt text](image.jpg)

### My Great Heading {#custom-id}

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

term
: definition




# CO2 emission prediction
## Table of Content

- Demo
- Overview
- Technical Aspect
- Installation
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

## Installation
- The Code is written in Python 3.7. If you don't have Python installed you can find it here. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:

> `pip install -r requirements.txt`

## Deployement on Virtual machine provided by google-collab with the help of flask-ngrok
- Google Colab provides a VM(virtual machine) so we cannot access the localhost(all it does it route it to our local machine’s localhost) as we do on our local machine when running a local web server. What we can do is expose it to a public URL using ngrok. Here comes the Python library flask-ngrok.
- install flask-ngrok in google-collab and import run_with_ngrok. That's it.

`!pip install flask-ngrok`

`from flask_ngrok import run_with_ngrok`
``
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

```
├── app 
│   ├── __init__.py
│   ├── main.py
│   ├── model
│   ├── static
│   └── templates
├── config
│   ├── __init__.py
├── processing
│   ├── __init__.py
├── requirements.txt
├── runtime.txt
├── LICENSE
├── Procfile
├── README.md
└── wsgi.py
````

## Bug / Feature Request
- If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/nehalvaghasiya/Data-Science-Portfolio/issues/new) by including your search query and the expected result.
- If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/nehalvaghasiya/Data-Science-Portfolio/issues/new). Please include sample queries and their corresponding results.

## Technologies Used
## Team
## Credits
