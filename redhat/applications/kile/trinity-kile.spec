# Default version for this component
%define kdecomp kile
%define version 2.0.2
%define release 3

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	KDE Integrated LaTeX Environment [Trinity]
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Publishing

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

%package i18n-ar
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Arabic (ar) translations for Kile [Trinity]
%description i18n-ar
This package contains the Arabic translations for Kile.

%package i18n-bg
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Bulgarian (bg) translations for Kile [Trinity]
%description i18n-bg
This package contains the Bulgarian translations for Kile.

%package i18n-br
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Brazilian (br) translations for Kile [Trinity]
%description i18n-br
This package contains the Brazilian translations for Kile.

%package i18n-ca
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Catalan (ca) translations for Kile [Trinity]
%description i18n-ca
This package contains the Catalan translations for Kile.

%package i18n-cs
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Czech (cs) translations for Kile [Trinity]
%description i18n-cs
This package contains the Czech translations for Kile.

%package i18n-cy
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Welsh (cy) translations for Kile [Trinity]
%description i18n-cy
This package contains the Welsh translations for Kile.

%package i18n-da
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Danish (da) translations for Kile [Trinity]
%description i18n-da
This package contains the Danish translations for Kile.

%package i18n-de
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: German (de) translations for Kile [Trinity]
%description i18n-de
This package contains the German translations for Kile.

%package i18n-el
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Greek (el) translations for Kile [Trinity]
%description i18n-el
This package contains the greek translations for Kile.

%package i18n-engb
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: British English (en_GB) translations for Kile [Trinity]
%description i18n-engb
This package contains the British English (en_GB) translations for Kile [Trinity].

%package i18n-es
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Spanish (es) translations for Kile [Trinity]
%description i18n-es
This package contains the Spanish translations for Kile.

%package i18n-et
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Estonian (et) translations for Kile [Trinity]
%description i18n-et
This package contains the Estonian translations for Kile.

%package i18n-eu
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Basque (eu) translations for Kile [Trinity]
%description i18n-eu
This package contains the Basque translations for Kile.

%package i18n-fi
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Finnish (fi) translations for Kile [Trinity]
%description i18n-fi
This package contains the Finnish translations for Kile.

%package i18n-fr
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: French (fr) translations for Kile [Trinity]
%description i18n-fr
This package contains the French translations for Kile.

%package i18n-ga
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Irish Gaelic (ga) translations for Kile [Trinity]
%description i18n-ga
This package contains the Irish Gaelic translations for Kile.

%package i18n-gl
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Galician (gl) translations for Kile [Trinity]
%description i18n-gl
This package contains the Galician translations for Kile.

%package i18n-hi
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Hindi (hi) translations for Kile [Trinity]
%description i18n-hi
This package contains the Hindi translations for Kile.

%package i18n-hu
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Hungarian (hu) translations for Kile [Trinity]
%description i18n-hu
This package contains the Hungarian translations for Kile.

%package i18n-is
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Icelandic (is) translations for Kile [Trinity]
%description i18n-is
This package contains the Icelandic translations for Kile.

%package i18n-it
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Italian (it) translations for Kile [Trinity]
%description i18n-it
This package contains the Italian translations for Kile.

%package i18n-ja
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Japanese (ja) translations for Kile [Trinity]
%description i18n-ja
This package contains the Japanese translations for Kile.

%package i18n-lt
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Lithuanian (lt) translations for Kile [Trinity]
%description i18n-lt
This package contains the Lithuanian translations for Kile.

%package i18n-ms
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Malay (ms) translations for Kile [Trinity]
%description i18n-ms
This package contains the Malay translations for Kile.

%package i18n-mt
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Maltese (mt) translations for Kile [Trinity]
%description i18n-mt
This package contains the Maltese translations for Kile.

%package i18n-nb
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Norwegian Bookmal (nb) translations for Kile [Trinity]
%description i18n-nb
This package contains the Norwegian Bookmal translations for Kile.

%package i18n-nds
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Low Saxon (nds) translations for Kile [Trinity]
%description i18n-nds
This package contains the Low Saxon translations for Kile.

%package i18n-nl
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Dutch (nl) translations for Kile [Trinity]
%description i18n-nl
This package contains the Dutch translations for Kile.

