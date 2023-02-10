from abc import ABC, abstractmethod


def add_years_to_date(original_date, years_to_add):
    result = original_date.replace(year=original_date.year + years_to_add)
    return result


class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass

