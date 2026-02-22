#include "RAM/ram.h"
#include "ROM/rom.h"

struct Storage {
    unsigned long long int ram_start_addr;
    unsigned long long int ram_end_addr;
    struct Ram ram;
    unsigned long long int rom_start_addr;
    unsigned long long int rom_end_addr;
    struct Rom rom;

    unsigned char undefine_value;

    unsigned char* (*read)(struct Storage *self, unsigned int address);
    int (*write)(struct Storage *self, unsigned int address, unsigned int size, unsigned char *data);
};

struct Storage new_storage(unsigned int ram_start_addr, struct Ram ram, unsigned int rom_start_addr, struct Rom rom, unsigned char undefine_value);
unsigned char* storage_meth_read_impl(struct Storage *self, unsigned int address);
int storage_meth_write_impl(struct Storage *self, unsigned int address, unsigned int size, unsigned char *data);