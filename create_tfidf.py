import sqlite3
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english')) 
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import numpy as np
conn=sqlite3.connect('bank-query-sf.db')
c=conn.cursor()
table=["card","loan","account_balance_enquiry","account_general_query","account_money_transfer","account_transaction_details"]
full_corpus=[]
for ii in table:
	query = 'SELECT * FROM {}'.format(ii)
	c.execute(query)
	rows=c.fetchall()
	punctuations=[',','.','/','?',"'",'"','{','}','[',']','(',')','_','-','*','^','!',':','+','&']
	
	for i in range(len(rows)):
		corpus=""
		if(rows[i][2]=='fetch'):
			temp=(rows[i][1]).split('||')
			temp1=' '.join([jj  for jj in temp if len(jj)>1])
			sent=temp1
		else:
			temp=(rows[i][1]).split('||')
			temp1=' '.join([jj  for jj in temp if len(jj)>1])
			sent=str(temp1)+" "+rows[i][2]
		for char in sent:
			if char not in punctuations:
				corpus = corpus + char
		sent=''.join([i.lower() for i in corpus if not i.isdigit()])
		word_tokens = word_tokenize(sent)
		sent=[w for w in word_tokens if not w in stop_words]
		sent1=' '.join([i for i in sent])
		full_corpus.append(sent1)
#print(full_corpus)
#print(len(full_corpus))

vectorizer_tfidf = TfidfVectorizer(ngram_range=(1,1))
tfidf = vectorizer_tfidf.fit_transform(full_corpus)


vectors=[]
index=[]
intent=[]

for ii in table:
	query = 'SELECT * FROM {}'.format(ii)
	c.execute(query)
	rows=c.fetchall()
	for i in range(len(rows)):
		sent=rows[i][1]
		sent=sent.split("||")
		for j in sent:
			query=""
			for char in j:
				if char not in punctuations:
					query=query+char
			query1=''.join([k.lower() for k in query if not k.isdigit()])
			word_tokens=word_tokenize(query1)
			query=[w for w in word_tokens if not w in stop_words]
			query1=' '.join([k for k in query])
			q=vectorizer_tfidf.transform([query1])
			q=q.toarray()
			vectors.append(q[0])
			index.append(i)
			intent.append(ii)

result1=[]
result2=[]
result3=[]
result4=[]
result5=[]
result6=[]
#print(vectors)
#print(len(vectors))
#print(len(index))
for i in range(len(index)):
	temp=[]
	if(intent[i]=="card"):
		temp.append(index[i])
		for j in vectors[i]:
			temp.append(j)
		result1.append(temp)
		
	elif(intent[i]=="account_balance_enquiry"):
		temp.append(index[i])
		for j in vectors[i]:
			temp.append(j)
		result2.append(temp)
		#print(len(temp))

	elif(intent[i]=="account_general_query"):
		temp.append(index[i])
		for j in vectors[i]:
			temp.append(j)
		result3.append(temp)

	elif(intent[i]=="account_money_transfer"):
		temp.append(index[i])
		for j in vectors[i]:
			temp.append(j)
		result4.append(temp)

	elif(intent[i]=="account_transaction_details"):
		temp.append(index[i])
		for j in vectors[i]:
			temp.append(j)
		result5.append(temp)

	elif(intent[i]=="loan"):
		temp.append(index[i])
		for j in vectors[i]:
			temp.append(j)
		result6.append(temp)

# print(len(result1[0]))
# print(len(result2[0]))
# print(len(result3[0]))
# print(len(result4[0]))
# print(len(result5[0]))

np.savetxt('card-vectors.txt', result1, delimiter=' ',  newline='\n',fmt='%0.4f')
np.savetxt('account_balance_enquiry-vectors.txt', result2, delimiter=' ',  newline='\n',fmt='%0.4f')
np.savetxt('account_general_query-vectors.txt', result3, delimiter=' ',  newline='\n',fmt='%0.4f')
np.savetxt('account_money_transfer-vectors.txt', result4, delimiter=' ',  newline='\n',fmt='%0.4f')
np.savetxt('account_transaction_details-vectors.txt', result5, delimiter=' ',  newline='\n',fmt='%0.4f')
np.savetxt('loan-vectors.txt', result6, delimiter=' ',  newline='\n',fmt='%0.4f')
pickle.dump(vectorizer_tfidf,open("feature.pkl","wb"))
