
from vehicle_model.wheel import Wheel


def test_wheel_initialization():
    wheel = Wheel()

    assert wheel.radius == 0.30
    assert wheel.inertia == 1.2
    assert wheel.angular_velocity == 0.0


def test_peripheral_speed():
    wheel = Wheel()
    wheel.angular_velocity = 20.0

    assert wheel.calculate_peripheral_speed() == 6.0


def test_brake_torque():
    wheel = Wheel()
    wheel.apply_brake(100.0)

    assert wheel.brake_torque == 100.0


def test_wheel_update():
    wheel = Wheel()
    wheel.angular_velocity = 20.0

    wheel.update(
        drive_torque=0.0,
        tyre_force=0.0,
        dt=0.1
    )

    assert wheel.angular_velocity == 20.0
