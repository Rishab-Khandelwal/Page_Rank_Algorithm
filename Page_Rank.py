from math import log
import operator


pages = []
inl_dict = {}
out_dict = {}
pr_dict = {}
sink_list = []
newPr =  {}

d = 0.85
def take_graph(graph):
	read_file = open(graph,'r')
	print "I reached here"
	for line in read_file.readlines():
		words = line.split()
		key = words[0]
		values = words[1:]
		inl_dict[key] = values
		pages.insert(0,words[0])

	for key in inl_dict.keys():
		for value in inl_dict[key]:
			if out_dict.has_key(value):
				out_dict[value] = out_dict[value] + 1
			else:
				out_dict[value] = 1



def calculate_pagerank():
	count = 0 
	perplexity = 0 
	itr = 0
	numPages = len(pages)
	for page in pages:
		pr_dict[page] = float(1)/numPages
	for page in pages:
		if not out_dict.has_key(page):
			sink_list.insert(0,page)
	while(count < 4 ):
	#while(itr < 4 ):
		sinkPR = 0
		for page in sink_list:
			sinkPR = sinkPR + pr_dict[page]
		for page in pages:
			newPr[page] = float(1-d)/len(pages)
			newPr[page] += d * float(sinkPR/len(pages))
			for inl_page in inl_dict[page] :
				newPr[page] = newPr[page] + (d * float(pr_dict[inl_page])/float(out_dict[inl_page]))
		for page in pages : 
			pr_dict[page] = newPr[page]

		
		entropy = 0
		for page in pages : 
			entropy += pr_dict[page] * log(1.0/pr_dict[page],2)
		perplexity_new = 2**entropy

		if abs(perplexity_new - perplexity) < 1 :
			count += 1
		else:
			count = 0
		perplexity = perplexity_new
		itr += 1
		print "Perplexity for iteration " + str(itr) + " is : " + str(perplexity_new)




def sortPageRank(pr):
	sortedDict = sorted(pr.items(),key= operator.itemgetter(1),reverse = True)
	count = 0
	print "\nTop 50 page Rank values are:"
	while count < 50 and count < len(sortedDict):
		print sortedDict[count]
		count += 1

# print the top 10 pages by their inlink counts 
def sortInlinkCount(pr):
	temp = {}
	for page in pr.keys():
		temp[page] = len(pr.get(page))
	sortedDict = sorted(temp.items(),key = operator.itemgetter(1),reverse = True)
	count = 0
	print "Top 10 pages with their inlink counts are :  \n"
	while count < 10 and count < len(sortedDict):
		print sortedDict[count]
		count += 1


def count_no_inlink(inl_dictionary):
	count = 0
	for page in inl_dictionary.keys():
		if not inl_dictionary[page]:
			count += 1
	return count



def main():

	take_graph("G1.txt")
	calculate_pagerank()

	sortPageRank(newPr)
	sortInlinkCount(inl_dict)

	print "Number of pages with no outlinks is : " + str(len(sink_list)) 
	print "Number of pages with no inlinks count is :" + str(count_no_inlink(inl_dict)) 

if __name__ == "__main__" : main()