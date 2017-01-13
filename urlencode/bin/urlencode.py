"""
# Author: Bernardo Macias <bmacias@httpstergeek.com>
#
#
# All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
from splunklib.searchcommands import (dispatch, StreamingCommand,
                                      Configuration, Option, validators)
import sys
import urllib


@Configuration(local=True, type='eventing',
               retainsevents=True, streaming=False)
class urlencodeCommand(StreamingCommand):

    fields = Option(require=True, validate=validators.List())

    def stream(self, records):
        searchinfo = self.metadata.searchinfo
        self.logger.debug(' excuted by username="%s" %s', searchinfo.username,
                          ' '.join(searchinfo.args))
        for record in records:
            for field in self.fields:
                if field not in record:
                    self.logger.warn('{} not in in record'.format(record))
                    next
            if len(record[field]) == 0:
                next

            pass


dispatch(urlencodeCommand, sys.argv, sys.stdin, sys.stdout, __name__)
