from django.core.management.base import BaseCommand
from octofit_tracker import models
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        models.Team.objects.all().delete()
        models.Activity.objects.all().delete()
        models.Leaderboard.objects.all().delete()
        models.Workout.objects.all().delete()

        # Create Teams
        marvel = models.Team.objects.create(name='Marvel')
        dc = models.Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create_user(email='tony@stark.com', username='ironman', team=marvel)
        steve = User.objects.create_user(email='steve@rogers.com', username='captainamerica', team=marvel)
        bruce = User.objects.create_user(email='bruce@wayne.com', username='batman', team=dc)
        clark = User.objects.create_user(email='clark@kent.com', username='superman', team=dc)

        # Create Activities
        models.Activity.objects.create(user=tony, type='Run', duration=30, calories=300)
        models.Activity.objects.create(user=steve, type='Swim', duration=45, calories=400)
        models.Activity.objects.create(user=bruce, type='Cycle', duration=60, calories=500)
        models.Activity.objects.create(user=clark, type='Yoga', duration=20, calories=150)

        # Create Workouts
        models.Workout.objects.create(name='Avenger HIIT', description='High intensity interval training for heroes', team=marvel)
        models.Workout.objects.create(name='Justice Strength', description='Strength training for justice league', team=dc)

        # Create Leaderboard
        models.Leaderboard.objects.create(user=tony, score=1000)
        models.Leaderboard.objects.create(user=steve, score=900)
        models.Leaderboard.objects.create(user=bruce, score=950)
        models.Leaderboard.objects.create(user=clark, score=980)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
