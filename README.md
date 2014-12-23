### gozerbot-burndown
[Gozerbot](https://launchpad.net/gozerbot) plugin to display [burndown charts](http://en.wikipedia.org/wiki/Burn_down_chart).

Gozerbot is an IRC/Jabber bot.
This plugin defines a command `!burndown` that displays charts like this (Story Points vs days):

    80|\
    SP| \
      |  \
      |   \ + (60 SP / 10 days)
      |    \
      |     \
      |      \
      |       \
      |        \
      |         \
      |          \
      |           \
      |____________
     0            20 days

### Installation
 * Install Gozerbot:
  * Project page: https://launchpad.net/gozerbot
  * On Ubuntu: `sudo apt-get install gozerbot`
 * Configure the bot e.g. for a basic setup:
  * 
 * Make the bot join your IRC channel:
  * `/etc/init.d/gozerbot start`
  * `/msg mygozerbot join #mychannel`
 * Invoke the command:
  * `!burndown`
 
### Customization
The plugin is based on hard-coded values.
TODO

### Debugging
`tail -f /var/log/gozerbot.log`.
