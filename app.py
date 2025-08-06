import streamlit as st
from queue import Queue
from streamlit_webrtc import webrtc_streamer, WebRtcMode
from ultralytics import YOLO

player_state = st.session_state.get("player")
busy = player_state and player_state.state.playing or player_state.state.signalling
model_name = st.selectbox(
    "Select YOLO model",
    options=["yolo11n.pt", "yolo11s.pt", "yolo11m.pt", "yolov8n.pt", "yolov8s.pt", "yolov8m.pt"],
    disabled=busy
)

with st.spinner(f"Loading model {model_name}..."):
    model = YOLO(model_name)

info_queue = Queue()

def video_frame_callback(input_frame):
    img = input_frame.to_ndarray(format="bgr24")
    results = model(img)
    annotated_frame = results[0].plot()
    info_queue.put({
        "speed": results[0].speed,
        "summary": results[0].summary()
    })
    output_frame = input_frame.from_ndarray(annotated_frame, format="bgr24")
    return output_frame

ctx = webrtc_streamer(
    key="player",
    mode=WebRtcMode.SENDRECV,
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False}
)

info_area = st.empty()

while ctx.state.playing:
    info = info_queue.get()

    with info_area.container():
        st.subheader("Speed")
        st.write(info["speed"])
        st.subheader("Summary")
        st.write(info["summary"])
