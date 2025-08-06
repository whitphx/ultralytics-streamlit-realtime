# Streamlit app for real-time YOLO object detection

Streamlit sample apps for real-time YOLO object detection using [Ultralytics YOLO](https://docs.ultralytics.com/).

| Samples   |   |
| --- | --- |
| [`app_simple.py`](./app_simple.py) (~20 LoC) | [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ultralytics-realtime-simple.streamlit.app/) |
| [`app.py`](./app.py) (~50 LoC) | [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ultralytics-realtime.streamlit.app/) |



## Deployment on Streamlit Community Cloud

When deploying this app on Streamlit Community Cloud,
you should be aware of some points:

### Configure STUN/TURN server
You need to configure a STUN/TURN server for WebRTC. Read [Streamlit WebRTC documentation](https://github.com/whitphx/streamlit-webrtc) for more details.

The easiest way is to set up a Twilio account to use its STUN/TURN server, get your Twilio credentials, and set the following environment variables in your Streamlit app:
```
TWILIO_ACCOUNT_SID = "..."
TWILIO_AUTH_TOKEN = "..."
```

### Configure Ultralytics library
You should set the `YOLO_CONFIG_DIR` environment variable to a writable directory, for example `/tmp/.config/Ultralytics`. This is `ultralytics` library's issue.

```
YOLO_CONFIG_DIR = "/tmp/.config/Ultralytics"
```

Otherwise, you will see the following warning message in the logs, and YOLO execution will fail in the first run:
```
WARNING ⚠️ user config directory '/home/appuser/.config/Ultralytics' is not writeable, defaulting to '/tmp' or CWD.Alternatively you can define a YOLO_CONFIG_DIR environment variable for this path.
```
