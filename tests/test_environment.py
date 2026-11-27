from pathlib import Path

import yaml


def test_environment_can_read_project_config():
    config_path = Path(__file__).resolve().parents[1] / "config.yaml"

    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))

    assert type(config["random_seed"]) is int
