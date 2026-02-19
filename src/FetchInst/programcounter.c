#include "ProgramCounter.h"

struct ProgramCounter new_programcounter() {
    struct ProgramCounter result = {
        0,
        meth_operate_impl,
        meth_reset_impl
    };

    return result;
};

int meth_operate_impl(struct ProgramCounter *self, int value) {
    self->current_value = self->current_value + (unsigned int)value;
}

int meth_reset_impl(struct ProgramCounter *self, int value) {
    self->current_value = (unsigned int)value;
};