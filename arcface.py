import torch

from insightface.app import FaceAnalysis
#from insightface.data import get_image as ins_get_image

app = FaceAnalysis('models')
app.prepare(ctx_id=0 , det_thresh=.12)