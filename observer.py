# -*- coding: utf-8 -*-
# file: observer.py
# author: JinTian
# time: 23/12/2017 12:36 PM
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
this environment class
"""
import os
from collections import namedtuple
from camera_manager import CameraManager
from lane_detector import LaneDetector
from infrared_detector import InfraredDetector
from ultrasonic_detector import UltrasonicDetector
from src.car import Car
from src.encoder import Encoder


Observation = namedtuple('Observation',
                         'frame_input current_l_speed current_r_speed is_obstacle obs_distance lane_res_image')


class Observer(object):

    def __init__(self):
        self.camera_manager = CameraManager()
        self.lane_detector = LaneDetector()
        self.infrared_detector = InfraredDetector()

        # the Car staff
        self.encoder = Encoder()

    def get_observations(self):
        """
        this method returns the observations collected from sensors
        :param self:
        :return:
        """
        frame_input = self.camera_manager.get_next_frame()
        current_l_speed, current_r_speed = self.encoder.get_speed()
        is_obstacle = False
        obs_distance = 0
        lane_res_image = self.lane_detector.detect(frame_input=frame_input)

        observation = Observation(frame_input=frame_input,
                                  current_l_speed=current_l_speed,
                                  current_r_speed=current_r_speed,
                                  is_obstacle=is_obstacle,
                                  obs_distance=obs_distance,
                                  lane_res_image=lane_res_image)
        print('# Current observation: {}, {}, {}'.format(observation.current_l_speed, observation.current_r_speed,
                                                         observation.is_obstacle))
        return observation