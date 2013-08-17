# TDE specific building variables
%define tde_version 3.5.13.2
%define tde_prefix /usr
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

Name:		trinity-dbus-tqt
Epoch:		1
Version:	0.63
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
License:	GPL
Summary:	Dbus TQT Interface
Group:		System Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

# [dbus-tqt] Fix build on RHEL 4
Patch1:		dbus-tqt-3.5.13-fix_old_dbus_types.patch

BuildRequires:	gcc-c++
%if 0%{?suse_version}
BuildRequires:	dbus-1-devel
%else
BuildRequires:	dbus-devel
%endif
BuildRequires:	trinity-tqtinterface-devel >= %{version}

BuildRequires:	cmake >= 2.8
BuildRequires:	qt3-devel >= 3.3.8d
Requires:		qt3 >= 3.3.8d

Obsoletes:		dbus-tqt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		dbus-tqt = %{?epoch:%{epoch}:}%{version}-%{release}


%description
Dbus TQT Interface

%post
/sbin/ldconfig || :

%postun
/sbin/ldconfig || :

%files
%defattr(-,root,root,-)
%{tde_libdir}/libdbus-tqt-1.so.0
%{tde_libdir}/libdbus-tqt-1.so.0.0.0

##########

%package devel
Requires:		%{name}
Summary:		%{name} - Development files
Group:			Development/Libraries

Obsoletes:		dbus-tqt-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		dbus-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Development files for %{name}

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

%files devel
%defattr(-,root,root,-)
%{tde_includedir}/dbus-1.0/*
%{tde_libdir}/libdbus-tqt-1.so
%{tde_libdir}/libdbus-tqt-1.la
%{tde_libdir}/pkgconfig/dbus-tqt.pc

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

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
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  \
  -DINCLUDE_INSTALL_DIR=%{tde_includedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  ..

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build


%clean
%__rm -rf %{?buildroot}


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 1:0.63-1
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-1
- Initial release for TDE 3.5.13.2
