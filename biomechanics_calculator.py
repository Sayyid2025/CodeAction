# Biomechanics Calculator for Human Action Analysis

"""
This calculator provides advanced metrics for analyzing human actions in biomechanical studies.
"""

class BiomechanicsCalculator:
    def __init__(self):
        pass

    def calculate_velocity(self, initial_position, final_position, time):
        """Calculate velocity given initial and final position and time"""
        if time <= 0:
            raise ValueError("Time must be greater than zero.")
        return (final_position - initial_position) / time

    def calculate_acceleration(self, initial_velocity, final_velocity, time):
        """Calculate acceleration given initial and final velocity and time"""
        if time <= 0:
            raise ValueError("Time must be greater than zero.")
        return (final_velocity - initial_velocity) / time

    def calculate_force(self, mass, acceleration):
        """Calculate force using Newton's second law"""
        return mass * acceleration

    def calculate_energy(self, mass, velocity):
        """Calculate kinetic energy"""
        return 0.5 * mass * (velocity ** 2)

    def calculate_work(self, force, distance):
        """Calculate work done"""
        return force * distance

# Example usage
if __name__ == '__main__':
    bc = BiomechanicsCalculator()
    print(bc.calculate_velocity(0, 10, 2))  # Should output 5.0
    print(bc.calculate_acceleration(0, 10, 2))  # Should output 5.0
    print(bc.calculate_force(70, 5))  # Should output 350
    print(bc.calculate_energy(70, 5))  # Should output 875.0
    print(bc.calculate_work(350, 10))  # Should output 3500
