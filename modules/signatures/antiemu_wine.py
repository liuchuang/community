# Copyright (C) 2012 Claudio "nex" Guarnieri (@botherder)
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

from lib.cuckoo.common.abstracts import Signature

class WineDetect(Signature):
    name = "antiemu_wine"
    description = "Detects the presence of Wine emulator"
    severity = 3
    categories = ["anti-emulation"]
    authors = ["nex"]
    minimum = "2.0"

    indicators = [
        "HKEY_CURRENT_USER\\Software\\Wine",
    ]

    def on_complete(self):
        for indicator in self.indicators:
            for regkey in self.check_key(pattern=indicator, all=True):
                self.match(None, "registry", regkey=regkey)
