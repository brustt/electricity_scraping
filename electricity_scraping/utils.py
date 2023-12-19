from datetime import datetime, timedelta




def get_date_range(start_date, n_days):
    for n in range(n_days):
        yield start_date + timedelta(n)

def date_to_string(date: datetime.date, format_date="%d.%m.%Y+00:00"):
    return date.strftime(format_date)
        
def form_url(date: datetime.date, template_url: str):
    return template_url.format(date_to_string(date))

def string_to_date(date_str: str, format_date="%m.%d.%Y+00:00"):
    return datetime.strptime(date_str, format_date)