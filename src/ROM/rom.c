#include <stdio.h>
#include <sys/stat.h>

#include "rom.h"

struct Rom new_rom(const char *init_fiel_path, unsigned char init_value) {
    struct Rom rom = {
        0,
        0,
        NULL
    };
    
    FILE *init_file;
    init_file = fopen(init_fiel_path, "r");
    if (init_file == NULL) {
        rom.is_empty = 1;
        return rom;
    }

    struct stat init_file_stat;
    if (fstat(init_file, &init_file_stat) == -1) {
        rom.is_empty = 1;
        return rom;
    }

    rom.data = (unsigned char*)(malloc(init_file_stat.st_size * sizeof(unsigned char)));

    for (off_t i = 0; i < init_file_stat.st_size; i++) {
        rom.data[i] = init_value;
    }

    fread(rom.data, sizeof(unsigned char), init_file_stat.st_size, init_file);
    fclose(init_file);
}