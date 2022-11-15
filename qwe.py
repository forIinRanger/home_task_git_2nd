import sqlite3

con = sqlite3.connect('coffee.sqlite')

cur = con.cursor()

result = cur.execute("""SELECT * FROM coffee_table""").fetchall()
print(result)

con.close()