# -*- coding: utf-8 -*-
# file: planner.py
# author: JinTian
# time: 23/12/2017 12:35 PM
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
this file will get the next move
"""
import os
from observer import Observation
from collections import namedtuple


Plan = namedtuple('Plan', 'l_speed r_speed time')


class Planner(object):

    def __init__(self):
        pass

    @staticmethod
    def get_next_plan(time_flag, observations):
        assert isinstance(observations, Observation)
        # we need do the plan based on the observation
        if observations.is_obstacle:
            # if obstacle, stop 3 seconds
            return Plan(l_speed=0, r_speed=0, time=3)
        else:
            if time_flag % 20 == 0:
                return Plan(l_speed=50, r_speed=50, time=10)
            elif time_flag % 20 > 12:
                return Plan(l_speed=20, r_speed=50, time=10)
            elif time_flag:
                return Plan(l_speed=-50, r_speed=-50, time=10)

