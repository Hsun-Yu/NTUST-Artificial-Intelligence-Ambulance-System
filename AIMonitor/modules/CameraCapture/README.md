# Azure IoT Edge Camera Capture module

這個 IoT Edge module 可以讀取你的視訊頭資料並將辨識結果回傳到iot hub。

## Optional parameters

|Environment variable  |Description  |
|---------|---------|
|IMAGE_PROCESSING_ENDPOINT     | Service endpoint to send the frames to for processing. Example: "http://my-ai-service:8080" (where "my-ai-service" is the name of another IoT Edge module). Leave empty when no external processing is needed (Default).  |
|IMAGE_PROCESSING_PARAMS     | Query parameters to send to the processing service. Example: "{'returnLabels': 'true'}". Empty by default. |
|SHOW_VIDEO     | Show the video. From a browser, go to "http://YourRaspberryPiIpAdress:5012". Examle: "FALSE". False by default. |
|VERBOSE     |  Show detailed logs and perf timers. Example: "FALSE". False by default.  |
|LOOP_VIDEO     | When reading from a video file, it will loop this video. Example: "TRUE". True by default. |
|CONVERT_TO_GRAY     | Convert to gray before sending to external service for processing. Example: "FALSE". False by default.  |
|RESIZE_WIDTH     | Resize frame width before sending to external service for processing. Example: "256". Does not resize by default (0). |
|RESIZE_HEIGHT     | Resize frame width before sending to external service for processing. Example: "456". Does not resize by default (0). |
