# Default version for this component
%define kdecomp krename
%define version 3.0.14
%define release 4

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	A TDE batch file renaming utility. 
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

BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils
BuildRequires: imlib-devel

%description
KRename is a powerful batch renamer for TDE. It allows you to easily rename hundreds or
even more files in one go. The filenames can be created by parts of the original filename,
numbering the files or accessing hundreds of informations about the file, like creation date
or Exif informations of an image. 

%prep
%setup -q -n applications/%{kdecomp}

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
    --enable-closure

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{kdecomp}


%clean
%__rm -rf %{buildroot}


%post
for f in hicolor locolor ; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done

%postun
for f in hicolor locolor ; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/*
%{_datadir}/applications/*/*.desktop
%{_datadir}/apps/*/
%{tde_docdir}/HTML/en/*/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/locolor/*/*/*


%Changelog
* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 3.0.14-4
- Rebuild for Fedora 17
- Fix HTML directory location

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.0.14-3
- Rebuilt for TDE 3.5.13 on RHEL 6, RHEL 5 and Fedora 15

* Tue Sep 14 2011 Francois Andriot <francois.andriot@free.fr> - 3.0.14-2
- Import to GIT

* Wed Aug 24 2011 Francois Andriot <francois.andriot@free.fr> - 3.0.14-1
- Correct macro to install under "/opt", if desired

* Sun Aug 14 2011 Francois Andriot <francois.andriot@free.fr> - 3.0.14-0
- Initial build for RHEL 6.0

