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
    """whole scale."""
    name: str
    scales: List[Key]


@dataclass
class TransPattern:
    """Pattern with transposed notes."""
    key: str
    pattern: List
