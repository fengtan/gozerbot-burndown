# plugs/burndown.py
#
#

__copyright__ = 'GPLv3 https://www.gnu.org/licenses/gpl-3.0.html' # TODO

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
    lines   = 12 # number of lines used to print the chart -- TODO define in constant or set as an option ?
    max_day = 15 # TODO dynamic
    day     = 10
    max_sp  = 60
    sp      = 20
    for line in range(0, lines):
        # TODO spread slope according to height
        padding_1 = ' ' * line                     # padding before '\'
        padding_2 = ' ' * (lines - len(padding_1)) # padding after  '\'
        string = "  |%s\\%s" % (padding_1, padding_2)
        # Set cross 
        if int(sp*lines/max_sp) == line:
            string = list(string)
            string[int(day*lines/max_day)] = '+'
            string = "".join(string)
        ievent.reply(string)
    ievent.reply('  |' + '_' * lines)
    ievent.reply(" 0%s%s days" % (' ' * lines, max_day))

# TODO time between each reply -- find a way to reduce that
cmnds.add('burndown', handle_burndown, ['USER', 'WEB', 'CLOUD']) # TODO USER/WEB/CLOUD

#TODO aliases.data['st'] = 'burndown'
#TODO tests.add('burndown').add('burndown exec')

# TODO support options ? e.g. burndown i50
examples.add('burndown', 'burndown .. show burndown chart of the current iteration', 'burndown')
