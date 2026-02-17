#ifdef __32bit__
    struct Decoder {
        unsigned char reg_A;

        unsigned char bit16_imme;
        unsigned char mid_p;
        unsigned char reg_B;
        unsigned char C_is_imme;
        unsigned char reg_C;

        int (*decode)(struct Decoder *self,int source_code);
    }

    struct Decoder new_decoder();

    int meth_decode_impl(struct Decoder *self, int source_code);
#endif