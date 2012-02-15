# Always install under standard prefix
%define _prefix /usr

# This allows the legacy RHEL/Fedora patches to apply in TDE version.
%define _default_patch_fuzz 2

# The following QT4 packages should NOT be installed to
# allow QT3 compilation (please uninstall them prior to compile)
#  qt
#  qt-sqlite
#  qt-mysql
#  qt-x11
#  qt-devel
# ...maybe others !!!!

%define _default_patch_fuzz 2

Summary: The shared library for the Qt 3 GUI toolkit
Version: 3.4.0
Release: 1%{?dist}
Name: tqt3

Obsoletes: qt < 1:%{version}-%{release}
Provides: qt = 1:%{version}-%{release}
Obsoletes: qt3 < 1:%{version}-%{release}
Provides: qt3 = 1:%{version}-%{release}

License: QPL or GPLv2 or GPLv3
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Url: http://www.troll.no
Source0: %{name}-%{version}.tar.gz
Source2: qt.sh
Source3: qt.csh
Source4: designer3.desktop
Source5: assistant3.desktop
Source6: linguist3.desktop
Source7: qtconfig3.desktop

Patch1: qt-3.3.4-print-CJK.patch
Patch2: tqt3-3.4.0-nodebug.patch
Patch3: qt-3.1.0-makefile.patch
Patch4: tqt3-3.4.0-umask.patch
Patch5: qt-x11-free-3.3.6-strip.patch
Patch7: tqt3-3.4.0-quiet.patch
Patch8: tqt3-3.4.0-embed.patch
Patch12: tqt3-3.4.0-uic-nostdlib.patch
Patch13: qt-x11-free-3.3.6-qfontdatabase_x11.patch
Patch27: tqt3-3.4.0-fontrendering-ml_IN-209097.patch
Patch29: qt-3.3.8-fontrendering-as_IN-209972.patch
Patch31: qt-3.3.6-fontrendering-te_IN-211259.patch
Patch32: tqt3-3.4.0-fontrendering-214371.patch
Patch33: tqt3-3.4.0-fontrendering-#214570.patch
Patch34: qt-3.3.6-fontrendering-ml_IN-209974.patch
Patch35: tqt3-3.4.0-fontrendering-ml_IN-217657.patch
Patch37: qt-3.3.6-fontrendering-gu-228452.patch
Patch38: tqt3-3.4.0-odbc.patch
Patch39: qt-x11-free-3.3.7-arm.patch
Patch40: qt-x11-free-3.3.8b-typo.patch

# immodule patches
Patch53: tqt3-3.4.0-qt-x11-immodule-unified-qt3.3.5-20060318-resetinputcontext.patch

# qt-copy patches
Patch110: 0084-compositing-properties.patch

# upstream patches
Patch200: qt-x11-free-3.3.4-fullscreen.patch

# TDE 3.5.13 patches
Patch300: qt3-3.3.8.d-updates_zh-tw_translations.patch

%define qt_dirname qt-3.3
%define qtdir %{_libdir}/%{qt_dirname}
%define qt_docdir %{_docdir}/qt-devel-%{version}

%define smp 1
%define immodule 1
%define debug 0

# MySQL plugins
%define plugin_mysql -plugin-sql-mysql
%define mysql_include_dir %{_includedir}/mysql
%define mysql_lib_dir %{_libdir}/mysql

# Postgres plugins
%define plugin_psql -plugin-sql-psql

# ODBC plugins
%define plugin_odbc -plugin-sql-odbc

# sqlite plugins
%define plugin_sqlite -plugin-sql-sqlite

%define plugins_style -qt-style-cde -qt-style-motifplus -qt-style-platinum -qt-style-sgi -qt-style-windows -qt-style-compact -qt-imgfmt-png -qt-imgfmt-jpeg -qt-imgfmt-mng
%define plugins %{plugin_mysql} %{plugin_psql} %{plugin_odbc} %{plugin_sqlite} %{plugins_style}

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: coreutils
Requires: fontconfig >= 2.0
Requires: /etc/ld.so.conf.d

