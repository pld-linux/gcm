
%define 	librtftohtml_ver	2.0.2

Summary:	GNOME Clipboard Manager - an application to manage your selections and clipboards
Summary(pl.UTF-8):	Zarządca schowka GNOME - aplikacja do zarządzania zaznaczeniami i schowkami
Name:		gcm
Version:	2.0.4
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gcm/%{name}-%{version}.tar.gz
# Source0-md5:	27e5dbea93240195296113c874411136
Patch0:		%{name}-desktop_location.patch
Patch1:		%{name}-gettext_fixes.patch
URL:		http://gcm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	gnome-panel-devel
BuildRequires:	intltool
BuildRequires:	libtool
Requires(post):	/sbin/ldconfig
Requires(post):	GConf2
Requires:	librtftohtml = %{librtftohtml_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Clipboard Manager (GCM) is an application for managing
selections and clipboards. It autocollects selections on a shelf and
has the option to choose which selection is to be pasted. Selections
can be edited, manually created, deleted, copied, and pasted. The
available selection types are clipboard, primary, secondary, or a
custom atom.

%description -l pl.UTF-8
GCM (GNOME Clipboard Manager - zarządca schowka GNOME) to aplikacja do
zarządzania zaznaczeniami i schowkami. Automatycznie zbiera zaznaczone
fragmenty i umożliwia wybór, który fragment ma zostać wklejony.
Zaznaczenia mogą być modyfikowane, ręcznie tworzone, usuwane,
kopiowane i wklejane. Dostępne rodzaje zaznaczeń to schowek,
podstawowe, drugorzędne lub własne.

%package devel
Summary:	Header files for gcm
Summary(pl.UTF-8):	Pliki nagłówkowe gcm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gcm.

%description devel -l pl.UTF-8
Pliki nagłówkowe gcm.

%package static
Summary:	Static gcm library
Summary(pl.UTF-8):	Statyczna biblioteka gcm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gcm library.

%description static -l pl.UTF-8
Statyczna biblioteka gcm.

%package -n librtftohtml
Summary:	RTF to HTML convert library
Summary(pl.UTF-8):	Biblioteka konwertująca RTF do HTML-a
Version:	%{librtftohtml_ver}
Group:		X11/Development/Libraries

%description -n librtftohtml
RTF to HTML convert library.

%description -n librtftohtml -l pl.UTF-8
Biblioteka konwertująca RTF do HTML-a.

%package -n librtftohtml-devel
Summary:	Header files for RTF to HTML convert library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki konwertującej RTF do HTML-a
Version:	%{librtftohtml_ver}
Group:		X11/Development/Libraries
Requires:	librtftohtml = %{librtftohtml_ver}

%description -n librtftohtml-devel
Header files for RTF to HTML convert library.

%description -n librtftohtml-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki konwertującej RTF do HTML-a.

%package -n librtftohtml-static
Summary:	Static RTF to HTML convert library
Summary(pl.UTF-8):	Statyczna biblioteka konwertująca RTF do HTML-a
Version:	%{librtftohtml_ver}
Group:		X11/Development/Libraries
Requires:	librtftohtml-devel = %{librtftohtml_ver}

%description -n librtftohtml-static
Static file for RTF to HTML convert library.

%description -n librtftohtml-static -l pl.UTF-8
Statyczna biblioteka konwertująca RTF do HTML-a.

%prep
%setup -q
%patch0 -p1
%patch1	-p1

%build
cd libgcm
%{__aclocal}
cd ../librtftohtml
%{__aclocal}
cd ../gcmapplet
%{__aclocal}
%{__autoconf}
cd ..
rm -f mkinstalldirs
cp /usr/share/automake/mkinstalldirs .
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install

rm -f gcmapplet/GNOME_GcmApplet.server{,.in}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

#remove obsolete files:
rm $RPM_BUILD_ROOT%{_libdir}/gcm/Plugins/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install

%postun	-p /sbin/ldconfig

%post   -n librtftohtml -p /sbin/ldconfig
%postun -n librtftohtml -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO doc/*.html doc/*.png doc/HACKING
%attr(755,root,root) %{_bindir}/gcm
%attr(755,root,root) %{_bindir}/gcmui
%attr(755,root,root) %{_libdir}/gcmapplet
%attr(755,root,root) %{_libdir}/libgcm.so.*.*.*
%dir %{_libdir}/gcm
%dir %{_libdir}/gcm/Plugins
%attr(755,root,root) %{_libdir}/gcm/Plugins/*.so
%{_datadir}/gnome-2.0/ui/*
%{_desktopdir}/*.desktop
%{_libdir}/bonobo/servers/*
%{_mandir}/man1/gcm.1*
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gcm-config
%attr(755,root,root) %{_libdir}/libgcm.so
%{_libdir}/libgcm.la
%{_includedir}/libgcm
%{_pkgconfigdir}/libgcm.pc
%{_mandir}/man1/gcm-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgcm.a

%files -n librtftohtml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librtftohtml.so.*.*.*

%files -n librtftohtml-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librtftohtml.so
%{_libdir}/librtftohtml.la
%{_includedir}/librtftohtml
%{_pkgconfigdir}/librtftohtml.pc

%files -n librtftohtml-static
%defattr(644,root,root,755)
%{_libdir}/librtftohtml.a
