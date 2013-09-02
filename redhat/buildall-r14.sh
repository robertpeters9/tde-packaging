#!/bin/bash

export PATH="$(dirname $0):${PATH}"

tdp='cd ~/tde/tde-packaging/redhat'
grp='./genrpm.sh -v 14.0.0 -a'

BUILDDIR="/dev/shm/BUILD${DIST}.$(uname -i)"
BUILDROOTDIR="/dev/shm/BUILDROOT${DIST}.$(uname -i)"
DIST="$(rpm -E %{dist})"

if [ -x /usr/sbin/urpmi ]; then
  PKGMGR="urpmi"
  PKGINST='sudo urpmi --auto --no-verify-rpm'
  PKGDEL='sudo urpme --auto'
  REPOUPDATE='(cd $(rpm -E %{_rpmdir}); genhdlist2 --clean --allow-empty noarch; genhdlist2 --clean --allow-empty $(uname -i); sudo urpmi.update rpmbuild.$(uname -i) rpmbuild.noarch)'
elif [ -x /usr/bin/zypper ]; then
  PKGMGR="zypper"
  PKGINST="sudo zypper install -y"
  PKGDEL="sudo zypper remove -y"
  REPOUPDATE='(cd $(rpm -E %{_rpmdir}); createrepo $(uname -i); createrepo noarch; sudo zypper refresh)'
elif [ -x /usr/bin/yum ]; then
  PKGMGR="yum"
  PKGINST='sudo yum install -y'
  PKGDEL='sudo yum remove -y'
  REPOUPDATE='(cd $(rpm -E %{_rpmdir}); createrepo $(uname -i); createrepo noarch; sudo yum clean all --disablerepo="*" --enablerepo="rpmbuild*")'
fi

BUILDDIR=$(rpm -E "%{_builddir}")

echo "Package Manager is '${PKGMGR}'"

pkg_listlocal() {
  rpm -qa --qf "%{name} %{buildhost}\n" | while read a b; do case "$b" in *.vtf) echo $a;; esac;done
}

pkg_delall() {
  PKGDEL $(pkg_listlocal)
}

is_installed() {
  rpm -q "$1" &>/dev/null
  return $?
}

# Build package if not already installed
grpi() {
  if ! is_installed trinity-"${1##*/}"; then
    eval ${grp} ${1}
    RET=$?
    if [ $RET -gt 0 ]; then
      echo "ERROR $RET !!!"
      exit $RET
    fi
  fi
}
# Build package if not already installed, then update repo
grpiu() {
  if ! is_installed trinity-"${1##*/}"; then
    grpi "$1"
    eval ${REPOUPDATE} || exit 1
  fi
}
# Build package if not already installed, then update repo, then install package
grpiui() {
  if ! is_installed trinity-"${1##*/}"; then
    grpiu "$1"
    eval ${PKGINST} "trinity-${1##*/}" || exit 1
  fi
}
# Build package if not already installed, then update repo, then install -devel package
grpiud() {
  if ! is_installed trinity-"${1##*/}"; then
    grpiu "$1"
    eval ${PKGINST} "trinity-${1##*/}" || exit 1
    eval ${PKGINST} "trinity-${1##*/}-devel" || exit 1
  fi
}

# TDE dependencies
grpiud dependencies/tqt3
grpiud dependencies/tqtinterface
grpiud dependencies/arts
grpiud dependencies/avahi-tqt
grpiud dependencies/dbus-1-tqt
grpiud dependencies/dbus-tqt
grpiud dependencies/libart-lgpl
grpiud dependencies/libcaldav
grpiud dependencies/libcarddav
grpiud dependencies/tqca

# Extra dependencies
grpiud extras/akode

# TDE main
# basic packages
grpiud tdelibs
grpiud tdebase
# Back to remaining dependencies ...
grpiud dependencies/tqscintilla
grpiud dependencies/python-tqt
# Main packages which are required by later main packages
grpiud tdepim
grpiud tdemultimedia
grpiud tdegames
grpiud tdebindings
grpiud tdegraphics
grpiud tdenetwork
# other main packages
grpiui tdeaccessibility
grpiui tdeaddons
grpiui tdeadmin
grpiui tdeartwork
grpiui tdeedu
grpiui tdetoys
grpiui tdeutils

if ! is_installed trinity-desktop; then
  grpiu extras/trinity-desktop
  eval ${PKGINST} trinity-desktop || exit 1
  # Disable trinity repository from here !!!
  if [ -r "/etc/yum.repos.d/trinity-3.5.13.repo" ]; then
    sed -i "/etc/yum.repos.d/trinity-3.5.13.repo" -e "s|enabled=.*|enabled=0|g"
  fi
fi

# devel packages
grpiud tdesdk
grpiui tdevelop
grpiui tdewebdev
if ! is_installed trinity-desktop-devel; then
  eval ${PKGINST} trinity-desktop-devel || exit 1
fi

# Build libraries
grpiud libraries/libkdcraw
grpiud libraries/libkexiv2
grpiud libraries/libkipi
grpiud libraries/libksquirrel
grpiud libraries/libtdeldap
grpiui libraries/libtqt-perl
grpiud libraries/python-trinity
grpiud libraries/pytdeextensions

