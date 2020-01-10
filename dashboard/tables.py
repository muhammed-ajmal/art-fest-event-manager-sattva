import django_tables2 as tables
from events.models import Participant

class ParticipantTable(tables.Table):
    select = tables.CheckBoxColumn(accessor="pk", orderable=False)
    class Meta:
        model = Participant
        template_name = "django_tables2/bootstrap.html"
        fields = ("select","name",'branch','event','contact','payment' )