# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE specific variables
BuildRequires: cmake >= 2.8
%define tde_docdir %{_docdir}/trinity
%define tde_libdir %{_libdir}/trinity

# Older RHEL/Fedora versions use packages named "qt", "qt-devel", ..
# whereas newer versions use "qt3", "qt3-devel" ...
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 8
%define _qt_suffix 3
%endif


Name:		tdelibs
Version:	r14
Release:	1%{?dist}%{?_variant}
License:	GPL
Summary:	TDE Libraries
Group:		System Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	tdelibs-%{version}.tar.gz
Patch0:		git.patch

## [kdelibs/kio] Disable 'max line length' detection [Bug #656]
Patch10:	kdelibs-3.5.13-maxlinelength.patch

BuildRequires:	libtool
BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-arts-devel
BuildRequires:	avahi-devel
BuildRequires:	lua-devel
BuildRequires:	krb5-devel libxslt-devel cups-devel libart_lgpl-devel pcre-devel
BuildRequires:	libutempter-devel
BuildRequires:	bzip2-devel
BuildRequires:	openssl-devel
BuildRequires:	gcc-c++
BuildRequires:	alsa-lib-devel
BuildRequires:	libidn-devel
BuildRequires:	tqt3-devel >= 3.4.0
BuildRequires:	avahi-tqt-devel
BuildRequires:	jasper-devel
BuildRequires:	libtiff-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	libtool-ltdl-devel
BuildRequires:	glib2-devel
BuildRequires:	gamin-devel
BuildRequires:	xorg-x11-proto-devel

Requires:		tqtinterface
Requires:		trinity-arts
Requires:		avahi
Requires:		tqt3 >= 3.4.0
Requires:		avahi-tqt

Obsoletes:		trinity-kdelibs <= 3.5.13

%if "%{?_prefix}" == "/usr"
Provides:		kdelibs%{?_qt_suffix} = %{version}
Obsoletes:		kdelibs%{?_qt_suffix} <= 3.5.10
%endif

%description
Libraries for the Trinity Desktop Environment:
KDE Libraries included: kdecore (KDE core library), kdeui (user interface),
kfm (file manager), khtmlw (HTML widget), kio (Input/Output, networking),
kspell (spelling checker), jscript (javascript), kab (addressbook),
kimgio (image manipulation).


%package devel
Summary:	%{name} - Development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:		trinity-kdelibs-devel <= 3.5.13
%if "%{?_prefix}" == "/usr"
Provides:	kdelibs%{?_qt_suffix}-devel = %{version}
Obsoletes:	kdelibs%{?_qt_suffix}-devel <= 3.5.10
%endif

%description devel
This package includes the header files you will need to compile
applications for TDE.

%package apidocs
Group:		Development/Libraries
Summary:	%{name} - API documentation
Requires:	%{name} = %{version}-%{release}
Obsoletes:		trinity-kdelibs-apidocs <= 3.5.13
%if "%{?_prefix}" == "/usr"
Provides:	kdelibs%{?_qt_suffix}-apidocs = %{version}
Obsoletes:	kdelibs%{?_qt_suffix}-apidocs <= 3.5.10
%endif

%description apidocs
This package includes the TDE API documentation in HTML
format for easy browsing


%prep
%setup -q -n tdelibs
#patch0 -p1
%patch10 -p1


%build
export PATH="%{_bindir}:${PATH}"
export LD_LIBRARY_PATH="%{_libdir}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"

%__mkdir build
cd build
%cmake \
  -DHAVE_REAL_TQT=ON \
  -DHTML_INSTALL_DIR=%{tde_docdir}/HTML \
  -DWITH_ARTS=ON \
  -DWITH_ALSA=ON \
  -DWITH_LIBART=ON \
  -DWITH_LIBIDN=OFF \
  -DWITH_SSL=ON \
  -DWITH_CUPS=ON \
  -DWITH_LUA=OFF \
  -DWITH_TIFF=ON \
  -DWITH_JASPER=ON \
  -DWITH_OPENEXR=ON \
  -DWITH_UTEMPTER=ON \
  -DWITH_AVAHI=ON \
  -DWITH_ASPELL=OFF \
  -DWITH_HSPELL=OFF \
  -DWITH_PCRE=ON \
  -DWITH_INOTIFY=ON \
  -DWITH_GAMIN=ON \
  ..

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

%__mkdir_p %{?buildroot}%{_sysconfdir}/ld.so.conf.d
cat <<EOF >%{?buildroot}%{_sysconfdir}/ld.so.conf.d/trinity.conf
%if "%{?_prefix}" != "/usr"
%{_libdir}
%endif
%{tde_libdir}
EOF

# Moves the XDG configuration files to TDE directory
%if "%{_prefix}" != "/usr"
  %__install -p -D -m644 \
    "%{?buildroot}%{_sysconfdir}/xdg/menus/applications.menu" \
    "%{?buildroot}%{_prefix}/etc/xdg/menus/kde-applications.menu"
  %__rm -rf "%{?buildroot}%{_sysconfdir}/xdg"