# Extra libraries
if ! is_installed imlib1-devel; then
  grpiu 3rdparty/imlib1
  eval ${PKGINST} imlib1-devel || exit 1
fi
if ! is_installed torsocks; then
  grpiu 3rdparty/torsocks
  eval ${PKGINST} torsocks || exit 1
fi

# Build applications
# K3B is required later for k9copy
grpiud applications/k3b
# other applications, any order ...
grpiui applications/abakus
#grpiui applications/adept
grpiui applications/amarok
grpiui applications/basket
grpiui applications/bibletime
#grpiui applications/compizconfig-backend-kconfig
grpiui applications/digikam
grpiui applications/dolphin
grpiui applications/filelight
#grpiui applications/filelight-l10n
#grpiui applications/fusion-icon
grpiui applications/gwenview
grpiui applications/gwenview-i18n
if ! is_installed trinity-k3b-i18n-French; then
  grpiu applications/k3b-i18n
  eval ${PKGINST} trinity-k3b-i18n-French || exit 1
fi
grpiui applications/k9copy
grpiui applications/kaffeine
grpiui applications/kaffeine-mozilla
grpiui applications/kasablanca
grpiui applications/katapult
grpiui applications/kbarcode
grpiui applications/kbfx
grpiui applications/kbibtex
grpiui applications/kbiff
grpiui applications/kbookreader
grpiui applications/kchmviewer
grpiui applications/kcmautostart
grpiui applications/kcmldap
grpiui applications/kcmldapcontroller
grpiui applications/kcmldapmanager
grpiui applications/kcpuload
grpiui applications/kdbg
grpiui applications/kdbusnotification
grpiui applications/kdiff3
grpiui applications/kdirstat
grpiui applications/keep
grpiui applications/kerberostray
#grpiui applications/kerry
grpiui applications/kftpgrabber
grpiui applications/kile
grpiui applications/kima
grpiui applications/kiosktool
grpiui applications/kmplayer
grpiui applications/kmyfirewall
grpiui applications/kmymoney
grpiui applications/knemo
grpiui applications/knetload
grpiui applications/knetstats
#grpiui applications/knetworkmanager
grpiui applications/knights
grpiui applications/knowit
grpiui applications/knmap
grpiui applications/knutclient
if ! is_installed trinity-koffice-suite; then
  grpiu applications/koffice
  eval ${PKGINST} trinity-koffice-suite
fi
if ! is_installed trinity-koffice-i18n-French; then
  grpiu applications/koffice-i18n
  eval ${PKGINST} trinity-koffice-i18n-French
fi
grpiui applications/konversation
grpiui applications/kopete-otr
grpiui applications/kpicosim
grpiui applications/kpilot
#grpiui applications/kpowersave
grpiui applications/krecipes
grpiui applications/krename
grpiui applications/krusader
grpiui applications/ksensors
grpiui applications/kshowmail
grpiui applications/kshutdown
grpiui applications/ksplash-engine-moodin
grpiui applications/ksquirrel
grpiui applications/kstreamripper
grpiui applications/ksystemlog
grpiui applications/ktechlab
grpiui applications/ktorrent
grpiui applications/kuickshow
grpiui applications/kvirc
grpiui applications/kvkbd
grpiui applications/kvpnc
grpiui applications/mplayerthumbs
grpiui applications/piklab
grpiui applications/potracegui
grpiui applications/rosegarden
grpiui applications/smartcardauth
grpiui applications/smb4k
grpiui applications/soundkonverter
grpiui applications/tde-guidance
grpiui applications/tdeio-apt
if ! is_installed trinity-tdeio-ftps; then
  grpiu applications/tdeio-ftps
  eval ${PKGINST} trinity-tdeio-ftps || exit 1
fi
grpiui applications/tdeio-locate
grpiui applications/tdeio-umountwrapper
grpiui applications/tdenetworkmanager
grpiui applications/tdepowersave
grpiui applications/tderadio
grpiui applications/tde-style-lipstik
grpiui applications/tde-style-qtcurve
grpiui applications/tdesudo
grpiui applications/tdesvn
grpiui applications/tde-systemsettings
grpiui applications/tdmtheme
grpiui applications/tellico
grpiui applications/tork
grpiui applications/twin-style-crystal
grpiui applications/wlassistant
grpiui applications/yakuake

# Decoration-related stuff are distribution-dependant.
if [ "${DIST}" != ".el4" ] && [ "${DIST}" != ".el5" ]; then
  grpiui applications/gtk-qt-engine
  #grpiui applications/kgtk-qt3
fi

if ! is_installed trinity-desktop-applications; then
  eval ${PKGINST} trinity-desktop-applications || exit 1
fi

if ! is_installed trinity-desktop-all; then
  eval ${PKGINST} trinity-desktop-all || exit 1
fi

exit 0

# Build extra packages
grpiui extras/icons-crystalsvg-updated
grpiui extras/icons-kfaenza
grpiui extras/icons-oxygen
#grpiui extras/kcheckgmail
#grpiui extras/kdebluetooth
grpiui extras/kickoff-i18n
#grpiui extras/knoda
grpiui extras/style-ia-ora
#grpiui extras/tdeio-sysinfo
grpiui extras/theme-baghira
#grpiui extras/trinity-desktop
#grpiui extras/trinity-live
grpiui extras/twinkle
eval ${PKGINST} trinity-desktop-extras

