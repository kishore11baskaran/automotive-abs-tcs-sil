
#ifndef CONTROLLER_INTERFACE_H
#define CONTROLLER_INTERFACE_H

/* ABS controller configuration */
#define ABS_TARGET_SLIP 15.0f
#define ABS_MAX_SLIP 20.0f
#define ABS_MIN_SLIP 10.0f

#define ABS_MAX_BRAKE_TORQUE 300.0f
#define ABS_MIN_BRAKE_TORQUE 0.0f

/* ABS controller function declaration */
float abs_controller_update(
    float slip_ratio,
    float current_brake_torque
);

#endif
