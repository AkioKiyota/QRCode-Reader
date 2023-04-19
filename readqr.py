import cv2
import os
import sys

# This function is for a specific use. It has nothing to do with data.
def get_password(data):
    start = data.index(";P:") + 3
    end = data.index(";H:")
    result = data[start:end]
    return result

if len(sys.argv) > 1:
    file_name = sys.argv[1]

    if os.path.exists(file_name):
        img = cv2.imread(file_name)
        detector = cv2.QRCodeDetector()
        data, b, c = detector.detectAndDecode(img)
        print(data)

    else:
        print(f"The file '{file_name}' does not exist :(")

else:
    print("please submit the file name!")

