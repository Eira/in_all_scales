"""Whole project types."""
from dataclasses import dataclass
from typing import List


@dataclass
class ScaleFormula:
    """Pattern with numbers."""
    name: str
    formula: List[int]


@dataclass
class Key:
    """One key in the scale."""
    name: str
    scale: List


@dataclass
class ScaleGroup:
    """Whole scale."""
    name: str
    scales: List[Key]


@dataclass
class Pattern:
    """Pattern with numbers."""
    name: str
    pattern: List[int]


@dataclass
class TransPattern:
    """Pattern with transposed notes."""
    key: str
    pattern: List
