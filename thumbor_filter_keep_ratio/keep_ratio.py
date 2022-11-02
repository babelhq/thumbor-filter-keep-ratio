#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com


import thumbor.filters
from thumbor.filters import BaseFilter, filter_method

# A Thumbor filter that resizes the image while allowing it to be less than the
# provided request height and width, but always keeping the aspect ratio.


class Filter(BaseFilter):
  phase = thumbor.filters.PHASE_AFTER_LOAD

  @filter_method()
  def keep_ratio(self):
    target_width = self.context.request.width
    target_height = self.context.request.height

    source_width, source_height = self.context.request.engine.size
    source_aspect_ratio = float(source_width) / float(source_height)

    if source_width < target_width:
      self.context.request.width = source_width
      self.context.request.height = source_height * source_aspect_ratio
    elif source_height < target_height:
      self.context.request.width = source_width / source_aspect_ratio
      self.context.request.height = source_height
