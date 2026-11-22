#include "controller_interface.h"

#define ABS_TORQUE_STEP 10.0f

float abs_controller_update(
    float slip_ratio,
    float current_brake_torque
)
{
    float new_brake_torque = current_brake_torque;

    if (slip_ratio > ABS_MAX_SLIP)
    {
        new_brake_torque -= ABS_TORQUE_STEP;
    }
    else if (slip_ratio < ABS_MIN_SLIP)
    {
        new_brake_torque += ABS_TORQUE_STEP;
    }
    else
    {
        new_brake_torque = current_brake_torque;
    }

    if (new_brake_torque > ABS_MAX_BRAKE_TORQUE)
    {
        new_brake_torque = ABS_MAX_BRAKE_TORQUE;
    }

    if (new_brake_torque < ABS_MIN_BRAKE_TORQUE)
    {
        new_brake_torque = ABS_MIN_BRAKE_TORQUE;
    }

    return new_brake_torque;
}