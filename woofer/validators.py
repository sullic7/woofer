from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_date(date):
    """ Check if turning the date into a string throws an error. """
    try:
        date.strftime("%d/%m/%y")
    except ValueError:
        raise ValidationError(
            _('%(date)s is not a valid date of the form YYYY-MM-DD.'),
            params={'date': date.isoformat()},
        )
def validate_greater_than_or_equal_zero(value):
    """ Check if the value is at least 0. """
    if value < 0:
        raise ValidationError(_("This value must be at least 0."))
        