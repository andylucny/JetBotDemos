import torch
from torchvision import transforms as T
import cv2
from PIL import Image

model_name = "trained_models/signatrix_efficientdet_coco.pth"
model = torch.load(model_name).module
model.cuda()

img_path = "../dataset/photo10.png"
image = cv2.imread(img_path)
image = cv2.resize(image,(512,512))
img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
img = Image.fromarray(img)
transform = T.Compose([T.ToTensor()])
img = transform(img)

print('start')
scores, labels, boxes = model(img.cuda().float().unsqueeze(dim=0))
print('stop')

if boxes.shape[0] > 0:
    for box_id in range(boxes.shape[0]):
        pred_prob = float(scores[box_id])
        if pred_prob < 0.3:
            break
        pred_label = int(labels[box_id])
        xmin, ymin, xmax, ymax = boxes[box_id, :]
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0,0,255), 2)

cv2.imwrite("prediction.png", image)


