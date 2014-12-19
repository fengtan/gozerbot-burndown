# plugs/burndown.py
#
# TODO readme

__copyright__ = 'GPLv3 https://www.gnu.org/licenses/gpl-3.0.html' # TODO

from gozerbot.commands import cmnds
from gozerbot.examples import examples
from gozerbot.plughelp import plughelp

# Define callback.
def handle_burndown(bot, ievent):
    """ burndown .. show burndown chart of the current iteration """
    lines   = 12 # number of lines used to print the chart -- TODO define in constant or set as an option ?
    day_maximum = 15 # TODO dynamic + doc
    day_current = 10
    spt_maximum = 60
    spt_current = 20
    for line in range(0, lines):
        # Build padding before (1) and after (2) the curve.
        padding_1 = ' ' * line
        padding_2 = ' ' * (lines - len(padding_1))
        # Set max story points on appropriate line.
        if line == 0:
            spt = spt_maximum
        elif line == 1:
            spt = 'SP'
        else:
            spt = '  ' # TODO what if 100 max
        # Format line.
        string = "%s|%s\\%s" % (spt, padding_1, padding_2)
        # Set cross on appropriate line.
        if int(spt_current*lines/spt_maximum) == line:
            string = list(string)
            string[int(day_current*lines/day_maximum)] = '+'
            string = "".join(string)
        # Display line.
        ievent.reply(string)
    # Display chart footer.
    ievent.reply('  |' + '_' * lines)
    ievent.reply(" 0%s%s days" % (' ' * lines, day_maximum))

# Register command.
cmnds.add('burndown', handle_burndown, ['USER', 'WEB', 'CLOUD'])

# Set help text.
plughelp.add('burndown', 'show a burndown chart of the current iteration')

# Set example.
examples.add('burndown', 'burndown .. show burndown chart of the current iteration', 'burndown')
