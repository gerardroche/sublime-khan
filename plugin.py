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
        rulers = self.view.settings().get('rulers')
        queue_save = False

        if action == 'add':
            for sel in self.view.sel():
                col = self.view.rowcol(sel.begin())[1]
                if col not in rulers:
                    rulers.append(col)
                    queue_save = True
        elif action == 'remove':
            for sel in self.view.sel():
                col = self.view.rowcol(sel.begin())[1]
                if col in rulers:
                    rulers.remove(col)
                    queue_save = True
        elif action == 'clear' and rulers != []:
            rulers = []
            queue_save = True

        if queue_save:
            rulers.sort()
            if rulers:
                self.view.settings().set('rulers', rulers)
            else:
                self.view.settings().erase('rulers')
