import encoder
import pycpu_core
import mem


if __name__ == "__main__":
    encoder.encodefile()
    pycpu_core.startcpu()

    for i in range(0, len(mem.getVal("mem")), 16):
        print(
            "{}-{}: {} {} {} {} {} {} {} {}, {} {} {} {} {} {} {} {}".format(
                "{:04X}".format(i), "{:04X}".format(i + 16),
                "{:04X}".format(mem.getVal("mem")[i]),
                "{:04X}".format(mem.getVal("mem")[i + 1]),
                "{:04X}".format(mem.getVal("mem")[i + 2]),
                "{:04X}".format(mem.getVal("mem")[i + 3]),
                "{:04X}".format(mem.getVal("mem")[i + 4]),
                "{:04X}".format(mem.getVal("mem")[i + 5]),
                "{:04X}".format(mem.getVal("mem")[i + 6]),
                "{:04X}".format(mem.getVal("mem")[i + 7]),
                "{:04X}".format(mem.getVal("mem")[i + 8]),
                "{:04X}".format(mem.getVal("mem")[i + 9]),
                "{:04X}".format(mem.getVal("mem")[i + 10]),
                "{:04X}".format(mem.getVal("mem")[i + 11]),
                "{:04X}".format(mem.getVal("mem")[i + 12]),
                "{:04X}".format(mem.getVal("mem")[i + 13]),
                "{:04X}".format(mem.getVal("mem")[i + 14]),
                "{:04X}".format(mem.getVal("mem")[i + 15])
                )
            )
