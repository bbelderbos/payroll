import pytest

from payroll.employee import Employee


def test_employee_rate_validation(company):
    expected_error = "If not hourly employee set a fixed rate"
    with pytest.raises(ValueError, match=expected_error):
        Employee(47, company, 'Henry', 10_000, False)
    Employee(47, company, 'Henry', 10_000, False, 100_000)
