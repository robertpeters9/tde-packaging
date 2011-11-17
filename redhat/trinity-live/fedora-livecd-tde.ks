# fedora-livecd-tde.ks
#
# Description:
# - Fedora Livecd Spin with the Trinity Desktop Environment (TDE)
# - Based on 'fedora-livecd-kde.ks' provided by Fedora 15
#
# Maintainer(s):
# - Francois Andriot <francois.andriot@free.fr>

%include fedora-live-tde-base.ks
%include fedora-live-minimization.ks

# 3rd party for VLC
#repo --name=atrpms --baseurl=http://dl.atrpms.net/f$releasever-$basearch/atrpms/stable


%packages
# Additional packages that are not default in trinity-desktop but useful
trinity-desktop-extras
trinity-live-openbox

# Some TDE applications
trinity-amarok
#trinity-digikam
trinity-dolphin
trinity-gwenview
trinity-k3b
trinity-kaffeine
trinity-kbookreader
#trinity-knetworkmanager
trinity-konversation
trinity-ksensors
trinity-kstreamripper
trinity-yakuake

# Some TDE translations
trinity-kde-i18n-French
#trinity-kde-i18n-German
trinity-kde-i18n-Spanish
trinity-kde-i18n-Chinese-Big5

# 3rd party stuff
#vlc

# Fedora stuff
fuse
liveusb-creator
#wlassistant
#wicd
#wicd-gtk


### more desktop stuff
fedora-icon-theme
adwaita-cursor-theme
adwaita-gtk2-theme
adwaita-gtk3-theme

# use yum-presto by default
yum-presto

### space issues

# fonts (we make no bones about admitting we're english-only)
wqy-microhei-fonts	# a compact CJK font, to replace:
-un-core-dotum-fonts	# Korean
-vlgothic-fonts		# Japanese
-wqy-zenhei-fonts	# Chinese

-paratype-pt-sans-fonts	# Cyrillic (already supported by DejaVu), huge
#-stix-fonts		# mathematical symbols

# remove input methods to free space
-@input-methods
-scim*
-m17n*
-ibus*
-iok

# save some space (from @base)
-make
-nss_db

## avoid serious bugs by omitting broken stuff

%end

%post
%end
