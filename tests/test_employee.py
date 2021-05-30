import pytest

from payroll.employee import Employee


def test_employee_rate_validation(company):
    expected_error = "Employee has either hourly or fixed rate"
    with pytest.raises(ValueError, match=expected_error):
        Employee(47, 'Henry', company, 10, 20_000)
    Employee(47, 'Henry', company, 0, 20_000)
