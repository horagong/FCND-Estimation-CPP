import numpy as np

graph1 = np.genfromtxt('config/log/Graph1.txt', delimiter=',', dtype=None, encoding='utf8')
graph2 = np.genfromtxt('config/log/Graph2.txt', delimiter=',', dtype=None, encoding='utf8')

graph1_std = np.std(graph1[1:,1].astype('float32'), ddof=1)
graph2_std = np.std(graph2[1:,1].astype('float32'), ddof=1)

print(graph1[0,1].astype('str'), graph1_std, graph2[0,1].astype('str'), graph2_std)
