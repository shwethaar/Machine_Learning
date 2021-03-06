import cv2
import glob
import shutil

print("Enter following paths to get started:")
print("  Paths to be of form E:\Images\Alphabet0xx  without escaped backslashes",end="\n\n")
file_good = input("Path for destination folder of good images for current alphabet:")
file_mis = input("Path for destination folder of mismatched images for current alphabet:")
file_bad = input("Path for destination folder of bad images for current alphabet:")
file_edit = input("Path for destination folder of to-edit images for current alphabet:")
file_src = input("Path for source folder for current alphabet:")
file_src+="\\*.png"
        
for img in glob.glob(file_src):
  pic = cv2.imread(img)
  cv2.imshow('',cv2.resize(pic,(84,84)))
  cv2.waitKey(1)
  choice = input("Enter (g/b/e/m)for {image}:".format(image=img[-9:]))
  if(choice == "g"):
    shutil.move(img,file_good)
  elif(choice == "b"):
    shutil.move(img,file_bad)
  elif(choice == "e"):
    shutil.move(img,file_edit)
  elif(choice == "m"):
    shutil.move(img,file_mis)
  continue
