from nautobot.core.celery import register_jobs

from .demo_jobs import DemoJob
jobs = [DemoJob]
register_jobs(*jobs)