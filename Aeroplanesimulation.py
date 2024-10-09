# Import the necessary libraries
import math

class Airplane:
    def __init__(self):
        self.altitude = 0  # Initial altitude
        self.speed = 0  # Initial speed
        self.heading = 0  # Initial heading (in degrees)

    def take_off(self):
        self.speed = 50  # Increase speed to 50 knots
        self.altitude = 100  # Climb to 100 feet

    def climb(self, rate):
        self.altitude += rate  # Climb at the specified rate (feet per minute)

    def descend(self, rate):
        self.altitude -= rate  # Descend at the specified rate (feet per minute)

    def turn(self, direction, degrees):
        self.heading += degrees  # Turn in degrees (positive for right, negative for left)

    def level_off(self):
        self.speed = 150  # Level off at 150 knots

    def land(self):
        self.speed = 0  # Reduce speed to 0
        self.altitude = 0  # Descend to 0 feet

# Create an instance of the Airplane class
airplane = Airplane()

# Simulate a flight
airplane.take_off()
print("Taking off...")

airplane.climb(500)  # Climb at 500 feet per minute
print("Climbing...")

airplane.turn(30)  # Turn 30 degrees right
print("Turning right...")

airplane.level_off()
print("Leveling off...")

airplane.descend(200)  # Descend at 200 feet per minute
print("Descending...")

airplane.land()
print("Landing...")
