
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
import uuid

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(id=str(uuid.uuid4()), name='marvel', description='Marvel Team')
        dc = Team.objects.create(id=str(uuid.uuid4()), name='dc', description='DC Team')

        # Create users
        ironman = User.objects.create(id=str(uuid.uuid4()), name='Iron Man', email='ironman@marvel.com', team='marvel')
        captain = User.objects.create(id=str(uuid.uuid4()), name='Captain America', email='cap@marvel.com', team='marvel')
        batman = User.objects.create(id=str(uuid.uuid4()), name='Batman', email='batman@dc.com', team='dc')
        superman = User.objects.create(id=str(uuid.uuid4()), name='Superman', email='superman@dc.com', team='dc')

        # Create activities
        Activity.objects.create(id=str(uuid.uuid4()), user=ironman, type='run', duration=30, date='2025-12-01')
        Activity.objects.create(id=str(uuid.uuid4()), user=batman, type='cycle', duration=45, date='2025-12-01')

        # Create workouts
        Workout.objects.create(id=str(uuid.uuid4()), name='Pushups', description='Do pushups', difficulty='easy')
        Workout.objects.create(id=str(uuid.uuid4()), name='Squats', description='Do squats', difficulty='medium')

        # Create leaderboard
        Leaderboard.objects.create(id=str(uuid.uuid4()), user=ironman, score=100, rank=1)
        Leaderboard.objects.create(id=str(uuid.uuid4()), user=batman, score=90, rank=2)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
