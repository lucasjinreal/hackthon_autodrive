# -*- coding: utf-8 -*-
# file: camera_manager.py
# author: JinTian
# time: 23/12/2017 11:19 AM
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
from picamera import PiCamera
import picamera
import picamera.array


class CameraManager(object):

    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (1024, 768)
        self.camera.start_preview()
        print('-> Camera init..')

    def get_next_frame(self):
        with picamera.array.PiRGBArray(self.camera) as output:
            self.camera.capture(output, 'rgb')
            print('Captured %dx%d image' % (
                output.array.shape[1], output.array.shape[0]))
            print(output.shape)
            return output
