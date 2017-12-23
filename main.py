# -*- coding: utf-8 -*-
# file: main.py
# author: JinTian
# time: 23/12/2017 10:49 AM
# Copyright 2017 JinTian. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------
"""
this file is the main logic of auto-drive
"""
from src.car import Car
import time

def test():

    car = Car()
    car.test()


def fuck_run():
    car = Car()
    try:
        while True:
            print('forward 4 seconds')
            car.set_speed(left_speed=10, right_speed=10)
            time.sleep(4)

            print('left 4 seconds')
            car.set_speed(left_speed=5, right_speed=15)
            time.sleep(4)

            print('forward 10 seconds')
            car.set_speed(left_speed=15, right_speed=15)
            time.sleep(10)

    except KeyboardInterrupt:
        car.__del__()

if __name__ == '__main__':
    fuck_run()