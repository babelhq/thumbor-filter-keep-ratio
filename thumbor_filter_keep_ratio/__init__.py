#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

__version__ = '0.0.1'

try:
    from thumbor_filter_keep_ratio.keep_ratio import Filter
except ImportError:
    logging.exception('Could not import thumbor_filter_keep_ratio. Probably due to setup.py installing it.')
