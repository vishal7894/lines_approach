import cv2
import os
import numpy as np
from contants import LINES_DRAWN_IMAGES, RAW_DATA_DIR, LINES_DATA_DIR, BLACK_WHITE


class LinesInfo:

    def __init__(self, image):
        self.image_name = image
        self.image_path = os.path.join(RAW_DATA_DIR, image)
        self.lines_info_text_path = os.path.join(LINES_DATA_DIR, "lines_"+image[:-4]+".txt")

    def get_content(self):

        """
        :return: returns a string type with all the content in the text file
        text file format --> x1,y1,x2,y2,x3,y3,x4,y4,text
        """
        with open(self.lines_info_text_path, 'r') as f:
            content = f.readlines()
        return content

    def get_image_array(self):

        """
        :return: an image array
        """
        img = cv2.imread(self.image_path)
        return img

    def get_blank_image(self):

        """
        :return: complete black image with same shape
        """
        img_ = np.zeros_like(self.get_image_array())
        return img_

    def write_image(self, dir_name, img, img_name):

        """
        :param dir_name:
        :param img:
        :param img_name:
        :return: nothing ( just writes the image in the given dir with given name
        """
        cv2.imwrite(os.path.join(dir_name, img_name), img)

    def get_lines_info(self, write_image=True):

        """
        :param write_image:
        :return: line_id_to_bbox dict containing line_id and line bounding box
                 line_id_to_bbox = {'line_id_1':([x1, y1, x3, y3],text_1), 'line_id_2':([x1, y1, x3, y3],text_2)}

                 black and white image with white bboxes of lines info --> for further contour processing

                 if write_image is true --> writes the image into LINES_DRAWN_IMAGES folder
        """

        line_id_to_bbox = dict()

        with open(self.lines_info_text_path, 'r') as f:
            info = f.readlines()

        img_path = self.image_path
        image = cv2.imread(img_path)
        img_for_cnt = self.get_blank_image()

        for count, line in enumerate(info):
            ents = line.split(",", 8)
            text = ents[-1]
            x1, y1, x3, y3 = int(ents[0]), int(ents[1]), int(ents[4]), int(ents[5])
            cv2.rectangle(image, (x1, y1), (x3, y3), (0, 255, 0), -1)
            cv2.putText(image, str(count), (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
            cv2.rectangle(img_for_cnt, (x1, y1), (x3, y3), (255, 255, 255), -1)
            line_id_to_bbox[count] = ([x1, y1, x3, y3], text)

        if write_image:
            self.write_image(LINES_DRAWN_IMAGES, image, self.image_name)

        return line_id_to_bbox, img_for_cnt

    def get_contour_info(self, write_contours_image=True):

        """
        :param write_contours_image: if True, writes the image in black_white directory
        :return: cnt_id_to_bbox
                 cnt_id_to_bbox = {cnt_id_1: [x,y,w,h], cnt_id_2:[x,y,w,h]..}
                 (these are bounding rectangles coordinates)
        """

        cnt_id_to_bbox = dict()
        kernel = np.ones((3, 3), np.uint8)
        _, img = self.get_lines_info()
        dilate = cv2.dilate(img, kernel, iterations=5)
        canny = cv2.Canny(dilate, threshold1=30, threshold2=180)
        contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        for count, cnt in enumerate(contours):
            x, y, w, h = cv2.boundingRect(cnt)
            cnt_id_to_bbox[count] = [x, y, w, h]
            if write_contours_image:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), -1)
                cv2.putText(img, str(count), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
            self.write_image(BLACK_WHITE, img, "cnt"+self.image_name)

        return cnt_id_to_bbox

    def lines_within_cnt(self):

        """
        this method gets the line_ids inside a contour_id
        :return: a mapper dict
                 mapper = {'cnt_id_1':[line_id_1, line_id_2, ... }

        """

        mapper = dict()
        cnt_dict = self.get_contour_info(write_contours_image=False)    # cnt_id : [x,y,w,h]
        lines_dict, _ = self.get_lines_info(write_image=False)          # line_id : ([x1, y1, x3, y3], text)
        cnt_keys = list(cnt_dict.keys())
        line_keys = list(lines_dict.keys())

        for i in range(len(cnt_keys)):
            if len(cnt_dict[cnt_keys[i]]) == 0:
                del cnt_dict[cnt_keys[i]]
            else:
                x, y, w, h = cnt_dict[cnt_keys[i]]
                mapper[cnt_keys[i]] = []
                for j in range(len(line_keys)):
                    l_bbox = lines_dict[line_keys[j]][0]
                    x1, y1, x3, y3 = l_bbox[0], l_bbox[1], l_bbox[2], l_bbox[3]
                    c_x, c_y = int(x1+x3)/2, int(y1+y3)/2
                    if x <= c_x <= x+w:
                        if y <= c_y <= y+h:
                            mapper[cnt_keys[i]].append(line_keys[j])

        return mapper

    def get_text_from_line_id(self, line_id):
        line_dict, _ = self.get_lines_info(write_image=False)
        text = line_dict[line_id][1]
        return text
