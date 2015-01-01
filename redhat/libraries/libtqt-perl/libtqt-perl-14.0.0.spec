#
# spec file for package libtqt-perl (version R14.0.0)
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
%define tde_epoch 2
%define tde_version 14.0.0
%define tde_pkg libtqt-perl
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeincludedir %{tde_includedir}/tde


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	3.008
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:	Perl bindings for the TQt library
Group:		Environment/Libraries
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}

BuildRequires:	automake autoconf libtool
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig

BuildRequires:	trinity-libsmoketqt-devel >= %{tde_version}

BuildRequires:	perl-ExtUtils-MakeMaker-

Provides:		perl(TQtShell)
Provides:		perl(TQtShellControl)


%description
This module lets you use the TQt library from Perl.
It provides an object-oriented interface and is easy to use.

%files
%defattr(-,root,root,-)
%{tde_bindir}/puic
%{tde_mandir}/man1/puic.1*
%{_bindir}/pqtapi
%{_bindir}/pqtsh
%{perl_vendorarch}/TQt.pm
%{perl_vendorarch}/TQt.pod
%{perl_vendorarch}/TQt/GlobalSpace.pm
%{perl_vendorarch}/TQt/attributes.pm
%{perl_vendorarch}/TQt/constants.pm
%{perl_vendorarch}/TQt/debug.pm
%{perl_vendorarch}/TQt/enumerations.pm
%{perl_vendorarch}/TQt/isa.pm
%{perl_vendorarch}/TQt/properties.pm
%{perl_vendorarch}/TQt/signals.pm
%{perl_vendorarch}/TQt/slots.pm
%{perl_vendorarch}/auto/TQt/
%{_mandir}/man3/TQt.3pm.*

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export TDEDIR=%{tde_prefix}
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
  --disable-gcc-hidden-visibility \
  \
  --disable-smoke

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Unwanted files
%__rm -f %{buildroot}%{perl_archlib}/perllocal.pod


%clean
%__rm -rf %{buildroot}


%Changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 3.008-1
- Initial release for TDE 14.0.0
