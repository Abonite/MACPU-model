#include <stdio.h>
#include <stdlib.h>

#define __32bit__

#include "FetchInst/Programcounter.h"
#include "Decoder/decoder.h"
#include "Decoder/prefetchdata.h"
#include "ALU/alu.h"
#include "ALU/registerfile.h"
#include "ROM/rom.h"
#include "RAM/ram.h"
#include "storage.h"

int main(int argc, char *argv[]) {
    char *init_file_path = "C:\\Users\\Habus\\Documents\\Code\\C\\MACPU-model\\docs\\test.bo";

    struct Rom rom = new_rom(init_file_path, 0x00, 65536);
    struct Ram ram = new_ram(8192, 0x00);
    struct Storage storage = new_storage(0, ram, 0xFFFFFFFF - 65535, rom, 0xFF);

    struct ProgramCounter pc = new_programcounter();
    struct Decoder decoder = new_decoder();
    struct RegisterFile register_file = new_registerfile();

    pc.reset(&pc, -4);

    char *fetch_data;
    while (1) {
        char *data = storage.read(&storage, pc.current_value);
        pc.operate(&pc, 4);
        struct CheckResult result = decoder.decode(&decoder, data);

        struct DataFetcher data_fetcher;
        if (result.check_pass) {
            data_fetcher = new_datafetcher(&decoder, &register_file);
        } else if (result.is_fatal) {
            printf("[FATAL]: code: %s;\n", result.err_type);
            register_file.write(&register_file, 4, result.err_type);
            decoder.reg_target = 0b111111;
            decoder.reg_source_0 = 0b111111;
            decoder.reg_source_1 = 0b111111;
            decoder.p = 0b1000;
            decoder.op_code = 0b1100000000; // JMP [0xFFFFFFF8]
            data_fetcher = new_datafetcher(&decoder, &register_file);
        } else {
            printf("[ERROR]: code: %s;\n", result.err_type);
            break;
        }

        unsigned int fetched_immediate_number = 0;
        if (data_fetcher.data_need_fetch) {
            fetch_data = storage.read(&storage, data_fetcher.address);
            for (int i = 3; i >= 0; i--) {
                fetched_immediate_number = fetched_immediate_number | (fetch_data[i] << (i * 8));
            }
        }

        integer_caculate_unit(&decoder, fetched_immediate_number, &pc, &register_file);
    }

    printf("Due to the early error, cpu stop.");
    return 1;
}