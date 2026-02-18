struct Rom {
    unsigned int size;
    int is_empty;
    unsigned char *data;
}

struct Rom new_rom(const char *init_file_path, unsigned char init_value);