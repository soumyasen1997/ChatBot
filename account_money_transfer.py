import sqlite3
conn=sqlite3.connect('bank-query-sf.db')
c=conn.cursor()
def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS account_money_transfer(no_of_question REAL,query TEXT,answer TEXT)")

def data_entry(a,b,e):
	c.execute("INSERT INTO account_money_transfer VALUES(?,?,?)",(a,b,e))
	conn.commit()
	#c.close()
	#conn.close()

create_table()

data_entry(4,'What is Inter Bank Transfer? || I want to know about Inter Bank Transfer || Tell me about Inter Bank Transfer || Inter Bank Transfer','Inter Bank Transfer is a special service that allows you to transfer funds electronically to accounts in other banks in India through RTGS/NEFT/IMPS.')
data_entry(6,'NEFT || Give me idea about NEFT || What is NEFT? || NEFT stands for what? || Tell me about NEFT || National Electronic Funds Transfer','The acronym NEFT stands for National Electronic Funds Transfer. Funds are transferred to the credit account with the other participating Bank using RBI\'s NEFT service. RBI acts as the service provider and transfers the credit to the other bank\'s account. This system of fund transfer operates on a Deferred Net Settlement basis.Presently, NEFT operates in hourly batches from 8 am to 7 pm on week days and 8 am to 1 pm on Saturdays. For more details, go to http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(6, 'RTGS || Give me idea about RTGS || What is RTGS? || RTGS stands for what? || Tell me about RTGS || Real Time Gross Settlement','The acronym RTGS stands for Real Time Gross Settlement. This is a system where the processing of funds transfer instructions takes place at the time they are received (real time). Also the settlement of funds transfer instructions occurs individually on an instruction by instruction basis (gross settlement). The RTGS system is the fastest possible interbank money transfer facility available through secure banking channels in India. For more details, go to http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(3, 'What is the minimum/maximum amount for RTGS? || transaction limit for RTGS  || How much I can transfer through RTGS','Minimum amount for RTGS transaction is Rs. 2 Lakh and no limit for Maximum amount. For more details, go to http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(2, 'What is the minimum amount for RTGS? || minimum transaction limit for RTGS','Minimum amount for RTGS transaction is Rs. 2 Lakh. For more details, go to http://sky-bits.com/ or contact your nearest Skybits bank branch.')
data_entry(2, 'What is the maximum amount for RTGS? || maximum transaction limit for RTGS','There is no maximum limit for RTGS transaction. For more details, go to http://sky-bits.com/ or contact your nearest Skybits bank branch.')
data_entry(2, 'What is the minimum amount for NEFT transactions? || minimum transaction limit for NEFT','Minimum amount for NEFT, there is no limit for minimum transaction. For more details, go to http://sky-bits.com/ or contact your nearest Skybits bank branch.')
data_entry(2, 'What is the maximum amount for NEFT transactions? || maximum transaction limit for NEFT','There is no maximum limit for NEFT transaction. For more details, go to http://sky-bits.com/ or contact your nearest Skybits bank branch.')
data_entry(2, 'What are the service charges applicable for RTGS transactions? || service charges applicable for RTGS transactions','For our bank, transaction from Rs 2.00 lakhs to Rs 5.00 Lakhs, charges is Rs. 25/- + Service Tax and for Above Rs 5.00 lakhs charges is Rs. 50/- + Service Tax. For more details, go to http://sky-bits.com/ or contact your nearest Skybits bank branch.')
data_entry(2, 'What are the service charges applicable for NEFT transactions?  ||  service charges applicable for NEFT transactions','For our bank, transaction Upto Rs 10,000, charges is Rs. 2.50/- + Service Tax, Above Rs 10,000 Up to Rs 1.00 lakh charges is Rs. 5/- + Service Tax, Above Rs 1.00 lakhs upto Rs 2.00 lakhs charges is Rs. 15/- + Service Tax and Above Rs 2.00 lakhs charges is Rs. 25/- + Service Tax. For more details, go to http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(2, 'Whom I can contact, in case of non-credit or delay in credit to the beneficiary account for NEFT transaction? || Delay in credit of a NEFT transaction. whom should I contact?','Please contact your nearest Skybits branch or the receiver bank/branch or the Customer Facilitation Service center of the banks. The Customer Facilitation Service details for NEFT can be downloaded from our website. Go to http://sky-bits.com/')
data_entry(4, 'What is the mandatory information required to make an RTGS & NEFT payment? || information required to make an RTGS & NEFT payment || information required to make a RTGS payment || information required to make a NEFT payment','The Remitter has to provide the details: Amount to be remitted, Account no. to be credited, Name of the beneficiary bank, Name of the beneficiary customer, Sender to receiver information, if any, IFSC code of the receiving branch and Mobile number of the remitter. The amount will be credited to the account basing on the account number only. As such remitter has should be cautious on the account number while transferring the amounts in electronic mode. For more details, go to http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(1, 'At what time during the day/week is the RTGS & NEFT service is available?','For RTGS and NEFT transaction, it is available from 8 am to 8 pm. For more details, go to http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(1, 'At what time during the day/week is the RTGS service is available?','For RTGS transaction, it is available from 8 am to 8 pm. For more details, go to http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(1, 'At what time during the day/week is the NEFT service is available?','For NEFT transaction, it is available from 8 am to 8 pm. For more details, go to http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(4, 'What is IMPS? || IMPS || Details about IMPS || innovative real-time payment service','IMPS is an innovative real time payment service that is available round the clock. This service is offered by National Payments Corporation of India (NPCI) that empowers customers to transfer money instantly through banks and RBI authorized Prepaid Payment Instrument Issuers (PPI) across India. For more details, go to http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(3, 'What are the benefits of IMPS? || Can you tell me the benefits of IMPS? || the benefits of IMPS','IMPS transaction is Instant, Available 24 x7 (functional even on holidays), Safe and secure, easily accessible and cost effective, Channel Independent can be initiated from Mobile/ Internet / ATM channels,Debit & Credit Confirmation by SMS. For more details, go to http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(1, 'How do I get IMPS enabled?','For Sender, the customer has to do the Mobile Banking Registration if he/she wants to initiate the transaction through mobile channel. For Internet Banking, ATM and bank branch channels, mobile registration is not required and for Receiver, Collect his/her MMID from bank and share with sender or alternatively share his/her Account number & IFS code or Aadhaar number for receiving money. The receiver can register his/her mobile no. for getting SMS alerts for transactions. For more details, go to http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(2, 'How do I transfer funds using IMPS? || I want to do IMPS transaction. How can I do that?','The following channels may be used to initiate IMPS transactions. 1.Mobile phones 2.Internet Bank’s Internet banking facility 3.ATM-By Using ATM Card at Banks ATM. The sender have to enter receiver\'s details like: 1.MMID & Mobile no. or Account number & IFS Code or Aadhaar number 2.Amount to be transferred 3.Remarks/Payment Reference number 4.Sender’s M-PIN Both sender & receiver will get SMS confirmation after money transfer. For more details, go to http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(2, 'Is the facility of Stop payments is available on IMPS? || I want to stop a IMPS transaction','IMPS is an immediate fund transfer service; after initiating the payment request payment cannot be stopped or cancelled. For more details, go to http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(2, 'What are the charges for the customer for sending and receiving money using IMPS? || charges for the customer for sending and receiving money using IMPS?','The charges for IMPS transaction are decided by the individual member banks. Please check our website http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(3, 'Does the customer need to have a bank account for availing IMPS? || I dont have an acocunt. Can I do IMPS transaction? || I dont have an account.  Can receive money using IMPS transaction?','Both banked as well as un-banked customer can avail IMPS. However, unbanked customer can initiate IMPS transaction using the services of Pre-Paid Payments instrument issuer (PPI). For more details, go to http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(2 ,'Does the customer need to register to remit the funds through IMPS? || Where do I register a complaint with reference to the IMPS transaction?','For using IMPS on mobile phones, a customer will have to register for mobile banking with his/her individual bank. However, for initiating IMPS using Bank branch, Internet banking and ATM channels, no prior Mobile banking registration is required. For more details, go to http://sky-bits.com/ or contact your nearest Skybits branch.')
data_entry(10, 'transfer 100 rupees from my current account || transfer 100 rupees from my savings account || transfer money from my current account to savings account || transfer money from my savings account || transfer money from my current account || transfer money from my account || help me to send money || help me to transfer money || send money || transfer 1000 rupees from my savings account ','Not Available')