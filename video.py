videoMEM = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ]

videoCTRreg = 0


def setVideo(addr, data):
    global videoCTRreg
    global videoMEM

    if addr == 0:
        videoCTRreg = data
    else:
        videoMEM[addr - 1] = data

    videoMEM = [" " for i in videoMEM if i == 0]

    if videoCTRreg == 0x80:
        print(
            "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\n".format(
                str(videoMEM[0]), str(videoMEM[1]), str(videoMEM[2]), str(videoMEM[3]),
                str(videoMEM[4]), str(videoMEM[5]), str(videoMEM[6]), str(videoMEM[7]),
                str(videoMEM[8]), str(videoMEM[9]), str(videoMEM[10]), str(videoMEM[11]),
                str(videoMEM[12]), str(videoMEM[13]), str(videoMEM[14]), str(videoMEM[15])
                )
            )
