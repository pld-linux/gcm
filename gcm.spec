Summary:	GNOME Clipboard Manager - an application to manage your selections and clipboards
Summary(pl):	Zarz±dca schowka GNOME - aplikacja do zarz±dzania zaznaczeniami i schowkami
Name:		gcm
Version:	2.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://unc.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-desktop_location.patch
Patch1:		%{name}-gettext_fixes.patch
URL:		http://gms.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
GNOME Clipboard Manager (GCM) is an application for managing
selections and clipboards. It autocollects selections on a shelf and
has the option to choose which selection is to be pasted. Selections
can be edited, manually created, deleted, copied, and pasted. The
available selection types are clipboard, primary, secondary, or a
custom atom.

%description -l pl
GCM (GNOME Clipboard Manager - zarz±dca schowka GNOME) to aplikacja do
zarz±dzania zaznaczeniami i schowkami. Automatycznie zbiera zaznaczone
fragmenty i umo¿liwia wybór, który fragment ma zostaæ wklejony.
Zaznaczenia mog± byæ modyfikowane, rêcznie tworzone, usuwane,
kopiowane i wklejane. Dostêpne rodzaje zaznaczeñ to schowek,
podstawowe, drugorzêdne lub w³asne.

%prep
%setup -q
%patch0 -p1
%patch1	-p1

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
./configure --prefix=%{_prefix}
	    
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL NEWS README TODO 
%doc doc/*.html doc/HACKING
%attr(755,root,root) %{_bindir}/gcm
%{_datadir}/applications/*
%{_pixmapsdir}/*

%clean
rm -rf $RPM_BUILD_ROOT
