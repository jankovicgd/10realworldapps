import cv2
import glob

images = glob.glob("*.jpg")

def resize(image):
    name = image.split(".")
    image = cv2.imread(image, 0)
    resized_img = cv2.resize(image, (100, 100))
    cv2.imwrite(name[0]+"_resized."+name[1], resized_img)

for image in images:
    resize(image)