%package i18n-nn
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Norwegian Nynorsk (nn) translations for Kile [Trinity]
%description i18n-nn
This package contains the Norwegian Nynorsk translations for Kile.

%package i18n-pa
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Punjabi (pa) translations for Kile [Trinity]
%description i18n-pa
This package contains the Punjabi translations for Kile.

%package i18n-pl
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Polish (pl) translations for Kile [Trinity]
%description i18n-pl
This package contains the Polish translations for Kile.

%package i18n-pt
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Portuguese (pt) translations for Kile [Trinity]
%description i18n-pt
This package contains the Portuguese translations for Kile.

%package i18n-ptbr
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Brazilian Portuguese (pt_BR) translations for Kile [Trinity]
%description i18n-ptbr
This package contains the Brazilian Portuguese translations for Kile.

%package i18n-ro
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Romanian (ro) translations for Kile [Trinity]
%description i18n-ro
This package contains the Romanian translations for Kile.

%package i18n-ru
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Russian (ru) translations for Kile [Trinity]
%description i18n-ru
This package contains the Russian translations for Kile.

%package i18n-rw
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Kinyarwanda (rw) translations for Kile [Trinity]
%description i18n-rw
This package contains the Kinyarwanda translations for Kile.

%package i18n-sk
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Slovak (sk) translations for Kile [Trinity]
%description i18n-sk
This package contains the Slovak translations for Kile.

%package i18n-sr
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Serbian (sr) translations for Kile [Trinity]
%description i18n-sr
This package contains the Serbian translations for Kile.

%package i18n-srlatin
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Latin Serbian (sr@Latn) translations for Kile [Trinity]
%description i18n-srlatin
This package contains the Latin Serbian translations for Kile.

%package i18n-sv
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Swedish (sv) translations for Kile [Trinity]
%description i18n-sv
This package contains the Swedish translations for Kile.

%package i18n-ta
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Tamil (ta) translations for Kile [Trinity]
%description i18n-ta
This package contains the Tamil translations for Kile.

%package i18n-th
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Thai (th) translations for Kile [Trinity]
%description i18n-th
This package contains the Thai translations for Kile.

%package i18n-tr
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Turkish (tr) translations for Kile [Trinity]
%description i18n-tr
This package contains the Turkish translations for Kile.

%package i18n-uk
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Ukrainian (uk) translations for Kile [Trinity]
%description i18n-uk
This package contains the Ukrainian translations for Kile.

%package i18n-zhcn
Group:		Applications/Publishing
Requires: %{name} >= %{version}
Provides: trinity-kile-i18n
Summary: Chinese Simplified (zh_CN) translations for Kile [Trinity]
%description i18n-zhcn
This package contains the Chinese Simplified translations for Kile.


%description
Kile is a user-friendly LaTeX source editor and TeX shell for TDE.

The source editor is a multi-document editor designed for .tex and .bib
files.  Menus, wizards and auto-completion are provided to assist with
tag insertion and code generation.  A structural view of the document
assists with navigation within source files.

The TeX shell integrates the various tools required for TeX processing.
It assists with LaTeX compilation, DVI and postscript document viewing,
generation of bibliographies and indices and other common tasks.

Kile can support large projects consisting of several smaller files.

