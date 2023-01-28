"""Whole project types."""
from dataclasses import dataclass
from typing import List, Set


@dataclass
class RowNotes:
    """Groups of notes, gathered in a rows."""
    quants: List[str]


@dataclass
class PatternType:
    name: str
    scale_types: Set[str]  # todo set
    pattern: List[RowNotes]


@dataclass
class Pattern(PatternType):
    """Pattern with numbers."""


@dataclass
class Lick(PatternType):
    """Lick with numbers."""


@dataclass
class ScaleFormula:
    """Pattern with numbers."""
    name: str
    formula: List[int]


@dataclass
class Key:
    """One key in the scale."""
    name: str
    scale: List[str]


@dataclass
class ScaleGroup:
    """Whole scale."""
    name: str
    scales: List[Key]


@dataclass
class TransRowNotes:
    """Groups of notes, gathered in a rows."""
    quants: List[str]


@dataclass
class PatternInKey:
    key_name: str
    pattern: List[TransRowNotes]


@dataclass
class PatternInScale:
    """Pattern with transposed notes to one type of scale."""
    scale_type_name: str
    pattern_name: str
    scales: List[PatternInKey]
