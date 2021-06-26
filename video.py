videoMEM = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
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

    print(
        "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\n".format(
            videoMEM[0], videoMEM[1], videoMEM[2], videoMEM[3],
            videoMEM[4], videoMEM[5], videoMEM[6], videoMEM[7],
            videoMEM[8], videoMEM[9], videoMEM[10], videoMEM[11],
            videoMEM[12], videoMEM[13], videoMEM[14], videoMEM[15]
            )
        )
