"""Small, reusable solar-energy estimation helpers.

The calculation is intentionally simple: energy (kWh) is estimated from
solar irradiance, panel area, efficiency, and sunlight duration.
"""


def estimate_energy_kwh(
    irradiance_w_m2: float,
    panel_area_m2: float,
    efficiency: float,
    sunlight_hours: float,
) -> float:
    """Estimate generated energy in kWh from basic panel parameters."""
    values = (irradiance_w_m2, panel_area_m2, efficiency, sunlight_hours)
    if any(value < 0 for value in values):
        raise ValueError("Solar inputs cannot be negative.")
    if efficiency > 1:
        raise ValueError("Efficiency must be between 0 and 1.")

    energy_wh = irradiance_w_m2 * panel_area_m2 * efficiency * sunlight_hours
    return energy_wh / 1000
