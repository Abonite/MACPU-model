from SystemTop import SystemTop
from src.CpuException import ExitError


if __name__ == "__main__":
    clk_num = 4096
    system = SystemTop(clk_num)
    while clk_num > 0:
        try:
            system.risingEdge()
        except ExitError:
            break
        clk_num -= 1

    system.memory.ram.printInLine()
