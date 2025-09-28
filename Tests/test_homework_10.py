import pytest
import logging
from Homework_10.homework_10 import log_event


def test_success_logged(caplog):
    caplog.set_level(logging.INFO, logger="log_event")  # додаємо рівень INFO
    log_event("Alice", "success")
    assert "Username: Alice, Status: success" in caplog.text

def test_expired_logged(caplog):
    caplog.set_level(logging.WARNING, logger="log_event")
    log_event("Bob", "expired")
    assert "Username: Bob, Status: expired" in caplog.text

def test_failed_logged(caplog):
    caplog.set_level(logging.ERROR, logger="log_event")
    log_event("Charlie", "failed")
    assert "Username: Charlie, Status: failed" in caplog.text