%else
  %__mv -f "%{?buildroot}%{_sysconfdir}/xdg/menus/applications.menu" "%{?buildroot}%{_sysconfdir}/xdg/menus/kde-applications.menu"
%endif


%clean
%__rm -rf %{?buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc README
%doc COPYING.LIB
%{_bindir}/artsmessage
%{_bindir}/cupsdconf
%{_bindir}/cupsdoprint
%{_bindir}/dcop
%{_bindir}/dcopclient
%{_bindir}/dcopfind
%{_bindir}/dcopobject
%{_bindir}/dcopquit
%{_bindir}/dcopref
%{_bindir}/dcopserver
%{_bindir}/dcopserver_shutdown
%{_bindir}/dcopstart
%{_bindir}/filesharelist
%{_bindir}/fileshareset
%{_bindir}/imagetops
%{_bindir}/kab2kabc
%{_bindir}/kaddprinterwizard
%{_bindir}/kbuildsycoca
%{_bindir}/kcmshell
%{_bindir}/kconf_update
%{_bindir}/kcookiejar
%{_bindir}/tde-config
%{_bindir}/kde-menu
%{_bindir}/kded
%{_bindir}/tdeinit
%{_bindir}/tdeinit_shutdown
%{_bindir}/tdeinit_wrapper
%{_bindir}/tdesu_stub
%{_bindir}/kdontchangethehostname
%{_bindir}/kdostartupconfig
%{_bindir}/kfile
%{_bindir}/kfmexec
%{_bindir}/khotnewstuff
%{_bindir}/kinstalltheme
%{_bindir}/kio_http_cache_cleaner
%{_bindir}/kio_uiserver
%{_bindir}/kioexec
%{_bindir}/kioslave
%{_bindir}/klauncher
%{_bindir}/kmailservice
%{_bindir}/kmimelist
%attr(4755,root,root) %{_bindir}/kpac_dhcp_helper
%{_bindir}/ksendbugmail
%{_bindir}/kshell
%{_bindir}/kstartupconfig
%{_bindir}/ktelnetservice
%{_bindir}/ktradertest
%{_bindir}/kwrapper
%{_bindir}/lnusertemp
%{_bindir}/make_driver_db_cups
%{_bindir}/make_driver_db_lpr
%{_bindir}/meinproc
%{_bindir}/networkstatustestservice
%{_bindir}/start_tdeinit
%{_bindir}/start_tdeinit_wrapper
%attr(4755,root,root) %{_bindir}/kgrantpty
%{_libdir}/lib*.so.*
%{_libdir}/libtdeinit_*.so
%{_libdir}/lib*.la
%{tde_libdir}/
%{_datadir}/applications/kde/*.desktop
%{_datadir}/autostart/kab2kabc.desktop
%{_datadir}/applnk/kio_iso.desktop
%{_datadir}/apps/*
%exclude %{_datadir}/apps/ksgmltools2/
%config(noreplace) %{_datadir}/config/*
%{_datadir}/emoticons/*
%{_datadir}/icons/default.kde
%{_datadir}/mimelnk/magic
%{_datadir}/mimelnk/*/*.desktop
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/icons/crystalsvg/
%{tde_docdir}/HTML/en/kspell
# remove conflicts with kdelibs-4
%if "%{?_prefix}" != "/usr"
%{_bindir}/checkXML
%{_bindir}/ksvgtopng
%{_bindir}/kunittestmodrunner
%{_bindir}/preparetips
%{_datadir}/icons/hicolor/index.theme
%{_datadir}/locale/all_languages
%{tde_docdir}/HTML/en/common/*
%else
%exclude %{_bindir}/checkXML
%exclude %{_bindir}/ksvgtopng
%exclude %{_bindir}/kunittestmodrunner
%exclude %{_bindir}/preparetips
%exclude %{_datadir}/config/colors
%exclude %{_datadir}/config/kdebug.areas
%exclude %{_datadir}/config/kdebugrc
%exclude %{_datadir}/config/ksslcalist
%exclude %{_datadir}/config/ui/ui_standards.rc
%exclude %{_datadir}/icons/hicolor/index.theme
%exclude %{_datadir}/locale/all_languages
%exclude %{tde_docdir}/HTML/en/common/*
%endif
%{_sysconfdir}/ld.so.conf.d/trinity.conf

# Avoid conflict with 'redhat-menus' package
%if "%{_prefix}" == "/usr"
%{_sysconfdir}/xdg/menus/kde-applications.menu
%else
%{_prefix}/etc/xdg/menus/kde-applications.menu
%endif

# New in TDE 3.5.13
%{_bindir}/kdetcompmgr

%files devel
%defattr(-,root,root,-)
%{_bindir}/dcopidl*
%{_bindir}/kconfig_compiler
%{_bindir}/makekdewidgets
%{_datadir}/apps/ksgmltools2/
%{_includedir}/
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%exclude %{_libdir}/libtdeinit_*.so
%{_datadir}/cmake/tdelibs.cmake

%files apidocs
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}/


%changelog
* Thu Feb 16 2012 Francois Andriot <francois.andriot@free.fr> - r14-1
- Initial build for TDE R14, using 'tqt3' instead of 'qt3'
