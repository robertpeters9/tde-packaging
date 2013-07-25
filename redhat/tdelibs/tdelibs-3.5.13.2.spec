# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.13 specific variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

Name:		trinity-tdelibs
Version:	3.5.13.2
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
License:	GPL
Summary:	TDE Libraries
Group:		Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz

Patch1:		tdelibs-3.5.13.2-xdg_dirs_set_path.patch
Patch2:		tdelibs-3.5.13.2-cups_by_default.patch

Obsoletes:	tdelibs < %{version}-%{release}
Provides:	tdelibs = %{version}-%{release}
Obsoletes:	trinity-kdelibs < %{version}-%{release}
Provides:	trinity-kdelibs = %{version}-%{release}
Obsoletes:	trinity-kdelibs-apidocs < %{version}-%{release}
Provides:	trinity-kdelibs-apidocs = %{version}-%{release}


BuildRequires:	cmake >= 2.8
BuildRequires:	libtool
BuildRequires:	qt3-devel
BuildRequires:	trinity-tqtinterface-devel >= %{version}
BuildRequires:	trinity-arts-devel >= %{version}
BuildRequires:	krb5-devel
BuildRequires:	libxslt-devel
BuildRequires:	cups-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	openssl-devel
BuildRequires:	gcc-c++
BuildRequires:	alsa-lib-devel
BuildRequires:	libidn-devel
BuildRequires:	libtiff-devel
BuildRequires:	glib2-devel
# LUA support are not ready yet
#BuildRequires:	lua-devel

# ASPELL support
BuildRequires:	aspell
BuildRequires:	aspell-devel

# GAMIN support
#  Not on openSUSE.
%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%define with_gamin 1
BuildRequires:	gamin-devel
%endif

# PCRE support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_pcre 1
BuildRequires:	pcre-devel
%endif

# INOTIFY support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_inotify 1
%endif

# BZIP2 support
%if 0%{?suse_version}
BuildRequires:	libbz2-devel
%else
BuildRequires:	bzip2-devel
%endif

# UTEMPTER support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	libutempter-devel
%endif
%if 0%{?rhel} == 4
BuildRequires:	utempter
%endif
%if 0%{?suse_version}
BuildRequires:	utempter-devel
%endif

# HSPELL support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%define with_hspell 1
BuildRequires:	hspell-devel
%endif

# JASPER support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_jasper 1
%if 0%{?suse_version}
BuildRequires:	libjasper-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}jasper-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	jasper-devel
%endif
%endif

# AVAHI support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_avahi 1
BuildRequires:	trinity-avahi-tqt-devel >= %{version}
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}avahi-client-devel
Requires:		%{_lib}avahi-client3
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version}
BuildRequires:	avahi-devel
Requires:		avahi
%endif
%endif

# OPENEXR support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_openexr 1
BuildRequires:	OpenEXR-devel
%endif

# LIBTOOL
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}ltdl-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version} >= 1220
BuildRequires:	libtool-ltdl-devel
%endif
%if 0%{?rhel} == 4 || 0%{?suse_version} == 1140
BuildRequires:	libtool
%endif

# X11 support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	x11-proto-devel
BuildRequires:	%{_lib}xcomposite%{?mgaversion:1}-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version}
BuildRequires:	xorg-x11-proto-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version} >= 1220
BuildRequires:	libXcomposite-devel
%endif
%if 0%{?rhel} == 4
BuildRequires:	xorg-x11-devel
%endif

# ICEAUTH
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version} >= 1220
Requires:		iceauth
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora}
Requires:		xorg-x11-server-utils
%endif
%if 0%{?rhel} == 4 || 0%{?suse_version}
Requires:		xorg-x11
%endif

# XZ support
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version}
%define with_lzma 1
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}lzma-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version}
BuildRequires:	xz-devel
%endif
%endif

Requires:		trinity-tqtinterface >= %{version}
Requires:		trinity-arts >= %{version}
Requires:		qt3 >= 3.3.8.d

