import os
import psycopg2
import psycopg2.extras

from lib.config import *
from lib import data_postgresql as pg

from flask import Flask, render_template, request

app = Flask(__name__)

members = [{}]

@app.route('/')
def mainIndex():
	return render_template('index.html', selected='home')

@app.route('/error')
def mainError():
	return render_template('error.html')
	
@app.route('/about')
def mainAbout():
    return render_template('about.html', selected='about')
    
@app.route('/blog')
def mainBlog():
    return render_template('blog.html', selected='blog')
    
@app.route('/meet')
def mainMeet():
    showMonth = "April"
    isPresent = False;
    shows = {'date': 'April 6-9', 'location': 'The Charlotte Motor Speedway', 'address': '5555 Concord Pkwy S, Concord, NC 28027', 'name': 'Charlotte AutoFair', 'description': 'These events provide collector car Flea Market Vendor spaces to buy and sell restoration parts and supplies for almost any vehicle ever produced - in addition to Car Corral vehicle spaces on the track oval for buying and selling collector vehicles of all descriptions! The collector car Flea Market includes everything automotive, including memorabilia, vintage signs, tires, wheels, automotive toys, restoration supplies, tools, and classic cars for sale!'}
    return render_template('meet.html', selected='meet', showMonth=showMonth, show=shows, isPres=isPresent)

@app.route('/form', methods=['GET', 'POST'])
def mainForm():
    if request.method == 'POST':
        members.append({'first': request.form['first'], 'last': request.form['last'], 'year': request.form['year'], 'model': request.form['model']})
    return render_template('form.html', selected='form', members=members)
    
@app.route('/form2', methods=['POST'])
def reply():
    thename=request.form['first']
    
    """Returns a list of members in the database"""
    print(request.form)
    insert_result = pg.add_member(request.form['first'], request.form['last'], request.form['email'], request.form['year'], request.form['model'])
    if insert_result == None:
        print ("There was an error executing insert command")
        return render_template('error.html')
    else:
        print ("Member add to database SUCCESSFUL")
        select_results = pg.get_member_list()
    if select_results == None:
        print("There was an error executing select command")
        return render_template('error.html')
    else:
        print ("Member list return SUCCESSFUL")
        return render_template('form2.html', name=thename, members_list=results)
    
@app.route('/vids')
def mainVids():
    videos = [  {'title': 'Famous GTOs: Walking Dead', 'link': 'hYHYW-vcIMw?start=107&end=155'}, 
                {'title': 'Quarter Mile Action', 'link': 'kEVJV8BFnpw?start=21'}, 
                {'title': 'Nice Example of Restored GTO', 'link': 'HT7bKCTxUhM?start=9'},
                {'title': 'Paul Cangialosi explains Gear Ratios', 'link': 'RyOWKW21I0c'}]
                
    return render_template('vids.html', selected='vids', vids=videos)
# start the server
if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
