---
name: day-planner
description: A simple daily task planner that helps organize your day with time slots and task management. Use when you need to create, view, or manage daily schedules with time allocations for tasks.
---

# Enhanced Day Planner

A simple daily task planner that helps organize your day with time slots and task management, featuring precise time slot allocation.

## Features

- Creating a simple daily schedule template with time slots
- Adding tasks with specific start and end times
- Basic time-slot allocation with HH:MM-HH:MM format
- Saving/loading daily plans
- Simple text-based interface
- View chronological schedule with time ranges

## Commands

- `/day-planner add "task" HH:MM-HH:MM` - Add a task with specific time slot
- `/day-planner view` - View today's schedule with time slots
- `/day-planner clear` - Clear today's schedule
- `/day-planner remove "task"` - Remove a specific task
- `/day-planner edit "task" HH:MM-HH:MM` - Update an existing task's time slot

## Usage

### Adding Tasks with Time Slots

Add tasks with specific time slots in HH:MM-HH:MM format:

```
/day-planner add "Wake up" 06:00-06:30
/day-planner add "Fajr prayer" 06:30-07:00
/day-planner add "Exercise" 07:00-08:00
/day-planner add "Getting ready for job" 08:00-09:00
/day-planner add "Office work" 09:00-18:00
/day-planner add "Rest" 20:00-21:00
/day-planner add "Skill development" 21:00-22:30
/day-planner add "Sleep" 22:30-06:00
```

### Viewing Schedule

View your current day's schedule with time slots:

```
/day-planner view
```

This will display all scheduled tasks in chronological order with their time slots in the format:
```
HH:MM - HH:MM: Task Description
```

### Removing Tasks

Remove a specific task:

```
/day-planner remove "Meeting"
```

### Editing Tasks

Update an existing task's time slot:

```
/day-planner edit "Exercise" 07:30-08:30
```

### Clearing Schedule

Clear the entire day's schedule:

```
/day-planner clear
```

## Storage

Daily plans are stored in JSON format in `.claude/day-plans/YYYY-MM-DD.json` where YYYY-MM-DD represents the date of the plan.

## Time Format

Times must be in 24-hour format (HH:MM) for consistency and easy sorting. Time slots are defined as HH:MM-HH:MM for start and end times.

## Example Complete Daily Schedule

Here's how to set up a complete daily schedule with time slots:

```
/day-planner add "Wake up" 06:00-06:30
/day-planner add "Fajr prayer" 06:30-07:00
/day-planner add "Exercise" 07:00-08:00
/day-planner add "Getting ready for job" 08:00-09:00
/day-planner add "Office work" 09:00-18:00
/day-planner add "Return home" 18:00-18:30
/day-planner add "Rest" 20:00-21:00
/day-planner add "Skill development" 21:00-22:30
/day-planner add "Sleep" 22:30-06:00
```

This creates a comprehensive daily schedule with specific time allocations for each activity.