# -*- coding: utf-8 -*-

"""Main module."""
import json
import logging


# this only works with post-19.7.1 gunicorn to pull in commit 610596c9
# which logs separate format and args
class AccessFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        pass

    def format(self, record):
        msg = {
            '@version': 1,
            # FIXME convert to Z-timezone? fractions of a second?
            '@timestamp': self.formatTime(record, "%Y-%m-%dT%H:%M:%S%z"),
            'access': {
                'method': record.args['m'],
                'http_version': record.args['H'].replace('HTTP/', ''),
                'response_code': record.args['s'],
                'url': record.args['{raw_uri}e'],
                'remote_ip': record.args['h'],
                'agent': record.args['a'],
                'body_sent': {'bytes': record.args['B']},
                'remote_user': record.args['u'],
                'referrer': record.args['f'],
                'elapsed_time': {'ms': record.args['D']/1000},
            }
        }
        return json.dumps(msg)
