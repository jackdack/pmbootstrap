"""
Copyright 2017 Martijn Braam

This file is part of pmbootstrap.

pmbootstrap is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pmbootstrap is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pmbootstrap.  If not, see <http://www.gnu.org/licenses/>.
"""
import pmb.chroot.root


def setup_keymap(args):
    """
    Set the keymap with the setup-keymap utility if the device requires it
    """
    suffix = "rootfs_" + args.device
    if args.keymap != "":
        layout, variant = args.keymap.split("/")
        pmb.chroot.root(args, ["setup-keymap", layout, variant], suffix, log=False)
