from historical_assistant.main.models import War
def to_delete():
    for i in range(124, 352):
        War.objects.filter(id=i).delete()