
from vehicle_model.vehicle import Vehicle
from vehicle_model.wheel import Wheel
from vehicle_model.road_model import Road


def run_simulation():
    # Create vehicle, wheel and road
    vehicle = Vehicle(mass=1500.0, speed=20.0)
    wheel = Wheel(radius=0.30, inertia=1.2)
    road = Road("dry")
    # Initialise wheel speed for rolling without slipping
    wheel.angular_velocity = vehicle.speed / wheel.radius

    # Simulation parameters
    dt = 0.01
    simulation_time = 2.0
    brake_torque = 300.0
    normal_load = 3750.0

    print("Starting vehicle braking simulation")
    print("------------------------------------")

    for step in range(int(simulation_time / dt)):

        # Apply braking torque
        wheel.apply_brake(brake_torque)

        # Calculate tyre force limit
        max_tyre_force = road.calculate_max_tyre_force(
            normal_load
        )

        # Use a simplified requested braking force
        requested_force = brake_torque / wheel.radius

        tyre_force = road.limit_tyre_force(
            requested_force,
            normal_load
        )

        # Update wheel and vehicle
        wheel.update(
            drive_torque=0.0,
            tyre_force=tyre_force,
            dt=dt
        )

        vehicle.update(
            tyre_force=tyre_force,
            dt=dt
        )

        if step % 50 == 0:
            print(
                f"Time: {step * dt:.2f}s | "
                f"Vehicle speed: {vehicle.speed:.2f} m/s | "
                f"Wheel speed: {wheel.angular_velocity:.2f} rad/s"
            )

    print("------------------------------------")
    print("Simulation completed")


if __name__ == "__main__":
    run_simulation()
