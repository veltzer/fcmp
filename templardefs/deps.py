'''
dependencies for this project
'''

def populate(d):
    d.packs=[
        'libtool',
        'automake',
        'autoconf',
    ]

def getdeps():
    return [
        __file__, # myself
    ]
