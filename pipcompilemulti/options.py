"""
Global dictionary holding configuration options
"""

OPTIONS = {
    'compatible_patterns': [],
    'base_dir': 'requirements',
    'forbid_post': [],
    'in_ext': 'in',
    'out_ext': 'txt',
    'header_file': None,
}

DEFAULT_HEADER = """
#
# This file is autogenerated by pip-compile-multi
# To update, run:
#
#    pip-compile-multi
#
""".lstrip()
