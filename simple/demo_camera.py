# Camera
#
# ls -l /dev/video0 must work, then install
# sudo apt-get install libcanberra-gtk-module:arm64
# to avoid error message 'Failed to load module "canberra-gtk-module"'
# or ignore it, the error message makes no harm

import cv2

def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=1280,
    display_height=720,
    framerate=60,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

camera = cv2.VideoCapture(gstreamer_pipeline(1280,720,224,224,21,0), cv2.CAP_GSTREAMER)

while True:
    re, image = camera.read()
    if not re:
        break

    #print(image.shape[1],'x',image.shape[0])
    cv2.imshow('camera',image)
    key = cv2.waitKey(1)
    if key == 27:
        break
        
cv2.destroyAllWindows()
