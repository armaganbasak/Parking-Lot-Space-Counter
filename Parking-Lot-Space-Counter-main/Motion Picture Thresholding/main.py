import cv2
import numpy as np

cap = cv2.VideoCapture("Assets/parking_lot.mp4")

def scanResults(img_median):
    for row in img_median:
        for col in row:
            if(col != 0):
                return True
    return False

while True:
    ret, frame = cap.read() #ret : if image taken(bool), frame: image itself(numpy)

    lot_original = frame[420:680]
    lot_resized = cv2.resize(lot_original, (0, 0), fx=0.5, fy=0.5)
    lot_grayscale = cv2.cvtColor(lot_resized, cv2.COLOR_RGB2GRAY)

    c = 255 / np.log(1 + np.max(lot_grayscale))
    log_image = 2.55 * c * (np.log(lot_grayscale + 1))
    log_image = np.array(log_image, dtype=np.uint8)

    cv2.imshow('frame2', log_image)

    ret, thresh = cv2.threshold(log_image, 220, 255, cv2.THRESH_BINARY)
    img_median = cv2.medianBlur(thresh, 7)

    #cv2.imshow('frame', img_median)
    lot = img_median

    space1 = lot[0:125, 43:103]
    space2 = lot[0:125, 113:173]
    space3 = lot[0:125, 183:243]
    space4 = lot[0:125, 253:313]
    space5 = lot[0:125, 323:383]
    space6 = lot[0:125, 393:453]
    space7 = lot[0:125, 463:523]
    space8 = lot[0:125, 533:593]
    space9 = lot[0:125, 603:663]
    space10 = lot[0:125, 673:733]
    space11 = lot[0:125, 745:805]
    space12 = lot[0:125, 815:875]

    empty_spaces = 12

    spaces = (space1, space2, space3, space4, space5, space6, space7, space8, space9, space10, space11, space12)
    for space in spaces:
        space = cv2.resize(space, (0, 0), fx=0.5, fy=0.5)
        if scanResults(space):
            empty_spaces -= 1

    byline_text = str(empty_spaces) + " of 12 parking space is available."

    #cv2.imshow('frame', cv2.resize(frame, (0,0), fx=0.5, fy=0.5))
    #cv2.imshow('threshold', img_median)
    #print(empty_spaces)

    frame_final = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    frame_final[0:130] = cv2.cvtColor(img_median[0:130], cv2.COLOR_GRAY2RGB)
    frame_final = cv2.putText(frame_final, byline_text, (5, frame_final.shape[0] - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 125, 0), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame_final)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()  # allows capture source to be used by other sources
cv2.destroyAllWindows()
