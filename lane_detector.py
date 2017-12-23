# -*- coding: utf-8 -*-
# file: lane_detector.py
# author: JinTian
# time: 23/12/2017 10:50 AM
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
import os
from src.lane_lines import annotate_image_array


class LaneDetector(object):
    def __init__(self):
        pass

    def detect(self, frame_input):
        lane_res = annotate_image_array(frame_input)
