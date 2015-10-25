"""Keyword Arguments"""
def cheesechop(kind, *arguments, **keywords):
    """cheesechop"""
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for key in keys:
        print key, ":", keywords[key]

cheesechop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client='John Cleese',
           sketch='Cheese Shop Sketch')

