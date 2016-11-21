# -*- coding: utf-8 -*-
# comment by heibanke
import cv2


################# 静态图像的输入，输出 ##################
image = cv2.imread('ship.png')
#这里image的维度image.shape = (w,h,3)，
#w*h是图片的长宽，3是BGR等三种颜色的channel值，每个值为0～255
cv2.imwrite('ship.jpg', image)
#灰度图片的颜色channel只有一个，0～255表示灰度值
grayImage = cv2.imread('ship.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
#显示图像
cv2.imshow('test',grayImage)
#捕获键盘输入
k=cv2.waitKey(0)
if k==27:
    cv2.destroyWindow('test')



"""
################# 视频文件的输入，输出 ##################

#读取视频文件
videoCapture = cv2.VideoCapture('test_in.avi')
fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
    int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

#写入到另一个视频文件 cv2.VideoWriter(filename, fourcc, fps, frame_size, is_color=true)
# filename – Name of the output video file.
# fourcc – 4-character code of codec used to compress the frames. 
#    For example, CV_FOURCC('P','I','M','1') is a MPEG-1 codec, 
#                 CV_FOURCC('M','J','P','G') is a motion-jpeg codec etc. 
#                 List of codes can be obtained at Video Codecs by http://www.fourcc.org/codecs.php.
# fps – Framerate of the created video stream.
# frameSize – Size of the video frames.
# isColor – If it is not zero, the encoder will expect and encode color frames, 
#    otherwise it will work with grayscale frames (the flag is currently supported on Windows only).
# I420-uncompress avi, XVID-avi
videoWriter = cv2.VideoWriter(
    'test_out.avi', cv2.cv.CV_FOURCC('X','V','I','D'), fps, size)

success, frame = videoCapture.read()

while success:
    # Loop until there are no more frames.
    #cv2.imshow('test',frame)
    #cv2.waitKey(1)
    videoWriter.write(frame)
    success, frame = videoCapture.read()





"""

"""
################# 摄像头的输入，输出 ##################
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.cv.CV_EVENT_LBUTTONUP:
        clicked = True

clicked = False

#读取摄像头输入
cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MyWindow')
#绑定鼠标callback
cv2.setMouseCallback('MyWindow', onMouse)
print 'Showing camera feed. Click window or press any key to stop.'
success, frame = cameraCapture.read()

while cv2.waitKey(1) == -1 and not clicked:
    if frame is not None:
        cv2.imshow('MyWindow', frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow('MyWindow')
"""
