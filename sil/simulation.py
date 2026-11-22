
import matplotlib.pyplot as plt

from vehicle_model.vehicle import Vehicle
from vehicle_model.wheel import Wheel
from vehicle_model.road_model import Road


def run_simulation(road_condition="dry"):

    # Create vehicle, wheel and road
    vehicle = Vehicle(mass=1500.0, speed=20.0)
    wheel = Wheel(radius=0.30, inertia=1.2)
    road = Road(road_condition)

    # Initialise wheel speed for rolling without slipping
    wheel.angular_velocity = vehicle.speed / wheel.radius

    # Simulation parameters
    dt = 0.001
    simulation_time = 2.0
    brake_torque = 900.0
    normal_load = 3750.0
    tyre_stiffness = 40000.0

    # Store simulation data
    time_data = []
    vehicle_speed_data = []
    wheel_speed_data = []
    slip_data = []
    tyre_force_data = []

    print(f"Starting braking simulation on {road_condition} road")
    print("-----------------------------------------------")

    for step in range(int(simulation_time / dt)):

        current_time = step * dt

        # Apply braking torque
        wheel.apply_brake(brake_torque)

        # Calculate braking slip ratio as a fraction
        if vehicle.speed > 0.1:
            slip_ratio = (
                vehicle.speed - wheel.calculate_peripheral_speed()
            ) / vehicle.speed
        else:
            slip_ratio = 0.0

        # Restrict slip to the braking range
        slip_ratio = max(0.0, min(slip_ratio, 1.0))

        # Calculate tyre force from wheel slip
        tyre_force = road.calculate_tyre_force(
            slip_ratio=slip_ratio,
            normal_load=normal_load,
            tyre_stiffness=tyre_stiffness
        )

        # Update wheel dynamics
        wheel.update(
            drive_torque=0.0,
            tyre_force=tyre_force,
            dt=dt
        )

        # One representative wheel models one quarter
        # of the vehicle's four-wheel braking force.
        vehicle.update(
            tyre_force=4.0 * tyre_force,
            dt=dt
        )

        # Store results
        time_data.append(current_time)
        vehicle_speed_data.append(vehicle.speed)
        wheel_speed_data.append(wheel.angular_velocity)
        slip_data.append(slip_ratio * 100.0)
        tyre_force_data.append(tyre_force)

    print("-----------------------------------------------")
    print(f"Road condition: {road_condition}")
    print(f"Final vehicle speed: {vehicle.speed:.2f} m/s")
    print(f"Final wheel speed: {wheel.angular_velocity:.2f} rad/s")
    print(f"Final slip ratio: {slip_data[-1]:.2f}%")
    print("Simulation completed")

    return (
        time_data,
        vehicle_speed_data,
        wheel_speed_data,
        slip_data,
        tyre_force_data
    )


def plot_results(results, road_condition):

    time_data, vehicle_speed, wheel_speed, slip, tyre_force = results

    # Plot vehicle and wheel speeds
    plt.figure(figsize=(10, 5))

    plt.plot(time_data, vehicle_speed, label="Vehicle speed (m/s)")
    plt.plot(
        time_data,
        [speed * 0.30 for speed in wheel_speed],
        label="Wheel peripheral speed (m/s)"
    )

    plt.xlabel("Time (seconds)")
    plt.ylabel("Speed (m/s)")
    plt.title(f"Braking Simulation - {road_condition.capitalize()} Road")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig(f"results/{road_condition}_speed.png")
    plt.show()

    # Plot wheel slip
    plt.figure(figsize=(10, 5))

    plt.plot(time_data, slip, label="Wheel slip (%)")

    plt.xlabel("Time (seconds)")
    plt.ylabel("Slip ratio (%)")
    plt.title(f"Wheel Slip - {road_condition.capitalize()} Road")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig(f"results/{road_condition}_slip.png")
    plt.show()

    # Plot tyre force
    plt.figure(figsize=(10, 5))

    plt.plot(time_data, tyre_force, label="Tyre force (N)")

    plt.xlabel("Time (seconds)")
    plt.ylabel("Tyre force (N)")
    plt.title(f"Tyre Force - {road_condition.capitalize()} Road")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig(f"results/{road_condition}_force.png")
    plt.show()


if __name__ == "__main__":

    results = run_simulation("wet")

    plot_results(results, "wet")
