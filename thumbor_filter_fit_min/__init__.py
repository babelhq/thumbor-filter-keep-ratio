#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

__version__ = '0.0.3'

try:
    from thumbor_filter_fit_min.fit_min import Filter
except ImportError:
    logging.exception('Could not import thumbor_filter_fit_min. Probably due to setup.py installing it.')
