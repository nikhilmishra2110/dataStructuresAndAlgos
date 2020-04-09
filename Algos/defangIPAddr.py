def defangIPAddr(addr):
    """A defanged IP address replaces every period "." with "[.]"."""
    return '[.]'.join(addr.split('.'))

print (defangIPAddr("1.1.1.1"))