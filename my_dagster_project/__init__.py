from dagster import (
    AssetSelection,
    Definitions,
    define_asset_job,
    load_assets_from_modules,
    ScheduleDefinition,
)
from . import assets

all_assets = load_assets_from_modules([assets])


dummy_job = define_asset_job(
    "dummy_job", selection=AssetSelection.all())

dummy_schedule = ScheduleDefinition(
    job=dummy_job,
    cron_schedule="* * * * *"
)

defs = Definitions(
    assets=all_assets,
    jobs=[dummy_job],
    schedules=[dummy_schedule]
)
