import re

from get_neighbours_info import get_neighbours
from line_mapper import LinesInfo
from contants import dateRegExp_,InvDateKey_

class InfoExtractor(LinesInfo):
    def __init__(self, image):
        super().__init__(image)
        self.lines_info = LinesInfo.get_lines_info()
        self.cnt_info = LinesInfo.get_contour_info()
        self.neighbours = get_neighbours(image)
        self.cnt_list = list(self.cnt_info.keys())
        self.line_list = list(self.lines_info.keys())
        self.lines_in_cnt = LinesInfo.lines_within_cnt()

    @staticmethod
    def update_dict(self, dict_, key):
        del dict_[key]

    @staticmethod
    def update_list(self, list_, element):
        list_.pop(element)

    def extract_date(self):
        for i in range(len(self.cnt_list)):
            for line_id in self.lines_in_cnt[self.cnt_list[i]]:
                text = self.lines_info[line_id][1]
                text = re.sub(r'[^\w\s]', '', text)
                text = text.rstrip()
                if text in InvDateKey_:



        pass

    def extract_amount(self):
        pass

    def extract_invoice_number(self):
        pass

    def extract_address(self):
        pass

        # obj = LinesInfo(image)
        # lines_info, _ = obj.get_lines_info(write_image=True)
        # neighbours = get_neighbours(image)
        # cnt_info = obj.get_contour_info(write_contours_image=False)

