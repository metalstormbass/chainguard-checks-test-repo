"""A tiny greeting service, the code the reusable checks run against."""

import json
from pathlib import Path


def load_config(path):
    """Read the service's JSON config."""
    return json.loads(Path(path).read_text(encoding="utf-8"))


def greet(name, config):
    """Greet name in the configured style."""
    greeting = config.get("greeting", "Hello")
    punctuation = "!" if config.get("excited", False) else "."
    return f"{greeting}, {name}{punctuation}"


def farewell(name, config):
    """Say goodbye to name, in the configured style."""
    punctuation = "!" if config.get("excited", False) else "."
    return f"Goodbye, {name}{punctuation}"
