import os
import psycopg2
import psycopg2.extras

from lib.config import *
from lib import data_postgresql as pg

from flask import Flask, render_template, request, session

app = Flask(__name__)

app.secret_key = os.urandom(24).encode('hex')

members = [{}]
logged = False;


@app.route('/', methods=['GET', 'POST'])
def mainIndex():
    if request.method == 'POST':
        login_result = pg.login_member(request.form['fn'], request.form['pass']);
        print ("************ printing login results =======> ")
        print (login_result)
        print (type(login_result))

        if (login_result!=None):
            session['username'] = login_result[0][1] + login_result[0][2]
            session['userlast'] = login_result[0][2]
        else:
            user = ['', '']
            return render_template('login.html', selected='', error=True, user=user)
            
    if 'username' in session:
        user = [session['username'], session['userlast']]
        logged = True;
    else:
        user = ['', '']
        logged = False;

    return render_template('index.html', selected='home', user=user, logged=logged)


@app.route('/error')
def mainError():
    return render_template('error.html')


@app.route('/about')
def mainAbout():
    if 'username' in session:
        user = [session['username'], session['userlast']]
    else:
        user = ['', '']

    return render_template('about.html', selected='about', user=user)


@app.route('/blog')
def mainBlog():
    if 'username' in session:
        user = [session['username'], session['userlast']]
    else:
        user = ['', '']

    return render_template('blog.html', selected='blog', user=user)


@app.route('/meet')
def mainMeet():
    showMonth = "April"
    isPresent = False
    shows = {'date': 'April 6-9', 'location': 'The Charlotte Motor Speedway', 'address': '5555 Concord Pkwy S, Concord, NC 28027', 'name': 'Charlotte AutoFair',
             'description': 'These events provide collector car Flea Market Vendor spaces to buy and sell restoration parts and supplies for almost any vehicle ever produced - in addition to Car Corral vehicle spaces on the track oval for buying and selling collector vehicles of all descriptions! The collector car Flea Market includes everything automotive, including memorabilia, vintage signs, tires, wheels, automotive toys, restoration supplies, tools, and classic cars for sale!'}
    if 'username' in session:
        user = [session['username'], session['userlast']]
    else:
        user = ['', '']
    return render_template('meet.html', selected='meet', showMonth=showMonth, show=shows, isPres=isPresent, user=user)


@app.route('/form', methods=['GET', 'POST'])
def mainForm():
    if request.method == 'POST':
        members.append({'first': request.form['first'], 'last': request.form[
                       'last'], 'year': request.form['year'], 'model': request.form['model']})
    if 'username' in session:
        user = [session['username'], session['userlast']]
    else:
        user = ['', '']

    return render_template('form.html', selected='form', members=members, user=user)


@app.route('/form2', methods=['POST'])
def reply():
    thename = request.form['first']
    if 'username' in session:
        user = [session['username'], session['userlast']]
    else:
        user = ['', '']

    """Returns a list of members in the database"""
    print("printing request.form")
    print(request.form)
    insert_result = pg.add_member(request.form['first'], request.form[
                                  'last'], request.form['email'], request.form['zip'], request.form['year'], request.form['model'], request.form['pass'])
    if insert_result == None:
        print("There was an error executing insert command")
        return render_template('error.html')
    else:
        print("Member add to database SUCCESSFUL")
        select_results = pg.get_member_list()
    if select_results == None:
        print("There was an error executing select command")
        return render_template('error.html')
    else:
        print("Member list return SUCCESSFUL")
        return render_template('form2.html', name=thename, members_list=select_results, user=user)


@app.route('/vids')
def mainVids():
    if 'username' in session:
        user = [session['username'], session['userlast']]
    else:
        user = ['', '']
    videos = [{'title': 'Famous GTOs: Walking Dead', 'link': 'hYHYW-vcIMw?start=107&end=155'},
              {'title': 'Quarter Mile Action', 'link': 'kEVJV8BFnpw?start=21'},
              {'title': 'Nice Example of Restored GTO',
               'link': 'HT7bKCTxUhM?start=9'},
              {'title': 'Paul Cangialosi explains Gear Ratios', 'link': 'RyOWKW21I0c'}]

    return render_template('vids.html', selected='vids', vids=videos, user=user)
    
@app.route('/login')
def mainLogin():
    error = False
    if 'username' in session:
        user = [session['username'], session['userlast']]
    else:
        user = ['', '']

    return render_template('login.html', selected='form', user=user)
    
@app.route('/dashboard')
def mainDash():
    selection = request.form["dash_option"]
    print (selection)
    if selection == "Search":
        return render_template('market.html', user=user)
    else:
        return render_template('market_post.html', user=user)
    return render_template('dashboard.html,' user=user)

@app.route('/market' methods='GET')
def mainMarket():
    #configuration variable convention
    # 1) borders - int
    # 2) header_01 - String
    # 3) header_02 - String
    config_values = {'borders':0, 'header_01':"", 'header_02':""};

    if (methods='GET') {
    config_values = {'borders':3, 'header_01':"Description", 'header_02':"Price"};
    
    }
    
    return render_template('/market', user=user, config=config_values,  )


# start the server
if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
