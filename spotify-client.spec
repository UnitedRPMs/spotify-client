%global	current	1.1.56.595

AutoReqProv: no

Name:           spotify-client
Version:        %{current}
Epoch:		1
Release:        2%{?dist}
Summary:        A Open Source installer for spotify a proprietary peer-to-peer music streaming service

License:        GPLv3
URL:            http://www.spotify.com
Group:          Applications/Multimedia
BuildArch: 	noarch
Source1:	https://raw.github.com/kuboosoft/spotify-client-installer/master/spotify
Source2:	spotify.protocol
Source3:	spotify-linux-128.png
Source4:	spotify-reset.png
Source5:	com.spotify.spotify.metainfo.xml
BuildRequires:	binutils
Requires:	desktop-file-utils alsa-lib glibc libXScrnSaver qtwebkit
Requires:	nspr nss nss-util systemd-libs openssl-spotify systemd xterm wget binutils tar 
Requires:	gtk2 dbus-x11 libssh2 libcurl libnotify libatomic curl libcurl-openssl

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

echo '#!/usr/bin/bash
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
  install -dm 755 %{buildroot}/%{_datadir}/kde4/services/
  install -m 644 %{SOURCE2} %{buildroot}/usr/share/kde4/services/

# Install AppData
  install -Dm 0644 %{S:5} %{buildroot}/%{_metainfodir}/com.spotify.spotify.metainfo.xml
         

%files
%defattr(755, root, root)
%{_bindir}/spotify
%{_bindir}/spotify-reset
%{_datadir}/kde4/services/spotify.protocol
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-reset.desktop
%{_datadir}/icons/spotify-linux-128.png
%{_datadir}/icons/spotify-reset.png
%{_metainfodir}/com.spotify.spotify.metainfo.xml


%changelog

* Mon Apr 26 2021 David Va <davidva AT tuta DOT io> 1.1.56.595-2
- Updated to 1.1.56.595

* Sat Mar 27 2021 David Va <davidva AT tuta DOT io> 1.1.55.498-2
- Updated to 1.1.55.498

* Mon Oct 12 2020 David Va <davidva AT tuta DOT io> 1.1.43.700-2
- Updated to 1.1.43.700

* Thu Sep 24 2020 David Va <davidva AT tuta DOT io> 1.1.42.622-2
- Updated to 1.1.42.622

* Mon Aug 31 2020 David Va <davidva AT tuta DOT io> 1.1.40.508-2
- Updated to 1.1.40.508

* Fri Jul 03 2020 David Va <davidva AT tuta DOT io> 1.1.35.458-2
- Updated to 1.1.35.458

* Sun May 24 2020 David Va <davidva AT tuta DOT io> 1.1.32.618-2
- Updated to 1.1.32.618

* Tue Mar 31 2020 David Va <davidva AT tuta DOT io> 1.1.26.501-2
- Updated to 1.1.26.501

* Thu Mar 19 2020 David Va <davidva AT tuta DOT io> 1.1.26-2
- Updated to 1.1.26

* Thu Jul 18 2019 David Va <davidva AT tuta DOT io> 1.1.10.546-2
- Updated to 1.1.10.546

* Tue Jun 11 2019 David Va <davidva AT tuta DOT io> 1.1.5.153-2
- Updated to 1.1.5.153

* Wed Apr 10 2019 David Va <davidva AT tuta DOT io> 1.1.0.237-2
- Updated to 1.1.0.237

* Sun Feb 17 2019 David Va <davidva AT tuta DOT io> 1.1.0-2
- Updated to 1.1.0

* Tue Jan 29 2019 David Va <davidva AT tuta DOT io> 1.0.98-2
- Updated to 1.0.98

* Thu Jan 24 2019 David Va <davidva AT tuta DOT io> 1.0.96.181-2
- Updated to 1.0.96.181

* Thu Jan 10 2019 David Va <davidva AT tuta DOT io> 1.0.96-2
- Updated to 1.0.96

* Tue Dec 11 2018 David Va <davidva AT tuta DOT io> 1.0.94.262-2
- Updated to 1.0.94.262

* Mon Oct 29 2018 David Va <davidva AT tuta DOT io> 1.0.92.390-2
- Updated to 1.0.92.390

* Thu Sep 20 2018 David Va <davidva AT tuta DOT io> 1.0.89.313-2
- Updated to 1.0.89.313

* Fri Sep 14 2018 David Va <davidva AT tuta DOT io> 1.0.89-2
- Updated to 1.0.89

* Fri Sep 07 2018 David Va <davidva AT tuta DOT io> 1.0.88.353-2
- Updated to 1.0.88.353

* Sat Aug 18 2018 David Va <davidva AT tuta DOT io> 1.0.88.345-2
- Updated to 1.0.88.345

* Thu May 31 2018 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.80.480-2
- Updated to 1.0.80.480

* Wed Apr 25 2018 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.79.223-2
- Updated to 1.0.79.223

* Thu Mar 29 2018 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.77.338-2
- Updated to 1.0.77.338
- libcurl fix

* Wed Mar 07 2018 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.72.117-1
- Updated to 1.0.72.117

* Wed Jan 17 2018 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.70.399-1
- Updated to 1.0.70.399

* Fri Dec 15 2017 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.69.336-1
- Updated to 1.0.69.336

* Sun Dec 10 2017 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.67.582-1
- Updated to 1.0.67.582

* Wed Oct 25 2017 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.66.478-1
- Updated to 1.0.66.478

* Sun Oct 22 2017 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.64.407-1
- Updated to 1.0.64.407

* Sat Jan 07 2017 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.44.100.ga60c0ce1-2
- Used openssl official

* Sat Jan 07 2017 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.44.100.ga60c0ce1-1
- Updated to 1.0.44.100.ga60c0ce1

* Tue Jun 21 2016 Pavlo Rudyi <paulcarroty at riseup.net> - 1.0.31.56.g526cfefe-2
- Added patch for the correct work with zsh shell, thx to @edgan

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
