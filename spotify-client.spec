%define	current	1.0.31.56.g526cfefe



AutoReqProv: no

Name:           spotify-client
Version:        %{current}
Release:        1%{?dist}
Summary:        A Open Source installer for spotify a proprietary peer-to-peer music streaming service

License:        GPLv3
URL:            http://www.spotify.com
Group:          Applications/Multimedia
BuildArch: 	noarch
Source1:	https://raw.github.com/kuboosoft/spotify-client-installer/master/spotify
Source2:	spotify.protocol
Source3:	spotify-linux-128.png
Source4:	spotify-reset.png
BuildRequires: 	binutils
Requires:	desktop-file-utils alsa-lib glibc libXScrnSaver qtwebkit
Requires:	nspr nss nss-util systemd-libs openssl-libs openssl1 systemd-devel xterm wget binutils tar 
Requires:	libgcrypt1.5.4 gtk2 dbus-x11 libssh2 libcurl libnotify

Conflicts:	lpf-spotify-client


%description
Think of Spotify as your new music collection. Your library. Only
this time your collection is vast: millions of tracks and counting.
Spotify comes in all shapes and sizes, available for your PC, Mac,
home audio system and mobile phone. Wherever you go, your music
follows you. And because the music plays live, there’s no need to wait
for downloads and no big dent in your hard drive.


%prep

# None

%build

# None

%install

# Bin Script
install -dm 755 %{buildroot}/usr/bin/
install -m 644 %{SOURCE1} %{buildroot}/usr/bin/
chmod a+x %{buildroot}/usr/bin/spotify

#icon

install -dm 755 %{buildroot}/%{_datadir}/icons/
install -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/icons/
install -m 644 %{SOURCE4} %{buildroot}/%{_datadir}/icons/

echo '#!/bin/sh
if [ -d $HOME/.local/share/spotify/ ]; then
rm -rf $HOME/.local/share/spotify/
fi
if [ -d $HOME/.config/spotify/ ]; then
rm -rf $HOME/.config/spotify/
fi
if [ -d $HOME/.cache/spotify/ ]; then
rm -rf $HOME/.cache/spotify/
fi
notify-send --hint=int:transient:1 "Restored Spotify-Client" -i "/usr/share/icons/spotify-reset.png"' > %{buildroot}/%{_bindir}/spotify-reset
chmod a+x %{buildroot}/%{_bindir}/spotify-reset

# menu-entry
install -dm 755 %{buildroot}/%{_datadir}/applications
cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=spotify
GenericName=spotify
Comment=A proprietary peer-to-peer music streaming service
Icon=/usr/share/icons/spotify-linux-128.png
Type=Application
Categories=AudioVideo;
Exec=spotify
StartupNotify=false
Terminal=false
EOF

# menu-entry spotify-reset
install -dm 755 %{buildroot}/%{_datadir}/applications
cat > %{buildroot}/%{_datadir}/applications/%{name}-reset.desktop << EOF
[Desktop Entry]
Name=spotify-reset
GenericName=spotify-reset
Comment=Reset Spotify
Icon=/usr/share/icons/spotify-reset.png
Type=Application
Categories=AudioVideo;
Exec=spotify-reset
StartupNotify=false
Terminal=false
EOF



  # Copy protocol file if KDE is installed
  install -dm 755 %{buildroot}/usr/share/kde4/services/
  install -m 644 %{SOURCE2} %{buildroot}/usr/share/kde4/services/
         

%files
%defattr(755, root, root)
%{_bindir}/spotify
%{_bindir}/spotify-reset
%{_datadir}/kde4/services/spotify.protocol
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-reset.desktop
%{_datadir}/icons/spotify-linux-128.png
%{_datadir}/icons/spotify-reset.png


%changelog

* Tue May 31 2016 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.31.56.g526cfefe-1
- Updated to 1.0.31.56.g526cfefe

* Thu Apr 28 2016 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.28.89.gf959d4ce-1
- Updated to 1.0.28.89.gf959d4ce

* Wed Oct 21 2015 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.16.104.g3b776c9e-1
- Updated to 1.0.16.104.g3b776c9e

* Mon Oct 12 2015 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.15.137.gbdf68615-1
- Updated to 1.0.15.137.gbdf68615

* Fri Sep 25 2015 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.14.124.g4dfabc51-1
- Updated to 1.0.14.124.g4dfabc51

* Wed Sep 16 2015 David Vásquez <davidjeremias82 AT gmail DOT com> - 1.0.13.112.g539ef41b-2
- Added some dependencies
- Fixed some pats in 32bits version

* Fri Sep 04 2015 David Vásquez <davidjeremias82 AT gmail DOT com> - 1.0.13.112.g539ef41b-1
- Updated to 1.0.13.112.g539ef41b (64bits) and 1.0.13.111.g6bd0deca (32bits)

* Fri Aug 14 2015 David Vásquez <davidjeremias82 AT gmail DOT com> - 1.0.11.131.gf4d47cb0-3
- Deleted old paths for i686 platform

* Wed Aug 12 2015 David Vásquez <davidjeremias82 AT gmail DOT com> - 1.0.11.131.gf4d47cb0-2
- Fixed some symlink

* Sun Aug 09 2015 David Vásquez <davidjeremias82 AT gmail DOT com> - 1.0.11.131.gf4d47cb0-1
- Updated to 1.0.11.131.gf4d47cb0 (64bits) and 1.0.11.129.g61510de3 (32bits)

* Sat Jul 18 2015 David Vásquez <davidjeremias82 AT gmail DOT com> - 1.0.9.133.gcedaee38-1
- Updated to 1.0.9.133.gcedaee38

* Tue Jun 16 2015 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.9.17.8.gd06432d-2
- Added new requires

* Mon Jun 08 2015 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.9.17.8.gd06432d-1
- Updated to 0.9.17.8.gd06432d
- Used new source only for 32bits version (old version, because isn't mantained anymore).

* Thu Apr 02 2015 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.9.17.1.g9b85d436-1
- Updated to 0.9.17.1.g9b85d436

* Tue Mar 03 2015 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.9.11.27.g2b1a638.81-3
- Added libudev0 as requires

* Mon Dec 15 2014 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.9.11.27.g2b1a638.81-2
- Changed requires libgcrypt to libgcrypt1.5.4

* Sun Jul 27 2014 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.9.11.27.g2b1a638.81-1
- Updated 0.9.11.26.g995ec04.78 to 0.9.11.27.g2b1a638.81
- Changed requires openssl0.9.8-spotify to openssl-spotify

* Thu Jul 10 2014 <davidjeremias82 AT gmail DOT com> 0.9.11.26.g995ec04.78-1
- Updated to 0.9.11.26.g995ec04.78-1

* Tue Jan 28 2014 <davidjeremias82 AT gmail DOT com> 0.9.4.183.g644e24e.428-3
- New Requires. 

* Thu Jan 23 2014 <davidjeremias82 AT gmail DOT com> 0.9.4.183.g644e24e.428-1
- initial rpm for Fedora 