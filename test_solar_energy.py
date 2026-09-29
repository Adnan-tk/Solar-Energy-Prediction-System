from solar_energy import estimate_energy_kwh


def test_estimate_energy_kwh():
    assert estimate_energy_kwh(1000, 10, 0.2, 5) == 10


def test_zero_irradiance_produces_zero_energy():
    assert estimate_energy_kwh(0, 10, 0.2, 5) == 0


def test_efficiency_above_one_is_rejected():
    try:
        estimate_energy_kwh(1000, 10, 1.1, 5)
    except ValueError:
        return
    raise AssertionError("Expected efficiency validation to reject values above 1")
