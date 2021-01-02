import numpy as np
from line_mapper import LinesInfo


def get_neighbours(image):
    """
    :param image:
    :return: neighbours dict of the image which contains a cnt_id neighbour information
             neighbours = {'cnt_id_1' : { 'right' : [id_1,id_2,..],
                                          'bottom' : [id_1,id_2,..],
                                          'left' : [id_1,id_2...]
                                          }

    """
    neighbours = dict()
    obj = LinesInfo(image)
    cnt_dict = obj.get_contour_info(write_contours_image=True)

    cnt_id = list(cnt_dict.keys())

    for i in range(len(cnt_id)):
        neighbours[cnt_id[i]] = []
        cnt_bbox = cnt_dict[cnt_id[i]]
        x, y, w, h = int(cnt_bbox[0]), int(cnt_bbox[1]), int(cnt_bbox[2]), int(cnt_bbox[3])
        temp_dict = {
                    "right": [],
                    "bottom": [],
                    "left": []
                    }
        right_range_min, right_range_max = y - (0.05 * h), y + h + (0.05 * h)
        bottom_range_min, bottom_range_max = x - (0.01 * w), x + w + (0.01 * w)

        for j in range(len(cnt_id)):
            if i != j:
                cnt_bbox_ = cnt_dict[cnt_id[j]]
                x_, y_, w_, h_ = int(cnt_bbox_[0]), int(cnt_bbox_[1]), int(cnt_bbox_[2]), int(cnt_bbox_[3])
                c_x, c_y = (x_ + x_ + w_) / 2, (y_ + y_ + h_) / 2
                if right_range_min <= c_y <= right_range_max:
                    if x_ >= x + w:
                        temp_dict['right'].append(cnt_id[j])
                if right_range_min <= c_y <= right_range_max:
                    if x_ + w_ <= x:
                        temp_dict['left'].append(cnt_id[j])
                if bottom_range_min <= c_x <= bottom_range_max:
                    if y_ >= y + h:
                        temp_dict['bottom'].append(cnt_id[j])

        neighbours[cnt_id[i]].append(temp_dict)

    return neighbours

# print(get_neighbours('0.png'))



