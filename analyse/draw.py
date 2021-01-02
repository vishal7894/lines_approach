import cv2
import os
from analyse.contansts import LINES_DATA_DIR, RAW_DATA_DIR, LINES_WITH_ID_IMAGES

files = os.listdir(LINES_DATA_DIR)

for file in files:
    with open(os.path.join(LINES_DATA_DIR, file), 'r') as f:
        content = f.readlines()
        img_path = os.path.join(RAW_DATA_DIR, file[6:-4]+".png")
        img = cv2.imread(str(img_path))

        for count, line in enumerate(content):
            ents = line.split(",", 8)
            x1, y1, x3, y3 = int(ents[0]), int(ents[1]), int(ents[4]), int(ents[5])
            text = ents[-1]
            cv2.rectangle(img, (x1, y1), (x3, y3), (0, 255, 0), 2)
            cv2.putText(img, str(count), (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))

    cv2.imwrite(os.path.join(LINES_WITH_ID_IMAGES, file.split("_")[-1].replace('.txt', "")+".png"), img)

# 1139,106,1405,106,1405,134,1139,134,ACME