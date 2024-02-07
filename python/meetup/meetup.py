"""Meetup."""
from datetime import date, timedelta
from typing import Literal

DAYS_OF_THE_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
DAY_OF_WEEK = Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
WEEK_OF_MONTH = Literal["first", "second", "third", "fourth", "fifth", "last", "teenth"]


class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date."""

    def __init__(self, message: str = "That day does not exist."):
        self.message = message
        super().__init__(self.message)


def meetup(year: int, month: int, week: DAY_OF_WEEK, day_of_week: WEEK_OF_MONTH) -> date:
    """Get meetup date by given criteria."""
    potential_dates_of_month = get_month_dates_of_weekday(year, month, day_of_week)
    ordinal_week = ("first", "second", "third", "fourth", "fifth")
    if week in ordinal_week and len(potential_dates_of_month) > ordinal_week.index(week):
        return potential_dates_of_month[ordinal_week.index(week)]
    if week == "last":
        return potential_dates_of_month[-1]
    if week == "teenth":
        for i in range(1, 4):
            if 13 <= potential_dates_of_month[i].day <= 19:
                return potential_dates_of_month[i]

    raise MeetupDayException


def get_month_dates_of_weekday(year: int, month: int, day_of_week: WEEK_OF_MONTH) -> list[date]:
    """Get dates of a given week-day for given month."""
    requested_day_iso_number = DAYS_OF_THE_WEEK.index(day_of_week) + 1
    first_month_day = date(year, month, 1)
    _, _, first_weekday = first_month_day.isocalendar()
    requested_day_delta_from_first_day_of_month = requested_day_iso_number - first_weekday
    if requested_day_delta_from_first_day_of_month < 0:
        requested_day_delta_from_first_day_of_month += 7
    potential_dates = [date(year, month, requested_day_delta_from_first_day_of_month + 1)]
    while True:
        next_date = potential_dates[-1] + timedelta(days=7)
        if next_date.month != potential_dates[0].month:
            break
        potential_dates.append(next_date)

    return potential_dates
