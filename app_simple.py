import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
from ultralytics import YOLO

with st.spinner("Loading YOLO model..."):
    model = YOLO("yolov8n.pt")

def video_frame_callback(input_frame):
    img = input_frame.to_ndarray(format="bgr24")
    results = model(img)
    annotated_frame = results[0].plot()
    output_frame = input_frame.from_ndarray(annotated_frame, format="bgr24")
    return output_frame

webrtc_streamer(
    key="yolo",
    mode=WebRtcMode.SENDRECV,
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False}
)
