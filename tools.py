# This file is part galatea_manufacturer module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import logging

try:
    import slug
except ImportError:
    logger = logging.getLogger(__name__)
    logger.error('Unable to import slug. Install slug package.')

def slugify(value):
    """Convert value to slug: az09 and replace spaces by -"""
    try:
        if isinstance(value, unicode):
            name = slug.slug(value)
        else:
            name = slug.slug(unicode(value, 'UTF-8'))
    except:
        name = ''
    return name

def slugify_file(value):
    """Convert attachment name to slug: az09 and replace spaces by -"""
    fname = value.lower().split('.')
    fn = fname[0]
    try:
        if isinstance(fn, unicode):
            name = slug.slug(fn)
        else:
            name = slug.slug(unicode(fn, 'UTF-8'))

        if len(fname) > 1:
            return '%s.%s' % (name, fname[1])
        else:
            return name
    except:
        return value