BuildRequires: desktop-file-utils
BuildRequires: libmng-devel
BuildRequires: glibc-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: giflib-devel
BuildRequires: perl
BuildRequires: sed
BuildRequires: findutils
BuildRequires: cups-devel
BuildRequires: tar
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: libXrender-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: libXinerama-devel
BuildRequires: libXft-devel
BuildRequires: libXext-devel
BuildRequires: libX11-devel
BuildRequires: libSM-devel
BuildRequires: libICE-devel
BuildRequires: libXt-devel
BuildRequires: libXmu-devel
BuildRequires: libXi-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: desktop-file-utils
BuildRequires: mysql-devel
BuildRequires: postgresql-devel
BuildRequires: unixODBC-devel
BuildRequires: sqlite-devel


%package config
Summary: Graphical configuration tool for programs using Qt 3
Group: User Interface/Desktops
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: qt-config < 1:%{version}-%{release}
Provides:  qt-config = 1:%{version}-%{release}
Obsoletes: qt3-config < 1:%{version}-%{release}
Provides:  qt3-config = 1:%{version}-%{release}


%package devel
Summary: Development files for the Qt 3 GUI toolkit
Group: Development/Libraries
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: freetype-devel
Requires: fontconfig-devel
Requires: libXrender-devel
Requires: libXrandr-devel
Requires: libXcursor-devel
Requires: libXinerama-devel
Requires: libXft-devel
Requires: libXext-devel
Requires: libX11-devel
Requires: libSM-devel
Requires: libICE-devel
Requires: libXt-devel
Requires: xorg-x11-proto-devel
Requires: libpng-devel
Requires: libjpeg-devel
Requires: libmng-devel
Requires: mesa-libGL-devel
Requires: mesa-libGLU-devel

Obsoletes: qt-devel < 1:%{version}-%{release}
Provides:  qt-devel = 1:%{version}-%{release}
Obsoletes: qt3-devel < 1:%{version}-%{release}
Provides:  qt3-devel = 1:%{version}-%{release}


