# -*- coding: utf-8 -*-
# file: train_classifier.py
# author: JinTian
# time: 23/12/2017 10:39 AM
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
train a classifier network, implement in Keras
"""
import keras
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.applications.mobilenet import MobileNet
import os


def get_data(batch_size=32):
    train_datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

    train_generator = train_datagen.flow_from_directory(
        'data/train',  # this is the target directory
        target_size=(150, 150),  # all images will be resized to 150x150
        batch_size=batch_size,
        class_mode='binary')  # since we use binary_crossentropy loss, we need binary labels
    return train_datagen, train_generator


def build_model(input_shape, num_classes):
    model = MobileNet(input_shape, include_top=False, classes=num_classes)
    return model


def train():
    batch_size = 32
    model_save_file = os.path.join(os.path.abspath(__file__), 'traffic_signs.h5')

    train_datagen, train_generator = get_data(batch_size=batch_size)
    model = build_model(input_shape=[256, 256], num_classes=11)

    if os.path.exists(model_save_file):
        model.load_weights(model_save_file)
        print('# load from previous saved model: ', model_save_file)

    model.fit(
        train_generator,
        steps_per_epoch=2000 // batch_size,
        epochs=50,
    )
    model.save(model_save_file)

if __name__ == '__main__':
    train()

