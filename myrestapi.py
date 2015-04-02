import json
import bottle
from bottle import route, run, request, abort
from pymongo import Connection
from json import JSONEncoder
import datetime
import time
import mysql.connector
import collections
import datetime


connection = Connection('localhost', 27017)
db = connection.admin

cnx = mysql.connector.connect(user='root',database='cmpe273',passwd='root')

rowarray_list = []
 
@route('/shirt/:id', method='GET')
def get_document(id):
   entity = db['quiz4'].find_one({'shirtId':id})
   entity["_id"] = str(entity["_id"])
   if not entity:
			abort(404, 'No document with id %s' % id)
   return entity

@route('/shirts', method='POST')
def put_document():
    data = request.body.read()
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    entity['date']=time.strftime("%x")
    try:
        db['quiz4'].save(entity)
    except ValidationError as ve:
        abort(400, str(ve))
     
@route('/shirts', method='PUT')
def get_doc():
  
   data = request.body.read()
   if not data:
        abort(400, 'No data received')
   entity = json.loads(data)
   entity2 = db['quiz4'].find_one({'shirtId':entity["shirtId"]})
   db['quiz4'].update({"_id": entity2["_id"]}, {"$set": entity}, upsert = True)
  
@route('/shirts/:id', method='PUT')
def get_doc(id):
  
   data = request.body.read()
   if not data:
        abort(400, 'No data received')
   entity = json.loads(data)
   entity2 = db['quiz4'].find_one({'shirtId':entity["shirtId"]})
   db['quiz4'].update({"_id": entity2["_id"]}, {"$set": entity}, upsert = True)

@route('/shirts', method='DELETE')
def get_doc():
   data = request.body.read()
   if not data:
        abort(400, 'No data received')
   entity = json.loads(data)
   entity3 = db['quiz4'].remove({'shirtId':entity["shirtId"]})
   return "Shoe-",entity["shirtId"]," is deleted!\n"

@route('/shirts/:id', method='DELETE')
def get_doc(id):
   data = request.body.read()
   if not data:
        abort(400, 'No data received')
   entity = json.loads(data)
   entity3 = db['quiz4'].remove({'shirtId':entity["shirtId"]})
   return "Shoe-",entity["shirtId"]," is deleted!\n"


@route('/shoe/:id',method="GET")
def get_shoe(id):
	cursor = cnx.cursor()
	query = "select * from product where shoeId="+id
	hire_start = datetime.date(1999, 1, 1)
	hire_end = datetime.date(1999, 12, 31)
	cursor.execute(query)
	rows = cursor.fetchall()
	data = {}
	for row in rows:
		data['shoeId'] = row[0]
		data['shoeName'] = row[1]
		data['shoeQuantity'] = row[2]
		data['createdBy'] = row[3]
		data['date'] = str(row[4])
				
	json_string = json.dumps(data)
	return json_string

@route('/shoes',method="POST")
def get_shoe():
 data = request.body.read()
 entity = json.loads(data)
 cursor = cnx.cursor()	
 now = datetime.datetime.now()
 add_salary = (
		 "INSERT INTO product (shoeId, shoeName, shoeQuantity, createdBy, date) VALUES (%(shoieId)s, %(shoeName)s, %(shoeQuantity)s, %(createdBy)s, %(date)s)")
 data_salary = {'shoieId': entity["shoeId"],'shoeName': entity["shoeName"],'shoeQuantity': entity["shoeQuantity"],'createdBy': entity["createdBy"],'date':now.isoformat()}
 cursor.execute(add_salary, data_salary)
 cnx.commit()
 cursor.close()

 
@route('/shoes',method="PUT")
def get_shoe():
 data = request.body.read()
 entity = json.loads(data)
 cursor = cnx.cursor()	
 add_salary = (
		 "update product set shoeName =  %(shoeName)s, shoeQuantity = %(shoeQuantity)s, createdBy =  %(createdBy)s where shoeId=%(id)s")
 data_salary = {'shoeName': entity["shoeName"],'shoeQuantity': entity["shoeQuantity"],'createdBy': entity["createdBy"], 'id':entity["shoeId"]}
 cursor.execute(add_salary, data_salary)
 cnx.commit()
 cursor.close()


@route('/shoes/:id',method="PUT")
def get_shoe():
 data = request.body.read()
 entity = json.loads(data)
 cursor = cnx.cursor()	
 add_salary = (
		 "update product set shoeName =  %(shoeName)s, shoeQuantity = %(shoeQuantity)s, createdBy =  %(createdBy)s where shoeId=%(id)s")
 data_salary = {'shoeName': entity["shoeName"],'shoeQuantity': entity["shoeQuantity"],'createdBy': entity["createdBy"], 'id':entity["shoeId"]}
 cursor.execute(add_salary, data_salary)
 cnx.commit()
 cursor.close()




@route('/shoes',method="DELETE")
def get_shoe():
 data = request.body.read()
 entity = json.loads(data)
 cursor = cnx.cursor()	
 add_salary = (
		 "delete from product where shoeId=%(id)s")
 data_salary = {'id':entity["shoeId"]}
 cursor.execute(add_salary, data_salary)
 cnx.commit()
 cursor.close()



@route('/shoes/:id',method="DELETE")
def get_shoe():
 data = request.body.read()
 entity = json.loads(data)
 cursor = cnx.cursor()	
 add_salary = (
		 "delete from product where shoeId=%(id)s")
 data_salary = {'id':entity["shoeId"]}
 cursor.execute(add_salary, data_salary)
 cnx.commit()
 cursor.close()
 cnx.close()




run(host='0.0.0.0', port=8080)


