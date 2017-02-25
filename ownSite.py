from flask import Flask, render_template
from flask import request
from datetime import datetime

import csv
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('homepage.html')
	
@app.route('/comments')
def comments():
	commentFile='static\\comments.csv'
	commentBook=readFile(commentFile)

	return render_template('comments.html', aList = commentBook )

@app.route('/contact')
def contact():
	return render_template('contact_details.html')	

@app.route('/facilities')
def facilities():
	return render_template('facilities.html')
	
@app.route('/gallery')
def gallery():
	return render_template('gallery.html')

@app.route('/details')
def details():
	return render_template('hotel_details.html')

@app.route('/attractions')
def attractions():
	return render_template('local_activities_attractions.html')

@app.route('/rooms')
def rooms():
	return render_template('rooms.html')

@app.route('/directions')
def directions():
	return render_template('directions.html')	

@app.route('/booking')
def booking():
	bookingFile='static\\bookings.csv'
	bookingBook=readFiles(bookingFile)
	
	confirmedd=[]
	for row in bookingBook:
			for field in row:
				if field == 'confirmed':
					for field in row:
						if field=='room3':
							cost1=int(row[4])*60
						if field=='room2':
							cost1=int(row[4])*40
						if field=='room1':
							cost1=int(row[4])*25
					cost= str(cost1)
					confentry=[row[2],row[3],'total cost:'+'' + cost, row[6]]
					confirmedd.append(confentry)
					
	return render_template('booking.html', aList = confirmedd)	
	

	
@app.route('/addComment', methods =['POST'])
def addComment():
	
	commentFile='static\\comments.csv'
	commentBook=readFile(commentFile)
	
	newname=request.form[('name')]
	newcomment=request.form[('comment')]
	
	if newname=='':
		newname= 'Unknown'
	
	if newcomment !='':
		text='   says:'
		time = datetime.now().strftime("%d/%m/%Y")
	
		newEntry=[newname + text, newcomment,time]
		commentBook.append(newEntry)
	
		writeFile(commentBook, commentFile)
	
	return render_template('comments.html', aList = commentBook )

def readFile(file):	
	with open('static\\comments.csv', 'r') as inFile:
		reader=csv.reader(inFile)
		aList=[row for row in reader]	
	return aList

def writeFile(commentBook, commentFile):	
	with open('static\\comments.csv', 'w', newline='') as outFile:
		writer=csv.writer(outFile)
		writer.writerows(commentBook)	
	return


	
	
@app.route('/addBooking', methods =['POST'])
def addBooking():
	
	bookingFile='static\\bookings.csv'
	bookingBook=readFiles(bookingFile)
	
	confirmedd=[]
	for row in bookingBook:
			for field in row:
				if field == 'confirmed':
					for field in row:
						if field=='room3':
							cost1=int(row[4])*60
						if field=='room2':
							cost1=int(row[4])*40
						if field=='room1':
							cost1=int(row[4])*25
					cost= str(cost1)
					confentry=[row[2],row[3],'total cost:'+'' + cost, row[6]]
					confirmedd.append(confentry)
	
			
	
	newname=request.form[('name')]
	newemail=request.form[('email')]
	newarrival=request.form[('arrival')]
	newdeparture=request.form[('departure')]
	room=request.form[('room')]
	
	arrival = datetime.strptime(newarrival, "%d/%m/%y").date()
	departure = datetime.strptime(newdeparture, "%d/%m/%y").date()
	
	totaldays = int(abs(departure - arrival).days)
	
	if (newname !='' and newemail !='' and newarrival !='' and newdeparture !='' and room!=''):
		status = 'unconfirmed'	
		newEntry=[newname, newemail, arrival, departure, totaldays, room, status]
		bookingBook.append(newEntry)
	
		writeFiles(bookingBook, bookingFile)
	
	return render_template('booking.html', aList = confirmedd)

def readFiles(file):	
	with open('static\\bookings.csv', 'r') as inFile:
		reader=csv.reader(inFile)
		aList=[row for row in reader]	
	return aList


def writeFiles(commentBook, commentFile):	
	with open('static\\bookings.csv', 'w', newline='') as outFile:
		writer=csv.writer(outFile)
		writer.writerows(commentBook)	
	return	
	
	

if __name__ == '__main__':
	app.run(debug = True)