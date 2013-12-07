%define api 0.7
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define develname %mklibname %{name} -d

Name:		rest
Summary:	Library for accessing rest web services
Group:		System/Libraries
Version:	0.7.12
Release:	4
License:	LGPLv2+
URL:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/rest/%{api}/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)

%description
Library for accessing rest web services.

%package -n %{libname}
Summary:	Library for accessing rest web services
Group:		System/Libraries
Obsoletes:	%{_lib}librest0 < %{version}
Conflicts:	%{develname} < 0.7.10

%description -n %{libname}
Library for accessing rest web services.

%package -n %{girname}
Summary:	GObject introspection interface library for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject introspection interface library for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
%rename		lib%{name}-doc

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--enable-introspection=yes \
	--enable-gtk-doc

%make

%install
%makeinstall_std
find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%doc COPYING
%{_libdir}/librest-%{api}.so.%{major}*
%{_libdir}/librest-extras-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Rest-%{api}.typelib
%{_libdir}/girepository-1.0/RestExtras-%{api}.typelib

%files -n %{develname}
%doc README AUTHORS ChangeLog
%{_includedir}/%{name}-%{api}
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/pkgconfig/%{name}-extras-%{api}.pc
%{_libdir}/librest-%{api}.so
%{_libdir}/librest-extras-%{api}.so
%{_datadir}/gtk-doc/html/%{name}*%{api}
%{_datadir}/gir-1.0/Rest-%{api}.gir
%{_datadir}/gir-1.0/RestExtras-%{api}.gir



%changelog
* Sun Apr 29 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.7.12-2
+ Revision: 794432
- rebuild for typelib

* Wed Nov 23 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.7.12-1
+ Revision: 732693
- fixed devel pkg list
- new version 0.7.12
- cleaned up spec
- removed defattr
- removed clean section
- split out gir pkg
- merged doc pkg into devel
- removed mkrel & BuildRoot
- converted BRs to pkgconfig provides
- updated URL
- removed .la files
- disabled static build
- source pkg is rest not librest, following mdv policy

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.7.10-1
+ Revision: 657594
- new version 0.7.10

* Thu Apr 14 2011 Funda Wang <fwang@mandriva.org> 0.7.2-2
+ Revision: 652963
- br g-ir
- rebuild for new libsoup

  + Claudio Matsuoka <claudio@mandriva.com>
    - Update for MeeGo 1.1

* Wed Aug 11 2010 Götz Waschk <waschk@mandriva.org> 0.6.1-5mdv2011.0
+ Revision: 568999
- rebuild for new libproxy

* Wed Oct 28 2009 Olivier Blin <blino@mandriva.org> 0.6.1-4mdv2010.0
+ Revision: 459749
- 0.6.1, with versionned lib and extra lib (from Caio Begotti)

* Mon Oct 05 2009 Olivier Blin <blino@mandriva.org> 0.6-4mdv2010.0
+ Revision: 454072
- provide librest-devel
- remove useless requires in -devel

* Fri Oct 02 2009 Olivier Blin <blino@mandriva.org> 0.6-3mdv2010.0
+ Revision: 452555
- fix devel group

* Thu Oct 01 2009 Olivier Blin <blino@mandriva.org> 0.6-2mdv2010.0
+ Revision: 452386
- fix naming that I broke (funny liblibrest will die)
- use major in file list

* Thu Oct 01 2009 Olivier Blin <blino@mandriva.org> 0.6-1mdv2010.0
+ Revision: 452264
- include la in devel package
- remove useless exclude
- fix name
- initial import (from Claudio Matsuoka and Caio Begotti, based on Fedora package)
- Created package structure for librest.

