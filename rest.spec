%define api 0.7
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define libextr %mklibname %{name}-extras %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define girextr %mklibname %{name}extras-gir %{api}
%define devname %mklibname %{name} -d

Summary:	Library for accessing rest web services
Name:		rest
Group:		System/Libraries
Version:	0.8.1
Release:	5
License:	LGPLv2+
Url:		http://www.gnome.org
Source0:	https://download.gnome.org/sources/rest/0.8/%{name}-%{version}.tar.xz
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	rootcerts

%description
Library for accessing rest web services.

%package -n %{libname}
Summary:	Library for accessing rest web services
Group:		System/Libraries
Obsoletes:	%{_lib}librest0 < %{version}
Conflicts:	%{devname} < 0.7.10

%description -n %{libname}
Library for accessing rest web services.

%package -n %{libextr}
Summary:	Library for accessing rest web services
Group:		System/Libraries
Obsoletes:	%{_lib}librest0 < %{version}
Conflicts:	%{devname} < 0.7.10
Conflicts:	%{_lib}rest0.7_0 < 0.7.90-2

%description -n %{libextr}
Library for accessing rest web services.

%package -n %{girname}
Summary:	GObject introspection interface library for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject introspection interface library for %{name}.

%package -n %{girextr}
Summary:	GObject introspection interface library for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}rest-gir0.7 < 0.7.90-2

%description -n %{girextr}
GObject introspection interface library for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libextr} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Requires:	%{girextr} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
%rename		lib%{name}-doc

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure \
	--enable-introspection=yes \
	--enable-gtk-doc

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/librest-%{api}.so.%{major}*

%files -n %{libextr}
%{_libdir}/librest-extras-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Rest-%{api}.typelib

%files -n %{girextr}
%{_libdir}/girepository-1.0/RestExtras-%{api}.typelib

%files -n %{devname}
%doc README AUTHORS ChangeLog COPYING
%{_includedir}/%{name}-%{api}
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/pkgconfig/%{name}-extras-%{api}.pc
%{_libdir}/librest-%{api}.so
%{_libdir}/librest-extras-%{api}.so
%{_datadir}/gtk-doc/html/%{name}*%{api}
%{_datadir}/gir-1.0/Rest-%{api}.gir
%{_datadir}/gir-1.0/RestExtras-%{api}.gir
