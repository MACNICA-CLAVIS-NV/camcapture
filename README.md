# camcapture
Video Capture Application Template

## Usage
```
python3 camcapture.py [-h] [--csi] [--camera CAMERA_NUM] [--width WIDTH]
                     [--height HEIGHT] [--fps FPS] [--qsize QSIZE] [--qinfo]
                     [--mjpg] [--title TITLE] [--max MAX]

Camera Capture Test

optional arguments:
  -h, --help            show this help message and exit
  --csi                 Set to use a CSI camera
  --camera CAMERA_NUM, -c CAMERA_NUM
                        Camera number
  --width WIDTH         Capture width
  --height HEIGHT       Capture height
  --fps FPS             Capture frame rate
  --qsize QSIZE         Capture queue size
  --qinfo               If set, print queue status information
  --mjpg                If set, capture video in motion jpeg format
  --title TITLE         Display window title
  --max MAX             Maximum number of capturing frames
```
