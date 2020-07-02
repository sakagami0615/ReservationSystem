from django.views import generic
from . import mixins


def test(request):
	from django.http import HttpResponse
	return HttpResponse('Helllo World')


class WeekCalendar(mixins.WeekCalendarMixin, generic.TemplateView):

    template_name = 'crs/week.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context