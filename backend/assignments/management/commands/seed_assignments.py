from django.core.management.base import BaseCommand
from assignments.models import Assignment
import factory
import factory.django


class AssignmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Assignment

    name = factory.Faker('name')
    description = factory.Faker('text')
    time_starts = factory.Faker('date_time')
    time_required = factory.Faker('date_time')
    parents_notified = factory.Faker('boolean')
    #
    time_added = factory.Faker('date_time')
    time_last_edited = factory.Faker('date_time')


class Command(BaseCommand):
    help = 'Seeds the database with Assignments'

    def add_arguments(self, parser):
        parser.add_argument('--assignments',
                            default=500,
                            type=int,
                            help='The number of fake assignments to create.')

    def handle(self, *args, **options):
        for _ in range(options['assignments']):
            AssignmentFactory.create()
