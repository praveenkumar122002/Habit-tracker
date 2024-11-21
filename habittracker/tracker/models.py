from django.contrib.auth.models import User
from django.db import models
from datetime import date, timedelta

class Habit(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('not-completed', 'Not Completed'),
        ('finished', 'Finished'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reminder_time = models.TimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ongoing',
    )

    def __str__(self):
        return self.name

class HabitCompletion(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date_completed = models.DateField()

    class Meta:
        unique_together = ('habit', 'date_completed')

    def __str__(self):
        return f"{self.habit.name} completed on {self.date_completed}"

class HabitStreak(models.Model):
    habit = models.OneToOneField(Habit, on_delete=models.CASCADE)
    current_streak = models.IntegerField(default=0)
    longest_streak = models.IntegerField(default=0)

    def update_streak(self, completed_today):
        yesterday = date.today() - timedelta(days=1)
        last_completion = HabitCompletion.objects.filter(habit=self.habit).order_by('-date_completed').first()

        if last_completion and last_completion.date_completed == yesterday:
            self.current_streak += 1
        elif not completed_today:
            self.current_streak = 0

        self.longest_streak = max(self.longest_streak, self.current_streak)
        self.save()
