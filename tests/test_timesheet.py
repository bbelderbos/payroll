from decimal import Decimal

from pytest import approx


def test_timesheet(timesheet):
    assert timesheet.base_pay == Decimal(500)
    assert timesheet.calculate_due() == Decimal(500)


def test_timesheet_with_advancement(timesheet):
    timesheet.advancements = Decimal(100)
    assert timesheet.base_pay == Decimal(500)
    assert timesheet.calculate_due() == Decimal(400)


def test_timesheet_with_saved(timesheet_with_saves):
    assert timesheet_with_saves.base_pay == Decimal(600)
    assert timesheet_with_saves.calculate_saving() == approx(Decimal(120))
    assert timesheet_with_saves.calculate_due() == approx(Decimal(480))


def test_timesheet_with_saved_and_advancement(timesheet_with_saves):
    timesheet_with_saves.advancements = Decimal(200)
    assert timesheet_with_saves.base_pay == Decimal(600)
    assert timesheet_with_saves.calculate_saving() == approx(Decimal(120))
    assert timesheet_with_saves.calculate_due() == approx(Decimal(280))


def test_timesheet_with_saved_and_overwork(timesheet_with_saves):
    timesheet_with_saves.overwork_hours = 2
    assert timesheet_with_saves.base_pay == Decimal(600)
    assert timesheet_with_saves.calculate_saving() == approx(Decimal(120))
    assert timesheet_with_saves.calculate_overwork() == approx(Decimal(180))
    assert timesheet_with_saves.calculate_due() == approx(Decimal(660))
