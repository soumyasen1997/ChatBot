import sqlite3
conn=sqlite3.connect('bank-query-sf.db')
c=conn.cursor()
def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS account_transaction_details(no_of_question REAL,query TEXT,answer TEXT, require TEXT)")

def data_entry(a,b,e,f):
	c.execute("INSERT INTO account_transaction_details VALUES(?,?,?,?)",(a,b,e,f))
	conn.commit()
	#c.close()
	#conn.close()

create_table()

data_entry(3, 'How do I deposit money into my current account? || How do I deposit money into my savings account? || How do I deposit money into my account? ','If you have an account at our bank, you can bring cash to your home branch. You typically need to use a deposit slip. That’s simply a slip of paper that tells the teller where to put the money. Write your name and account number on the deposit slip (deposit slips are usually available at the lobby or drive through). The first line on the right side of the deposit slip is generally labeled “CASH,” and that is where you would write the amount of your deposit.','')
data_entry(3, 'How do I withdraw money from my current account? || How do I withdraw money from my savings account? || How do I withdraw money from my account?','You can visit your home branch with the passbook and ask for a withdrawal form. By filling up the form and presenting it to the Teller along with your passbook you can withdraw cash.','')
data_entry(5, 'check my last withdrawal || check my last deposit || withdrawal history || deposit history || Tell me my last transaction','fetch','SELECT last_withdrawal_amt FROM database where acc_no =')
data_entry(6, 'my spending on 12/12/2018 || how much did I withdraw on 03/05/2018? || how much did I deposit on 03/05/2018? || how much did I spend on 03/05/2018? || how much did I spend on 3rd May 2018? || how much did I deposit on 2nd December 2018?','fetch','SELECT last_withdrawal_amt FROM database where acc_no =')
data_entry(3, 'how much did I deposit yesterday? || my deposit yesterday || How much money did I spend yesterday?','fetch','SELECT last_deposit_amt FROM databse where acc_no =')
data_entry(14, 'my spending this week || how much did I deposit December 2018? || tell me my deposit history in this week || my deposit this month || my transaction this week || show my withdrawal in March || show my deposit in April || how much did I deposit in June ? || how much did I withdraw in July ? || how much did I spend in May ? || my spending  this month || how much did I spend in May 2019? || tell me how much did I spend this weekend || how much did I spend this weekend?','fetch','SELECT last_deposit_amt FROM database where acc_no =')
