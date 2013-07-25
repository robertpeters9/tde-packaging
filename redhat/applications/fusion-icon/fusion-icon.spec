# Default version for this component
%define kdecomp fusion-icon

%if "%{?python2_sitelib}" == ""
%define python2_sitelib    %(python2 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%endif


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
Summary:	tray icon to launch and manage Compiz Fusion [Trinity]
Version:	0.0.0+git20071028
Release:	2%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

# [fusion-icon] Allow python installation under /usr instead of tde_prefix
Patch1:		fusion-icon-3.5.13-fix_python_sitelib.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-tdelibs-devel
BuildRequires:	trinity-tdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	python
Requires:		python
Requires:		trinity-compizconfig-backend-kconfig

%description
The OpenCompositing Project brings 3D desktop visual effects that
improve the usability and eye candy of the X Window System and provide
increased productivity.

This package contains a tray icon that can launch Compiz and its
decorators.


%prep
%setup -q -n applications/%{kdecomp}
%patch1 -p1


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install \
  DESTDIR=%{buildroot} \
  PREFIX=%{tde_prefix} \
  PYTHON_SITELIB=%{?python2_sitelib}

# Removes 'egg-info'
find "%{?buildroot}%{python2_sitelib}" -name "*.egg-info" -delete


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%{tde_bindir}/fusion-icon
%{python2_sitelib}/FusionIcon/
%{tde_datadir}/applications/fusion-icon.desktop
%{tde_datadir}/icons/hicolor/*/apps/fusion-icon.png
%{tde_datadir}/icons/hicolor/scalable/apps/fusion-icon.svg


%Changelog
* Sat Aug 04 2012 Francois Andriot <francois.andriot@free.fr> - 0.0.0+git20071028-2
- Fix python module installation

* Sat Nov 19 2011 Francois Andriot <francois.andriot@free.fr> - 0.0.0+git20071028-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16