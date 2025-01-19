class DigitalCounter:
    def __init__(self, min_value=0, max_value=100, initial_value=0):
        if min_value > max_value:
            raise ValueError("Minimum value cannot be greater than maximum value.")
        if not (min_value <= initial_value <= max_value):
            raise ValueError("Initial value must be within the range of min_value and max_value.")

        self.min_value = min_value
        self.max_value = max_value
        self.current_value = initial_value

    def set_min_value(self, min_value):
        if min_value > self.max_value:
            raise ValueError("Minimum value cannot be greater than maximum value.")
        if self.current_value < min_value:
            raise ValueError("Current value cannot be less than the new minimum value.")
        self.min_value = min_value

    def set_max_value(self, max_value):
        if max_value < self.min_value:
            raise ValueError("Maximum value cannot be less than minimum value.")
        if self.current_value > max_value:
            raise ValueError("Current value cannot be greater than the new maximum value.")
        self.max_value = max_value

    def set_initial_value(self, initial_value):
        if not (self.min_value <= initial_value <= self.max_value):
            raise ValueError("Initial value must be within the range of min_value and max_value.")
        self.current_value = initial_value

    def step_up(self):
        if self.current_value >= self.max_value:
            raise ValueError("Counter has reached its maximum value.")
        self.current_value += 1

    def step_down(self):
        if self.current_value <= self.min_value:
            raise ValueError("Counter has reached its minimum value.")
        self.current_value -= 1

    def get_value(self):
        return self.current_value


counter = DigitalCounter(min_value=0, max_value=10, initial_value=5)
counter.step_up()
counter.step_down()
print(counter.get_value())
