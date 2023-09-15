# Copyright (C) 2023 Gerard Roche
#
# This file is part of Khan.
#
# Khan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Khan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Khan.  If not, see <https://www.gnu.org/licenses/>.

import sublime_plugin


class KhanCommand(sublime_plugin.TextCommand):

    def run(self, edit, action):
        col = self.view.rowcol(self.view.sel()[0].begin())[1]
        if col < 0:
            return

        queue_save = False
        settings = self.view.settings()
        rulers = settings.get('rulers')

        if action == 'add':
            if col not in rulers:
                rulers.append(col)
                queue_save = True
        elif action == 'remove':
            if col in rulers:
                rulers.remove(col)
                queue_save = True
        elif action == 'clear':
            if rulers != []:
                rulers = []
                queue_save = True
        else:
            raise Exception('unknown action')

        if queue_save:
            rulers.sort()
            if rulers:
                settings.set('rulers', rulers)
            else:
                settings.erase('rulers')
