from SystemTop import SystemTop


if __name__ == "__main__":
    clk_num = 2048
    system = SystemTop(clk_num)
    while clk_num > 0:
        system.risingEdge()
        clk_num -= 1
