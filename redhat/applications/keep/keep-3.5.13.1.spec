# Default version for this component
%define kdecomp keep

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
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-%{kdecomp}
Summary:	backup system for KDE [Trinity]
Version:	0.4.0
Release:	3%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{tde_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.1.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= 3.5.13.1
BuildRequires:	trinity-tdelibs-devel >= 3.5.13.1
BuildRequires:	trinity-tdebase-devel >= 3.5.13.1
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

Requires: rdiff-backup

%description
Keep is an automatic backup program that allows users to set the parameters of
the backup, including the frequency and the number of backups.

Homepage: http://jr.falleri.free.fr/keep


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{kdecomp}-3.5.13.1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --disable-rpath \
  --with-extra-includes=%{tde_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{kdecomp}

%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
update-desktop-database %{tde_appdir} &> /dev/null

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
update-desktop-database %{tde_appdir} &> /dev/null


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%{tde_bindir}/keep
%{tde_tdelibdir}/kded_keep.la
%{tde_tdelibdir}/kded_keep.so
%{tde_tdeappdir}/keep.desktop
%{tde_datadir}/icons/hicolor/scalable/apps/keep.svgz
%{tde_datadir}/apps/keep/
%{tde_datadir}/config.kcfg/keepsettings.kcfg
%{tde_datadir}/icons/hicolor/*/apps/keep.png
%{tde_datadir}/services/kded/keep.desktop


%changelog
* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.4.0-3
- Initial release for TDE 3.5.13.1

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.4.0-2
- Rebuilt for Fedora 17

* Thu Nov 24 2011 Francois Andriot <francois.andriot@free.fr> - 0.4.0-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16