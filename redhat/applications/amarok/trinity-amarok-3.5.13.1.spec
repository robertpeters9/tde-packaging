# Basic package informations
%define kdecomp amarok

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.13 specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-%{kdecomp}
Summary:	Media player
Version:	1.4.10
Release:	8%{?dist}%{?_variant}

Group: 	    Applications/Multimedia
License:    GPLv2+
Url:        http://amarok.kde.org

Prefix:     %{tde_prefix}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:    amarok-3.5.13.1.tar.gz

Patch1:		amarok-3.5.13.1-add_xine12_support.patch
Patch2:		amarok-3.5.13.1-fix_inotify_detection.patch
Patch3:		amarok-3.5.13.1-fix_rhel4_libs.patch

BuildRequires:	trinity-tqtinterface-devel >= 3.5.13.1
BuildRequires:	trinity-tdelibs-devel >= 3.5.13.1
BuildRequires:	trinity-tdebase-devel >= 3.5.13.1
BuildRequires:	trinity-akode-devel
BuildRequires:	trinity-konqueror-devel >= 3.5.13.1

BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  esound-devel
BuildRequires:  gettext
BuildRequires:	pcre-devel
BuildRequires:  taglib-devel 

%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	libmp4v2-devel
%endif

BuildRequires:  libtool
%if 0%{?fedora} > 4 || 0%{?rhel} > 4
BuildRequires:  libtool-ltdl-devel
%endif
BuildRequires:  libusb-devel
BuildRequires:  mysql-devel
BuildRequires:  postgresql-devel
BuildRequires:  SDL-devel
BuildRequires:  taglib-devel
BuildRequires:	sqlite-devel
# not used anymore, in favor of libvisual ? -- Rex
#%{?fedora:BuildRequires:  xmms-devel}


# DBUS support
%if 0%{?suse_version}
BuildRequires:	dbus-1-devel
%else
BuildRequires:	dbus-devel
%endif
%if 0%{?rhel} == 4
BuildRequires:	dbus-qt
%else
BuildRequires:	trinity-dbus-tqt-devel >= 3.5.13.1
%endif

# IFP support
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%define with_ifp 1
BuildRequires:  libifp-devel
%endif

# KARMA support
%if 0%{?mgaversion} || 0%{?mdkversion}
%define with_karma 1
BuildRequires:	libkarma-devel
BuildRequires:	karma-sharp
%endif

%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}

# GPOD (ipod) support
%define with_gpod 1
%if 0%{?rhel} == 5
BuildRequires:  trinity-libgpod-devel >= 0.4.2
%else
BuildRequires:  libgpod-devel >= 0.4.2
%endif

# MTP players
%define with_mtp 1
BuildRequires:  libmtp-devel
BuildRequires:  libmusicbrainz-devel

# Creative Nomad Jukebox
%define with_njb 1
BuildRequires:  libnjb-devel

# VISUAL support
%define with_libvisual 1
BuildRequires:  libvisual-devel

# TUNEPIMP support
BuildRequires:  libtunepimp-devel

# INOTIFY support
%define with_inotify 1
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}inotifytools-devel
%endif

# XINE support
%define with_xine 1
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
BuildRequires:  libxine-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:  xine-lib-devel
%endif

# YAUAP support
%define with_yauap 1

%endif

# ruby
BuildRequires:	ruby
BuildRequires:  ruby-devel

# To open the selected browser, works with Patch2
Requires:  xdg-utils
Requires(post): xdg-utils
Requires(postun): xdg-utils


