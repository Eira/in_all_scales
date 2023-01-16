"""Whole project types."""
from dataclasses import dataclass
from typing import List


@dataclass
class QuantNotes:
    """Group of notes, that should be shown together, like one bar."""
    notes: list[int]


@dataclass
class RowNotes:
    """Groups of notes, gathered in a rows."""
    quants: list[QuantNotes]


@dataclass
class Pattern:
    """Pattern with numbers."""
    name: str
    scale_types: List[str]
    pattern: List[RowNotes]


@dataclass
class Lick:
    """Lick with numbers."""
    name: str
    scale_types: List[str]
    pattern: List[RowNotes]


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
class TransQuantNotes:
    """Group of notes, that should be shown together, like one bar."""
    notes: List[str]


@dataclass
class TransRowNotes:
    """Groups of notes, gathered in a rows."""
    quants: List[QuantNotes]


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
