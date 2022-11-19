from sklearn import cluster

import numpy as np
y_pred = cluster.AgglomerativeClustering(n_clusters=None, distance_threshold=1.14 , linkage='single').fit_predict(R)
y_pred_compelet = list(y_pred) + list(range(max(y_pred)+1,max(y_pred)+len(NR)+1))
y_pred_compelet=np.array(y_pred_compelet)

if 0 in y_pred_compelet:
  y_pred_compelet_New=y_pred_compelet + 1
else:
  y_pred_compelet_New=y_pred_compelet
    
#print((y_pred_compelet0))
#print('num of clusters: %d' % (max(y_pred_compelet0)+1))

evaluate_clustering(labels, y_pred_compelet_New)

C=pd.read_csv('Clustering.csv')  
C['cluster']=y_pred_compelet_New
sorted_C = C.sort_values(by=["cluster"], ascending=True)
C.value_counts('name')
sorted_C 