%description
Amarok is a multimedia player with:
 - fresh playlist concept, very fast to use, with drag and drop
 - plays all formats supported by the various engines
 - audio effects, like reverb and compressor
 - compatible with the .m3u and .pls formats for playlists
 - nice GUI, integrates into the TDE look, but with a unique touch

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS ChangeLog README
%{tde_bindir}/amarok
%{tde_bindir}/amarokapp
%{tde_bindir}/amarokcollectionscanner
%{tde_bindir}/amarok_proxy.rb
%{tde_datadir}/apps/amarok/
%{tde_datadir}/icons/hicolor/*/*/*
%{tde_datadir}/applications/kde/*.desktop
%{tde_datadir}/servicetypes/*.desktop
%{tde_datadir}/apps/profiles/amarok.profile.xml
%{tde_datadir}/config/amarokrc
%{tde_datadir}/config.kcfg/*.kcfg
%{tde_datadir}/services/amarokitpc.protocol
%{tde_datadir}/services/amaroklastfm.protocol
%{tde_datadir}/services/amarokpcast.protocol
# -libs ?  -- Rex
%{tde_libdir}/libamarok.so.0
%{tde_libdir}/libamarok.so.0.0.0
# DAAP
%{tde_bindir}/amarok_daapserver.rb
%{tde_tdelibdir}/libamarok_daap-mediadevice.*
%{tde_datadir}/services/amarok_daap-mediadevice.desktop
# Mass-storage
%{tde_datadir}/services/amarok_massstorage-device.desktop
%{tde_tdelibdir}/libamarok_massstorage-device.*
# NFS
%{tde_datadir}/services/amarok_nfs-device.desktop
%{tde_tdelibdir}/libamarok_nfs-device.*
# SMB
%{tde_datadir}/services/amarok_smb-device.desktop
%{tde_tdelibdir}/libamarok_smb-device.*
# IPod
%if 0%{?with_gpod}
%{tde_datadir}/services/amarok_ipod-mediadevice.desktop
%{tde_tdelibdir}/libamarok_ipod-mediadevice.*
%endif
# VFAT
%{tde_datadir}/services/amarok_generic-mediadevice.desktop
%{tde_tdelibdir}/libamarok_generic-mediadevice.*
# iRiver
%if 0%{?with_ifp}
%{tde_datadir}/services/amarok_ifp-mediadevice.desktop
%{tde_tdelibdir}/libamarok_ifp-mediadevice.*
%endif
# Creative Zen
%if 0%{?with_njb}
%{tde_datadir}/services/amarok_njb-mediadevice.desktop
%{tde_tdelibdir}/libamarok_njb-mediadevice.*
%endif
# MTP players
%if 0%{?with_mtp}
%{tde_datadir}/services/amarok_mtp-mediadevice.desktop
%{tde_tdelibdir}/libamarok_mtp-mediadevice.*
%endif
# Rio Karma
%if 0%{?with_karma}
%{tde_datadir}/services/amarok_riokarma-mediadevice.desktop
%{tde_tdelibdir}/libamarok_riokarma-mediadevice.*
%endif
# Void engine (noop)
%{tde_datadir}/services/amarok_void-engine_plugin.desktop
%{tde_tdelibdir}/libamarok_void-engine_plugin.*
# Xine engine
%if 0%{?with_xine}
%{tde_datadir}/services/amarok_xine-engine.desktop
%{tde_tdelibdir}/libamarok_xine-engine.*
%endif
## Gstreamer engine
#%{tde_datadir}/services/amarok_gst10engine_plugin.desktop
#%{tde_tdelibdir}/libamarok_gst10engine_plugin.*
# YAUAP
%if 0%{?with_yauap}
%{tde_datadir}/services/amarok_yauap-engine_plugin.desktop
%{tde_tdelibdir}/libamarok_yauap-engine_plugin.*
%endif
# AKODE
%{tde_datadir}/services/amarok_aKode-engine.desktop
%{tde_tdelibdir}/libamarok_aKode-engine.*

%post
/sbin/ldconfig
xdg-icon-resource forceupdate --theme hicolor 2> /dev/null || :
xdg-desktop-menu forceupdate 2> /dev/null || :

%postun
/sbin/ldconfig
xdg-icon-resource forceupdate --theme hicolor 2> /dev/null || :
xdg-desktop-menu forceupdate 2> /dev/null || :


##########

%package ruby
Summary:	%{name} Ruby support
Group:		Applications/Multimedia
Requires: %{name} = %{version}-%{release}
# For dir ownership and some default plugins (lyrics)
Requires:  ruby

%description ruby
%{summary}.

%files ruby
%defattr(-,root,root,-)
%{tde_libdir}/ruby_lib/*

##########

%package konqueror
Summary:	Amarok konqueror (service menus, sidebar) support
Group:		Applications/Multimedia

Requires:	%{name} = %{version}-%{release}
Requires:	trinity-konqueror

%description konqueror
%{summary}.

%files konqueror
%defattr(-,root,root,-)
%{tde_datadir}/apps/konqueror/servicemenus/*.desktop
%{tde_tdelibdir}/konqsidebar_universalamarok.*
%{tde_datadir}/apps/konqsidebartng/*/amarok.desktop


