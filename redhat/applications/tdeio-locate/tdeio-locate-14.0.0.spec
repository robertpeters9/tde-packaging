# Default version for this component
%define tde_pkg tdeio-locate
%define tde_version 14.0.0

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		kio-slave for the locate command [Trinity]
Version:		0.4.5
Release:		%{?!preversion:5}%{?preversion:4_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	cmake >= 2.8

Obsoletes:		trinity-kio-locate < %{version}-%{release}
Provides:		trinity-kio-locate = %{version}-%{release}

%description
Adds support for the "locate" and "locater:"
protocols to Konqueror and other TDE applications.

This enables you to perform locate searches as you
would in a terminal. The result is displayed just
as a directory.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

export CMAKE_INCLUDE_PATH="%{tde_tdeincludedir}"

# Shitty hack for RHEL4 ...
if [ -d "/usr/X11R6" ]; then
  export CMAKE_INCLUDE_PATH="${CMAKE_INCLUDE_PATH}:/usr/X11R6/include:/usr/X11R6/%{_lib}"
  export CFLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
  export CXXFLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
fi

%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%__mkdir_p build
cd build
%endif


%cmake \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  -DCMAKE_SKIP_RPATH="OFF" \
  -DBUILD_ALL=ON \
  ..

# SMP safe !
%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

%find_lang kio-locate

%clean
%__rm -rf %{buildroot}



%files -f kio-locate.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING TODO
%{tde_tdelibdir}/tdeio_locate.la
%{tde_tdelibdir}/tdeio_locate.so
%{tde_tdedocdir}/HTML/en/kio-locate/
%{tde_datadir}/services/locate.protocol
%{tde_datadir}/services/locater.protocol
%{tde_datadir}/services/rlocate.protocol
%{tde_datadir}/services/searchproviders/locate.desktop

%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.4.5-5
- Initial release for TDE 14.0.0

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.4.5-4
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.4.5-3
- Initial release for TDE 3.5.13.1

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.4.5-2
- Rebuilt for Fedora 17
- Removes post and postun
- Fix compilation with GCC 4.7

* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 0.4.5-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
