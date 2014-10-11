#
# spec file for package arts (version 3.5.13-SRU)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http:/www.trinitydesktop.org/
#

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 1
%define tde_version 3.5.13.2
%define tde_pkg arts
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.5.10
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:	ARTS (analog realtime synthesizer) - the TDE sound system
Group:		System Environment/Daemons 
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	libtqt4-devel >= %{tde_epoch}:4.2.0
BuildRequires:	trinity-filesystem >= %{tde_version}
Requires:		trinity-filesystem >= %{tde_version}

BuildRequires:	cmake >= 2.8
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig

BuildRequires:	audiofile-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	glib2-devel
BuildRequires:	gsl-devel
BuildRequires:	libvorbis-devel

# ESOUND support
%define with_esound 1
BuildRequires:	esound-devel

# JACK support
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?fedora} || 0%{?suse_version} [[ 0%{?with_jack}
%define with_jack 1
%if 0%{?mgaversion} || 0%{?mdkversion}
%define jack_devel %{_lib}jack-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora}
%define jack_devel jack-audio-connection-kit-devel
%endif
%if 0%{?suse_version}
%define jack_devel libjack-devel
%endif
BuildRequires:	%{jack_devel}
%endif

# LIBTOOL
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}ltdl-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora}
BuildRequires:	libtool-ltdl-devel
%endif
%if 0%{?suse_version}
%if 0%{?suse_version} >= 1220
BuildRequires:	libltdl-devel
%else
BuildRequires:	libtool
%endif
%endif

# MAD support
%ifarch %{ix86} x86_64
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel} 
%define with_libmad 1
%if 0%{?mdkversion} || 0%{?mgaversion}
%define mad_devel %{_lib}mad-devel
%endif
%if 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
%define mad_devel libmad-devel
%endif
BuildRequires:		%{mad_devel}
%endif
%endif

# Pulseaudio config file
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?suse_version}
%define with_pulseaudio 1
%endif

Requires:		libtqt4 >= %{tde_epoch}:4.2.0
Requires:		audiofile

%if "%{?tde_prefix}" == "/usr"
Obsoletes:	arts
%endif

%description
arts (analog real-time synthesizer) is the sound system of TDE.

The principle of arts is to create/process sound using small modules which do
certain tasks. These may be create a waveform (oscillators), play samples,
filter data, add signals, perform effects like delay/flanger/chorus, or
output the data to the soundcard.

By connecting all those small modules together, you can perform complex
tasks like simulating a mixer, generating an instrument or things like
playing a wave file with some effects.

%files
%defattr(-,root,root,-)
%doc COPYING.LIB
%dir %{tde_libdir}/mcop
%dir %{tde_libdir}/mcop/Arts
%{tde_libdir}/mcop/Arts/*
%{tde_libdir}/mcop/*.mcopclass
%{tde_libdir}/mcop/*.mcoptype
%{tde_libdir}/lib*.so.*
%{tde_bindir}/artscat
%{tde_bindir}/artsd
%{tde_bindir}/artsdsp
%{tde_bindir}/artsplay
%{tde_bindir}/artsrec
%{tde_bindir}/artsshell
%{tde_bindir}/artswrapper
# The '.la' files are needed for runtime, not devel !
%{tde_libdir}/lib*.la

%post
/sbin/ldconfig || :

%postun
/sbin/ldconfig || :

##########

%package devel
Group:		Development/Libraries
Summary:	ARTS (analog realtime synthesizer) - the TDE sound system (Development files)
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%if "%{?tde_prefix}" == "/usr"
Obsoletes:	arts-devel
%endif

Requires:	alsa-lib-devel
Requires:	audiofile-devel
Requires:	libvorbis-devel
Requires:	esound-devel
%{?with_libmad:Requires: %{mad_devel}}
%{?with_jack:Requires: %{jack_devel}}

%description devel
arts (analog real-time synthesizer) is the sound system of TDE.

The principle of arts is to create/process sound using small modules which do
certain tasks. These may be create a waveform (oscillators), play samples,
filter data, add signals, perform effects like delay/flanger/chorus, or
output the data to the soundcard.

By connecting all those small modules together, you can perform complex
tasks like simulating a mixer, generating an instrument or things like
playing a wave file with some effects.

%files devel
%defattr(-,root,root,-)
%{tde_bindir}/mcopidl
# Arts includes are under 'tde' - this is on purpose !
%{tde_tdeincludedir}/arts/
# Artsc includes are not under 'tde'.
%{tde_includedir}/artsc/
%{tde_bindir}/artsc-config
%{tde_libdir}/lib*.so
%{tde_libdir}/pkgconfig/*.pc
%{tde_libdir}/*.a

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

##########

%if 0%{?with_pulseaudio}

%package config-pulseaudio
Group:		System Environment/Daemons
Summary:	ARTS - Default configuration file for Pulseaudio
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description config-pulseaudio
This package contains a default ARTS configuration file, that is 
intended for systems running the Pulseaudio server.

%files config-pulseaudio
%defattr(-,root,root,-)
%{tde_datadir}/config/kcmartsrc

%endif

##########

%if 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
. /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

if ! rpm -E %%cmake|grep -q "cd build"; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  \
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DBIN_INSTALL_DIR="%{tde_bindir}" \
  -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}/arts" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig" \
  \
  -DWITH_ALSA=ON \
  -DWITH_AUDIOFILE=ON \
  -DWITH_VORBIS=ON \
  %{?with_libmad:-DWITH_MAD=ON} %{!?with_libmad:-DWITH_MAD=OFF} \
  %{?with_esound:-DWITH_ESOUND=ON} \
  %{?with_jack:-DWITH_JACK=ON} \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf %{?buildroot}
%__make install -C build DESTDIR=%{?buildroot}

%__install -d -m 755 %{?buildroot}%{tde_datadir}/config
%__install -d -m 755 %{?buildroot}%{tde_datadir}/doc

# Installs the Pulseaudio configuration file
%if 0%{?with_pulseaudio}
cat <<EOF >"%{?buildroot}%{tde_datadir}/config/kcmartsrc"
[Arts]
Arguments=\s-F 10 -S 4096 -a esd -n -s 1 -m artsmessage -c drkonqi -l 3 -f
NetworkTransparent=true
SuspendTime=1
EOF
chmod 644 "%{?buildroot}%{tde_datadir}/config/kcmartsrc"
%endif


%clean
%__rm -rf %{?buildroot}


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 1:1.5.10-1
- Build for Fedora 19

* Sun Jul 28 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-2
- Rebuild with NDEBUG option

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-1
- Initial release for TDE 3.5.13.2

