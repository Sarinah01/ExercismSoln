# Constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Return remaining bake time in minutes."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(layers):
    """Return preparation time for the lasagna based on layers."""
    return layers * PREPARATION_TIME

def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Return total time elapsed for preparation and baking."""
    return preparation_time_in_minutes(layers) + elapsed_bake_time
