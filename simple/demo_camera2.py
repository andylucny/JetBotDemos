# Camera
#
# ls -l /dev/video0 must work, then install
# sudo apt-get install libcanberra-gtk-module:arm64
# to avoid error message 'Failed to load module "canberra-gtk-module"'
# or ignore it, the error message makes no harm

import cv2

def gstreamer_pipeline(
    device_id=0,
    width=640,
    height=360,
    framerate=20
):
    return (
        "v4l2src device=/dev/video%d ! jpegdec ! video/x-raw,width=%d,height=%d,framerate=%d/1 ! videoconvert ! video/x-raw, format=(string)BGR ! appsink" % (device_id, width, height, framerate)
    )

# v4l2-ctl -d /dev/video1 --list-formats-ext
# gst-launch-1.0 v4l2src device=/dev/video1 ! video/x-raw,format=H264,width=640,height=480,framerate=20/1 ! 'video/x-raw(memory:NVMM),format=NV12' ! nvoverlaysink

camera = cv2.VideoCapture(gstreamer_pipeline(1,640,360,20), cv2.CAP_GSTREAMER)

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
