# University of Mary Washington
# Jacques J. Troussard
# Computer Science 350 - Database Applications
# Roxanne Returns Website Project
#
# Best Practices 1: Code that is database specifc
# should be kept in a separate file.

import psycopg2
import psycopg2.extras

from lib.config import *

def ConnectToPostgres():
	connectionString = 'dbname=%s user=%s password=%s host=%s' % (POSTGRES_DATABASE, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST)
	print (connectionString)

	try:
		return psycopg2.connect(connectionString)
	except Exception as e:
		print(type(e))
		print(e)
		print ("Can't connect to database")
		return None

def execute_query(query, conn, select=True, args=None):
	print ("in execute query")
	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	results = None
	try:
		quer = cur.mogrify(query, args)
		cur.execute(quer)
		if select:
			results = cur.fetchall()
		conn.commit()
	except Exception as e:
		conn.rollback()
		print(type(e))
		print(e)
	cur.close()
	return results

def add_member(rqst_fname, rqst_lname, rqst_email, rqst_year, rqst_model):
	conn = ConnectToPostgres();
	if conn == None:
		return None

	query_string = "INSERT INTO members (first_name, last_name, email, year, model) VALUES (%s, %s, %s, %s, %s)"
	execute_query(query_string, conn, select=False, args=(rqst_fname, rqst_lname, rqst_email, rqst_year, rqst_model))
	conn.commit()
	conn.close()
	return 0

def get_member_list():
	conn = ConnectToPostgres();
	if conn == None:
		return None

	query_string = "SELECT * FROM members"
	results = execute_query(query_string, conn)
	conn.close()
	return results


