"""Datatypes connected with patterns anf licks."""

from dataclasses import dataclass


@dataclass
class RowNotes:
    """Groups of notes, gathered in a rows."""

    quants: list[str]


@dataclass
class PatternType:
    """Base structure for patterns and licks."""

    name: str
    scale_types: set[str]
    pattern: list[RowNotes]


@dataclass
class Pattern(PatternType):
    """Pattern with numbers."""


@dataclass
class Lick(PatternType):
    """Lick with numbers."""


@dataclass
class TransRowNotes:
    """Groups of notes, gathered in a rows."""

    quants: list[str]


@dataclass
class PatternInKey:
    """Pattern with transposed notes in one key."""

    key_name: str
    pattern: list[TransRowNotes]


@dataclass
class PatternInScale:
    """Pattern with transposed notes to one type of scale."""

    scale_type_name: str
    pattern_name: str
    scales: list[PatternInKey]
