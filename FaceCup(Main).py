import csv
import os
import glob
import cv2
import sklearn
from sklearn import cluster
import numpy as np
from sklearn import metrics

def calculate_f_measure(labels_true, labels_pred, beta=1.0):
  [[tn, fp], [fn, tp]] = metrics.cluster.pair_confusion_matrix(labels_true, labels_pred)
  precision = tp/(tp + fp)
  recall = tp/(tp + fn)
  f_measure = (beta*beta + 1)*precision*recall/(beta*beta*precision + recall)
  return f_measure

def evaluate_clustering(labels, predictions, beta=1.0):
  rand_index = metrics.rand_score(labels, predictions)
  nmi = metrics.normalized_mutual_info_score(labels, predictions)
  f_measure = calculate_f_measure(labels, predictions, beta=beta)
  print('Rand Index: %f, NMI: %f, F-measure: %f' % (rand_index, nmi, f_measure))
  return


from insightface.app import FaceAnalysis
#from insightface.data import get_image as ins_get_image

app = FaceAnalysis('models')
app.prepare(ctx_id=0 , det_thresh=.12)


images_path='Dataset'

R = []
labels = []
NR = []
accepted_files = []
counter = 1
with open('Clustering.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  header = ['name','label']
  writer.writerow(header)
  
  for i, matrix_path in enumerate(glob.glob('*.jpg')):
    filename = os.path.basename(matrix_path)
    image_path = os.path.join(matrix_path)
    img = cv2.imread(os.path.join(image_path))
    #img=RetinaFace.extract_faces(img , align=True)
    faces_location =app.get(img)
    #faces_location=RetinaFace.get_image(faces_location)
    if len(faces_location) < 1:
      NR.append(int(filename[1:3]))
      dat=[[filename, filename[1:5]]]
    else:
      R.append(faces_location[0].normed_embedding)
      labels.append(int(filename[1:3]))
      dat=[[filename, filename[1:5]]]
      writer.writerows(dat)
      print('prosessing image %d: %s'%(counter,filename))
      accepted_files.append(matrix_path)

    counter+=1

labels += NR # add images without face detection
print('number of images without face: %d' % len(NR))



y_pred = cluster.AgglomerativeClustering(n_clusters=None, distance_threshold=1.14 , linkage='single').fit_predict(R)
y_pred_compelet = list(y_pred) + list(range(max(y_pred)+1,max(y_pred)+len(NR)+1))
y_pred_compelet=np.array(y_pred_compelet)

if 0 in y_pred_compelet:
  y_pred_compelet_New=y_pred_compelet + 1
else:
  y_pred_compelet_New=y_pred_compelet
    
print((y_pred_compelet0))
print('num of clusters: %d' % (max(y_pred_compelet0)+1))

evaluate_clustering(labels, y_pred_compelet_New)

C=pd.read_csv('Clustering.csv')  
C['cluster']=y_pred_compelet_New
sorted_C = C.sort_values(by=["cluster"], ascending=True)
C.value_counts('name')
sorted_C 