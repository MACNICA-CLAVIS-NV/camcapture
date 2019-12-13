#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# MIT License
#
# Copyright (c) 2019 MACNICA Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE. 
#

import sys
import cv2
import argparse
from video_app_utils import ContinuousVideoCapture
from video_app_utils import IntervalCounter

WINDOW_TITLE = 'Camera Caputure Test'

def main():
    # Parse the command line parameters
    parser = argparse.ArgumentParser(description='Camera Capture Test')
    parser.add_argument('--camera', '-c', \
        type=int, default=0, metavar='CAMERA_NUM', \
        help='Camera number, use any negative integer for MIPI-CSI camera')
    parser.add_argument('--width', \
        type=int, default=640, metavar='WIDTH', \
        help='Capture width')
    parser.add_argument('--height', \
        type=int, default=480, metavar='HEIGHT', \
        help='Capture height')
    parser.add_argument('--fps', \
        type=int, default=30, metavar='FPS', \
        help='Capture frame rate')
    parser.add_argument('--qsize', \
        type=int, default=1, metavar='QSIZE', \
        help='Capture queue size')
    parser.add_argument('--qinfo', \
        action='store_true', \
        help='If set, print queue status information')
    parser.add_argument('--mjpg', \
        action='store_true', \
        help='If set, capture video in motion jpeg format')
    args = parser.parse_args()
    
    fpsCounter = IntervalCounter(10)
    
    fourcc = None
    if args.mjpg:
        fourcc = 'MJPG'
    capture = ContinuousVideoCapture( \
        args.camera, args.width, args.height, args.fps, args.qsize, fourcc)
    capture.start()
    
    while True:
    
        frame = capture.get()
        
        # Debug
        if args.qinfo:
            print('%02d %06d' % (capture.qsize(), capture.numDrops))
        
        interval = fpsCounter.measure()
        if interval is not None:
            fps = 1.0 / interval
            fpsInfo = '{0}{1:.2f}   ESC to Quit'.format('FPS:', fps)
            cv2.putText(frame, fpsInfo, (32, 32), \
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
        
        cv2.imshow(WINDOW_TITLE, frame)
        
        # Check if ESC key is pressed to terminate this application
        key = cv2.waitKey(1)
        if key == 27: # ESC
            break
            
    capture.stop()

if __name__ == '__main__':
    main() 
    sys.exit(0)   
