#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from scripttest import TestFileEnvironment

from migrate.tests.fixture.pathed import *


class Shell(Pathed):
    """Base class for command line tests"""

    def setUp(self):
        super(Shell, self).setUp()
        self.env = TestFileEnvironment(
            base_path=os.path.join(self.temp_usable_dir, 'env'),
            script_path=[os.path.dirname(sys.executable)], # PATH to migrate development script folder
        )

    def run_version(self, repos_path):
        result = self.env.run('migrate version %s' % repos_path)
        return int(result.stdout.strip())

    def run_db_version(self, url, repos_path):
        result = self.env.run('migrate db_version %s %s' % (url, repos_path))
        return int(result.stdout.strip())