##########

%if 0%{?with_libvisual}

%package visualisation
Summary:    Visualisation plugins for Amarok
Group:      Applications/Multimedia
Requires:   %{name} = %{version}-%{release}
# No plugins by default, we need libvisual-plugins
#Requires:   libvisual-plugins

%description visualisation
Amarok can use visualisation plugins from different origins.
Right now, only xmms is supported, which means that you can
use any of xmms' visualisation plugins with Amarok.

%files visualisation
%defattr(-,root,root,-)
%{tde_bindir}/amarok_libvisual

%endif

##########

%if 0%{?suse_version}
%debug_package
%endif

##########

%prep
%setup -q -n amarok-3.5.13.1
%patch1 -p1 -b .xine
%patch2 -p1 -b .inotify
%if 0%{?rhel} == 4
%patch3 -p1 -b .rhel4
%endif

%build
unset QTDIR; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"
export CMAKE_INCLUDE_PATH="%{tde_includedir}:%{tde_includedir}/tqt:%{tde_tdeincludedir}"

# Do not build against any "/usr" installed KDE
export KDEDIR=%{tde_prefix}

# Specific path for RHEL4
if [ -d /usr/X11R6 ]; then
  export CXXFLAGS="${CXXFLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
fi

%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%__mkdir_p build
cd build
%endif

%cmake \
	-DBIN_INSTALL_DIR=%{tde_bindir} \
	-DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
	-DLIB_INSTALL_DIR=%{tde_libdir} \
	-DSHARE_INSTALL_PREFIX=%{tde_datadir} \
	-DCMAKE_SKIP_RPATH="OFF" \
	-DQT_LIBRARY_DIRS="${QTLIB:-${QTDIR}/%{_lib}}" \
	%{?with_libvisual:-DWITH_LIBVISUAL=ON} \
	-DWITH_KONQSIDEBAR=ON \
	%{?with_xine:-DWITH_XINE=ON} \
	%{?with_yauap:-DWITH_YAUAP=ON} \
	-DWITH_AKODE=ON \
	%{?with_gpod:-DWITH_IPOD=ON} \
	%{?with_ifp:-DWITH_IFP=ON} \
	%{?with_njb:-DWITH_NJB=ON} \
	%{?with_mtp:-DWITH_MTP=ON} \
	%{?with_karma:-DWITH_RIOKARMA=ON} \
	%{?with_inotify:-DWITH_INOTIFY=ON} \
	-DWITH_DAAP=ON \
	-DBUILD_ALL=ON \
	..

%__make %{?_smp_mflags}

%install
%__rm -fr $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT -C build


# unpackaged files
%__rm -f $RPM_BUILD_ROOT%{tde_libdir}/lib*.la
# Removes '.so' to avoid automatic -devel dependency
%__rm -f $RPM_BUILD_ROOT%{tde_libdir}/libamarok.so

# HTML
for lang_dir in $RPM_BUILD_ROOT%{tde_tdedocdir}/HTML/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    [ "$lang" == "en" ] && d=en/amarok || d=$lang
    echo "%lang($lang) %doc %{tde_tdedocdir}/HTML/$d" >> %{name}.lang
  fi
done

# Locales
for locale in $RPM_BUILD_ROOT%{tde_datadir}/locale/* ; do
  if [ -r $locale/LC_MESSAGES/amarok.mo ]; then
    lang=$(basename $locale)
    echo "%lang($lang) %{tde_datadir}/locale/$lang/LC_MESSAGES/amarok.mo" >> %{name}.lang
  fi
done


%clean
%__rm -fr $RPM_BUILD_ROOT


%changelog
* Tue Oct 02 2012 Francois Andriot <francois.andriot@free.fr> - 1.4.10-8
- Initial release for TDE 3.5.13.1