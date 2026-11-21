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