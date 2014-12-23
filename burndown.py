# plugs/burndown.py
#
# TODO readme
# Update functions to make the chart dynamic, e.g. by querying your ticketing system.
# TODO test edge cases (SP + days)

__copyright__ = 'GPLv3 https://www.gnu.org/licenses/gpl-3.0.html'

from gozerbot.commands import cmnds
from gozerbot.examples import examples
from gozerbot.plughelp import plughelp
from math import log

# Return number of days in the iteration.
def get_day_maximum():
    return 20

# Return current day in the iteration [between 0 and get_day_maximum()].
def get_day_current():
    return 10

# Return total number of story points in the iteration.
def get_spt_maximum():
    return 80 #TODO test .5 (current + max)

# Return number of story points left in the iteration [between 0 and get_spt_maximum()].
def get_spt_current():
    return 30

# Replace characters located from 'start' in 'string' with 'replacement'.
def replace_string(string, replacement, start):
    string = list(string)
    replacement = list(replacement)
    for position in range(0, len(replacement)):
        try:
            string[start + position] = replacement[position]
        except IndexError:
            string.append(replacement[position])
    return "".join(string)

# Define callback.
def handle_burndown(bot, ievent):
    """ burndown .. show burndown chart of the current iteration """
    lines       = 12 # Number of lines used to print the chart.
    day_maximum = get_day_maximum()
    day_current = get_day_current()
    spt_maximum = get_spt_maximum()
    spt_current = get_spt_current()
    # Set margin for vertical scale.
    margin = int(log(spt_maximum, 10)) + 1 # Margin for integer part.
    if spt_maximum != int(spt_maximum):
      margin += 2 # Margin for decimal part (round to 0.5).
      spt_maximum = int(spt_maximum) + 0.5
    for line in range(0, lines):
        # Set padding before (1) and after (2) the curve.
        padding_1 = ' ' * line
        padding_2 = ' ' * (lines - len(padding_1))
        # Format line.
        string = "%s|%s\\%s" % (' ' * margin, padding_1, padding_2)
        # Set vertical scale.
        if line == 0:
            string = replace_string(string, str(spt_maximum), 0)
        elif line == 1:
            string = replace_string(string, 'SP', 0)
        # Set cross on appropriate line.
        ievent.reply(spt_maximum)
        ievent.reply(spt_current)
        ievent.reply(spt_maximum - spt_current)
        if int((spt_maximum - spt_current) * lines / spt_maximum) == line:
            cross = "+ (%s SP / %s days)" % (spt_current, day_current)
            string = replace_string(string, cross, int(day_current * lines / day_maximum) + margin)
        # Display line.
        ievent.reply(string)
    # TODO see errors "can't add ..."
    # Set horizontal scale.
    ievent.reply(' ' * margin + '|' + '_' * lines)
    ievent.reply("%s0%s%s days" % (' ' * (margin - 1), ' ' * lines, day_maximum))

# Register command.
cmnds.add('burndown', handle_burndown, ['USER', 'WEB', 'CLOUD'])

# Set help text.
plughelp.add('burndown', 'show a burndown chart of the current iteration')

# Set example.
examples.add('burndown', 'burndown .. show burndown chart of the current iteration', 'burndown')
