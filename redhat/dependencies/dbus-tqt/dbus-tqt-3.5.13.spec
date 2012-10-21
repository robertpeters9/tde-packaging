# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

Name:		trinity-dbus-tqt
Version:	3.5.13
Release:	3%{?dist}%{?_variant}
License:	GPL
Summary:	Dbus TQT Interface
Group:		System Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	dbus-tqt-3.5.13.tar.gz

# [dbus-tqt] Fix build on RHEL 4
Patch1:		dbus-tqt-3.5.13-fix_old_dbus_types.patch

BuildRequires:	gcc-c++
%if 0%{?suse_version}
BuildRequires:	dbus-1-devel
%else
BuildRequires:	dbus-devel
%endif
BuildRequires:	tqtinterface-devel >= 3.5.13

# TDE 3.5.13 specific building variables
BuildRequires:	cmake >= 2.8
BuildRequires:	qt3-devel

Requires:		qt3

Obsoletes:		dbus-tqt < %{version}-%{release}
Provides:		dbus-tqt = %{version}-%{release}


%description
Dbus TQT Interface


%package devel
Requires:		%{name}
Summary:		%{name} - Development files
Group:			Development/Libraries

Obsoletes:		dbus-tqt-devel < %{version}-%{release}
Provides:		dbus-tqt-devel = %{version}-%{release}

%description devel
Development files for %{name}


%if 0%{?suse_version}
%debug_package
%endif


%prep
%setup -q -n dependencies/dbus-tqt

%if 0%{?rhel} == 4
%patch1 -p1 -b .dbustypes
%endif

%build
unset QTDIR || : ; . /etc/profile.d/qt?.sh
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

%if 0%{?rhel} == 4
export CXXFLAGS="-DDBUS_API_SUBJECT_TO_CHANGE ${CXXFLAGS}"
%endif

%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%__mkdir_p build
cd build
%endif

%cmake \
  -DINCLUDE_INSTALL_DIR=%{tde_includedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  ..

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

%clean
%__rm -rf %{?buildroot}

%post
/sbin/ldconfig || :

%postun
/sbin/ldconfig || :

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

%files
%{tde_libdir}/libdbus-tqt-1.so.0
%{tde_libdir}/libdbus-tqt-1.so.0.0.0

%files devel
%{tde_includedir}/dbus-1.0/*
%{tde_libdir}/libdbus-tqt-1.so
%{tde_libdir}/libdbus-tqt-1.la
%{tde_libdir}/pkgconfig/dbus-tqt.pc

%changelog
* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Updates BuildRequires

* Tue Nov 07 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Updates BuildRequires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sun Sep 02 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13.0
- Import to GIT
- Built with future TDE version (3.5.13 + cmake + QT3.3.8d)
