import csv
import os
import glob
import cv2
import sklearn

Dataset_path='/content/drive/My Drive/FaceCup (1)/Dataset/images/'

R = []
labels = []
NR = []
accepted_files = []
counter = 1
with open('Clustering.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  header = ['name','label']
  writer.writerow(header)
  
  for i, matrix_path in enumerate(glob.glob(Dataset_path + '*.jpg')):
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