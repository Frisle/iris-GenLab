# Summary
IRIS-GenLab is a generative AI Application that leverages the functionality of Flask web framework, SQLALchemy ORM, and InterSystems IRIS. 
The application contains user registration and authentication with the help of Flask-Login python library, a responsive user interface to create and edit posts.

# Application layout
![main](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/9cd462a5-920f-4d0d-9c8f-604468ca8244)

# Features
* User registration and authentication
* Named entity recognition (NER), natural language processing (NLP) method for text information extraction
* Sentiment analysis, NLP approch that identifies the emotional tone of the message 
* HuggingFace Text generation with the help of GPT2 LLM (Large Language Model) model and Hugging Face pipeline
* Google PALM API, to access the advanced capabilities of Google's large language models (LLM) like PaLM2
* Google Flan-T5 XXL, a fine-tuned on a large corpus of text data that was not filtered for explicit contents.
* OpenAI is a private research laboratory that aims to develop and direct artificial intelligence (AI)

# Used Technologies
Flask: A micro web framework for Python that allows you to build web applications quickly and efficiently.Conduit.

SQLAlchemy: An Object-Relational Mapping (ORM) library that provides a high-level, Pythonic interface for interacting with databases.

InterSystems IRIS: A high-performance, data platform that combines a powerful database with integration, analytics, and AI capabilities.


# Installation
1. Clone/git pull the repo into any local directory

```
git clone https://github.com/mwaseem75/iris-GenLab.git
```

2. Open a Docker terminal in this directory and run:

```
docker-compose build
```

3. Run the IRIS container:

```
docker-compose up -d 
```

# Required Keys
## HuggingFace
  from hugging face
## Google Palm Api
  from google palm Api
## OpenAI
  from open AI


# Getting Started 
## Run the application
To run the application Navigate to [**http://localhost:4040**](http://localhost:4040) 
#### Home Page
![image](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/a484538b-1fb7-435c-9254-25f1dc6b8c92)

#### Register a User
To register a user, Click on Sign Up link
![image](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/acf3e68b-cf2d-4ce1-9997-b4b648ec845f)

Once registered, the user will log in automatically, To sign out click on the User Name link and then click on Sign out.
In order to log in, click on sign in link
![image](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/047f88dd-db3d-45d3-ba57-d7d83a30e6d8)

#### Named entity recognition (NER)
#### Sentiment analysis
#### HuggingFace, Text generation (Gpt-2)
#### Google PALM API
#### Google Flan-T5 XXL
#### OpenAI


## Application database
SQLALchemy will create below table:

* user: To store User information

To view table details, navigate to 
[**http://localhost:52775/csp/sys/exp/%25CSP.UI.Portal.SQL.Home.zen?$NAMESPACE=USER#**](http://localhost:52775/csp/sys/exp/%25CSP.UI.Portal.SQL.Home.zen?$NAMESPACE=USER#)
![image](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/de303374-af23-40cc-874b-cad560ca1a87)


## Special Thanks to:
Evgeny Shvarov for: [iris-embedded-python-template](https://openexchange.intersystems.com/package/iris-embedded-python-template) template for guidance
