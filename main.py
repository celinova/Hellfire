# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License
# as published by the Free Software Foundation either version
# 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this script. If not, see <https://www.gnu.org/licenses/>.

import time
import asyncio
import logging
import httpx
from bs4 import BeautifulSoup
import tkinter as tk

logger = logging.getLogger(__name__)
site_url = "https://www.nationstates.net"
api_endpoint = "https://www.nationstates.net/cgi-bin/api.cgi"
