"""Pytest configuration."""

from __future__ import annotations

from typing import TYPE_CHECKING

from cgt_calc.const import CGT_TEST_MODE, TestMode

if TYPE_CHECKING:
    import pytest


def pytest_configure(config: pytest.Config) -> None:
    """Force single worker in RECORD mode to avoid parallel write races."""
    if CGT_TEST_MODE == TestMode.RECORD:
        config.option.numprocesses = (
            1  # avoid parallel write races on exchange_rates_data.csv
        )
