# Default version for this component
%define tde_pkg tdesvn
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
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		subversion client with tight TDE integration [Trinity]
Version:		1.0.4
Release:		%{?!preversion:6}%{?preversion:5_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.elliptique.net/~ken/kima/

Prefix:			%{_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	subversion-devel
Requires:		%{name}-tdeio-plugins = %{version}-%{release}

Obsoletes:	trinity-kdesvn < %{version}-%{release}
Provides:	trinity-kdesvn = %{version}-%{release}

%description
TDESvn is a graphical client for the subversion revision control
system (svn).

Besides offering common and advanced svn operations, it features
a tight integration into TDE and can be embedded into other TDE 
applications like konqueror via the TDE component technology KParts.


%package -n trinity-libsvnqt
Group:			Development/Libraries
Summary:		Qt wrapper library for subversion [Trinity]

%description -n trinity-libsvnqt
This package provides svnqt, a Qt wrapper library around the 
subversion library.

It is based on the RapidSvn SvnCpp library, a subversion client API 
written in C++.

%package -n trinity-libsvnqt-devel
Group:			Development/Libraries
Requires:		trinity-libsvnqt = %{version}-%{release}
Requires:		qt-devel
Requires:		subversion-devel
Summary:		Qt wrapper library for subversion (development files) [Trinity]

%description -n trinity-libsvnqt-devel
This package contains the header files and symbolic links that developers
using svnqt will need.


%package tdeio-plugins
Group:			Development/Libraries
Conflicts:	trinity-kdesdk-tdeio-plugins
Summary:		subversion I/O slaves for Trinity

Obsoletes:	trinity-kdesvn-kio-plugins < %{version}-%{release}
Provides:	trinity-kdesvn-kio-plugins = %{version}-%{release}
Obsoletes:	trinity-tdesvn-kio-plugins < %{version}-%{release}
Provides:	trinity-tdesvn-kio-plugins = %{version}-%{release}

%description tdeio-plugins
This packages includes KIO slaves for svn, svn+file, svn+http, 
svn+https, svn+ssh. This allows you to access subversion repositories 
inside any KIO enabled TDE application.

This package is part of tdesvn-trinity.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

# More ugly hack to add TQT include directory in CMakeLists.txt	
%__sed -i CMakeLists.txt \
  -e "s,^\(INCLUDE_DIRECTORIES (\)$,\1\n,"

# Moves HTML files to the correect location
find . -name "*.cmake" -exec %__sed -i {} \
  -e "s,/doc/HTML,/doc/tde/HTML,g" \
  \;


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${QTDIR}/bin:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

export CMAKE_INCLUDE_PATH="%{tde_tdeincludedir}"

%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%__mkdir_p build
cd build
%endif

%cmake \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_includedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DMAN_INSTALL_DIR=%{tde_mandir}/man1 \
  -DDATA_INSTALL_DIR=%{tde_datadir} \
  -DPKGCONFIG_INSTALL_DIR=%{tde_tdelibdir}/pkgconfig \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  -DCMAKE_SKIP_RPATH="OFF" \
  ..

# SMP safe !
%__make %{?_smp_mflags} || %__make


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build


# Installs SVN protocols as alternatives
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+file.protocol %{?buildroot}%{tde_datadir}/services/svn+file.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+http.protocol %{?buildroot}%{tde_datadir}/services/svn+http.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+https.protocol %{?buildroot}%{tde_datadir}/services/svn+https.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+ssh.protocol %{?buildroot}%{tde_datadir}/services/svn+ssh.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn.protocol %{?buildroot}%{tde_datadir}/services/svn.protocol_tdesvn
%__ln_s /etc/alternatives/svn+file.protocol %{?buildroot}%{tde_datadir}/services/svn+file.protocol
%__ln_s /etc/alternatives/svn+http.protocol %{?buildroot}%{tde_datadir}/services/svn+http.protocol
%__ln_s /etc/alternatives/svn+https.protocol %{?buildroot}%{tde_datadir}/services/svn+https.protocol
%__ln_s /etc/alternatives/svn+ssh.protocol %{?buildroot}%{tde_datadir}/services/svn+ssh.protocol
%__ln_s /etc/alternatives/svn.protocol %{?buildroot}%{tde_datadir}/services/svn.protocol


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%post -n trinity-libsvnqt
/sbin/ldconfig || :

%post tdeio-plugins
for proto in svn+file svn+http svn+https svn+ssh svn; do
  update-alternatives --install \
    %{tde_datadir}/services/${proto}.protocol \
    ${proto}.protocol \
    %{tde_datadir}/services/${proto}.protocol_tdesvn \
    20
done

%preun tdeio-plugins
if [ $1 -eq 0 ]; then
  for proto in svn+file svn+http svn+https svn+ssh svn; do
    update-alternatives --remove \
      ${proto}.protocol \
      %{tde_datadir}/services/${proto}.protocol_tdesvn
  done
fi



%postun -n trinity-libsvnqt
/sbin/ldconfig || :


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{tde_bindir}/tdesvn
%{tde_bindir}/tdesvnaskpass
%{tde_tdelibdir}/tdesvnpart.la
%{tde_tdelibdir}/tdesvnpart.so
%{tde_datadir}/applications/tde/tdesvn.desktop
%{tde_datadir}/tdeconf_update/tdesvn-use-external-update.sh
%{tde_datadir}/tdeconf_update/tdesvnpartrc-use-external.upd
%{tde_datadir}/tdesvn/tdesvnui.rc
%{tde_datadir}/tdesvnpart/tdesvn_part.rc
%{tde_datadir}/konqueror/servicemenus/tdesvn_subversion.desktop
%{tde_datadir}/config.kcfg/tdesvn_part.kcfg
%{tde_datadir}/icons/hicolor/*/*/*.png
%{tde_datadir}/icons/hicolor/*/*/*.svgz
#%{tde_mandir}/man1/tdesvn.1
#%{tde_mandir}/man1/tdesvnaskpass.1
#%{tde_tdedocdir}/HTML/*/
%{tde_libdir}/libksvnwidgets.la
%{tde_libdir}/libksvnwidgets.so
%{tde_libdir}/libsvnfrontend.la
%{tde_libdir}/libsvnfrontend.so
%{tde_libdir}/libtdesvncfgreader.la
%{tde_libdir}/libtdesvncfgreader.so
%{tde_libdir}/libtdesvnevents.la
%{tde_libdir}/libtdesvnevents.so
%{tde_libdir}/libtdesvnhelpers.la
%{tde_libdir}/libtdesvnhelpers.so
%{tde_datadir}/tdesvn/icons/hicolor/*/apps/tdesvn.png
%{tde_datadir}/tdesvn/icons/hicolor/scalable/apps/tdesvn.svgz

%files -n trinity-libsvnqt
%defattr(-,root,root,-)
%{tde_libdir}/libsvnqt.so.4
%{tde_libdir}/libsvnqt.so.4.2.2

%files -n trinity-libsvnqt-devel
%defattr(-,root,root,-)
%{tde_includedir}/svnqt
%{tde_libdir}/libsvnqt.so

%files tdeio-plugins
%defattr(-,root,root,-)
%{tde_datadir}/services/kded/tdesvnd.desktop
%{tde_datadir}/services/ksvn+file.protocol
%{tde_datadir}/services/ksvn+http.protocol
%{tde_datadir}/services/ksvn+https.protocol
%{tde_datadir}/services/ksvn+ssh.protocol
%{tde_datadir}/services/ksvn.protocol
%{tde_datadir}/services/svn+file.protocol
%{tde_datadir}/services/svn+http.protocol
%{tde_datadir}/services/svn+https.protocol
%{tde_datadir}/services/svn+ssh.protocol
%{tde_datadir}/services/svn.protocol
%{tde_datadir}/services/svn+file.protocol_tdesvn
%{tde_datadir}/services/svn+http.protocol_tdesvn
%{tde_datadir}/services/svn+https.protocol_tdesvn
%{tde_datadir}/services/svn+ssh.protocol_tdesvn
%{tde_datadir}/services/svn.protocol_tdesvn
%{tde_tdelibdir}/tdeio_ksvn.la
%{tde_tdelibdir}/tdeio_ksvn.so
%{tde_tdelibdir}/kded_tdesvnd.la
%{tde_tdelibdir}/kded_tdesvnd.so


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 1.0.4-6
- Initial release for TDE 14.0.0

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 1.0.4-5
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 1.0.4-4
- Initial release for TDE 3.5.13.1

* Mon Jul 30 2012 Francois Andriot <francois.andriot@free.fr> - 1.0.4-3
- Installs SVN protocols as alternative, avoids conlict with TDESDK

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 1.0.4-2
- Rebuilt for Fedora 17
- Fix post and postun
- Fix compilation with GCC 4.7
 
* Thu Dec 01 2011 Francois Andriot <francois.andriot@free.fr> - 1.0.4-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16