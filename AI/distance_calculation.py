from imutils import paths
import numpy as np
import imutils
import cv2

def find_marker(image):
    # convert the image to grayscale, blur it, and detect edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 35, 125)
    # find the contours in the edged image and keep the largest one
    # we'll assume that this is our piece of paper in the image
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)
    # compute the bounding box of the paper region and return it
    return cv2.minAreaRect(c)

def distance_to_camera(knownWidth, focalLength, perWidth):
    # compute and return the distance from the marker to the camera
    return (knownWidth * focalLength) / perWidth

# initialize the known distance from the camera to the object, which
# in this case is 24 inches (converted to centimeters)
KNOWN_DISTANCE = 24.0 * 2.54  # in centimeters
# initialize the known object width, which in this case, the piece of
# paper is 11 inches wide (converted to centimeters)
KNOWN_WIDTH = 11.0 * 2.54  # in centimeters
# load the first image that contains an object that is KNOWN TO BE 2 feet
# from our camera, then find the paper marker in the image, and initialize
# the focal length
image = cv2.imread("/media/ahmed/Work/Robotics Club/Projects/Hit-the-insects-project/AI/images/5_jpg.rf.064d4cf57610024d01aeeac43bef5f06.jpg")
marker = find_marker(image)
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH

# loop over the images
for imagePath in sorted(paths.list_images("images")):
    # load the image, find the marker in the image, then compute the
    # distance to the marker from the camera
    image = cv2.imread(imagePath)
    marker = find_marker(image)
    # calculate the distance in centimeters
    distance_cm = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
    
    # draw a bounding box around the image and display it
    box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
    box = np.int0(box)
    cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
    # display the distance in centimeters
    cv2.putText(image, "%.2f cm" % distance_cm,
                (image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
                2.0, (0, 255, 0), 3)
    cv2.imshow("image", image)
    
    # Wait for 'q' key press to move to the next image
    key = cv2.waitKey(0)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
