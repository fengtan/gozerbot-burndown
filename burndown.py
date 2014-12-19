# plugs/burndown.py
#
# TODO readme
# Update functions to make the chart dynamic, e.g. by querying your ticketing system.
# TODO support floats (e.g. 10.5 SP)

__copyright__ = 'GPLv3 https://www.gnu.org/licenses/gpl-3.0.html'

from gozerbot.commands import cmnds
from gozerbot.examples import examples
from gozerbot.plughelp import plughelp

# Return number of days in the iteration.
def get_day_maximum():
    return 20

# Return current day in the iteration [between 0 and get_day_maximum()].
def get_day_current():
    return 10

# Return total number of story points in the iteration.
def get_spt_maximum():
    return 80

# Return number of story points left in the iteration [between 0 and get_spt_maximum()].
def get_spt_current():
    return 30

# Replace character located at 'position' in 'string' with 'replacement'.
def replace_char(string, replacement, position):
    string = list(string)
    string[position] = '+'
    string = "".join(string)
    return string

# Define callback.
def handle_burndown(bot, ievent):
    """ burndown .. show burndown chart of the current iteration """
    lines       = 12 # Number of lines used to print the chart.
    day_maximum = get_day_maximum()
    day_current = get_day_current()
    spt_maximum = get_spt_maximum()
    spt_current = get_spt_current()
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
            spt = '  '
        # Format line.
        string = "%s|%s\\%s" % (spt, padding_1, padding_2)
        # Set cross on appropriate line.
        if int(spt_current*lines/spt_maximum) == line:
            string = replace_char(string, '+', int(day_current*lines/day_maximum))
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
