import os
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def mainIndex():
	return render_template('index.html')
	
@app.route('/about')
def mainAbout():
    return render_template('about.html')
    
@app.route('/blog')
def mainBlog():
    return render_template('blog.html')
    
@app.route('/meet')
def mainMeet():
    showMonth = "April"
    isPresent = False;
    shows = {'date': 'April 6-9', 'location': 'The Charlotte Motor Speedway', 'address': '5555 Concord Pkwy S, Concord, NC 28027', 'name': 'Charlotte AutoFair', 'description': 'These events provide collector car Flea Market Vendor spaces to buy and sell restoration parts and supplies for almost any vehicle ever produced - in addition to Car Corral vehicle spaces on the track oval for buying and selling collector vehicles of all descriptions! The collector car Flea Market includes everything automotive, including memorabilia, vintage signs, tires, wheels, automotive toys, restoration supplies, tools, and classic cars for sale!'}
    
    
    return render_template('meet.html', showMonth=showMonth, show=shows, isPres=isPresent)
    
@app.route('/vids')
def mainVids():
    videos = [  {'title': 'Famous GTOs: Walking Dead', 'link': 'hYHYW-vcIMw?start=107&end=155'}, 
                {'title': 'Quarter Mile Action', 'link': 'kEVJV8BFnpw?start=21'}, 
                {'title': 'Nice Example of Restored GTO', 'link': 'HT7bKCTxUhM?start=9'},
                {'title': 'Paul Cangialosi explains Gear Ratios', 'link': 'RyOWKW21I0c'}]
                
    return render_template('vids.html', vids=videos)
# start the server
if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
