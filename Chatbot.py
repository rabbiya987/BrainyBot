from flask import Flask, render_template, request, redirect,url_for #For web developement
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import secrets
import cohere #To interact with Cohere's API
import os

#Getting API from enviromental variables

API=os.getenv('Cohere_API')

#Initializing an instance of Flask
app=Flask(__name__)
app.secret_key=secrets.token_hex(16) #For preventing CSRF

class Form(FlaskForm):
    text=StringField('Enter your message:', validators=[DataRequired()])
    submit=SubmitField('Send')

#Creating global ariable for storing chat history.
chat_history=[]

@app.route('/',methods=['GET','POST']) #Setting a route for root URL allowing GET and POST request

def home():
    global chat_history
    form=Form()
    co=cohere.Client(API) #Initializing cohere client using API 

    if form.validate_on_submit():
        user=form.text.data #Getting input from Form class
        chat_history.append((user,"user")) #Adding input to chat history

        response=co.generate(
            model='command-nightly', #AI model for text generation
            prompt=user,
            max_tokens=300,
            temperature=1, #Controlling tha randomness of output
            k=0, #Diversity of output
            p=0.75,
            stop_sequences=[],
            return_likelihoods='NONE'
        )
        bot_response=response.generations[0].text.strip() #Extract the text from the response object
        chat_history.append((bot_response,"bot")) #Adding response to chat history

        return render_template('temp.html', form=form, messages=chat_history) #Passes the form ad output for display
    return render_template('temp.html', form=form, messages=chat_history)

if __name__=='__main__':
    app.run(debug=True)
