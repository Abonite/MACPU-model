#include <stdio.h>
#include <stdlib.h>

#define __32bit__

#include "FetchInst/Programcounter.h"
#include "Decoder/decoder.h"
#include "ROM/rom.h"
#include "RAM/ram.h"
#include "storage.h"

int main(int argc, char *argv[]) {
    char *init_file_path = "H:\\Code\\MACPU-model\\docs\\test.bo";

    struct Rom rom = new_rom(init_file_path, 0x00, 65536);
    struct Ram ram = new_ram(8192, 0x00);
    struct Storage storage = new_storage(0, ram, 0xFFFFFFFF - 65535, rom, 0xFF);

    struct ProgramCounter pc = new_programcounter();
    struct Decoder decoder = new_decoder();

    pc.reset(&pc, -4);

    while (1) {
        char *data = storage.read(&storage, pc.current_value);
        struct CheckResult result = decoder.decode(&decoder, data);
        pc.operate(&pc, 4);
    }
}