%package devel-docs
Summary: Documentation for the Qt 3 GUI toolkit
Group: Development/Libraries
Requires: %{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes: qt-devel-docs < 1:%{version}-%{release}
Provides:  qt-devel-docs = 1:%{version}-%{release}
Obsoletes: qt3-devel-docs < 1:%{version}-%{release}
Provides:  qt3-devel-docs = 1:%{version}-%{release}


%package ODBC
Summary: ODBC drivers for Qt 3's SQL classes
Group: System Environment/Libraries
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes: qt-ODBC < 1:%{version}-%{release}
Provides:  qt-ODBC = 1:%{version}-%{release}
Obsoletes: qt3-ODBC < 1:%{version}-%{release}
Provides:  qt3-ODBC = 1:%{version}-%{release}


%package MySQL
Summary: MySQL drivers for Qt 3's SQL classes
Group: System Environment/Libraries
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes: qt-MySQL < 1:%{version}-%{release}
Provides:  qt-MySQL = 1:%{version}-%{release}
Obsoletes: qt3-MySQL < 1:%{version}-%{release}
Provides:  qt3-MySQL = 1:%{version}-%{release}


%package PostgreSQL
Summary: PostgreSQL drivers for Qt 3's SQL classes
Group: System Environment/Libraries
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes: qt-PostgreSQL < 1:%{version}-%{release}
Provides:  qt-PostgreSQL = 1:%{version}-%{release}
Obsoletes: qt3-PostgreSQL < 1:%{version}-%{release}
Provides:  qt3-PostgreSQL = 1:%{version}-%{release}


%package sqlite
Summary: sqlite drivers for Qt 3's SQL classes
Group: System Environment/Libraries
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes: qt-sqlite < 1:%{version}-%{release}
Provides:  qt-sqlite = 1:%{version}-%{release}
Obsoletes: qt3-sqlite < 1:%{version}-%{release}
Provides:  qt3-sqlite = 1:%{version}-%{release}


%package designer
Summary: In3erface designer (IDE) for the Qt 3 toolkit
Group: Development/Tools
Requires: %{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes: qt-designer < 1:%{version}-%{release}
Provides:  qt-designer = 1:%{version}-%{release}
Obsoletes: qt3-designer < 1:%{version}-%{release}
Provides:  qt3-designer = 1:%{version}-%{release}


%description
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications
for the X Window System.

Qt is written in C++ and is fully object-oriented.

This package contains the shared library needed to run Qt 3
applications, as well as the README files for Qt 3.


%description config
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications
for the X Window System.

Qt is written in C++ and is fully object-oriented.

This package contains a graphical configuration tool for programs using Qt 3.


%description devel
The %{name}-devel package contains the files necessary to develop
applications using the Qt GUI toolkit: the header files, the Qt meta
object compiler.

Install %{name}-devel if you want to develop GUI applications using the Qt 3
toolkit.


%description devel-docs
The %{name}-devel-docs package contains the man pages, the HTML documentation and
example programs for Qt 3.


%description ODBC
ODBC driver for Qt 3's SQL classes (QSQL)


%description MySQL
MySQL driver for Qt 3's SQL classes (QSQL)


%description PostgreSQL
PostgreSQL driver for Qt 3's SQL classes (QSQL)


%description sqlite
sqlite driver for Qt 3's SQL classes (QSQL)


%description designer
The %{name}-designer package contains an User Interface designer tool
for the Qt 3 toolkit.


%prep
%setup -q -n %{name}
%patch1 -p1 -b .cjk
%patch2 -p1 -b .ndebug
%patch3 -p1 -b .makefile
%patch4 -p1 -b .umask
%patch5 -p1
%patch7 -p1 -b .quiet
%patch8 -p1 -b .qembed
%patch12 -p1 -b .nostdlib
%patch13 -p1 -b .fonts
%patch27 -p1 -b .fontrendering-ml_IN-bz#209097
%patch29 -p1 -b .fontrendering-as_IN-bz#209972
%patch31 -p1 -b .fontrendering-te_IN-bz#211259
%patch32 -p1 -b .fontrendering-bz#214371
%patch33 -p1 -b .fontrendering-#214570
%patch34 -p1 -b .fontrendering-#209974
%patch35 -p1 -b .fontrendering-ml_IN-217657
%patch37 -p1 -b .fontrendering-gu-228452
%patch38 -p1 -b .odbc
# it's not 100% clear to me if this is safe for all archs -- Rex
%ifarch armv5tel
%patch39 -p1 -b .arm
%endif
%patch40 -p1

# immodule patches
%if %{immodule}
%patch53 -p1 -b .resetinputcontext
%endif

# qt-copy patches
%patch110 -p0 -b .0084-compositing-properties

# upstream patches
%patch200 -p1 -b .fullscreen

# TDE 3.5.13 patches
%patch300 -p1

# convert to UTF-8
iconv -f iso-8859-1 -t utf-8 < doc/man/man3/qdial.3qt > doc/man/man3/qdial.3qt_
mv doc/man/man3/qdial.3qt_ doc/man/man3/qdial.3qt

%build
export QTDIR=`/bin/pwd`
export LD_LIBRARY_PATH="$QTDIR/lib:$LD_LIBRARY_PATH"
export PATH="$QTDIR/bin:$PATH"
export QTDEST=%{qtdir}

%if %{smp}
   export SMP_MFLAGS="%{?_smp_mflags}"
%endif

%if %{immodule}
   sh ./make-symlinks.sh
%endif

# set correct X11 prefix
perl -pi -e "s,QMAKE_LIBDIR_X11.*,QMAKE_LIBDIR_X11\t=," mkspecs/*/qmake.conf
perl -pi -e "s,QMAKE_INCDIR_X11.*,QMAKE_INCDIR_X11\t=," mkspecs/*/qmake.conf
perl -pi -e "s,QMAKE_INCDIR_OPENGL.*,QMAKE_INCDIR_OPENGL\t=," mkspecs/*/qmake.conf
perl -pi -e "s,QMAKE_LIBDIR_OPENGL.*,QMAKE_LIBDIR_OPENGL\t=," mkspecs/*/qmake.conf

# don't use rpath
perl -pi -e "s|-Wl,-rpath,| |" mkspecs/*/qmake.conf

perl -pi -e "s|-O2|$INCLUDES %{optflags} -fno-strict-aliasing|g" mkspecs/*/qmake.conf

# set correct lib path
if [ "%{_lib}" == "lib64" ] ; then
  perl -pi -e "s,/usr/lib /lib,/usr/%{_lib} /%{_lib},g" config.tests/{unix,x11}/*.test
  perl -pi -e "s,/lib /usr/lib,/%{_lib} /usr/%{_lib},g" config.tests/{unix,x11}/*.test
fi

# build shared, threaded (default) libraries
echo yes | ./configure \
  -prefix $QTDEST \
  -docdir %{qt_docdir} \
%if %{_lib} == lib64
  -platform linux-g++-64 \
%else
  -platform linux-g++ \
%endif
%if %{debug}
  -debug \
%else
  -release \
%endif
  -shared \
  -largefile \
  -qt-gif \
  -system-zlib \
  -system-libpng \
  -system-libmng \
  -system-libjpeg \
  -no-exceptions \
  -enable-styles \
  -enable-tools \
  -enable-kernel \
  -enable-widgets \
  -enable-dialogs \
  -enable-iconview \
  -enable-workspace \
  -enable-network \
  -enable-canvas \
  -enable-table \
  -enable-xml \
  -enable-opengl \
  -enable-sql \
  -qt-style-motif \
  %{plugins} \
  -stl \
  -thread \
  -cups \
  -sm \
  -xinerama \
  -xrender \
  -xkb \
  -ipv6 \
  -dlopen-opengl \
  -xft \
  -tablet

make $SMP_MFLAGS src-qmake

# build sqlite plugin
pushd plugins/src/sqldrivers/sqlite
qmake -o Makefile sqlite.pro
popd

# build psql plugin
pushd plugins/src/sqldrivers/psql
qmake -o Makefile "INCLUDEPATH+=%{_includedir}/pgsql %{_includedir}/pgsql/server %{_includedir}/pgsql/internal" "LIBS+=-lpq" psql.pro
popd

# build mysql plugin
pushd plugins/src/sqldrivers/mysql
qmake -o Makefile "INCLUDEPATH+=%{mysql_include_dir}" "LIBS+=-L%{mysql_lib_dir} -lmysqlclient" mysql.pro
popd

# build odbc plugin
pushd plugins/src/sqldrivers/odbc
qmake -o Makefile "LIBS+=-lodbc" odbc.pro
popd

make $SMP_MFLAGS src-moc
make $SMP_MFLAGS sub-src
make $SMP_MFLAGS sub-tools UIC="$QTDIR/bin/uic -nostdlib -L $QTDIR/plugins"

%install
rm -rf %{buildroot}

export QTDIR=`/bin/pwd`
export LD_LIBRARY_PATH="$QTDIR/lib:$LD_LIBRARY_PATH"
export PATH="$QTDIR/bin:$PATH"
export QTDEST=%{qtdir}

make install INSTALL_ROOT=%{buildroot}

for i in findtr qt20fix qtrename140 lrelease lupdate ; do
   install bin/$i %{buildroot}%{qtdir}/bin/
done

mkdir -p %{buildroot}%{_libdir}/pkgconfig/
mv %{buildroot}%{qtdir}/lib/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/

# install man pages
mkdir -p %{buildroot}%{_mandir}
cp -fR doc/man/* %{buildroot}%{_mandir}/

# clean up
make -C tutorial clean
make -C examples clean

# Make sure the examples can be built outside the source tree.
# Our binaries fulfill all requirements, so...
perl -pi -e "s,^DEPENDPATH.*,,g;s,^REQUIRES.*,,g" `find examples -name "*.pro"`

# don't include Makefiles of qt examples/tutorials
find examples -name "Makefile" | xargs rm -f
find examples -name "*.obj" | xargs rm -rf
find examples -name "*.moc" | xargs rm -rf
find tutorial -name "Makefile" | xargs rm -f

for a in */*/Makefile ; do
  sed 's|^SYSCONF_MOC.*|SYSCONF_MOC		= %{qtdir}/bin/moc|' < $a > ${a}.2
  mv -v ${a}.2 $a
done

mkdir -p %{buildroot}/etc/profile.d
install -m 644 %{SOURCE2} %{SOURCE3} %{buildroot}/etc/profile.d/

# Add desktop files
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --vendor="qt" \
  %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7}

# Patch qmake to use qt-mt unconditionally
perl -pi -e "s,-lqt ,-lqt-mt ,g;s,-lqt$,-lqt-mt,g" %{buildroot}%{qtdir}/mkspecs/*/qmake.conf

# remove broken links
rm -f %{buildroot}%{qtdir}/mkspecs/default/linux-g++*
rm -f %{buildroot}%{qtdir}/lib/*.la

mkdir -p %{buildroot}/etc/ld.so.conf.d
echo "%{qtdir}/lib" > %{buildroot}/etc/ld.so.conf.d/qt-%{_arch}.conf

# install icons
mkdir %{buildroot}%{_datadir}/pixmaps
install -m 644 tools/assistant/images/qt.png %{buildroot}%{_datadir}/pixmaps/qtconfig3.png
install -m 644 tools/assistant/images/designer.png %{buildroot}%{_datadir}/pixmaps/designer3.png
install -m 644 tools/assistant/images/assistant.png %{buildroot}%{_datadir}/pixmaps/assistant3.png
install -m 644 tools/assistant/images/linguist.png %{buildroot}%{_datadir}/pixmaps/linguist3.png

# own style directory
mkdir -p %{buildroot}%{qtdir}/plugins/styles

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc FAQ LICENSE* README* changes*
%dir %{qtdir}
%dir %{qtdir}/bin
%dir %{qtdir}/lib
%dir %{qtdir}/plugins
%dir %{qtdir}/plugins/sqldrivers
%dir %{qtdir}/plugins/styles
%{qtdir}/translations
%{qtdir}/plugins/designer/
%if %{immodule}
%{qtdir}/plugins/inputmethods
%endif
%config /etc/profile.d/*
/etc/ld.so.conf.d/*
%{qtdir}/lib/libtqui.so.*
%{qtdir}/lib/libtqt*.so.*

# TQT 3.4.0: WTF is this file ??
%exclude %{_mandir}/README

%files config
%defattr(-,root,root,-)
%{qtdir}/bin/qtconfig
%{_datadir}/applications/*qtconfig*.desktop
%{_datadir}/pixmaps/qtconfig3.png

%files devel
%defattr(-,root,root,-)
%{qt_docdir}/
%{qtdir}/bin/moc
%{qtdir}/bin/uic
%{qtdir}/bin/findtr
%{qtdir}/bin/qt20fix
%{qtdir}/bin/qtrename140
%{qtdir}/bin/assistant
%{qtdir}/bin/qm2ts
%{qtdir}/bin/qmake
%{qtdir}/bin/qembed
%{qtdir}/bin/linguist
%{qtdir}/bin/lupdate
%{qtdir}/bin/lrelease
%{qtdir}/include
%{qtdir}/mkspecs
%{qtdir}/lib/libtqt*.so
%{qtdir}/lib/libtqui.so
%{qtdir}/lib/libeditor.a
%{qtdir}/lib/libdesigner*.a
%{qtdir}/lib/libqassistantclient.a
%{qtdir}/lib/*.prl
%{qtdir}/phrasebooks
%{_libdir}/pkgconfig/*
%{_datadir}/applications/*linguist*.desktop
%{_datadir}/applications/*assistant*.desktop
%{_datadir}/pixmaps/linguist3.png
%{_datadir}/pixmaps/assistant3.png

# QT 3.3.8.D (TDE): 4 binaries have appeared
%{qtdir}/bin/createcw
%{qtdir}/bin/makeqpf
%{qtdir}/bin/mergetr
%{qtdir}/bin/msg2qm

# QT 3.3.8.D (TDE): removes lots of unnecessary include files
# (where do they come from ??? They were not in 3.3.8b !)
%exclude %{qtdir}/include/btree.h
%exclude %{qtdir}/include/crc32.h
%exclude %{qtdir}/include/debian_qsql_odbc.h
%exclude %{qtdir}/include/deflate.h
%exclude %{qtdir}/include/ftglue.h
%exclude %{qtdir}/include/ftxgdef.h
%exclude %{qtdir}/include/ftxgpos.h
%exclude %{qtdir}/include/ftxgsub.h
%exclude %{qtdir}/include/ftxopen.h
%exclude %{qtdir}/include/ftxopenf.h
%exclude %{qtdir}/include/hash.h
%exclude %{qtdir}/include/inffast.h
%exclude %{qtdir}/include/inffixed.h
%exclude %{qtdir}/include/inflate.h
%exclude %{qtdir}/include/inftrees.h
%exclude %{qtdir}/include/jchuff.h
%exclude %{qtdir}/include/jconfig.h
%exclude %{qtdir}/include/jdct.h
%exclude %{qtdir}/include/jdhuff.h
%exclude %{qtdir}/include/jerror.h
%exclude %{qtdir}/include/jinclude.h
%exclude %{qtdir}/include/jmemsys.h
%exclude %{qtdir}/include/jmorecfg.h
%exclude %{qtdir}/include/jversion.h
%exclude %{qtdir}/include/moc_yacc.h
%exclude %{qtdir}/include/opcodes.h
%exclude %{qtdir}/include/os.h
%exclude %{qtdir}/include/otlbuffer.h
%exclude %{qtdir}/include/pager.h
%exclude %{qtdir}/include/parse.h
%exclude %{qtdir}/include/pngasmrd.h
%exclude %{qtdir}/include/pngconf.h
%exclude %{qtdir}/include/sqlite.h
%exclude %{qtdir}/include/sqliteInt.h
%exclude %{qtdir}/include/trees.h
%exclude %{qtdir}/include/vdbe.h
%exclude %{qtdir}/include/vdbeInt.h
%exclude %{qtdir}/mkspecs/linux-g++-sparc

%files devel-docs
%defattr(-,root,root,-)
%doc examples
%doc tutorial
%{_mandir}/*/*

%files sqlite
%defattr(-,root,root,-)
%{qtdir}/plugins/sqldrivers/libqsqlite.so

%files ODBC
%defattr(-,root,root,-)
%{qtdir}/plugins/sqldrivers/libqsqlodbc.so

%files PostgreSQL
%defattr(-,root,root,-)
%{qtdir}/plugins/sqldrivers/libqsqlpsql.so

%files MySQL
%defattr(-,root,root,-)
%{qtdir}/plugins/sqldrivers/libqsqlmysql.so

%files designer
%defattr(-,root,root,-)
%{qtdir}/templates
%{qtdir}/bin/designer
%{_datadir}/applications/*designer*.desktop
%{_datadir}/pixmaps/designer3.png


%changelog
* Mon Feb 13 2012 Francois Andriot <francois.andriot@free.fr> - 3.4.0-1
- Initial build for TDE R14
- Renames 'qt3' to 'tqt3'
- Spec file based on 'qt3-3.3.8b-30' from RHEL 6

* Sun Dec 18 2011 Francois Andriot <francois.andriot@free.fr> - 3.3.8.d-3
- Updates zh_TW translations, thanks to Wei-Lun Chao .

* Thu Nov 03 2011 Francois Andriot <francois.andriot@free.fr> - 3.3.8.d-2
- Add missing BuildRequires

* Fri Sep 02 2011 Francois Andriot <francois.andriot@free.fr> - 3.3.8.d-1
- Initial build for RHEL 6, RHEL 5, and Fedora 15
- Switch to Trinity Version
- Spec file based on RHEL 6 'qt3-3.3.8b-29'
