#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `gunicorn_logstash_formatter` package."""

import json
import logging
import pytest
from pytest import approx


from gunicorn_logstash_formatter import AccessFormatter



def test_thing():
    formatter = AccessFormatter()
    args = {
        'f': 'referer value',
        'm': 'PATCH',
        'H': 'HTTP/1.1',
        '{raw_uri}e' : '/foo?bar',
        's': '418',
        'h': '192.0.2.42',
        'a': 'user agent value',
        'B': 42,
        'u': 'root',
        'D': 45182,
    }
    log_record = logging.LogRecord('foo', logging.INFO, None, None, 'fake msg', args, None)
    result = formatter.format(log_record)
    parsed = json.loads(result)
    assert parsed['@version'] == 1
    # TODO: check RFC 3339 format of parsed['@timestamp']
    access = parsed['access']
    assert access['referrer'] == 'referer value'
    assert access['method'] == 'PATCH'
    assert access['response_code'] == '418'
    assert access['url'] == '/foo?bar'
    assert access['remote_ip'] == '192.0.2.42'
    assert access['agent'] == 'user agent value'
    assert access['body_sent'] == {'bytes': 42}
    assert access['remote_user'] == 'root'
    assert access['elapsed_time'] == {'ms': approx(45.182)}
    assert access['http_version'] == '1.1'
