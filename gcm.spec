
%define 	librtftohtml_ver	2.0.2

Summary:	GNOME Clipboard Manager - an application to manage your selections and clipboards
Summary(pl):	Zarz±dca schowka GNOME - aplikacja do zarz±dzania zaznaczeniami i schowkami
Name:		gcm
Version:	2.0.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-desktop_location.patch
Patch1:		%{name}-gettext_fixes.patch
URL:		http://gcm.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	intltool
BuildRequires:	libtool
Requires:	librtftohtml = %{librtftohtml_ver}
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package devel
Summary:	Header files for gcm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for gcm.

%package static
Summary:	Static file for gcm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static files for gcm.

%package -n librtftohtml
Summary:	RTF to HTML convert library
Version:	%{librtftohtml_ver}
Group:		X11/Development/Libraries

%description -n librtftohtml
RTF to HTML convert library.

%package -n librtftohtml-devel
Summary:	Header files for RTF to HTML convert library
Version:	%{librtftohtml_ver}
Group:		X11/Development/Libraries
Requires:	librtftohtml = %{librtftohtml_ver}

%description -n librtftohtml-devel
Header files for RTF to HTML convert library.

%package -n librtftohtml-static
Summary:	Static file for RTF to HTML convert library
Version:	%{librtftohtml_ver}
Group:		X11/Development/Libraries
Requires:	librtftohtml-devel = %{librtftohtml_ver}

%description -n librtftohtml-static
Static file for RTF to HTML convert library.

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
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install
	    
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#remove obsolete files:
rm $RPM_BUILD_ROOT%{_libdir}/gcm/Plugins/*.{a,la}	

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install

%postun
/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL NEWS README TODO 
%attr(755,root,root) %{_bindir}/gcm
%attr(755,root,root) %{_bindir}/gcmui
%attr(755,root,root) %{_libdir}/gcmapplet
%attr(755,root,root) %{_libdir}/libgcm.so.*.*.*
%attr(755,root,root) %{_libdir}/gcm//Plugins/*.so
%dir %{_libdir}/gcm
%doc %{_docdir}/%{name}
%{_datadir}/gnome-2.0/ui/*
%{_desktopdir}/*
%{_libdir}/bonobo/servers/*
%{_mandir}/man1/gcm.1.gz
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*


%files devel
%attr(755,root,root) %{_bindir}/gcm-config
%{_includedir}/libgcm
%{_pkgconfigdir}/libgcm.pc
%{_mandir}/man1/gcm-config.1.gz
%{_libdir}/libgcm.so
%{_libdir}/libgcm.la

%files static
%{_libdir}/libgcm.a

%files -n librtftohtml
%attr(755,root,root) %{_libdir}/librtftohtml.so.*.*.*

%files -n librtftohtml-devel
%{_includedir}/librtftohtml
%{_libdir}/librtftohtml.so
%{_libdir}/librtftohtml.la
%{_pkgconfigdir}/librtftohtml.pc

%files -n librtftohtml-static
%{_libdir}/librtftohtml.a
