from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


# ── Constraints ───────────────────────────────────────────────────────────────

@dataclass
class Constraint:
    type: str

    def is_satisfied(self, task: Task, plan: DailyPlan) -> bool:  # add params
        raise NotImplementedError


# ── Owner Preferences ─────────────────────────────────────────────────────────

@dataclass
class OwnerPreferences:
    time_available: int  # minutes per day

    def validate(self) -> bool:
        raise NotImplementedError



# ── Task ──────────────────────────────────────────────────────────────────────

class Task(ABC):
    def __init__(
        self,
        description: str,
        time: str,           # e.g. "08:00 AM"
        frequency: str,      # e.g. "daily", "weekly"
        priority: int,
        duration: int,       # minutes needed
        pet: "Pet" = None,
    ):
        self.description = description
        self.time = time
        self.frequency = frequency
        self.priority = priority
        self.duration = duration
        self.pet = pet
        self.completed = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

     def __repr__(self) -> str:
        """Return a readable string showing task status and details."""
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.__class__.__name__}: {self.description} @ {self.time}"

    @abstractmethod
     def execute(self) -> None:
        """Execute the task and mark it complete."""
        pass


class Walk(Task):
    def execute(self) -> None:
        print(f"Walking {self.pet.name} — {self.duration} min")
        self.mark_complete()

class Feeding(Task):
    def execute(self) -> None:
        print(f"Feeding {self.pet.name} — {self.description}")
        self.mark_complete()

class Medication(Task):
    def execute(self) -> None:
        print(f"Giving medication to {self.pet.name} — {self.description}")
        self.mark_complete()

class Enrichment(Task):
    def execute(self) -> None:
        print(f"Enrichment for {self.pet.name} — {self.description}")
        self.mark_complete()

class Grooming(Task):
    def execute(self) -> None:
        print(f"Grooming {self.pet.name} — {self.description}")
        self.mark_complete()


# ── Pet ───────────────────────────────────────────────────────────────────────

class Pet:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a task to this pet and set the back-reference."""
        task.pet = self
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def get_pending_tasks(self) -> List[Task]:
        return [t for t in self.tasks if not t.completed]

    def __repr__(self) -> str:
        return f"Pet({self.name}, {self.species}, {len(self.tasks)} tasks)"


# ── Owner ─────────────────────────────────────────────────────────────────────

class Owner:
    def __init__(self, name: str, time_available: int):
        self.name = name
        self.time_available = time_available  # minutes per day
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def get_pets(self) -> List[Pet]:
        return self.pets

    def get_all_tasks(self) -> List[Task]:
        return [task for pet in self.pets for task in pet.get_tasks()]

    def get_total_task_time(self) -> int:
        return sum(t.duration for t in self.get_all_tasks())

    def __repr__(self) -> str:
        return f"Owner({self.name}, {len(self.pets)} pets)"


# ── Scheduler ─────────────────────────────────────────────────────────────────

class PetCareScheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def generate_plan(self) -> List[Task]:
        all_tasks = self.owner.get_all_tasks()
        total_time = self.owner.get_total_task_time()

        if total_time > self.owner.time_available:
            print(f"Warning: tasks need {total_time} min but only {self.owner.time_available} min available.")

        # Sort by priority (lower number = higher priority)
        plan = sorted(all_tasks, key=lambda t: t.priority)

        print(f"\n--- Daily Plan for {self.owner.name} ({date.today()}) ---")
        for task in plan:
            print(f"  Priority {task.priority} | {task}")
        print(f"Total time: {total_time} min / {self.owner.time_available} min available\n")

        return plan

    def execute_plan(self) -> None:
        plan = self.generate_plan()
        print("--- Executing Plan ---")
        for task in plan:
            task.execute()
