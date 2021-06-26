import video

addr = 0
data = 0


def setOUT(cpuaddr, cpudata):
    global addr
    global data

    addr = cpuaddr
    data = cpudata

    if addr == 0xF900:
        video.setVideo(00, data)
    elif addr == 0xF910:
        video.setVideo(1, data)
