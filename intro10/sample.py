from datetime import date


def diff_days(from_date, to_date):
    """
    - from_date から to_date までの日数を返す。
    - from_date が to_date 以降であれば None を返す。
    """
    if from_date >= to_date:
        return None
    return (to_date - from_date).days


# Usage --
date1 = date(2018, 1, 1)
date2 = date(2018, 1, 6)

print(diff_days(date1, date2))  # => 5
print(diff_days(date2, date1))  # => None
