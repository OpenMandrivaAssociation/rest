%define api		0.7
%define major	0
%define libname		%mklibname %{name} %{api} %{major}
%define girlibname	%mklibname %{name}-gir %{api}
%define develname	%mklibname %{name} -d

Name: rest
Summary: Library for accessing rest web services
Group: System/Libraries
Version: 0.7.12
License: LGPLv2+
URL: http://www.gnome.org
Release: 1
Source0: http://ftp.gnome.org/pub/GNOME/sources/rest/%{api}/%{name}-%{version}.tar.xz

BuildRequires: gtk-doc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)

%description
Library for accessing rest web services

%package -n %{libname}
Summary: Library for accessing rest web services
Group: System/Libraries
Obsoletes: %{_lib}librest0 < %{version}
Conflicts: %{develname} < 0.7.10

%description -n %{libname}
Library for accessing rest web services

%package -n %{girlibname}
Summary: GObject introspection interface library for %{name}
Group: System/Libraries
Requires: %{libname} = %{version}-%{release}

%description -n %{girlibname}
GObject introspection interface library for %{name}.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
%rename lib%{name}-doc

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
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%doc COPYING
%{_libdir}/librest-%{api}.so.%{major}*
%{_libdir}/librest-extras-%{api}.so.%{major}*

%files -n %{girlibname}
%{_libdir}/girepository-1.0/Rest-%{api}.typelib
%{_libdir}/girepository-1.0/RestExtras-%{api}.typelib

%files -n %{develname}
%doc NEWS README AUTHORS ChangeLog
%{_includedir}/%{name}-%{api}
%{_libdir}/pkgconfig/%{name}*
%{_libdir}/librest-%{api}.so
%{_libdir}/librest-extras-%{api}.so
%{_datadir}/gtk-doc/html/%{name}*%{api}
%{_datadir}/gir-1.0/Rest-%{api}.gir
%{_datadir}/gir-1.0/RestExtras-%{api}.gir

