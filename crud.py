from django.db import transaction

@require_http_methods(["POST"])
def handle_commit(request):
    data = request.json()
    with transaction.atomic():
        for person_data in data.get('add', []):
            Person.objects.create(**person_data)
        for person_data in data.get('update', []):
            person_id = person_data.pop('id', None)
            if person_id:
                Person.objects.filter(id=person_id).update(**person_data)
        for person_id in data.get('delete', []):
            Person.objects.filter(id=person_id).delete()
    people = list(Person.objects.all().values())
    return JsonResponse(people, safe=False)
