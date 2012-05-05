# Default version for this component
%define kdecomp kmymoney
%define version 1.0.5
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%define _mandir %{_datadir}/man
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	personal finance manager for TDE

Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz
Source1:	kmymoneytitlelabel.png
Patch0:		kmymoney-3.5.13-recode_ftbfs.patch

# TDE Commit: 2a54aa58cfe166f48d6f1395cbc6c9bfd5e31bfc
Patch1:		kmymoney-3.5.13-lots_of_crash.patch

# TDE Commit: 8654cea10f6902719006d5975db7dc07b2fcc713
Patch2:		kmymoney-3.5.13-update_to_1.0.5.patch

# [kmymoney] Fix compilation with GCC 4.7 [Bug #958]
Patch3:		kmymoney-3.5.13-fix_gcc47_compilation.patch

BuildRequires: tqtinterface-devel
BuildRequires: trinity-arts-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils

BuildRequires: recode
BuildRequires: html2ps
BuildRequires: opensp-devel
BuildRequires: libofx-devel

Requires:		%{name}-common == %{version}

%description
KMyMoney is the Personal Finance Manager for TDE. It operates similar to
MS-Money and Quicken, supports different account types, categorisation of
expenses, QIF import/export, multiple currencies and initial online banking
support.


%package common
Summary:	KMyMoney architecture independent files
Group:		Applications/Utilities
Requires:	%{name} == %{version}

%description common
This package contains architecture independent files needed for KMyMoney to
run properly. It also provides KMyMoney documentation. Therefore, unless you
have '%{name}' package installed, you will hardly find this package useful.


%package devel
Summary:	KMyMoney development files
Group:		Development/Libraries
Requires:	%{name} == %{version}

%description devel
This package contains development files needed for KMyMoney plugins.


%prep
%setup -q -n applications/%{kdecomp}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%__install -m644 %{SOURCE1} kmymoney2/widgets/

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt \
    --enable-closure \
    --enable-pdf-docs \
    --enable-ofxplugin \
    --enable-ofxbanking \
    --enable-qtdesigner \
    --enable-sqlite3

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}



## File lists
# HTML (1.0)
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d %{buildroot}$HTML_DIR ]; then
	for lang_dir in %{buildroot}$HTML_DIR/* ; do
	  if [ -d $lang_dir ]; then
		lang=$(basename $lang_dir)
		echo "%lang($lang) $HTML_DIR/$lang/*" >> %{name}.lang
		# replace absolute symlinks with relative ones
		pushd $lang_dir
		  for i in *; do
			[ -d $i -a -L $i/common ] && rm -f $i/common && ln -sf ../common $i/common
		  done
		popd
	  fi
	done
fi

%find_lang kmymoney2

%clean
%__rm -rf %{buildroot}


%post
/sbin/ldconfig
for f in hicolor locolor Tango oxygen; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done

%postun
/sbin/ldconfig
for f in hicolor locolor Tango oxygen; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done

%files
%defattr(-,root,root,-)
%{_bindir}/kmymoney
%{_bindir}/kmymoney2
%{_datadir}/applications/kde/kmymoney2.desktop
%{_datadir}/mimelnk/application/x-kmymoney2.desktop
%{_datadir}/servicetypes/kmymoneyimporterplugin.desktop
%{_datadir}/servicetypes/kmymoneyplugin.desktop
%{_libdir}/*.so.*
%{tde_libdir}/kmm_ofximport.la
%{tde_libdir}/kmm_ofximport.so

%files common -f kmymoney2.lang
%defattr(-,root,root,-)
%{_datadir}/apps/kmymoney2/html/
%{_datadir}/apps/kmymoney2/icons/*/*/*/*.png
%{_datadir}/apps/kmymoney2/kmymoney2ui.rc
%{_datadir}/apps/kmymoney2/misc/financequote.pl
%{_datadir}/apps/kmymoney2/pics/*.png
%{_datadir}/apps/kmymoney2/templates/*/*.kmt
%{_datadir}/apps/kmymoney2/tips
%{_datadir}/config.kcfg/kmymoney2.kcfg
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/Tango/*/*/*.png
%{_datadir}/icons/Tango/scalable/*.svgz
%{_datadir}/icons/locolor/*/*/*.png
%{_datadir}/icons/oxygen/*/*/*.png
%{_datadir}/icons/oxygen/scalable/*.svgz
%{tde_docdir}/HTML/en/kmymoney2/*.docbook
%{tde_docdir}/HTML/en/kmymoney2/*.png
%{tde_docdir}/HTML/en/kmymoney2/common
%{tde_docdir}/HTML/en/kmymoney2/index.cache.bz2
%{_mandir}/man1/kmymoney2.*
%{_datadir}/apps/kmm_ofximport/kmm_ofximport.rc
%{_datadir}/services/kmm_ofximport.desktop


%files devel
%defattr(-,root,root,-)
%{_includedir}/kmymoney/*.h
%{_libdir}/libkmm_kdchart.la
%{_libdir}/libkmm_mymoney.la
%{_libdir}/libkmm_plugin.la
%{_libdir}/*.so
%{_usr}/%{_lib}/qt-3.3/plugins/sqldrivers/libsqlite3*.so
%{_usr}/%{_lib}/qt-3.3/plugins/designer/libkmymoney.so

%Changelog
* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 1.0.5-2
- Rebuild for Fedora 17
- Fix compilation with GCC 4.7 [Bug #958]

* Sun Jan 15 2012 Francois Andriot <francois.andriot@free.fr> - 1.0.5-1
- Updates to upstream 1.0.5

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 1.0.4-1
- Initial release for TDE 3.5.13 on RHEL 6, RHEL 5 and Fedora 15
