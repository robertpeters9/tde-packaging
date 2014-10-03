# Default version for this component
%define tde_pkg kopete-otr
%define tde_version 14.0.0

# Required for Mageia 2: removes the ldflag '--no-undefined'
%define _disable_ld_no_undefined 1

# Under Mageia 3, we require "libotr3" package

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
Summary:		Off-The-Record encryption for Kopete [Trinity]
Version:		0.7
Release:		%{?!preversion:6}%{?preversion:5_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tdenetwork-devel >= %{tde_version}

# Kopete is provided by tdenetwork
Requires:		trinity-kopete >= %{tde_version}

# OTR support
BuildRequires:	libotr-devel

%description
This plugin enables Off-The-Record encryption for the TDE instant
messenger Kopete. Using this plugin you can encrypt chatsessions to other
users with IM-Cients supporting the OTR encryption method.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility

%__make %{_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Unwanted files
%__rm -f %{?buildroot}%{tde_libdir}/libkotr.so

%find_lang kopete_otr


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/crystalsvg || :
/sbin/ldconfig || :

%postun
touch --no-create %{tde_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/crystalsvg || :
/sbin/ldconfig || :


%files -f kopete_otr.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%{tde_libdir}/libkotr.la
%{tde_libdir}/libkotr.so.0
%{tde_libdir}/libkotr.so.0.0.0
%{tde_tdelibdir}/kcm_kopete_otr.la
%{tde_tdelibdir}/kcm_kopete_otr.so
%{tde_tdelibdir}/kopete_otr.la
%{tde_tdelibdir}/kopete_otr.so
%{tde_datadir}/apps/kopete_otr
%{tde_datadir}/config.kcfg/kopete_otr.kcfg
%{tde_tdedocdir}/HTML/en/kopete_otr/
%{tde_datadir}/icons/crystalsvg/16x16/apps/kopete_otr.png
%{tde_datadir}/services/tdeconfiguredialog/kopete_otr_config.desktop
%{tde_datadir}/services/kopete_otr.desktop


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.7-6
- Initial release for TDE 14.0.0
