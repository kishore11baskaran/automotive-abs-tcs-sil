from vehicle_model.vehicle import calculate_slip_ratio


def test_normal_braking():
    result = calculate_slip_ratio(20, 50, 0.3)
    assert abs(result - 25.0) < 0.01


def test_no_slip():
    result = calculate_slip_ratio(20, 66.6666667, 0.3)
    assert abs(result) < 0.01


def test_locked_wheel():
    result = calculate_slip_ratio(20, 0, 0.3)
    assert result == 100.0


def test_zero_vehicle_speed():
    result = calculate_slip_ratio(0, 0, 0.3)
    assert result == 0.0


import pytest

from vehicle_model.vehicle import Vehicle


def test_vehicle_initialization():
    vehicle = Vehicle(mass=1500.0, speed=20.0)

    assert vehicle.mass == 1500.0
    assert vehicle.speed == 20.0
    assert vehicle.acceleration == 0.0


def test_vehicle_deceleration():
    vehicle = Vehicle(mass=1500.0, speed=20.0)

    vehicle.update(tyre_force=3000.0, dt=0.1)

    assert vehicle.acceleration == -2.0
    assert vehicle.speed == 19.8


def test_invalid_time_step():
    vehicle = Vehicle()

    with pytest.raises(ValueError):
        vehicle.update(tyre_force=1000.0, dt=0.0)
