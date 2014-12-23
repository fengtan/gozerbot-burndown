### Description
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
Install Gozerbot e.g. for a quick setup on IRC:

    sudo apt-get install gozerbot (or download https://launchpad.net/gozerbot)
    vi /etc/gozerbot/mainconfig
        owner = ["~bart@127.0.0.1"]
    vi /etc/gozerbot/fleet/default/config
        enable = 1
        type = "irc"
        owner = ["irc"]
        nick = "mygozerbot"
        password = "foobar"
        username = "mygozerbot"
        realname = "mygozerbot"
        
Enable the plugin:

    cp burndown.py /usr/lib/pymodules/python2.7/gplugs/
    vi /etc/gozerbot/mainconfig
        loglist = ["idle", "burndown"]
        loadlist = ["foo", "bar", "burndown"]
        
Make the bot join IRC:

    /etc/init.d/gozerbot start
    /msg mygozerbot join #mychannel
    
Invoke the command:

    !burndown
 
### Customization
The plugin is based on hard-coded values.
TODO

### Debugging
`tail -f /var/log/gozerbot.log`