%description
Libraries for the Trinity Desktop Environment:
TDE Libraries included: tdecore (TDE core library), kdeui (user interface),
kfm (file manager), khtmlw (HTML widget), kio (Input/Output, networking),
kspell (spelling checker), jscript (javascript), kab (addressbook),
kimgio (image manipulation).

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING-DOCS COPYING.LIB README TODO
%{tde_bindir}/artsmessage
%{tde_bindir}/cupsdconf
%{tde_bindir}/cupsdoprint
%{tde_bindir}/dcop
%{tde_bindir}/dcopclient
%{tde_bindir}/dcopfind
%{tde_bindir}/dcopobject
%{tde_bindir}/dcopquit
%{tde_bindir}/dcopref
%{tde_bindir}/dcopserver
%{tde_bindir}/dcopserver_shutdown
%{tde_bindir}/dcopstart
%{tde_bindir}/filesharelist
%{tde_bindir}/fileshareset
%{tde_bindir}/imagetops
%{tde_bindir}/kab2kabc
%{tde_bindir}/kaddprinterwizard
%{tde_bindir}/kbuildsycoca
%{tde_bindir}/kcmshell
%{tde_bindir}/kconf_update
%{tde_bindir}/kcookiejar
%{tde_bindir}/kde-config
%{tde_bindir}/kde-menu
%{tde_bindir}/kded
%{tde_bindir}/kdeinit
%{tde_bindir}/kdeinit_shutdown
%{tde_bindir}/kdeinit_wrapper
%{tde_bindir}/kdesu_stub
%{tde_bindir}/kdontchangethehostname
%{tde_bindir}/kdostartupconfig
%{tde_bindir}/kfile
%{tde_bindir}/kfmexec
%{tde_bindir}/khotnewstuff
%{tde_bindir}/kinstalltheme
%{tde_bindir}/kio_http_cache_cleaner
%{tde_bindir}/kio_uiserver
%{tde_bindir}/kioexec
%{tde_bindir}/kioslave
%{tde_bindir}/klauncher
%{tde_bindir}/kmailservice
%{tde_bindir}/kmimelist
%attr(4755,root,root) %{tde_bindir}/kpac_dhcp_helper
%{tde_bindir}/ksendbugmail
%{tde_bindir}/kshell
%{tde_bindir}/kstartupconfig
%{tde_bindir}/ktelnetservice
%{tde_bindir}/ktradertest
%{tde_bindir}/kwrapper
%{tde_bindir}/lnusertemp
%{tde_bindir}/make_driver_db_cups
%{tde_bindir}/make_driver_db_lpr
%{tde_bindir}/meinproc
%{tde_bindir}/networkstatustestservice
%{tde_bindir}/start_kdeinit
%{tde_bindir}/start_kdeinit_wrapper
%attr(4755,root,root) %{tde_bindir}/kgrantpty
%{tde_tdelibdir}/*
%{tde_libdir}/lib*.so.*
%{tde_libdir}/lib[kt]deinit_*.la
%{tde_libdir}/lib[kt]deinit_*.so
%{tde_datadir}/applications/kde/*.desktop
%{tde_datadir}/autostart/kab2kabc.desktop
%{tde_datadir}/applnk/kio_iso.desktop
%{tde_datadir}/apps/*
%exclude %{tde_datadir}/apps/ksgmltools2/
%config(noreplace) %{tde_datadir}/config/*
%{tde_datadir}/emoticons/*
%{tde_datadir}/icons/default.kde
%{_sysconfdir}/alternatives/default.kde
%{tde_datadir}/mimelnk/magic
%{tde_datadir}/mimelnk/*/*.desktop
%{tde_datadir}/services/*
%{tde_datadir}/servicetypes/*
%{tde_datadir}/icons/crystalsvg/
%{tde_tdedocdir}/HTML/en/kspell/
# remove conflicts with kdelibs-4
%if "%{?tde_prefix}" != "/usr"
%{tde_bindir}/checkXML
%{tde_bindir}/ksvgtopng
%{tde_bindir}/kunittestmodrunner
%{tde_bindir}/preparetips
%{tde_datadir}/icons/hicolor/index.theme
%{tde_datadir}/locale/all_languages
%{tde_tdedocdir}/HTML/en/common/*
%{_sysconfdir}/ld.so.conf.d/trinity.conf
%else
%exclude %{tde_bindir}/checkXML
%exclude %{tde_bindir}/ksvgtopng
%exclude %{tde_bindir}/kunittestmodrunner
%exclude %{tde_bindir}/preparetips
%exclude %{tde_datadir}/config/colors
%exclude %{tde_datadir}/config/kdebug.areas
%exclude %{tde_datadir}/config/kdebugrc
%exclude %{tde_datadir}/config/ksslcalist
%exclude %{tde_datadir}/config/ui/ui_standards.rc
%exclude %{tde_datadir}/icons/hicolor/index.theme
%exclude %{tde_datadir}/locale/all_languages
%exclude %{tde_tdedocdir}/HTML/en/common/*
%endif

# Avoid conflict with 'redhat-menus' package
%if "%{tde_prefix}" == "/usr"
%{_sysconfdir}/xdg/menus/kde-applications.menu
%else
%{tde_prefix}/etc/xdg/menus/kde-applications.menu
%endif

# New in TDE 3.5.13
%{tde_bindir}/kdetcompmgr

%pre
# TDE Bug #1074
if [ -d "%{tde_datadir}/locale/all_languages" ]; then
  rm -rf "%{tde_datadir}/locale/all_languages"
fi

%post
/sbin/ldconfig || :
# Sets default theme as 'crystalsvg'
update-alternatives --install \
  %{tde_datadir}/icons/default.kde \
  default.kde \
  %{tde_datadir}/icons/crystalsvg \
  10 || :

%preun
if [ $1 -eq 0 ]; then
  update-alternatives --remove \
    default.kde \
    %{tde_datadir}/icons/crystalsvg || :
fi

%postun
/sbin/ldconfig || :

##########

%package devel
Summary:	%{name} - Development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

Obsoletes:	tdelibs-devel < %{version}-%{release}
Provides:	tdelibs-devel = %{version}-%{release}
Obsoletes:	trinity-kdelibs-devel < %{version}-%{release}
Provides:	trinity-kdelibs-devel = %{version}-%{release}

%description devel
This package includes the header files you will need to compile
applications for TDE.

%files devel
%defattr(-,root,root,-)
%{tde_bindir}/dcopidl*
%{tde_bindir}/kconfig_compiler
%{tde_bindir}/makekdewidgets
%{tde_datadir}/apps/ksgmltools2/
%{tde_tdeincludedir}/*
%{tde_libdir}/*.la
%{tde_libdir}/*.so
%{tde_libdir}/*.a
%exclude %{tde_libdir}/lib[kt]deinit_*.la
%exclude %{tde_libdir}/lib[kt]deinit_*.so

# New in TDE 3.5.13
%{tde_datadir}/cmake/[kt]delibs.cmake

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}
%patch1 -p1 -b .xdg_path
%patch2 -p1 -b .cups_by_default


%build
unset QTDIR || : ; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${QTDIR}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{tde_includedir}:%{tde_includedir}/tqt"

# We need LD_LIBRARY_PATH here because ld.so.conf file has not been written yet
export LD_LIBRARY_PATH="%{tde_libdir}"

export KDEDIR="%{tde_prefix}"

if [ -d "/usr/X11R6" ]; then
  export CXXFLAGS="${RPM_OPT_FLAGS} -L/usr/X11R6/%{_lib} -I/usr/X11R6/include"
fi


%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%__mkdir_p build
cd build
%endif

%cmake \
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DBIN_INSTALL_DIR="%{tde_bindir}" \
  -DDOC_INSTALL_DIR="%{tde_docdir}" \
  -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig" \
  -DSHARE_INSTALL_PREFIX="%{tde_datadir}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DWITH_ARTS=ON \
  -DWITH_ALSA=ON \
  -DWITH_LIBART=ON \
  -DWITH_LIBIDN=ON \
  -DWITH_SSL=ON \
  -DWITH_CUPS=ON \
  -DWITH_LUA=OFF \
  -DWITH_TIFF=ON \
  %{?with_jasper:-DWITH_JASPER=ON} \
  %{?with_openexr:-DWITH_OPENEXR=ON} \
  -DWITH_UTEMPTER=ON \
  %{?with_avahi:-DWITH_AVAHI=ON} \
  %{?!with_pcre:-DWITH_PCRE=OFF} \
  %{?!with_inotify:-DWITH_INOTIFY=OFF} \
  %{?!with_gamin:-DWITH_GAMIN=OFF} %{?with_gamin:-DWITH_GAMIN=ON} \
  -DWITH_SUDO_KDESU_BACKEND=OFF \
  %{?with_lzma:-DWITH_LZMA=ON} %{?!with_lzma:-DWITH_LZMA=OFF} \
  -DWITH_ASPELL=ON \
  %{?with_hspell:-DWITH_HSPELL=ON} \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf "%{?buildroot}"
%__make install DESTDIR="%{?buildroot}" -C build

%if "%{?tde_prefix}" != "/usr"
%__mkdir_p "%{?buildroot}%{_sysconfdir}/ld.so.conf.d"
cat <<EOF >"%{?buildroot}%{_sysconfdir}/ld.so.conf.d/trinity.conf"
%{tde_libdir}
EOF
%endif

# Moves the XDG configuration files to TDE directory
%if "%{tde_prefix}" != "/usr"
%__install -p -D -m644 \
  "%{?buildroot}%{_sysconfdir}/xdg/menus/applications.menu" \
  "%{?buildroot}%{tde_prefix}/etc/xdg/menus/kde-applications.menu"
%__rm -rf "%{?buildroot}%{_sysconfdir}/xdg"
%else
%__mv -f "%{?buildroot}%{_sysconfdir}/xdg/menus/applications.menu" "%{?buildroot}%{_sysconfdir}/xdg/menus/kde-applications.menu"
%endif

# Makes 'default.kde' theme an alternative with 'crystalsvg-updated'
%__rm -f "%{?buildroot}%{tde_datadir}/icons/default.kde"
%__ln_s "%{_sysconfdir}/alternatives/default.kde" "%{?buildroot}%{tde_datadir}/icons/default.kde"
%__mkdir_p "%{?buildroot}%{_sysconfdir}/alternatives"
%__ln_s "%{tde_datadir}/icons/crystalsvg" "%{?buildroot}%{_sysconfdir}/alternatives/default.kde"


%clean
%__rm -rf "%{?buildroot}"


%changelog
* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-1
- Initial release for TDE 3.5.13.2