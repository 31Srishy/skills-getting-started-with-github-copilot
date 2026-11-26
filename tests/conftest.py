from copy import deepcopy

import pytest

from src import app as app_module


_INITIAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def isolate_activities(monkeypatch):
    monkeypatch.setattr(app_module, "activities", deepcopy(_INITIAL_ACTIVITIES))
