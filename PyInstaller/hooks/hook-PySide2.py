#-----------------------------------------------------------------------------
# Copyright (c) 2005-2021, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------

import os
from PyInstaller.utils.hooks import collect_system_data_files
from PyInstaller.utils.hooks.qt import pyside2_library_info, get_qt_binaries

# Only proceed if PySide2 can be imported.
if pyside2_library_info.version is not None:
    hiddenimports = ['shiboken2']

    # Collect the ``qt.conf`` file.
    datas = [x for x in
             collect_system_data_files(pyside2_library_info.location['PrefixPath'],
                                       pyside2_library_info.qt_rel_dir)
             if os.path.basename(x[0]) == 'qt.conf']

    # Collect required Qt binaries.
    binaries = get_qt_binaries(pyside2_library_info)
