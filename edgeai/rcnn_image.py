import torchvision
from torchvision import transforms as T
from PIL import Image
import cv2

coco_labels = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

print('loading model')
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
print('model loaded')
model.eval()
model.cuda()

img_path = "../dataset/photo10.png"
image = cv2.imread(img_path)

img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
img = Image.fromarray(img)
transform = T.Compose([T.ToTensor()])
img = transform(img)
img = img.cuda()

pred = model([img])

labels = [coco_labels[i] for i in list(pred[0]['labels'].cpu().numpy())]
boxes = [[(int(i[0]), int(i[1])), (int(i[2]), int(i[3]))] for i in list(pred[0]['boxes'].cpu().detach().numpy())]
scores = list(pred[0]['scores'].cpu().detach().numpy())

threshold = 0.3
for label, box, score in zip(labels, boxes, scores):
    if score > threshold:
        cv2.rectangle(image,box[0],box[1],(0,0,255),2)
        cv2.putText(image,label,(box[0][0],box[0][1]+10),0,0.5,(0,0,255),1)

cv2.imshow('detection',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

