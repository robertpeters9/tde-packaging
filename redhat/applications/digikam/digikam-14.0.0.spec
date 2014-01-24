# Default version for this component
%define tde_pkg digikam
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

%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		digital photo management application for TDE [Trinity]
Version:		0.9.6
Release:		%{?!preversion:8}%{?preversion:7_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

# [Digikam] Revert PNG support to libpng12 (for RHEL4)
Patch1:		digikam-3.5.13.2-fix_png12_support.patch

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-libkexiv2-devel
BuildRequires:	trinity-libkdcraw-devel
BuildRequires:	trinity-libkipi-devel

BuildRequires:	libtiff-devel
BuildRequires:	gettext

# GPHOTO2 support
%if 0%{?rhel} == 4 || 0%{?rhel} == 5 || 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	gphoto2-devel
%else
BuildRequires:	libgphoto2-devel
%endif

# JASPER support
%if 0%{?suse_version}
BuildRequires:	libjasper-devel
%else
BuildRequires:	jasper-devel
%endif

# EXIV2 support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}exiv2-devel
%endif
%if 0%{?suse_version}
BuildRequires:	libexiv2-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	exiv2-devel
%endif

Requires:		trinity-libkexiv2
Requires:		trinity-libkdcraw
Requires:		trinity-libkipi

%description
An easy to use and powerful digital photo management
application, which makes importing, organizing and manipulating
digital photos a "snap".  An interface is provided to connect to
your digital camera, preview the images and download and/or
delete them.

The digiKam built-in image editor makes the common photo correction
a simple task. The image editor is extensible via plugins and,
the digikamimageplugins project has been merged to digiKam core
since release 0.9.2, all useful image editor plugins are available
in the base installation.

digiKam can also make use of the KIPI image handling plugins to
extend its capabilities even further for photo manipulations,
import and export, etc. The kipi-plugins package contains many
very useful extentions.

digiKam is based in part on the work of the Independent JPEG Group.

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_bindir}/digikam
%{tde_bindir}/digikamthemedesigner
%{tde_bindir}/digitaglinktree
%{tde_bindir}/showfoto
%{tde_libdir}/libdigikam.so.0
%{tde_libdir}/libdigikam.so.0.0.0
%{tde_tdelibdir}/tdeio_digikamalbums.la
%{tde_tdelibdir}/tdeio_digikamalbums.so
%{tde_tdelibdir}/tdeio_digikamdates.la
%{tde_tdelibdir}/tdeio_digikamdates.so
%{tde_tdelibdir}/digikamimageplugin_adjustcurves.la
%{tde_tdelibdir}/digikamimageplugin_adjustcurves.so
%{tde_tdelibdir}/digikamimageplugin_adjustlevels.la
%{tde_tdelibdir}/digikamimageplugin_adjustlevels.so
%{tde_tdelibdir}/digikamimageplugin_antivignetting.la
%{tde_tdelibdir}/digikamimageplugin_antivignetting.so
%{tde_tdelibdir}/digikamimageplugin_blurfx.la
%{tde_tdelibdir}/digikamimageplugin_blurfx.so
%{tde_tdelibdir}/digikamimageplugin_border.la
%{tde_tdelibdir}/digikamimageplugin_border.so
%{tde_tdelibdir}/digikamimageplugin_channelmixer.la
%{tde_tdelibdir}/digikamimageplugin_channelmixer.so
%{tde_tdelibdir}/digikamimageplugin_charcoal.la
%{tde_tdelibdir}/digikamimageplugin_charcoal.so
%{tde_tdelibdir}/digikamimageplugin_colorfx.la
%{tde_tdelibdir}/digikamimageplugin_colorfx.so
%{tde_tdelibdir}/digikamimageplugin_core.la
%{tde_tdelibdir}/digikamimageplugin_core.so
%{tde_tdelibdir}/digikamimageplugin_distortionfx.la
%{tde_tdelibdir}/digikamimageplugin_distortionfx.so
%{tde_tdelibdir}/digikamimageplugin_emboss.la
%{tde_tdelibdir}/digikamimageplugin_emboss.so
%{tde_tdelibdir}/digikamimageplugin_filmgrain.la
%{tde_tdelibdir}/digikamimageplugin_filmgrain.so
%{tde_tdelibdir}/digikamimageplugin_freerotation.la
%{tde_tdelibdir}/digikamimageplugin_freerotation.so
%{tde_tdelibdir}/digikamimageplugin_hotpixels.la
%{tde_tdelibdir}/digikamimageplugin_hotpixels.so
%{tde_tdelibdir}/digikamimageplugin_infrared.la
%{tde_tdelibdir}/digikamimageplugin_infrared.so
%{tde_tdelibdir}/digikamimageplugin_inpainting.la
%{tde_tdelibdir}/digikamimageplugin_inpainting.so
%{tde_tdelibdir}/digikamimageplugin_inserttext.la
%{tde_tdelibdir}/digikamimageplugin_inserttext.so
%{tde_tdelibdir}/digikamimageplugin_lensdistortion.la
%{tde_tdelibdir}/digikamimageplugin_lensdistortion.so
%{tde_tdelibdir}/digikamimageplugin_noisereduction.la
%{tde_tdelibdir}/digikamimageplugin_noisereduction.so
%{tde_tdelibdir}/digikamimageplugin_oilpaint.la
%{tde_tdelibdir}/digikamimageplugin_oilpaint.so
%{tde_tdelibdir}/digikamimageplugin_perspective.la
%{tde_tdelibdir}/digikamimageplugin_perspective.so
%{tde_tdelibdir}/digikamimageplugin_raindrop.la
%{tde_tdelibdir}/digikamimageplugin_raindrop.so
%{tde_tdelibdir}/digikamimageplugin_restoration.la
%{tde_tdelibdir}/digikamimageplugin_restoration.so
%{tde_tdelibdir}/digikamimageplugin_sheartool.la
%{tde_tdelibdir}/digikamimageplugin_sheartool.so
%{tde_tdelibdir}/digikamimageplugin_superimpose.la
%{tde_tdelibdir}/digikamimageplugin_superimpose.so
%{tde_tdelibdir}/digikamimageplugin_texture.la
%{tde_tdelibdir}/digikamimageplugin_texture.so
%{tde_tdelibdir}/digikamimageplugin_whitebalance.la
%{tde_tdelibdir}/digikamimageplugin_whitebalance.so
%{tde_tdelibdir}/tdeio_digikamsearch.la
%{tde_tdelibdir}/tdeio_digikamsearch.so
%{tde_tdelibdir}/tdeio_digikamtags.la
%{tde_tdelibdir}/tdeio_digikamtags.so
%{tde_tdelibdir}/tdeio_digikamthumbnail.la
%{tde_tdelibdir}/tdeio_digikamthumbnail.so
%{tde_tdeappdir}/digikam.desktop
%{tde_tdeappdir}/showfoto.desktop
%{tde_datadir}/apps/digikam/
%{tde_datadir}/apps/konqueror/servicemenus/digikam-download.desktop
%{tde_datadir}/apps/konqueror/servicemenus/digikam-gphoto2-camera.desktop
%{tde_datadir}/apps/konqueror/servicemenus/digikam-mount-and-download.desktop
%{tde_datadir}/apps/showfoto/
%{tde_datadir}/icons/hicolor/*/apps/digikam.png
%{tde_datadir}/icons/hicolor/*/apps/showfoto.png
%{tde_datadir}/services/digikamalbums.protocol
%{tde_datadir}/services/digikamdates.protocol
%{tde_datadir}/services/digikamimageplugin_adjustcurves.desktop
%{tde_datadir}/services/digikamimageplugin_adjustlevels.desktop
%{tde_datadir}/services/digikamimageplugin_antivignetting.desktop
%{tde_datadir}/services/digikamimageplugin_blurfx.desktop
%{tde_datadir}/services/digikamimageplugin_border.desktop
%{tde_datadir}/services/digikamimageplugin_channelmixer.desktop
%{tde_datadir}/services/digikamimageplugin_charcoal.desktop
%{tde_datadir}/services/digikamimageplugin_colorfx.desktop
%{tde_datadir}/services/digikamimageplugin_core.desktop
%{tde_datadir}/services/digikamimageplugin_distortionfx.desktop
%{tde_datadir}/services/digikamimageplugin_emboss.desktop
%{tde_datadir}/services/digikamimageplugin_filmgrain.desktop
%{tde_datadir}/services/digikamimageplugin_freerotation.desktop
%{tde_datadir}/services/digikamimageplugin_hotpixels.desktop
%{tde_datadir}/services/digikamimageplugin_infrared.desktop
%{tde_datadir}/services/digikamimageplugin_inpainting.desktop
%{tde_datadir}/services/digikamimageplugin_inserttext.desktop
%{tde_datadir}/services/digikamimageplugin_lensdistortion.desktop
%{tde_datadir}/services/digikamimageplugin_noisereduction.desktop
%{tde_datadir}/services/digikamimageplugin_oilpaint.desktop
%{tde_datadir}/services/digikamimageplugin_perspective.desktop
%{tde_datadir}/services/digikamimageplugin_raindrop.desktop
%{tde_datadir}/services/digikamimageplugin_restoration.desktop
%{tde_datadir}/services/digikamimageplugin_sheartool.desktop
%{tde_datadir}/services/digikamimageplugin_superimpose.desktop
%{tde_datadir}/services/digikamimageplugin_texture.desktop
%{tde_datadir}/services/digikamimageplugin_whitebalance.desktop
%{tde_datadir}/services/digikamsearch.protocol
%{tde_datadir}/services/digikamtags.protocol
%{tde_datadir}/services/digikamthumbnail.protocol
%{tde_datadir}/servicetypes/digikamimageplugin.desktop
%{tde_mandir}/man*/*
#%{tde_tdedocdir}/HTML/en/digikam-apidocs/
%{tde_tdedocdir}/HTML/en/digikam/
%{tde_tdedocdir}/HTML/en/showfoto/

%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
/sbin/ldconfig
update-desktop-database %{tde_appdir} 2> /dev/null || : 

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
/sbin/ldconfig
update-desktop-database %{tde_appdir} 2> /dev/null || : 

##########

%package devel
Group:			Development/Libraries
Summary:		Development files for %{name}
Requires:		%{name} = %{version}-%{release}

%description devel
%{summary}

%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/digikam_export.h
%{tde_tdeincludedir}/digikam/
%{tde_libdir}/libdigikam.so
%{tde_libdir}/libdigikam.la

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

##########

%package i18n
Summary:		Translation files for %{tde_pkg}
Group:			Applications/Utilities
Requires:		%{name} = %{version}-%{release}

%description i18n
%{summary}

%files i18n
%defattr(-,root,root,-)
%lang(da) %{tde_tdedocdir}/HTML/da/digikam/
%lang(da) %{tde_tdedocdir}/HTML/da/showfoto/
%lang(de) %{tde_tdedocdir}/HTML/de/digikam/
%lang(de) %{tde_tdedocdir}/HTML/de/showfoto/
%lang(es) %{tde_tdedocdir}/HTML/es/digikam/
%lang(es) %{tde_tdedocdir}/HTML/es/showfoto/
%lang(et) %{tde_tdedocdir}/HTML/et/digikam/
%lang(et) %{tde_tdedocdir}/HTML/et/showfoto/
%lang(it) %{tde_tdedocdir}/HTML/it/digikam/
%lang(it) %{tde_tdedocdir}/HTML/it/showfoto/
%lang(nl) %{tde_tdedocdir}/HTML/nl/digikam/
%lang(nl) %{tde_tdedocdir}/HTML/nl/showfoto/
%lang(pt_BR) %{tde_tdedocdir}/HTML/pt_BR/digikam/
#%lang(pt_BR) %{tde_tdedocdir}/HTML/pt_BR/showfoto/
%lang(ru) %{tde_tdedocdir}/HTML/ru/digikam/
#%lang(ru) %{tde_tdedocdir}/HTML/ru/showfoto/
%lang(sv) %{tde_tdedocdir}/HTML/sv/digikam/
%lang(sv) %{tde_tdedocdir}/HTML/sv/showfoto/

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}
%if 0%{?rhel} == 4
%patch1 -p1 -b .png12
%endif

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --datadir=%{tde_datadir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath \
  --enable-gcc-hidden-visibility

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%changelog
* Mon Jul 29 2013 Francois Andriot <francois.andriot@free.fr> - 0.9.6-8
- Initial release for TDE 14.0.0
