import sqlite3
conn=sqlite3.connect('bank-query-sf.db')
c=conn.cursor()
def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS database(acc_no REAL,employee_name TEXT,acc_balance REAL,last_deposit_amt REAL,last_withdrawal_amt REAL)")

def data_entry(a,b,e,f,g):
	c.execute("INSERT INTO database VALUES(?,?,?,?,?)",(a,b,e,f,g))
	conn.commit()
	#c.close()
	#conn.close()

create_table()

data_entry(98794567,'Arka Mukherjee',134000,45000,70000)


data_entry(87094567,'Rounak Das',105000,34000,67000)

