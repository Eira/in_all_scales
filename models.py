"""Whole project types."""
from dataclasses import dataclass
from typing import List


@dataclass
class Pattern:
    """Pattern with numbers."""
    name: str
    pattern: List[int]


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
class TransPattern:
    """Pattern with transposed notes."""
    key: str
    notes: List
