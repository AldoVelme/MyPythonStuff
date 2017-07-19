#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  YOUTUBE DOWNLOADER BY TATO VEMEZA
#
#  Copyright 2016 AVELAZCX <aldo.alfonsox.velasco.meza@intel.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

import subprocess
import sys

video_link, threads = sys.argv[1], sys.argv[2]
subprocess.call([
    "youtube-dl",
    video_link,
    "--external-downloader",
    "aria2c",
    "--external-downloader-args",
    "-x"+threads
])
