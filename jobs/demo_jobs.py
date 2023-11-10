from nautobot.core.celery import register_jobs
from nautobot.extras.jobs import BooleanVar, Job


name = "Demo Jobs for Nautobot 2.0"


class DemoJob(Job):
    """A Demo Job."""

    class Meta:
        name = "Create Site"
        description = "A job used to demonstrate the jobs feature of Nautobot"

    debug = BooleanVar(description="Enable for more verbose debug logging", default=False)

    def run(self, debug):
        self.debug = debug

        self.logger.info("The job ran successfully.")
