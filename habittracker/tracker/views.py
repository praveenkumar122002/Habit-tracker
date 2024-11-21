from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import Habit, HabitCompletion, HabitStreak
from .forms import HabitForm
from datetime import date
from django.utils.timezone import now

def register(request):
    """
    Register a new user and log them in.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('dashboard')  # Redirect to the dashboard after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    """
    Display the dashboard with the user's habits.
    """
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'tracker/dashboard.html', {'habits': habits})

@login_required
def add_habit(request):
    if request.method == 'POST':
        # Get data from the form
        description = request.POST.get('description', '').strip()
        
        # Check if description is not empty
        if description:
            # Save the new habit to the database
            Habit.objects.create(
                user=request.user,  # Associate with logged-in user
                description=description,
                status='ongoing'   # Default status
            )
            return redirect('dashboard')  # Redirect to the dashboard
        
    # Render the form if GET or invalid POST
    return render(request, 'tracker/add_habit.html')


@login_required
def edit_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)

    if request.method == 'POST':
        description = request.POST.get('description', '').strip()

        if description:
            habit.description = description
            habit.save()  # Save changes to the habit
            return redirect('dashboard')  # Redirect to dashboard after saving changes

    return render(request, 'tracker/edit_habit.html', {'habit': habit})

@login_required
def mark_complete(request, habit_id):
    """
    Mark a habit as completed for today and update the streak.
    """
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    # Check if completion already exists for today
    completion, created = HabitCompletion.objects.get_or_create(
        habit=habit,
        date_completed=date.today()
    )

    # Update the streak
    streak, _ = HabitStreak.objects.get_or_create(habit=habit)
    streak.update_streak(completed_today=created)

    return redirect('dashboard')

@login_required
def mark_habit_completed(request, habit_id):
    """
    Mark a habit as completed and update its status and last completed date.
    """
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    habit.status = 'finished'
    habit.last_completed_date = now().date()  # Update the last completed date
    habit.save()

    # Optional: Update streaks
    streak, _ = HabitStreak.objects.get_or_create(habit=habit)
    streak.update_streak(completed_today=True)

    return redirect('dashboard')  # Redirect to the dashboard

@login_required
def delete_habit(request, habit_id):
    """
    Delete a habit belonging to the logged-in user.
    """
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        habit.delete()
        return redirect('dashboard')

    # Render confirmation page if not a POST request
    return render(request, 'tracker/confirm_delete.html', {'habit': habit})

@login_required
def update_status(request, habit_id, new_status):
    # Get the habit by ID
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)

    # Update the status based on the action
    if new_status in ['not-completed', 'finished', 'ongoing']:
        habit.status = new_status
    
    habit.save()  # Save the changes to the database

    # Redirect back to the dashboard
    return redirect('dashboard')
def custom_logout_view(request):
    logout(request)
    return redirect('login')




