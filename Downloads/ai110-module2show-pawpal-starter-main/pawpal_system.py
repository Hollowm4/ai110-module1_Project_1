from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date
from typing import List


# ── Constraints ───────────────────────────────────────────────────────────────

@dataclass
class Constraint:
    type: str

    def is_satisfied(self) -> bool:
        raise NotImplementedError


# ── Owner Preferences ─────────────────────────────────────────────────────────

@dataclass
class OwnerPreferences:
    time_available: int  # minutes per day

    def validate(self) -> bool:
        raise NotImplementedError


# ── Tasks ─────────────────────────────────────────────────────────────────────

class Task(ABC):
    def __init__(self, priority: int):
        self.priority = priority

    @abstractmethod
    def execute(self) -> None:
        pass


class Walk(Task):
    def execute(self) -> None:
        raise NotImplementedError

class Feeding(Task):
    def execute(self) -> None:
        raise NotImplementedError

class Medication(Task):
    def execute(self) -> None:
        raise NotImplementedError

class Enrichment(Task):
    def execute(self) -> None:
        raise NotImplementedError

class Grooming(Task):
    def execute(self) -> None:
        raise NotImplementedError


# ── Core Domain ───────────────────────────────────────────────────────────────

@dataclass
class Pet:
    name: str
    tasks: List[Task] = field(default_factory=list)

    def get_tasks(self) -> List[Task]:
        raise NotImplementedError


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)
    preferences: OwnerPreferences = None

    def get_pets(self) -> List[Pet]:
        raise NotImplementedError


# ── Daily Plan ────────────────────────────────────────────────────────────────

@dataclass
class DailyPlan:
    date: date
    tasks: List[Task] = field(default_factory=list)
    constraints: List[Constraint] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        raise NotImplementedError


# ── Scheduler ─────────────────────────────────────────────────────────────────

class PetCareScheduler:
    def __init__(self, owners: List[Owner]):
        self.owners = owners
        self.plan: DailyPlan = None

    def generate_plan(self) -> DailyPlan:
        raise NotImplementedError