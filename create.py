
import sqlite3

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table

# c.execute("""CREATE TABLE addresses (
# 		first_name text,
# 		last_name text,
# 		address text,
# 		city text,
# 		state text,
# 		zipcode integer
# 		)""")
# conn.commit()		

# c.execute(""" insert into addresses values ('john123','john123','john134','john','john','1234')
# 		""")
# c.execute(
# 	"""INSERT INTO addresses (first_name) VALUES ("Geek6")""")
# conn.commit()	


# to select all column we will use
statement = '''SELECT * FROM addresses'''

c.execute(statement)

print("All the data")
output = c.fetchall()
for row in output:
    print(row)

conn.commit()

