# Chatbot Deployment with Flask and JavaScript

This gives 2 deployment options:

- Deploy within Flask app with jinja2 template
- Serve only the Flask prediction API. The used html and javascript files can be included in any Frontend application (with only a slight modification) and can run completely separate from the Flask App then.

## Initial Setup

This repo currently contains the starter files.

Clone repo and create a virtual environment

```
git clone https://github.com/TuhinB10/college-enquiry-ai-assistant.git
cd college-enquiry-ai-assistant
python3 -m venv venv
. venv/bin/activate
```

Install dependencies

```
(venv) pip install -r requirements.txt
```

Install nltk package

```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt_tab')
```

Modify `intents.json` with different intents and responses for your Chatbot

Run

```
(venv) python train.py
```

This will dump data.pth file. And then run
the following command to test it in the console.

```
(venv) python chat.py
(venv) python app.py
(venv) python -m http.server -d standalone-frontend 8000
```
