import cv2 as cv

cap = cv.VideoCapture(0) #video capturing from video files, image sequences or cameras
#VideoCapture() returns a VideoCapture object.
#We store this object in cap so that we can repeatedly access the camera and retrieve video frames.

while True:
    ok, frame = cap.read()
    """ok- This is a Boolean value.
- True: Successfully captured a frame.
- False: Failed to capture a frame.
    frame- This contains the actual image captured from the webcam. represented as a NumPy array.
    (height, width, 3) -> typical colour webcam image's shae
"""

    cap.read()
#read() is a method of the VideoCapture object. It attempts to read the next frame from the video source.
    if not ok: break
    frame = cv.flip(frame,1)
    cv.imshow("Webcam", frame)
    #This function displays an image or video frame in a window.


    if cv.waitKey(1) & 0xFF == ord('q'): #ord('a') = 97; ord('A')  # 65

        #waitkety() - allows users to display a window for given milliseconds or until any key is pressed
        break

cap.release()# releases the connection made with the webcam, releases resource for other apps to access
cv.destroyAllWindows()