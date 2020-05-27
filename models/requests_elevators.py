# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 27/05/2020

"""

from datetime import datetime

class Requests_Elevators():

    def __init__(self, current_floor, next_floor):
        self.timestamp = datetime.now()
        self.current_floor = current_floor
        self.next_floor = next_floor
        self.direction = self._calculate_direction(current_floor, next_floor)

    def set_order(self, order):
        self.order = order

    def _calculate_direction(self, current_floor, next_floor):
        if next_floor > current_floor:
            return 1
        else: return 0