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
from camera_manager import CameraManager
from planner import Planner
from observer import Observer
from executor import Executor


def test():

    car = Car()
    car.test()


def fuck_run():
    car = Car()

    planner = Planner()
    observer = Observer()
    executor = Executor()

    frequent = 1

    try:
        hold_times = 0
        i = 0
        while True:
            print('current frame flag: ', i)
            print('-> Make observations.')
            observations = observer.get_observations()
            print('-> Do next planning.')
            next_plan = planner.get_next_plan(time_flag=i, observation=observations)
            print('-> Execute plan.')

            if i == 0:
                print('---- Car start to run! ------')
                hold_times = next_plan.time * frequent
            else:
                i += 0.01
                if i > hold_times:
                    print('\n')
                    print('-> New a plan.')
                    executor.execute_plan(car, next_plan)
                    i = 0
                    hold_times = next_plan.time * frequent
                else:
                    pass
                    print('*** Normal cruise... current work: {}%'.format((i/hold_times)*100))
            # executor.execute_plan(car, next_plan)

    except KeyboardInterrupt:
        executor.save_operation_to_local()
    except Exception as e:
        print(e)
        executor.save_operation_to_local()
    executor.go_back_home(car)
    car.__del__()


if __name__ == '__main__':
    fuck_run()