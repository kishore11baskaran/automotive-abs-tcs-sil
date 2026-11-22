def calculate_slip_ratio(vehicle_speed, wheel_speed, wheel_radius):
    """
    Calculate braking wheel slip ratio.

    Args:
        vehicle_speed: Vehicle speed in m/s
        wheel_speed: Wheel angular velocity in rad/s
        wheel_radius: Wheel radius in metres

    Returns:
        Slip ratio as a percentage
    """

    if vehicle_speed <= 0:
        return 0.0

    wheel_peripheral_speed = wheel_speed * wheel_radius

    slip_ratio = (
        (vehicle_speed - wheel_peripheral_speed)
        / vehicle_speed
    )

    return slip_ratio * 100


# Example calculation
vehicle_speed = 20.0
wheel_speed = 33.33
wheel_radius = 0.30

slip = calculate_slip_ratio(
    vehicle_speed,
    wheel_speed,
    wheel_radius
)

print(f"Wheel Slip Ratio: {slip:.2f}%")


class Vehicle:
    def __init__(self, mass=1500.0, speed=20.0):
        self.mass = mass
        self.speed = speed
        self.acceleration = 0.0

    def update(self, tyre_force, dt):
        if dt <= 0:
            raise ValueError("Time step must be positive")

        self.acceleration = -tyre_force / self.mass

        self.speed += self.acceleration * dt

        # Vehicle cannot move backwards in this simplified model.
        self.speed = max(0.0, self.speed)

        
