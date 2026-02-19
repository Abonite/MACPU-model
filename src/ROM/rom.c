#include <stdio.h>
#include <stdlib.h>

#include "rom.h"

struct Rom new_rom(const char *init_file_path, unsigned char init_value, unsigned int size) {
    struct Rom rom = {
        size,
        0,
        NULL
    };
    
    FILE *init_file;
    init_file = fopen(init_file_path, "r");
    if (init_file == NULL) {
        rom.is_empty = 1;
        return rom;
    }

    rom.data = (unsigned char*)(malloc(size * sizeof(unsigned char)));

    for (unsigned int i = 0; i < size; i++) {
        rom.data[i] = init_value;
    }

    fpos_t current_fops;
    fgetpos(init_file, &current_fops);
    fseek(init_file, 0, SEEK_END);
    long file_size = ftell(init_file);
    fsetpos(init_file, &current_fops);

    if (file_size > (long)size) {
        rom.is_empty = 1;
        return rom;
    }

    fread(rom.data, sizeof(unsigned char), file_size, init_file);
    fclose(init_file);
    return rom;
}