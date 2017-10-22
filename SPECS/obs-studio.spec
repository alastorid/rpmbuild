%global commit0 d3c163b77510359f4b2b6fb31a201141ea726c30
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}
Summary: Open Broadcaster Software Studio
Name: obs-studio
Version: 20.1.0
Release: 1%{gver}%{dist}
Group: Applications/Multimedia
URL: https://obsproject.com/
License: GPLv2+ 
Source0:  https://github.com/jp9000/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildRequires: cmake 
BuildRequires: gcc 
BuildRequires: gcc-c++
BuildRequires: gcc-objc 
BuildRequires: pkgconfig 
BuildRequires: ffmpeg-devel 
BuildRequires: jansson-devel 
BuildRequires: pulseaudio-libs-devel
BuildRequires: jack-audio-connection-kit-devel 
BuildRequires: qt5-qtbase-devel 
BuildRequires: qt5-qtx11extras-devel 
BuildRequires: zlib-devel 
BuildRequires: mesa-libGL-devel 
BuildRequires: libXext-devel 
BuildRequires: libxcb-devel 
BuildRequires: libX11-devel 
BuildRequires: libcurl-devel 
BuildRequires: libv4l-devel 
BuildRequires: x264-devel 
BuildRequires: git
BuildRequires: desktop-file-utils
BuildRequires: libXcomposite-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: faac-devel
BuildRequires: ImageMagick-devel
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: systemd-devel
BuildRequires:  doxygen 
Requires:      ffmpeg x264

%description
Open Broadcaster Software is free and open source
software for video recording and live streaming.

%package libs
Summary: Open Broadcaster Software Studio libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description libs
Library files for Open Broadcaster Software

%package devel
Summary: Open Broadcaster Software Studio header files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for Open Broadcaster Software

%package        doc
Summary:        Documentation files for %{name}
Group:          Documentation
BuildArch:      noarch

%description    doc
The %{name}-doc package contains html documentation
that use %{name}.

%prep
%autosetup -n %{name}-%{commit0}

# rpmlint reports E: hardcoded-library-path
# replace OBS_MULTIARCH_SUFFIX by LIB_SUFFIX
sed -i 's|OBS_MULTIARCH_SUFFIX|LIB_SUFFIX|g' cmake/Modules/ObsHelpers.cmake

%build
%cmake -DOBS_VERSION_OVERRIDE=%{version} -DUNIX_STRUCTURE=1
%make_build

# build docs
doxygen

%install
%make_install

mkdir -p %{buildroot}/%{_libexecdir}/obs-plugins/obs-ffmpeg/
mv -f %{buildroot}/%{_datadir}/obs/obs-plugins/obs-ffmpeg/ffmpeg-mux \
      %{buildroot}/%{_libexecdir}/obs-plugins/obs-ffmpeg/ffmpeg-mux

%check
/usr/bin/desktop-file-validate %{buildroot}/%{_datadir}/applications/obs.desktop

%post libs -p /sbin/ldconfig

%post
/usr/bin/update-desktop-database >&/dev/null || :
/usr/bin/touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :

%postun
/usr/bin/update-desktop-database >&/dev/null || :
if [ $1 -eq 0 ]; then
  /usr/bin/touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi

%postun libs -p /sbin/ldconfig

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :

%files
%doc README.rst
%license UI/data/license/gplv2.txt
%license COPYING
%{_bindir}/obs
%{_datadir}/applications/obs.desktop
%{_datadir}/icons/hicolor/256x256/apps/obs.png
%{_datadir}/obs/
%{_libexecdir}/obs-plugins/

%files libs
%{_libdir}/obs-plugins/
%{_libdir}/*.so.*

%files devel
%{_libdir}/cmake/LibObs/
%{_libdir}/*.so
%{_includedir}/obs/

%files doc
%doc docs/html

%changelog

* Sun Oct 22 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 20.1.0-1.git7bd06e7
- Updated to 20.1.0-1.git7bd06e7

* Wed Oct 18 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 20.0.1-2.gitd3c163b  
- Automatic Mass Rebuild

* Tue Sep 26 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 20.0.1-1.gitd3c163b
- Updated to 20.0.1-1.gitd3c163b

* Thu Aug 10 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 20.0.0-1.git8b315186
- Updated to 20.0.0-1.git8b315186

* Sat Jul 08 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 19.0.3-1.gitd295ad3
- Updated to 19.0.3-1.gitd295ad3.

* Sat Mar 25 2017 Pavlo Rudyi <paulcarroty at riseup.net> - 18.0.1-1
- Update to 18.0.1

* Sat Mar 18 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 17.0.2-2.20170226gitc8d0893
- Rebuilt for libbluray

* Sun Feb 26 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 17.0.2-1.20170226gitc8d0893
- Updated to 17.0.2-1.20170226gitc8d0893

* Sun Jan 08 2017 Pavlo Rudyi <paulcarroty at riseup.net> - 17.0.0-1
- Update to 17.0.0

* Thu Oct 06 2016 Pavlo Rudyi <paulcarroty at riseup.net> - 0.16.2-1
- Update to 0.16.2

* Tue Aug 16 2016 Pavlo Rudyi <paulcarroty at riseup.net> - 0.15.4-1 
- Update to 0.15.4

* Fri Jul 22 2016 Pavlo Rudyi <paulcarroty at riseup net> - 0.15.2-1
- Update to 0.15.2 

* Thu Jul 07 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 0.14.2-6.20160618gite3deb7
- Rebuilt for FFmpeg 3.1 

* Sun Jun 26 2016 The UnitedRPMs Project (Key for UnitedRPMs infrastructure) <unitedrpms@protonmail.com> - 0.14.2-5.20160618gite3deb71
- Rebuild with new ffmpeg

* Thu Jun 23 2016 Pavlo Rudyi <paulcarroty at riseup net> - 0.14.2-4-20160618gite3deb71
- Add faac-devel depends for recording crash

* Mon Jun 20 2016 Pavlo Rudyi <paulcarroty at riseup net> - 0.14.2-3-20160618gite3deb71
- Include the previos changes by Sergio Basto

* Sat Jun 18 2016 David Vasquez <davidjeremias82 at gmail dot com> - 0.14.2-2-20160618gite3deb71
- Enabled linux-capture
- Enabled fdk
- Enabled Imagemagick
- Enabled Multiarch Suffix

* Fri Jun 17 2016 Pavlo Rudyi <paulcarroty at riseup net> - 0.14.2-1.20160617gite3deb71
- update to 14.2
- change version according to Fedora Package Naming Guidelines
- use the macros in %prep

* Mon May 02 2016 David Vasquez <davidjeremias82 at gmail dot com> - 0.14.1-2-20160502-3cb36bb
- Fixed Shared libraries
- Added desktop-file-validate check
- Fixed arch-dependent-file-in-usr-share

* Tue Apr 26 2016 Yiwan <caoli5288@gmail.com> - 0.14.1-1
- Updated to 0.14.1

* Thu Sep 24 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.12.0-0.1
- Updated to 0.12.0

* Mon Aug 17 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.11.4-0.1
- Added OBS_VERSION_OVERRIDE to correct version in compilation
- Updated to 0.11.4

* Sat Aug 08 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.11.3-0.1
- Updated to 0.11.3

* Thu Jul 30 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.11.2-0.1
- Updated to 0.11.2

* Fri Jul 10 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.11.1-0.1
- Updated to 0.11.1

* Wed May 27 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.10.1-0.1
- Initial .spec file
