%define package_name gcm
%define version 2.0.1
%define release 1

Summary: GNOME Clipboard Manager is an application to manage your selections and clipboards.

Name: %{package_name}
Version: %{version}
Release: %{release}
License: GPL
Group: Applications/GUI/Gnome
Source: gcm-2.0.1.tar.gz

Vendor: me at freax dot org
Packager: me at freax dot org

%description
GNOME Clipboard Manager (GCM) is an application for managing selections and clipboards.
It auto- collects selections on a shelf and has the option to choose which selection is
to be pasted. Selections can be edited, manually created, deleted, copied, and pasted.
The available selection types are clipboard, primary, secondary, or a custom atom.


%prep
%setup

%build
./autogen.sh
./configure --prefix=/usr
make

%install
make install

%files 
%attr (755, root, root) /usr/bin/gcm
