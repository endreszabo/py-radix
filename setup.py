#!/usr/bin/env python

# Copyright (c) 2004 Damien Miller <djm@mindrot.org>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# $Id$

import sys
from distutils.core import setup, Extension

VERSION = "0.3"

if __name__ == '__main__':
	radix = Extension('radix',
		define_macros = [('PROGVER', '"' + VERSION + '"')],
		sources = ['radix.c', 'radix_python.c'])
	setup(	name = "radix",
		version = VERSION,
		author = "Damien Miller",
		author_email = "djm@mindrot.org",
		url = "http://www.mindrot.org/py-radix.html",
		description = "Radix tree implementation",
		long_description = """\
py-radix is an implementation of a radix tree data structure for the storage 
and retrieval of IPv4 and IPv6 network prefixes.

The radix tree is the data structure most commonly used for routing table 
lookups. It efficiently stores network prefixes of varying lengths and 
allows fast lookups of containing networks.
""",
		license = "BSD",
		ext_modules = [radix]
	     )
