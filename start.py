# -*- coding: utf-8 -*-

from schedule.task import start_background_scheduler
from web.api import start_server


def main():
    start_background_scheduler()
    start_server()


if __name__ == '__main__':
    main()
