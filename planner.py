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
import cv2

Plan = namedtuple('Plan', 'l_speed r_speed time')


class Planner(object):

    def __init__(self):
        pass

    @staticmethod
    def record_observation(time_flag, observation):
        frame = observation.frame_input
        lane_res = observation.lane_res_image

        frame_dir = 'images/frames'
        lane_res_dir = 'images/lanes'
        if not os.path.exists(frame_dir):
            os.makedirs(frame_dir)
        if not os.path.exists(lane_res_dir):
            os.makedirs(lane_res_dir)
        i = time_flag % 1000
        frame_f = os.path.join(frame_dir, 'frame_%05d.jpg' % i)
        lane_f = os.path.join(lane_res_dir, 'lane_%05d.jpg' % i)
        cv2.imwrite(frame_f, frame)
        cv2.imwrite(lane_f, lane_res)

    @staticmethod
    def forward(speed=80, time=2):
        return Plan(l_speed=speed, r_speed=speed, time=time)

    @staticmethod
    def turn_left_litter():
        return Plan(l_speed=50, r_speed=100, time=4)

    def get_next_plan(self, time_flag, observation):
        assert isinstance(observation, Observation)
        # we need do the plan based on the observation
        self.record_observation(time_flag, observation)
        if observation.is_obstacle:
            # if obstacle, stop 3 seconds
            return Plan(l_speed=0, r_speed=0, time=3)
        else:
            if time_flag == 1:
                return self.forward(time=5)
            elif time_flag == 2:
                return self.turn_left_litter()
            elif time_flag == 3:
                return self.forward(time=5)
            elif time_flag == 4:
                return self.forward(time=5)


