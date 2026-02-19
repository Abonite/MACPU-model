#ifndef __RAM__
    #define __RAM__
    struct Ram {
        unsigned int size;
        unsigned char *data;
    };

    struct Ram new_ram(unsigned int ram_size, unsigned char init_value);
#endif