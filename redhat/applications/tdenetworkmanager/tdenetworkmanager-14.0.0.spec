# Default version for this component
%define tde_pkg tdenetworkmanager
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

%define _docdir %{tde_tdedocdir}


Name:			trinity-%{tde_pkg}
Version:		0.9
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}

Summary:		Trinity applet for Network Manager

Group:			Applications/Internet
License:		GPLv2+
#URL:			http://en.opensuse.org/Projects/KNetworkManager
URL:			http://www.trinitydesktop.org/

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext


Obsoletes:		trinity-knetworkmanager < %{version}-%{release}
Provides:		trinity-knetworkmanager = %{version}-%{release}

%if 0%{?rhel} || 0%{?fedora}
Requires:		NetworkManager-gnome
%else
Requires:		networkmanager
%endif

BuildRequires:	trinity-dbus-1-tqt-devel
BuildRequires:	trinity-dbus-tqt-devel
BuildRequires:	NetworkManager-glib-devel

%description
KNetworkManager is a system tray applet for controlling network
connections on systems that use the NetworkManager daemon.


%package devel
Summary:		Common data shared among the MySQL GUI Suites
Group:			Development/Libraries
Requires:		%{name} = %{version}-%{release}

%description devel
Development headers for knetworkmanager


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep 
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{tde_includedir}"
export LD_LIBRARY_PATH="%{tde_libdir}"

%if 0%{?rhel} || 0%{?fedora}
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
  ..
  
%__make %{?_smp_mflags} 


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=%{?buildroot} -C build


%clean
%__rm -rf $RPM_BUILD_ROOT


%post
update-desktop-database %{tde_appdir} > /dev/null
/sbin/ldconfig
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
update-desktop-database %{tde_appdir} > /dev/null
/sbin/ldconfig
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

%files 
%defattr(-,root,root,-)
%{tde_bindir}/tdenetworkmanager
%{tde_libdir}/*.la
%{tde_libdir}/*.so
%{_sysconfdir}/dbus-1/system.d/tdenetworkmanager.conf
%{tde_tdeappdir}/tdenetworkmanager.desktop
%{tde_datadir}/apps/tdenetworkmanager
%{tde_datadir}/icons/hicolor/*/apps/tdenetworkmanager*
%{tde_datadir}/servicetypes/tdenetworkmanager_plugin.desktop
%{tde_datadir}/servicetypes/tdenetworkmanager_vpnplugin.desktop
%{tde_datadir}/autostart/tdenetworkmanager.desktop
%{tde_datadir}/services/tdenetman_openvpn.desktop
%{tde_datadir}/services/tdenetman_pptp.desktop
%{tde_datadir}/services/tdenetman_strongswan.desktop
%{tde_datadir}/services/tdenetman_vpnc.desktop


%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/*.h
%{tde_tdelibdir}/*.la
%{tde_tdelibdir}/*.so

%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.9-1
- Initial release for TDE 14.0.0