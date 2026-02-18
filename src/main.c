#include <stdio.h>
#include <stdlib.h>

#define __32bit__

#include "Decoder/decoder.h"
#include "ROM/rom.h"

int main(int argc, char *argv[]) {
    char *init_file_path = NULL;
    int ram_size = 0;

    for (int i = 0; i < argc; i++) {
        if (argv[i] == "--rom") {
            init_file_path = argv[i + 1];
        } else if (argv[i] == "--ram-size") {
            ram_size = atoi(argv[i + 1]);
        } else if (argv[i] == "--rom-start-addr") {
            ram_size = atoi(argv[i + 1]);
        }
    }

    struct Decoder decoder = new_decoder();

    struct CheckResult result = decoder.decode(&decoder, 0);
}