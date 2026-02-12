struct decoder {
    unsigned int current_code;

    unsigned short op_code;
    unsigned char  target_register;
    unsigned char  source_register_1;
    unsigned char  source_register_2;
    unsigned char  immediate_number;

    int (*set_code)(struct decoder *self, unsigned int code);
    int (*decode)(struct decoder *self);
};

struct decoder new_decoder() {
    struct result = decoder {
        current_code = 0,
    };
}