
class Wheel:
    def __init__(self, radius=0.30, inertia=1.2):

        if radius <= 0:
            raise ValueError("Wheel radius must be positive")

        if inertia <= 0:
            raise ValueError("Wheel inertia must be positive")

        self.radius = radius
        self.inertia = inertia
        self.angular_velocity = 0.0
        self.brake_torque = 0.0

    def calculate_peripheral_speed(self):
        return self.angular_velocity * self.radius

    def apply_brake(self, torque):
        self.brake_torque = max(0.0, torque)

    def update(self, drive_torque, tyre_force, dt):

        if dt <= 0:
            raise ValueError("Time step must be positive")

        net_torque = (
            drive_torque
            - self.brake_torque
            - tyre_force * self.radius
        )

        angular_acceleration = net_torque / self.inertia

        self.angular_velocity += angular_acceleration * dt

        self.angular_velocity = max(0.0, self.angular_velocity)

