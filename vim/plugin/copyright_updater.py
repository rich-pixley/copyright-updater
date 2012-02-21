#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2012 Martin Ueding <dev@martin-ueding.de>

import vim

import copyrightupdate

def update_copyright():
    copyrightupdate.process_lines(vim.current.buffer, 5, load_config_regex())
