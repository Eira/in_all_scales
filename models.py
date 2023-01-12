"""Whole project types."""
from dataclasses import dataclass
from typing import List


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
    name: str
    key: str
    pattern: List
