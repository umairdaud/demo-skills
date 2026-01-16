#!/usr/bin/env python3
"""
Day Planner Script

A simple daily task planner that manages tasks with time slots.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

def get_plan_file():
    """Get the path to today's plan file."""
    today = datetime.now().strftime('%Y-%m-%d')
    plan_dir = Path('.claude/day-plans')
    plan_dir.mkdir(exist_ok=True)
    return plan_dir / f'{today}.json'

def load_plan():
    """Load today's plan from file."""
    plan_file = get_plan_file()
    if plan_file.exists():
        with open(plan_file, 'r') as f:
            return json.load(f)
    return []

def save_plan(plan):
    """Save today's plan to file."""
    plan_file = get_plan_file()
    with open(plan_file, 'w') as f:
        json.dump(plan, f, indent=2)

def add_task(task, time_slot):
    """Add a task with time slot to today's plan."""
    plan = load_plan()

    # Validate time slot format (HH:MM-HH:MM)
    if '-' not in time_slot:
        print(f"Error: Time slot must be in HH:MM-HH:MM format, got: {time_slot}")
        return

    start_time, end_time = time_slot.split('-')

    # Validate time format (HH:MM)
    try:
        datetime.strptime(start_time, '%H:%M')
        datetime.strptime(end_time, '%H:%M')
    except ValueError:
        print(f"Error: Time must be in HH:MM format, got: {start_time} or {end_time}")
        return

    # Check for overlapping times
    for item in plan:
        existing_start, existing_end = item['time_slot'].split('-')
        if (start_time < existing_end and end_time > existing_start):
            print(f"Warning: Time slot {time_slot} overlaps with existing task '{item['task']}' ({item['time_slot']})")

    plan.append({
        'task': task,
        'time_slot': time_slot,
        'added_at': datetime.now().isoformat()
    })

    # Sort by start time
    plan.sort(key=lambda x: x['time_slot'].split('-')[0])

    save_plan(plan)
    print(f"Added task: '{task}' with time slot {time_slot}")

def view_plan():
    """Display today's plan."""
    plan = load_plan()

    if not plan:
        print("No tasks scheduled for today.")
        return

    print("Today's Schedule:")
    print("-" * 50)
    for item in plan:
        print(f"{item['time_slot']}: {item['task']}")

def remove_task(task_name):
    """Remove a task from today's plan."""
    plan = load_plan()

    original_length = len(plan)
    plan = [item for item in plan if item['task'].lower() != task_name.lower()]

    if len(plan) == original_length:
        print(f"Task '{task_name}' not found in today's plan.")
    else:
        save_plan(plan)
        print(f"Removed task: '{task_name}'")

def edit_task(task_name, new_time_slot):
    """Edit a task's time slot."""
    plan = load_plan()

    task_found = False
    for item in plan:
        if item['task'].lower() == task_name.lower():
            item['time_slot'] = new_time_slot
            task_found = True
            break

    if task_found:
        # Sort by start time
        plan.sort(key=lambda x: x['time_slot'].split('-')[0])
        save_plan(plan)
        print(f"Updated task '{task_name}' with new time slot: {new_time_slot}")
    else:
        print(f"Task '{task_name}' not found in today's plan.")

def clear_plan():
    """Clear today's plan."""
    plan_file = get_plan_file()
    if plan_file.exists():
        plan_file.unlink()
        print("Cleared today's schedule.")
    else:
        print("No schedule to clear.")

def main():
    if len(sys.argv) < 2:
        print("Usage: day_planner.py <command> [arguments]")
        print("Commands: add, view, remove, edit, clear")
        return

    command = sys.argv[1].lower()

    if command == 'add':
        if len(sys.argv) != 4:
            print("Usage: day_planner.py add \"task\" HH:MM-HH:MM")
            return
        add_task(sys.argv[2], sys.argv[3])
    elif command == 'view':
        view_plan()
    elif command == 'remove':
        if len(sys.argv) != 3:
            print("Usage: day_planner.py remove \"task\"")
            return
        remove_task(sys.argv[2])
    elif command == 'edit':
        if len(sys.argv) != 4:
            print("Usage: day_planner.py edit \"task\" HH:MM-HH:MM")
            return
        edit_task(sys.argv[2], sys.argv[3])
    elif command == 'clear':
        clear_plan()
    else:
        print(f"Unknown command: {command}")
        print("Available commands: add, view, remove, edit, clear")

if __name__ == "__main__":
    main()