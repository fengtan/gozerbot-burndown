# plugs/burndown.py
#
#

__copyright__ = 'GPLv3 https://www.gnu.org/licenses/gpl-3.0.html'

# TODO clean up imports
from gozerbot.generic import elapsedstring, getwho, jsonstring
from gozerbot.commands import cmnds
from gozerbot.callbacks import callbacks, jcallbacks
from gozerbot.examples import examples
from gozerbot.datadir import datadir
from gozerbot.persist.persist import PlugPersist
from gozerbot.plughelp import plughelp
from gozerbot.aliases import aliases
from gozerbot.tests import tests

import time, os

plughelp.add('burndown', 'show a burndown chart of the current iteration') # TODO or static data ?

# TODO register callback for private messages

def handle_burndown(bot, ievent):
    """ burndown .. show burndown chart of the current iteration """ #TODO drop
    height = 12 # number of lines used to print the chart -- TODO define in constant or set as an option ?
    for y in range(1, height):
        ievent.reply("|")

cmnds.add('burndown', handle_burndown, ['USER', 'WEB', 'CLOUD']) # TODO USER/WEB/CLOUD

#TODO aliases.data['st'] = 'burndown'
#TODO tests.add('burndown').add('burndown exec')

# TODO support options ? e.g. burndown i50
examples.add('burndown', 'burndown .. show burndown chart of the current iteration', 'burndown')
