from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

with open("county_demographics.json") as demographics_data:
        counties = json.load(demographics_data)

@app.route("/")
def render_main():
    return render_template('index.html',val = getStateOptions(counties))

def getStateOptions(counties):
    ret = ""
    lis = {"doestmantter":True}
    for i in counties:
        if not(i["State"] in lis):
            ret += Markup("<option value=\"" + i['State'] + "\">" + i['State'] + "</option>")
            lis[i['State']] = True
    return ret

@app.route("/response")
def render_response():
        ins = request.args['state']
        x = 0
        for i in counties:
                if i['State'] == ins:
                        x += i['Population']['2014 Population']
        y = "The populatin of all the counties in " + ins + " is: " + str(x)
        #The request object stores information that was sent by the client to the server.
        #the args is a multidict
        #the way we get info from args is that it is visible in a url. - the information in args is visible in the url for hte page being requested(ex. .../response?color=blue)
        return render_template('response.html', val = getStateOptions(counties), funfact = y  )

