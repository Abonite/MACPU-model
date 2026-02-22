#ifndef __PROGRAMCOUNTER__
    #define __PROGRAMCOUNTER__

    struct ProgramCounter {
        unsigned int current_value;

        int (*operate)(struct ProgramCounter *self, int value);
        int (*reset)(struct ProgramCounter *self, int value);
    };

    struct ProgramCounter new_programcounter();
    int programcounter_meth_operate_impl(struct ProgramCounter *self, int value);
    int programcounter_meth_reset_impl(struct ProgramCounter *self, int value);
#endif