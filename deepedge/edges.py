import numpy as np
import cv2

class CropLayer(object):
    def __init__(self, params, blobs):
        self.xstart = 0
        self.xend = 0
        self.ystart = 0
        self.yend = 0
 
    # Our layer receives two inputs. We need to crop the first input blob
    # to match a shape of the second one (keeping batch size and number of channels)
    def getMemoryShapes(self, inputs):
        inputShape, targetShape = inputs[0], inputs[1]
        batchSize, numChannels = inputShape[0], inputShape[1]
        height, width = targetShape[2], targetShape[3]
 
        self.ystart = (inputShape[2] - targetShape[2]) // 2
        self.xstart = (inputShape[3] - targetShape[3]) // 2
        self.yend = self.ystart + height
        self.xend = self.xstart + width
 
        return [[batchSize, numChannels, height, width]]
 
    def forward(self, inputs):
        return [inputs[0][:,:,self.ystart:self.yend,self.xstart:self.xend]]

cv2.dnn_registerLayer('Crop', CropLayer)
        
face_architecture = 'deploy.prototxt'
face_weights = 'hed_pretrained_bsds.caffemodel'
print('model loading')
net = cv2.dnn.readNetFromCaffe(face_architecture, face_weights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
print('model loaded')

def edges(frame):
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    blob = cv2.dnn.blobFromImage(rgb, scalefactor=1.0, size=(300, 300), mean=(104.00698793, 116.66876762, 122.67891434), swapRB=False, crop=False)
                                      
    net.setInput(blob)
    out = net.forward()

    out = out[0, 0]
    out = cv2.resize(out, (frame.shape[1], frame.shape[0]))
    out = 255 * out
    out = out.astype(np.uint8)
    
    return out

#frame = cv2.imread('circle.png')
#result = edges(frame)
#cv2.imwrite('circle-edges.png',result)
