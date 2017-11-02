from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    with open('static/county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('index.html',getStateOptions(counties))

def getStateOptions(counties):
    ret = ""
    for i in counties:
        ret += Markup("<option value=\"" + i[State] + "\">" + i[State] + "</option>")
    return ret

#@app.route("/response")
#def render_response():
#        ins = float(request.args['inches'])
#        #The request object stores information that was sent by the client to the server.
#        #the args is a multidict
#        #the way we get info from args is that it is visible in a url. - the information in args is visible in the url for hte page being requested(ex. .../response?color=blue)
#        res = str(ins*2.54)
#        return render_template('response.html', their = request.args['inches'], response = res)

