import sqlite3
conn=sqlite3.connect('bank-query-sf.db')
c=conn.cursor()
def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS account_balance_enquiry(no_of_question REAL,query TEXT,answer TEXT, require TEXT)")

def data_entry(a,b,e,f):
	c.execute("INSERT INTO account_balance_enquiry VALUES(?,?,?,?)",(a,b,e,f))
	conn.commit()
	#c.close()
	#conn.close()

create_table()
data_entry(36, 'check my account balance || show my balance || how much money in my  account? || Tell me how much money is there in my account || how much money do i have in my account? || Can you show me my balance? || check my balance || how much money do i have? || available balance in my account || balance || how much money in my current account || how much money in my savings account || can you check my  account current balance as well? || can you check my savings account balance as well? || and for current || and for savings || Can you show me my balance in current account? || Can you show me my balance in savings account? || how much money do i have in my current account? || how much money do i have in my savings account? || available balance in my current account || available balance in my savings account || show available money in my current account || show available money in my savings account || what is the balance in my current account? || what is the balance in my savings account? || check my savings account || check my current account balance || check account balance of account number 123 || show balance of account number 123 || how much money in the account of account number 123? || Tell me how much money is there in the account which has account number 123 || Can you show me the balance of account number 123? || check balance of account number 123 || how much money do account number 123 have? || available balance in the account which has account number 123', 'fetch','SELECT acc_balance FROM database where acc_no =')

