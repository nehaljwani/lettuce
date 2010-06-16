# -*- coding: utf-8 -*-
# <Lettuce - Behaviour Driven Development for python>
# Copyright (C) <2010>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import commands
from tests.asserts import assert_equals
from lettuce.fs import FileSystem

current_directory = FileSystem.dirname(__file__)

def test_django_agains_alfaces():
    'running the "harvest" django command with verbosity 3'

    FileSystem.pushd(current_directory, "django", "alfaces")

    status, out = commands.getstatusoutput("python manage.py harvest --verbosity=3")
    assert_equals(status, 0)

    assert "Test the django app DO NOTHING" in out
    assert "Test the django app FOO BAR" in out
    FileSystem.popd()

def test_django_agains_alfaces_foo():
    'running the "harvest" will run only on configured apps if the setting LETTUCE_APPS is set'

    FileSystem.pushd(current_directory, "django", "alfaces_foo")

    status, out = commands.getstatusoutput("python manage.py harvest --verbosity=3")
    assert_equals(status, 0)

    assert "Test the django app FOO BAR" in out
    assert "Test the django app DO NOTHING" not in out
    FileSystem.popd()

