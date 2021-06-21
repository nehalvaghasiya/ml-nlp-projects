


# Neural Machine Translation
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
<img src="https://user-images.githubusercontent.com/78668871/122808604-620bc800-d2cd-11eb-87b5-5662fa442f29.PNG" width="450"/> <img src="https://user-images.githubusercontent.com/78668871/122808609-63d58b80-d2cd-11eb-9ef0-d3e7db9f59e4.PNG" width="450"/>




## Overview
- Machine Translation with the help of neural network is very efficient. This project is a translator which translates the German sentence into English sentence. It follows the common sequence-to-sequence learning architecture. It consists of an encoder and a decoder Recurrent Neural Networks (RNN).

## Technical Aspect
- This project is divided into two part:

> 1. Training a Neural Machine translation with seq2seq model in keras.
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
├── app.py
├── model.py
├── Deutsch(German) to Englisch(English) Translation.ipynb
├── deployment_with_flask_app.ipynb
├── requirements.txt
├── Procfile
├── README.md
├── deu_tokenizer.pickle
└── eng_tokenizer.pickle
````

## Setting up the Environment
- To setup the environment (to run globally) - Recommended

> - [x] Open google collab and mount it on your google drive
> - [x] Clone the repo `git clone https://github.com/nehalvaghasiya/Data-Science-Portfolio/tree/main/Natural%20Language%20Processing/Neural%20Machine%20Translation `
> - [x] Upload it to the drive that is being used with google-collab
> - [x] For dataset of german to english translation, send a note over [here](https://github.com/nehalvaghasiya/Data-Science-Portfolio/issues/new)
> - [x] Run the file `"Deutsch(German) to Englisch(English) Translation.ipynb"` to train and test the model, use the model parameters and tokenizer for deployment in `"deployment_with_flask_app.ipynb"`
> - [x] Install flask-ngrok for deployment `pip install flask-ngrok  `
> - [x] For Production deployment, a link will be generated. Navigate to URL which has ending `".ngrok.io"`


- To setup the environment (to run locally)

> - [x] Install pip and Python 3
> - [x] Clone the repo `git clone https://github.com/nehalvaghasiya/Data-Science-Portfolio/tree/main/Natural%20Language%20Processing/Neural%20Machine%20Translation `
> - [x] Navigate to the working directory  `cd Neural Machine Translation`
> - [x] For dataset of german to english translation, send a note over [here](https://github.com/nehalvaghasiya/Data-Science-Portfolio/issues/new)
> - [x] Install pandas  `pip install pandas`
> - [x] Install numpy   `pip install numpy`
> - [x] Install keras   `pip install keras`
> - [x] Install scikit-learn   `pip install sklearn`
> - [x] Install flask-ngrok for deployment `pip install flask-ngrok  `
> - [x] Install the Python dependencies  `pip install -r requirements.txt `
> - [x] Create Machine learning model by running `python model.py `
> - [x] To start Flask API, run  `python app.py `
> - [x] Flask will run on port 5000, Navigate to URL `http://localhost:5000` 





## Bug / Feature Request
- If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/nehalvaghasiya/Data-Science-Portfolio/issues/new) by including your search query and the expected result.
- If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/nehalvaghasiya/Data-Science-Portfolio/issues/new). Please include sample queries and their corresponding results.

## Technologies Used
<img src="https://user-images.githubusercontent.com/78668871/116827827-753acb00-ab9b-11eb-93fb-0aadf41d4ba8.png" width="125"/> <img src="https://user-images.githubusercontent.com/78668871/116829280-c8188080-aba3-11eb-936b-4f13999faa76.png" width="125"/> <img src="https://user-images.githubusercontent.com/78668871/116829376-031ab400-aba4-11eb-8724-d81e2d6a4970.png" width="125"/> <img src="https://user-images.githubusercontent.com/78668871/116829387-1463c080-aba4-11eb-9a08-f1595d2899a8.png" width="125"/> <img src="https://user-images.githubusercontent.com/78668871/121388288-a69d7800-c94b-11eb-9f40-35c4c7b81542.png" width="125"/> <img src="https://user-images.githubusercontent.com/78668871/122805037-df810980-d2c8-11eb-9ad4-9a8c965b919b.png" width="125"/>






