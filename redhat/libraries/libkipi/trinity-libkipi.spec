# Default version for this component
%define kdecomp libkipi


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
%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdeincludedir %{tde_includedir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-%{kdecomp}
Summary:	library for apps that want to use kipi-plugins (runtime version) [Trinity]

Version:	3.5.13
Release:	1%{?dist}%{?_variant}

License:	GPLv2+
Group:		Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires: tqtinterface-devel
BuildRequires: trinity-arts-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: desktop-file-utils
BuildRequires: lcms-devel, libjpeg-devel, pkgconfig
BuildRequires: automake autoconf libtool 
BuildRequires: gettext

%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}ltdl-devel
%else
BuildRequires:	libtool-ltdl-devel
%endif

%description
Libkipi is a library
  o that contains common routines and widget used by kipi-plugins
  o to ease implementation of the kipi-plugins interface in an application
    that wants to use kipi-plugins
    
Homepage: http://www.kipi-plugins.org/


%package devel
Group:		Development/Libraries
Summary:	library for apps that want to use kipi-plugins (development version) [Trinity]
Requires:	%{name} = %{version}

%description devel
Libkipi is a library
  o that contains common routines and widget used by kipi-plugins
  o to ease implementation of the kipi-plugins interface in an application
    that wants to use kipi-plugins
    
This package contains development files and documentation for libkipi library.
Homepage: http://www.kipi-plugins.org/

%prep
%setup -q -n libraries/%{kdecomp}

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"

%build
unset QTDIR || : ; source /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
	--datadir=%{tde_datadir} \
	--libdir=%{tde_libdir} \
	--includedir=%{tde_includedir} \
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
/sbin/ldconfig || :

%postun
/sbin/ldconfig || :

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%{tde_libdir}/libkipi.so.0
%{tde_libdir}/libkipi.so.0.1.1
%{tde_datadir}/apps/kipi/
%{tde_datadir}/icons/hicolor/*/apps/kipi.png
%{tde_datadir}/servicetypes/kipiplugin.desktop

%files devel
%defattr(-,root,root,-)
%{tde_libdir}/libkipi.so
%{tde_libdir}/libkipi.la
%{tde_includedir}/libkipi/
%{tde_libdir}/pkgconfig/libkipi.pc

%Changelog
* Sun Nov 06 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for TDE 3.5.13 on RHEL 6, RHEL 5 and Fedora 15
