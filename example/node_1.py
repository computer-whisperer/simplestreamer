# just dumps time data into the streamer at 100 hz
import simplestreamer
import time

streamer = simplestreamer.SimpleStreamer(5200)

while True:
    streamer.send_data({"current time.time()": time.time()})
    time.sleep(0.01)
