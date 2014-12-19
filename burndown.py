# plugs/burndown.py
#
# TODO readme

__copyright__ = 'GPLv3 https://www.gnu.org/licenses/gpl-3.0.html' # TODO

from gozerbot.commands import cmnds
from gozerbot.examples import examples
from gozerbot.plughelp import plughelp

plughelp.add('burndown', 'show a burndown chart of the current iteration')

def handle_burndown(bot, ievent):
    """ burndown .. show burndown chart of the current iteration """
    lines   = 12 # number of lines used to print the chart -- TODO define in constant or set as an option ?
    max_day = 15 # TODO dynamic
    day     = 10
    max_sp  = 60
    sp      = 20
    for line in range(0, lines):
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

cmnds.add('burndown', handle_burndown, ['USER', 'WEB', 'CLOUD'])

examples.add('burndown', 'burndown .. show burndown chart of the current iteration', 'burndown')
