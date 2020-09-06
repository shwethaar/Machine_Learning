import cv2
import glob
import shutil

file_good = "E:\\Shwethaa\\Images\\Good_Images\\Alphabet013"
file_mis = "E:\\Shwethaa\\Images\\Mismatch_Images\\Alphabet013"
file_bad = "E:\\Shwethaa\\Images\\Bad_Images\\Alphabet013"
file_edit = "E:\\Shwethaa\\Images\\Edited_Images\\Alphabet013"
        
for img in glob.glob("E:\\Shwethaa\\Images\\Alphabet013\\*.png"):
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
