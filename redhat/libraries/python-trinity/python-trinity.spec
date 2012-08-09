%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

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
%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdeincludedir %{tde_includedir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

%define __arch_install_post %{nil}


Name:		python-trinity
Summary:	Trinity bindings for Python [Trinity]
Version:	3.16.3
Release:	2%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.simonzone.com/software/pykdeextensions

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	python-trinity-3.5.13.tar.gz

## RHEL/Fedora patches
Patch1:		python-trinity-3.5.13-install_directories.patch
# [python-trinity] Fix compilation with GCC 4.7
Patch2:		python-trinity-3.5.13-fix_gcc47_compilation.patch
# [python-trinity] Fix Mandrake detection function
Patch3:		python-trinity-3.5.13-fix_mandrake_detection.patch


BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	python

%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	python-sip
BuildRequires:	python-qt
%else
%if 0%{?rhel} == 5
# RHEL 5 comes with old version, so we brought ours ...
BuildRequires:	trinity-sip-devel
BuildRequires:	trinity-PyQt-devel
%else
BuildRequires:	sip-devel
BuildRequires:	PyQt-devel
%endif
%endif

%description
Python binding module that provides wide access to the Trinity API,
also known as PyKDE. Using this, you'll get (for example) classes
from kio, kjs, khtml and kprint.


%package devel
Summary:		Trinity bindings for Python - Development files and scripts [Trinity]
Group:			Development/Libraries

%description devel
Development .sip files with definitions of PyKDE classes. They
are needed to build PyKDE, but also as building blocks of other
packages based on them. 
The package also contains kdepyuic, a wrapper script around PyQt's 
user interface compiler.


%package doc
Summary:		Documentation and examples for PyKDE [Trinity]
Group:			Development/Libraries

%description doc
General documentation and examples for PyKDE providing programming
tips and working code you can use to learn from.


%prep
%setup -q -n libraries/python-trinity
%patch1 -p1
%patch2 -p1
%patch3 -p1


# Hack to get TQT include files under /opt
%__sed -i "configure.py" \
	-e "s|/usr/include/tqt|%{tde_includedir}/tqt|g"


%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

export LDFLAGS="${LDFLAGS} -lpython2.7"

export PYTHONPATH=%{python_sitearch}/trinity-sip:%{python_sitearch}/trinity-PyQt

%__python configure.py \
	-k %{tde_prefix} \
	-L %{_lib} \
	-v %{_datadir}/sip/trinity

%if 0%{?mgaversion} || 0%{?mdkversion}
# Shitty hack to add LDFLAGS
%__sed -i */Makefile \
	-e "/^LIBS = / s|$| -lpython2.7 -lDCOP -lkdecore -lkdefx -lkdeui -lkresources -lkabc -lkparts -lkio|"
%endif

%__make %{_smp_mflags}

%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Install documentation
%__mkdir_p %{buildroot}%{tde_tdedocdir}/HTML/en/
%__cp -rf doc %{buildroot}%{tde_tdedocdir}/HTML/en/python-trinity/



%clean
%__rm -rf %{buildroot}



%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{python_sitearch}/*.so
%{python_sitearch}/dcop*.py*
%{python_sitearch}/pykde*.py*

%files devel
%defattr(-,root,root,-)
%{tde_bindir}/kdepyuic
# The SIP files are outside TDE's prefix
%{_datadir}/sip/trinity/

%files doc
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/en/python-trinity/


%Changelog
* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 3.16.3-2
- Rebuild for Fedora 17
- Fix compilation with GCC 4.7
- Fix compilation for RHEL 5
 
* Fri Dec 02 2011 Francois Andriot <francois.andriot@free.fr> - 3.16.3-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
