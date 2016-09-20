import os;
import sys;
import random;

## number of samples generated.
sampleNum = int(sys.argv[1]);
nodeNum = int(sys.argv[2]);
edgeNum = int(sys.argv[3]);
graphFile = file(sys.argv[4], 'w');

def reachable(graph, src, tgt, nodeNum):
	connect = {}
	connect[src] = 1;
	
	if(src == tgt):
		return 1;
	
	for i in range(0, nodeNum):
		reconnect = {};
		for seed in connect:
			for nei in graph[seed]:
				reconnect[nei] = 1;
		if(reconnect.has_key(tgt)):
			return 1;
		connect = reconnect;
		if(len(connect) == 0):
			break;
	return 0;

	
def graph2str(graph, nodeNum, edgeNum):
	graphStr = "";
	for n in range(0, nodeNum):
		for nei in graph[n]:
			graphStr += str(n)+ " -> " + str(nei) +" # ";
	return graphStr;

hit_num = 0;

## number of nodes generated
def gengraph(nodeNum, edgeNum):
	global hit_num;
	graph = [];
	for i in range(0, nodeNum):
		graph.append({});
	
	for i in range(0, edgeNum):
		edgeIdx = random.randint(0, nodeNum * nodeNum - 1);
		src = edgeIdx / nodeNum;
		tgt = edgeIdx % nodeNum;
		
		## connect from src to tgt.
		graph[src][tgt] = 1;
	
	#src = -1;
	#tgt = -1;
	#while(True):
	edgeIdx = random.randint(0, nodeNum * nodeNum - 1);
	src = edgeIdx / nodeNum;
	tgt = edgeIdx % nodeNum;
	#if(src <> tgt):
	#	break;
	answer = reachable(graph, src, tgt, nodeNum);
	
	hit_num += answer;
	
	query =  str(src)+ " -> " + str(tgt);
	return graph2str(graph, nodeNum, edgeNum)+"\t" + query + "\t" + str(answer);

print 'generate data : ',sampleNum;

	
### sample total number of records
for i in range(0, sampleNum):
	smp = gengraph(nodeNum, edgeNum);
	if((i+1) % 10000 == 0):
		print "stat", i + 1, hit_num, hit_num * 1.0 / (i + 1);
	graphFile.write(smp+"\n");
graphFile.close();