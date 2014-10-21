#
# spec file for package trinity-filesystem (version R14.0.0)
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

# TDE variables
%define tde_version 14.0.0
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define _docdir %{tde_docdir}
%define tde_docdir %{tde_datadir}/doc
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_includedir %{tde_prefix}/include
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_tdelibdir %{tde_libdir}/trinity



Name:		trinity-filesystem
Version:	%{tde_version}
Release:	1%{?dist}
Summary:	Trinity Directory Layout
Group:		System/Fhs
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		/usr
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch


%description
This package installs the Trinity directory structure.


%files
%defattr(-,root,root,-)
%dir %{tde_prefix}

%dir %{tde_bindir}

%dir %{tde_datadir}
%dir %{tde_datadir}/config

%dir %{tde_docdir}
%dir %{tde_tdedocdir}
%dir %{tde_tdedocdir}/HTML
%dir %{tde_tdedocdir}/HTML/en
%dir %{tde_tdedocdir}/HTML/en/common

%dir %{tde_includedir}
%dir %{tde_tdeincludedir}

%dir %{tde_libdir}
%dir %{tde_libdir}/pkgconfig
%dir %{tde_tdelibdir}

%dir %{tde_datadir}/applications
%dir %{tde_datadir}/applications/tde
%dir %{tde_datadir}/applnk
%dir %{tde_datadir}/applnk/.hidden
%dir %{tde_datadir}/applnk/*
%dir %{tde_datadir}/applnk/*/*
%dir %{tde_datadir}/apps
%dir %{tde_datadir}/apps/*
%dir %{tde_datadir}/cmake
%dir %{tde_datadir}/config.kcfg
%dir %{tde_datadir}/autostart
%dir %{tde_datadir}/emoticons
%dir %{tde_datadir}/icons
%dir %{tde_datadir}/icons/crystalsvg
%dir %{tde_datadir}/icons/crystalsvg/*
%dir %{tde_datadir}/icons/crystalsvg/*/*
%dir %{tde_datadir}/icons/hicolor
%dir %{tde_datadir}/icons/hicolor/*
%dir %{tde_datadir}/icons/hicolor/*/*
%dir %{tde_datadir}/icons/locolor
%dir %{tde_datadir}/icons/locolor/*
%dir %{tde_datadir}/icons/locolor/*/*
%dir %{tde_datadir}/locale
%dir %{tde_datadir}/locale/en_US
%dir %{tde_datadir}/locale/l10n
%dir %{tde_datadir}/locale/l10n/*
%dir %{tde_datadir}/mimelnk
%dir %{tde_datadir}/mimelnk/*
%dir %{tde_datadir}/services
%dir %{tde_datadir}/servicetypes
%dir %{tde_datadir}/wallpapers


%dir %{_sysconfdir}/trinity
%dir %{_sysconfdir}/xdg/menus

##########

%prep

%build

%install
%__install -d -m 755 %{?buildroot}%{tde_prefix}

%__install -d -m 755 %{?buildroot}%{tde_bindir}

%__install -d -m 755 %{?buildroot}%{tde_datadir}
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applications
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applications/tde
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/.hidden
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Applications
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Development
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Edutainment
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Games
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Graphics
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Internet
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Multimedia
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Office
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Settings
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Settings/WebBrowsing
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/System
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Toys
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Utilities
%__install -d -m 755 %{?buildroot}%{tde_datadir}/apps
%__install -d -m 755 %{?buildroot}%{tde_datadir}/apps/plugin
%__install -d -m 755 %{?buildroot}%{tde_datadir}/apps/profiles
%__install -d -m 755 %{?buildroot}%{tde_datadir}/apps/videothumbnail
%__install -d -m 755 %{?buildroot}%{tde_datadir}/autostart
%__install -d -m 755 %{?buildroot}%{tde_datadir}/cmake
%__install -d -m 755 %{?buildroot}%{tde_datadir}/config
%__install -d -m 755 %{?buildroot}%{tde_datadir}/config.kcfg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/emoticons
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/all
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/application
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/audio
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/fonts
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/image
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/interface
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/inode
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/media
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/message
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/model
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/multipart
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/print
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/text
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/uri
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/video
%__install -d -m 755 %{?buildroot}%{tde_datadir}/services
%__install -d -m 755 %{?buildroot}%{tde_datadir}/servicetypes

%__install -d -m 755 %{?buildroot}%{tde_datadir}/wallpapers

# Create icons directories
%__install -d -m 755 %{?buildroot}%{tde_datadir}/icons
for t in crystalsvg hicolor locolor ; do
  %__install -d -m 755 "%{?buildroot}%{tde_datadir}/icons/${t}"
  %__install -d -m 755 "%{?buildroot}%{tde_datadir}/icons/${t}/scalable"
  for i in {16,22,32,48,64,128} ; do
    %__install -d -m 755 "%{?buildroot}%{tde_datadir}/icons/${t}/${i}x${i}"
  done
  
  # Create subdirectories
  for r in actions apps categories devices mimetypes places ; do
    %__install -d -m 755 "%{?buildroot}%{tde_datadir}/icons/${t}/scalable/${r}"
    for i in {16,22,32,48,64,128} ; do
      %__install -d -m 755 "%{?buildroot}%{tde_datadir}/icons/${t}/${i}x${i}/${r}"
    done
  done
done

%__install -d -m 755 %{?buildroot}%{tde_docdir}
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/en
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/en/common

%__install -d -m 755 %{?buildroot}%{tde_includedir}
%__install -d -m 755 %{?buildroot}%{tde_tdeincludedir}

%__install -d -m 755 %{?buildroot}%{tde_libdir}
%__install -d -m 755 %{?buildroot}%{tde_libdir}/pkgconfig
%__install -d -m 755 %{?buildroot}%{tde_tdelibdir}

%__install -d -m 755 %{?buildroot}%{_sysconfdir}/trinity
%__install -d -m 755 %{?buildroot}%{_sysconfdir}/xdg/menus

%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/en_US
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/C
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ad
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ae
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/af
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ag
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ai
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/al
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/am
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/an
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ao
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ar
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/as
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/at
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/au
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/aw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ax
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/az
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ba
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bb
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bd
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/be
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bf
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bh
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bi
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bj
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bo
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/br
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bs
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bt
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/by
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ca
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cc
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cd
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cf
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ch
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ci
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ck
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cl
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/co
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cu
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cv
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cx
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cy
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/de
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/dj
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/dk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/dm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/do
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/dz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ec
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ee
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/eg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/eh
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/er
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/es
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/et
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/fi
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/fj
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/fk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/fm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/fo
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/fr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ga
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gb
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gd
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ge
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gh
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gi
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gl
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gp
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gq
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gt
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gu
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gy
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/hk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/hn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/hr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ht
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/hu
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/id
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ie
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/il
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/in
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/iq
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ir
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/is
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/it
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/jm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/jo
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/jp
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ke
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/kg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/kh
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ki
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/km
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/kn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/kp
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/kr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/kw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ky
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/kz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/la
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/lb
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/lc
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/li
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/lk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/lr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ls
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/lt
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/lu
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/lv
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ly
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ma
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mc
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/md
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/me
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mh
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ml
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mo
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mq
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ms
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mt
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mu
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mv
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mx
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/my
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/na
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/nc
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ne
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/nf
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ng
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ni
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/nl
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/no
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/np
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/nr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/nu
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/nz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/om
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pa
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pe
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pf
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ph
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pl
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ps
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pt
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/py
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/qa
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ro
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/rs
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ru
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/rw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sa
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sb
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sc
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sd
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/se
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sh
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/si
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/so
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/st
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sv
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sy
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tc
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/td
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/th
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tj
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/to
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tp
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tt
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tv
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ua
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ug
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/us
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/uy
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/uz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/va
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/vc
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ve
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/vg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/vi
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/vn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/vu
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/wf
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ws
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ye
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/za
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/zm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/zw

%post
%if 0%{?suse_version}
# Add setuid files in '/etc/permissions.local'
for b in kcheckpass kgrantpty kpac_dhcp_helper start_tdeinit tdmtsak tdekbdledsync ; do
  if ! grep -q "^%{tde_bindir}/${b}" "/etc/permissions.local"; then
    echo "%{tde_bindir}/${b}          root:root       4711" >>/etc/permissions.local
  fi
done
%endif


%changelog
* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 14.0.0-1
- Initial build for TDE R14