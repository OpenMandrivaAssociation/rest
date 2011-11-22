%define shortname rest
%define name lib%{shortname}

%define api		0.7
%define major           0
%define libname         %mklibname %{shortname} %{api} %{major}
%define develname       %mklibname %{shortname} -d

Name: %{name}
Summary: Library for accessing rest web services
Group: System/Libraries
Version: 0.7.10
License: LGPLv2+
URL: http://www.meego.com
Release: %mkrel 1
Source0: http://ftp.gnome.org/pub/GNOME/sources/rest/%{api}/%{shortname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxml2-devel
BuildRequires: glib2-devel
BuildRequires: libsoup-devel
BuildRequires: gtk-doc
BuildRequires: gobject-introspection-devel

%description
Library for accessing rest web services

%package -n %{libname}
Summary: Library for accessing rest web services
Group: System/Libraries
Obsoletes: %{_lib}librest0 < %version
Conflicts: %{develname} < 0.7.10

%description -n %{libname}
Library for accessing rest web services

%package -n %{name}-doc

Summary: Documentation for %{name}
Group: System/Libraries

%description -n %{name}-doc
Documentation for %{name}

%package -n %{develname}

Summary: Development files for %{name}
Group: Development/C

Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{shortname}-%{version}

%build
%configure2_5x --enable-gtk-doc
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}/%{_datadir}/doc/%{name}-%{version}
for f in `ls %{buildroot}/%{_datadir}/doc/`; do
	if [ -f %{buildroot}/%{_datadir}/doc/$f ]; then
		mv %{buildroot}/%{_datadir}/doc/$f %{buildroot}/%{_datadir}/doc/%{name}-%{version}
	fi
done

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc COPYING NEWS README AUTHORS ChangeLog
%{_libdir}/%{name}*-%{api}.so.%{major}*
%{_libdir}/girepository-1.0/*

%files -n %{name}-doc
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/*

%files -n %{develname}
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
%{_includedir}/rest*/*
%{_libdir}/%{name}*.so
%{_libdir}/%{name}*.la
%{_datadir}/gir-1.0/*
