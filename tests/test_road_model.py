
import pytest

from vehicle_model.road_model import Road


def test_dry_road():
    road = Road("dry")
    assert road.friction_coefficient == 0.9


def test_wet_road():
    road = Road("wet")
    assert road.friction_coefficient == 0.5


def test_ice_road():
    road = Road("ice")
    assert road.friction_coefficient == 0.1


def test_max_tyre_force():
    road = Road("wet")

    force = road.calculate_max_tyre_force(4000)

    assert force == 2000


def test_invalid_road():
    with pytest.raises(ValueError):
        Road("mud")


def test_negative_normal_load():
    road = Road("dry")

    with pytest.raises(ValueError):
        road.calculate_max_tyre_force(-100)
def test_wet_road_force_limit():
    road = Road("wet")
    actual_force = road.limit_tyre_force(2500, 3750)
    assert actual_force == 1875.0


def test_negative_force_limit():
    road = Road("wet")
    actual_force = road.limit_tyre_force(-2500, 3750)
    assert actual_force == -1875.0


def test_force_within_limit():
    road = Road("dry")
    actual_force = road.limit_tyre_force(1000, 3750)
    assert actual_force == 1000