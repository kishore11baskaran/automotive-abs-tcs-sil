
class Road:
    ROAD_CONDITIONS = {
        "dry": 0.9,
        "wet": 0.5,
        "snow": 0.2,
        "ice": 0.1
    }

    def __init__(self, condition="dry"):
        if condition not in self.ROAD_CONDITIONS:
            raise ValueError("Invalid road condition")

        self.condition = condition
        self.friction_coefficient = self.ROAD_CONDITIONS[condition]

    def calculate_max_tyre_force(self, normal_load):
        if normal_load < 0:
            raise ValueError("Normal load cannot be negative")

        return self.friction_coefficient * normal_load

    def limit_tyre_force(self, requested_force, normal_load):
        max_force = self.calculate_max_tyre_force(normal_load)

        return max(
            -max_force,
            min(requested_force, max_force)
        )


# Example calculation
if __name__ == "__main__":
    road = Road("wet")

    actual_force = road.limit_tyre_force(
        requested_force=2500,
        normal_load=3750
    )

    print(f"Actual tyre force: {actual_force}")
