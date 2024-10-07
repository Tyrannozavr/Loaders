from loaders.models import Loader, Incidents

def is_incident_completed(incident_id: int):
    incident = Incidents.objects.get(pk=incident_id)
    return incident.started_at and incident.finished_at

def process_loader_status(loader_id: int):
    loader = Loader.objects.get(pk=loader_id)
    for incident in loader.incidents.all():
        if not is_incident_completed(incident.id):
            loader.is_active = False
            loader.save()
            return False  # Return False immediately if any incident is not completed

    loader.is_active = True
    loader.save()
    return True



def update_loader_status(incident_id: int):
    incident = Incidents.objects.get(id=incident_id)
    print('update status')
    print(incident.finished_at, bool(incident.finished_at))
    if incident.started_at and not incident.finished_at:
        loader = incident.loader
        loader.is_active = False
        loader.save()
    else:
        process_loader_status(loader_id=incident.loader_id)


