# acessando databases com python utilizando DB-API
from MySQLdb import connect

# create a connection object
connection = connect('databasename', 'username', 'pwsd')

# create a cursor object
cursor = connection.cursor()

# run queries
cursor.execute('selecct * from mytable')
results = cursor.fetchall()

# free resources
cursor.close()
connection.close()
