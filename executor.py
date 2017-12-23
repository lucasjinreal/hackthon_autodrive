# -*- coding: utf-8 -*-
# file: executor.py
# author: JinTian
# time: 23/12/2017 12:47 PM
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
this class will execute the commands
"""
import os
from src.car import Car
from planner import Plan
import time
import pickle


class Executor(object):

    def __init__(self):
        self.local_record_f = 'record.pkl'
        self.all_plans = list()

    def go_back_home(self, car):
        with open(self.local_record_f, 'rb') as f:
            all_plans = pickle.load(f)
        if len(all_plans) >= 1:
            for p in all_plans:
                self.execute_plan(car, plan=p)

    def save_operation_to_local(self):
        with open(self.local_record_f, 'wb') as f:
            pickle.dump(self.all_plans, f)

    def execute_plan(self, car, plan):
        assert isinstance(car, Car), 'car must be car'
        assert isinstance(plan, Plan), 'plan must be plan'
        l_speed = plan.l_speed
        r_speed = plan.r_speed
        hold_time = plan.time
        car.set_duty_cycle(l_speed, r_speed)
        print('# Currently do the plan: l: {} r: {} time: {}'.format(l_speed,
                                                                     r_speed,
                                                                     hold_time))
        time.sleep(hold_time)
        self.all_plans.append(plan)