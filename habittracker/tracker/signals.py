from django.db.models.signals import post_save
from django.dispatch import receiver
from tracker.models import Habit  # Import Habit directly

@receiver(post_save, sender=Habit)  # Specify Habit as the sender
def send_reminder(sender, instance, **kwargs):
    """
    Sends a reminder when a Habit instance is saved.
    """
    reminder_time = instance.reminder_time  # Ensure 'reminder_time' is a field in the Habit model
    if reminder_time:
        print(f"Reminder: Complete your habit '{instance.name}' at {reminder_time} today!")
