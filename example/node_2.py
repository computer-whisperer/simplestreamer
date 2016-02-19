# subscribes to the stream from node 1 and periodically reads the data
import simplestreamer
import time

streamer = simplestreamer.SimpleStreamer(5201)
streamer.subscribe("127.0.0.1", 5200, "streamer 1")
# You can optionally configure the rate at which the remote streamer sends you data
#streamer.subscribe("127.0.0.1", 5200, "streamer 1", updates_per_sec=1.5)

while True:
    print(streamer.get_data("streamer 1"))
    time.sleep(0.5)
