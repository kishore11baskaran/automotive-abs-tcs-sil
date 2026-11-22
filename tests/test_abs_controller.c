#include <stdio.h>
#include "../controllers/controller_interface.h"

int main(void)
{
    float torque;

    /* Test 1: Excessive slip */
    torque = abs_controller_update(30.0f, 200.0f);
    printf("High slip: %.2f Nm\n", torque);

    /* Test 2: Normal slip */
    torque = abs_controller_update(15.0f, 200.0f);
    printf("Normal slip: %.2f Nm\n", torque);

    /* Test 3: Low slip */
    torque = abs_controller_update(5.0f, 200.0f);
    printf("Low slip: %.2f Nm\n", torque);

    return 0;
}