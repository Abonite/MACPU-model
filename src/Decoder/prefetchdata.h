#ifndef __PREFETCHDATA__
    #define __PREFETCHDATA__

    struct DataFetcher {
        int data_need_fetch;
        unsigned int address;
    };

    struct DataFetcher new_datafetcher(struct Decoder *decoder, struct RegisterFile *rf);
#endif