%prep
%setup -q -n applications/%{kdecomp}

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || \
%__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
  --disable-rpath \
  --with-extra-includes=%{_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%__chmod +x %{buildroot}%{_datadir}/apps/kile/test/runTests.sh

%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%{_bindir}/kile
%{_datadir}/applications/kde/kile.desktop
%exclude %{_datadir}/apps/katepart/syntax/bibtex.xml
%exclude %{_datadir}/apps/katepart/syntax/latex.xml
%{_datadir}/apps/kconf_update
%{_datadir}/apps/kile
%{_datadir}/config.kcfg/kile.kcfg
%{_datadir}/icons/hicolor/*/apps/kile.png
%{_datadir}/icons/hicolor/scalable/apps/kile.svgz
%{tde_docdir}/HTML/en/kile
%{_datadir}/mimelnk/text/x-kilepr.desktop

%files i18n-da
%lang(da) %{tde_docdir}/HTML/da/kile
%lang(da) %{_datadir}/locale/da/LC_MESSAGES/kile.mo

%files i18n-es
%lang(es) %{tde_docdir}/HTML/es/kile
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/kile.mo

%files i18n-et
%lang(et) %{tde_docdir}/HTML/et/kile
%lang(et) %{_datadir}/locale/et/LC_MESSAGES/kile.mo

%files i18n-it
%lang(it) %{tde_docdir}/HTML/it/kile
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/kile.mo

%files i18n-nl
%lang(nl) %{tde_docdir}/HTML/nl/kile
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/kile.mo

%files i18n-pt
%lang(pt) %{tde_docdir}/HTML/pt/kile
%lang(pt) %{_datadir}/locale/pt/LC_MESSAGES/kile.mo

%files i18n-sv
%lang(sv) %{tde_docdir}/HTML/sv/kile
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/kile.mo

%files i18n-ar
%lang(ar) %{_datadir}/locale/ar/LC_MESSAGES/kile.mo

%files i18n-bg
%lang(bg) %{_datadir}/locale/bg/LC_MESSAGES/kile.mo

%files i18n-br
%lang(br) %{_datadir}/locale/br/LC_MESSAGES/kile.mo

%files i18n-ca
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/kile.mo

%files i18n-cs
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/kile.mo

%files i18n-cy
%lang(cy) %{_datadir}/locale/cy/LC_MESSAGES/kile.mo

%files i18n-de
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/kile.mo

%files i18n-el
%lang(el) %{_datadir}/locale/el/LC_MESSAGES/kile.mo

%files i18n-engb
%lang(en_GB) %{_datadir}/locale/en_GB/LC_MESSAGES/kile.mo

%files i18n-eu
%lang(eu) %{_datadir}/locale/eu/LC_MESSAGES/kile.mo

%files i18n-fi
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/kile.mo

%files i18n-fr
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/kile.mo

%files i18n-ga
%lang(ga) %{_datadir}/locale/ga/LC_MESSAGES/kile.mo

%files i18n-gl
%lang(gl) %{_datadir}/locale/gl/LC_MESSAGES/kile.mo

%files i18n-hi
%lang(hi) %{_datadir}/locale/hi/LC_MESSAGES/kile.mo

%files i18n-hu
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/kile.mo

%files i18n-is
%lang(is) %{_datadir}/locale/is/LC_MESSAGES/kile.mo

%files i18n-ja
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/kile.mo

%files i18n-lt
%lang(lt) %{_datadir}/locale/lt/LC_MESSAGES/kile.mo

%files i18n-ms
%lang(ms) %{_datadir}/locale/ms/LC_MESSAGES/kile.mo

%files i18n-mt
%lang(mt) %{_datadir}/locale/mt/LC_MESSAGES/kile.mo

%files i18n-nb
%lang(nb) %{_datadir}/locale/nb/LC_MESSAGES/kile.mo

%files i18n-nds
%lang(nds) %{_datadir}/locale/nds/LC_MESSAGES/kile.mo

%files i18n-nn
%lang(nn) %{_datadir}/locale/nn/LC_MESSAGES/kile.mo

%files i18n-pa
%lang(pa) %{_datadir}/locale/pa/LC_MESSAGES/kile.mo

%files i18n-pl
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/kile.mo

%files i18n-ptbr
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/kile.mo

%files i18n-ro
%lang(ro) %{_datadir}/locale/ro/LC_MESSAGES/kile.mo

%files i18n-ru
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/kile.mo

%files i18n-rw
%lang(rw) %{_datadir}/locale/rw/LC_MESSAGES/kile.mo

%files i18n-sk
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/kile.mo

%files i18n-sr
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/kile.mo

%files i18n-srlatin
%lang(sr@Latn) %{_datadir}/locale/sr@Latn/LC_MESSAGES/kile.mo

%files i18n-ta
%lang(ta) %{_datadir}/locale/ta/LC_MESSAGES/kile.mo

%files i18n-th
%lang(th) %{_datadir}/locale/th/LC_MESSAGES/kile.mo

%files i18n-tr
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/kile.mo

%files i18n-uk
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/kile.mo

%files i18n-zhcn
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/kile.mo
 



%Changelog
* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 2.0.2-3
- Rebuilt for Fedora 17
- Removes the XPM icon

* Fri Apr 20 2012 Francois Andriot <francois.andriot@free.fr> - 2.0.2-2
- Fix file conflict with trinity-kdelibs

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 2.0.2-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16