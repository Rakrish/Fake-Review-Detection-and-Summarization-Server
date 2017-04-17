import sys
import re
import json
import nltk
import pickle
import settings
import TextRank
import TFIDFSummary
sys.path.append(settings.SRC_PATH)
import SummaryLauncher

object_file = None
def brandsParse(domain):
	global object_file
	f = open(settings.DATASET_BRANDS_PATH + domain.lower() + ".pickle",'rb')
	object_file = pickle.load(f)
	c=0
	brandslist={}
	for brand in object_file.keys():
		if c<20:
			brandslist[c+1]=brand
		else:
			break
		c+=1
	return brandslist

def prodsParse(domain,choice):
	global object_file
	prodslist={}
	brandslist = brandsParse(domain)
	selectedBrand = brandslist[choice]
	c=0
	for prods in range(len(object_file[selectedBrand])):
		if c<20:
			proddict = {}
			for prod in object_file[selectedBrand][prods].keys():
				proddict[object_file[selectedBrand][prods][prod]] = prod
				prodslist[c+1]= proddict
				#print str(c+1)+". "+prod+"\n"
		else:
			break
		c+=1
	return prodslist

def summarymain(domain, prodID, choice, ch_token, token=4):

	summary=""

	if choice==1:
		rankedText = TextRank.summaryGen(prodID,domain,debugging=True)

	if choice==2:
		if ch_token=="y" or ch_token=="yes":
			rankedText=TFIDFSummary.summaryGen(prodID,domain,gram=token,debug=True)
		else:
			rankedText=TFIDFSummary.summaryGen(prodID,domain,debug=True)
	
	return rankedText

	'''keys=keywords.extract_keywords(domain,prodslist[ch])
	rankedSummary=""
	for i in range(len(rankedText)):
		rankedSummary+=rankedText[i]
	stopwords=load_stop_words("../stoplist.txt")
	tokenizer = RegexpTokenizer("[\w']+", flags=re.UNICODE)
	tokens = tokenizer.tokenize(rankedSummary)
	tokens = [token for token in tokens if token.lower() not in stopwords]
	precision = float(len(set(tokens).intersection(set(keys))))/float(len(tokens))
	recall = float(len(set(tokens).intersection(set(keys))))/float(len(keys))
	fmeasure = 2*(precision*recall)/(precision+recall)
	return 
	print "\n\n"
	print "Precision =",precision
	print "Recall =",recall
	print "F-Measure =",fmeasure'''

