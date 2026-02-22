#include "ProgramCounter.h"

struct ProgramCounter new_programcounter() {
    struct ProgramCounter result = {
        0,
        programcounter_meth_operate_impl,
        programcounter_meth_reset_impl
    };

    return result;
};

int programcounter_meth_operate_impl(struct ProgramCounter *self, int value) {
    self->current_value = self->current_value + (unsigned int)value;
}

int programcounter_meth_reset_impl(struct ProgramCounter *self, int value) {
    self->current_value = (unsigned int)value;
};