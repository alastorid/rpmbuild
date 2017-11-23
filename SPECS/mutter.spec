%global gtk3_version 3.19.8
%global gsettings_desktop_schemas_version 3.21.4
%global json_glib_version 0.12.0

Name:          mutter
Version:       3.22.3
Release:       11%{?dist}
Summary:       Window and compositing manager based on Clutter

License:       GPLv2+
#VCS:          git:git://git.gnome.org/mutter
URL:           http://www.gnome.org
Source0:       http://download.gnome.org/sources/%{name}/3.22/%{name}-%{version}.tar.xz

# https://bugzilla.gnome.org/show_bug.cgi?id=771442
Patch0:        fall-back-to-xorg-on-hybrid-gpus.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1331382
Patch1:        0001-Revert-backend-x11-Ensure-the-Xkb-group-index-remain.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1390607
Patch2:        0001-wayland-xdg-shell-Handle-the-wl_output-on-the-set_fu.patch

Patch3:         startup-notification.patch

Patch4:        deal-more-gracefully-with-oversized-windows.patch
Patch5:        support-headless-mode.patch

Patch6:        0001-monitor-manager-xrandr-Work-around-spurious-hotplugs.patch
Patch7:        0001-monitor-manager-xrandr-Force-an-update-when-resuming.patch
Patch8:        0001-monitor-config-Consider-external-layout-before-defau.patch

Patch9:       Enable-threeaded-swap-wait.patch

Patch10:       0001-events-Don-t-move-sloppy-focus-while-buttons-are-pre.patch
Patch11:       0001-backends-x11-Support-synaptics-configuration.patch

Patch12:       0001-display-Check-we-have-a-screen-before-freeing-it.patch

Patch13:       0001-cogl-Prefer-swizzling-to-convert-BGRA-buffers.patch

Patch14:       0001-cally-Fix-translation-to-screen-coordinates.patch

Patch15:       0001-window-actor-Special-case-shaped-Java-windows.patch

Patch16:       0001-clutter-clone-Unset-source-when-source-actor-is-dest.patch

Patch17:       0001-stack-tracker-Keep-override-redirect-windows-on-top.patch

Patch18:       0001-screen-Remove-stray-assert.patch

Patch19:       Tweak-disable-this-window-is-unresponsive.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=733277
Patch20: 0008-Add-support-for-quad-buffer-stereo.patch
Patch21: 0001-build-Lower-automake-requirement.patch

BuildRequires: chrpath
BuildRequires: pango-devel
BuildRequires: startup-notification-devel
BuildRequires: gnome-desktop3-devel
BuildRequires: gtk3-devel >= %{gtk3_version}
BuildRequires: pkgconfig
BuildRequires: gobject-introspection-devel >= 1.41.0
BuildRequires: libSM-devel
BuildRequires: libX11-devel
BuildRequires: libXdamage-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libXi-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libXcursor-devel
BuildRequires: libXcomposite-devel
BuildRequires: libxcb-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libxkbfile-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: pam-devel
BuildRequires: upower-devel
BuildRequires: xkeyboard-config-devel
BuildRequires: zenity
BuildRequires: desktop-file-utils
# Bootstrap requirements
BuildRequires: gtk-doc gnome-common gettext-devel
BuildRequires: libcanberra-devel
BuildRequires: gsettings-desktop-schemas-devel >= %{gsettings_desktop_schemas_version}
BuildRequires: automake, autoconf, libtool

BuildRequires: json-glib-devel >= %{json_glib_version}
BuildRequires: libgudev1-devel

Obsoletes: mutter-wayland < 3.13.0
Obsoletes: mutter-wayland-devel < 3.13.0

# Make sure yum updates gnome-shell as well; otherwise we might end up with
# broken gnome-shell installations due to mutter ABI changes.
Conflicts: gnome-shell < 3.21.1

Requires: control-center-filesystem
Requires: gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: startup-notification
Requires: dbus-x11
Requires: zenity

Requires:      json-glib%{?_isa} >= %{json_glib_version}

%description
Mutter is a window and compositing manager that displays and manages
your desktop via OpenGL. Mutter combines a sophisticated display engine
using the Clutter toolkit with solid window-management logic inherited
from the Metacity window manager.

While Mutter can be used stand-alone, it is primarily intended to be
used as the display core of a larger system such as GNOME Shell. For
this reason, Mutter is very extensible via plugins, which are used both
to add fancy visual effects and to rework the window management
behaviors to meet the needs of the environment.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for developing Mutter plugins. Also includes
utilities for testing Metacity/Mutter themes.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1 -b .deal-with-oversized-windows
%patch5 -p1 -b .support-headless-mode
%patch6 -p1 -b .workaround-xvnc-spurious-hotplugs
%patch7 -p1 -b .force-randr-update-on-resume
%patch8 -p1 -b .support-external-monitor-layout
%patch9 -p1 -b .threaded-swap-wait
%patch10 -p1 -b .dont-move-sloppy-focus-with-button-pressed
%patch11 -p1 -b .synaptics-touchpad-configuration
%patch12 -p1 -b .fix-segfault-on-early-exit
%patch13 -p1 -b .bgra-buffer-swizzling
%patch14 -p1 -b .fix-cally-screen-coordinates
%patch15 -p1 -b .special-case-shaped-java-windows
%patch16 -p1 -b .unset-source-when-actor-is-destroyed
%patch17 -p1 -b .keep-OR-windows-on-top
%patch18 -p1 -b .drop-stray-assert
%patch19 -p2 -b .disable-this-window-is-unresponsive
%patch20 -p1 -b .quad-buffer-stereo
%patch21 -p1 -b .lower-automake-requirement

%build
autoreconf
(if ! test -x configure; then NOCONFIGURE=1 ./autogen.sh; fi;
 %configure --disable-static --enable-compile-warnings=maximum --disable-wayland-egl-server)

SHOULD_HAVE_DEFINED="HAVE_SM HAVE_RANDR HAVE_STARTUP_NOTIFICATION"

for I in $SHOULD_HAVE_DEFINED; do
  if ! grep -q "define $I" config.h; then
    echo "$I was not defined in config.h"
    grep "$I" config.h
    exit 1
  else
    echo "$I was defined as it should have been"
    grep "$I" config.h
  fi
done

make %{?_smp_mflags} V=1

%install
%make_install

#Remove libtool archives.
rm -rf %{buildroot}/%{_libdir}/*.la

%find_lang %{name}

# Mutter contains a .desktop file so we just need to validate it
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post -p /sbin/ldconfig

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%license COPYING
%doc NEWS
%{_bindir}/mutter
%{_datadir}/applications/*.desktop
%{_libdir}/lib*.so.*
%{_libdir}/mutter/
%{_libexecdir}/mutter-restart-helper
%{_datadir}/GConf/gsettings/mutter-schemas.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.wayland.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-*.xml
%{_mandir}/man1/mutter.1*

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%changelog
* Mon Jun 26 2017 Florian Müllner <fmuellner@redhat.com> - 3.24.3-11
- Prevent crash when removing workspace with on-all-workspaces windows
  present (like desktop icons)
- Resolves: #1453065

* Wed Jun 14 2017 Florian Müllner <fmuellner@redhat.com> - 3.24.3-10
- Keep OR windows stacked on top
- Resolves: #1437203

* Thu Jun 08 2017 Florian Müllner <fmuellner@redhat.com> - 3.24.3-9
- Fix crash when a window closes during Alt+Tab
- Resolves: #1438722

* Tue May 16 2017 Florian Müllner <fmuellner@redhat.com> - 3.24.3-8
- Special-case shaped java windows to fix OpenJDK's compliance test
- Resolves: #1363784

* Fri Apr 28 2017 Florian Müllner <fmuellner@redhat.com> - 3.24.3-7
- Fix cally translation of screen coordinates
- Resolves: #1439194

* Fri Mar 17 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-6
- Recreate build files after modifying templates with the last patch
- Resolves: #1387025

* Thu Mar 16 2017 Owen Taylor <otaylor@redhat.com> - 3.22.3-6
- Add back quad-buffer stereo patches, rebased to 3.22
- Resolves: #1387025

* Wed Mar 15 2017 Carlos Garnacho <cgarnach@redhat.com> - 3.22.3-5
- Swizzle BGRA buffers to avoid pixel conversions
- Resolves: #1387025

* Tue Mar 14 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-4
- Don't segfault on early exit
- Resolves: #1369073

* Mon Mar 13 2017 Carlos Garnacho <cgarnach@redhat.com> - 3.22.3-3
- Handle synaptics settings
- Resolves: #1387025

* Mon Mar 13 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-2
- Re-add downstream patches
- Resolves: #1387025

* Thu Feb 16 2017 Kalev Lember <klember@redhat.com> - 3.22.3-1
- Update to 3.22.3
- Resolves: #1387025

* Fri Feb 03 2017 Kalev Lember <klember@redhat.com> - 3.22.2-1
- Update to 3.22.2
- Resolves: #1387025

* Fri Sep 16 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-31
- Make meta_window_actor_update_visibility() public
  Related: #1306670

* Mon Aug 29 2016 Owen Taylor <otaylor@redhat.com - 3.14.4-30
- Make Mutter exit cleanly when opening $DISPLAY fails
  Resolves: #1346814

* Mon Aug 15 2016 Rui Matos <rmatos@redhat.com> - 3.14.4-29
- Allow clutter to fallback to the classic gl driver since mesa's
  software driver doesn't support gl3
  Related: #1361251

* Thu Aug 11 2016 Rui Matos <rmatos@redhat.com> - 3.14.4-28
- Add patch to require clutter to use the gl3 driver
  Resolves: #1361251

* Mon Jul 18 2016 Rui Matos <rmatos@redhat.com> - 3.14.4-27
- Require a clutter version that provides all the new APIs
  Related: rhbz#1330488

* Thu Jun 30 2016 Owen Taylor <otaylor@redhat.com> - 3.14.4-26
- Turn on newly added "threaded swap wait" functionality in Cogl
  so that on NVIDIA cards, frame completion is handled in a proper
  non-blocking fashion, fixing bugs with idles not running when
  they should.
  Resolves: #1305076

* Wed Jun 29 2016 Rui Matos <rmatos@redhat.com> - 3.14.4-25
- Handle video memory purge errors
  Resolves: #1330488

* Tue Jun 28 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-24
- Update translations
  Resolves: #1304233

* Fri Jun 17 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-23
- Track ignored damage
  Resolves: #1165840

* Thu May 19 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-22
- Support external monitor layout configuration
  Related: #1290448

* Thu May 12 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-21
- Ignore window groups for stacking
  Resolves: #1167889

* Tue May 10 2016 Owen Taylor <otaylor@redhat.com> - 3.14.4-20
- Rebase and add back stereo support patch that was dropped in
  update to 3.14.
- Retain the last active window for seamless restarts.
  Resolves: #1305076

* Thu Apr 21 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-19
- Make Cogl errors non-fatal
  Related: #1326372

* Wed Apr 20 2016 Carlos Garnacho <cgarnach@redhat.com> - 3.14.4-18
- Fix unredirected windows being transparent to input in sloppy focus
  Resolves: #1299616

* Mon Oct 26 2015 Rui Matos <rmatos@redhat.com> - 3.14.4-17
- Fix a crash when plugging monitors
  Resolves: #1275215
- Avoid a critical message when unplugging monitors
  Resolves: #1275220
- Fix monitors remaining undetected on resume from suspend
  Resolves: #1219476

* Fri Oct 16 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-16
- Fix crash during session saving when saving sticky windows
  Related: #1272106

* Tue Oct  6 2015 Rui Matos <rmatos@redhat.com> - 3.14.4-15
- Fix integer sign oversight in the previous patch
  Related: #1265511

* Tue Oct  6 2015 Rui Matos <rmatos@redhat.com> - 3.14.4-14
- Add a couple of fixes for Xvnc resolution changes
  Resolves: #1265511

* Thu Oct 01 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-13
- Fix a couple more errors in headless mode
  Related: #1212702

* Fri Sep 04 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-12
- Fix maximum potential number of monitors
  Resolves: #1260082

* Thu Sep 03 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-11
- Fix screen flicking issue with propriertary NVidia drivers
  Resolves: #1258842

* Thu Jul 30 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-10
- Fix placement of fullscreen windows
  Resolves: #1247718

* Fri Jul 24 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-9
- Fix some more headless-mode warnings
  Related: #1212702

* Fri Jul 24 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-8
- Fix focus_serial overflow
  Resolves: #1236113

* Tue Jul 21 2015 Matthias Clasen <mclasen@redhat.com> - 3.14.4-7
- Fix coverity spotted bugs
  Related #1174722

* Fri Jul 17 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-6
- Fix oversight in headless-mode backport
  Resolves: #1212702

* Thu Jul 16 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-5
- Support headless mode
  Resolves: #1212702

* Fri Jul 10 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-4
- Don't try to focus hidden windows
  Related: #1174722

* Thu May 21 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-3
- support suggested output position
  Resolves: rhbz#1166319

* Wed May 06 2015 Ray Strode <rstrode@redhat.com> 3.14.4-2
- rebuild against new gnome-desktop3
  Related: #1174722

* Tue Mar 24 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-1
- Drop obsolete patches, rebase still relevant one

* Mon Mar 23 2015 Richard Hughes <rhughes@redhat.com> - 3.14.3-1
- Update to 3.14.3
- Resolves: #1174722

* Wed Jan 14 2015 Florian Müllner <fmuellner@redhat.com> - 3.8.4.16
- Fix window placement regression
  Resolves: rhbz#1153641

* Thu Nov 13 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-15
- Fix delayed mouse mode
  Resolves: rhbz#1149585

* Thu Oct 09 2014 Florian Müllner <fmueller@redhat.com> - 3.8.4-14
- Preserve window placement on monitor changes
  Resolves: rhbz#1126754

* Thu Oct 09 2014 Florian Müllner <fmueller@redhat.com> - 3.8.4-13
- Improve handling of vertical monitor layouts
  Resolves: rhbz#1108322

* Thu Jul 17 2014 Owen Taylor <otaylor@redhat.com> 3.8.4-13
- Add patches for quadbuffer stereo suppport
  Fix a bad performance problem drawing window thumbnails
  Resolves: rhbz#861507

* Tue Mar 11 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-10
- Fix crash when encountering over-sized windows
  Resolves: #1027832

* Tue Mar 11 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-10
- Backport another minor memory leak fix
  Resolves: #1067456

* Tue Mar 11 2014 Debarshi Ray <rishi@fedoraproject.org> - 3.8.4-9
- Do not save pixbuf in user data
  Resolves: #1067456

* Wed Feb 12 2014 Carlos Garnacho <cgarnach@redhat.com> - 3.8.4-8
- Fix window dragging on touchscreens
  Resolves: #1051006

* Tue Feb 11 2014 Owen Taylor <otaylor@redhat.com> - 3.8.4-7
- Add an upstream patch that fixes a bug with left-over window
  shadows that show up when we add patches to Clutter to stop
  redrawing the entire screen on every window move.
  Resolves: rhbz#1063984

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.8.4-6
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.4-5
- Mass rebuild 2013-12-27

* Thu Nov 28 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.4-4
- Include translation updates
  Resolves: rhbz#1030369

* Mon Nov 11 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.4-3
- Backport allowing sliced textures for large backgrounds
  Resolves: rhbz#1028586

* Thu Oct 31 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.4-2
- Backport performance improvements for software rendering from 3.10

* Tue Jul 30 2013 Ray Strode <rstrode@redhat.com> 3.8.4-1
- Update to 3.8.4

* Tue Jul 02 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.3-2
- Rebuild with (re-)fixed download URL

* Fri Jun 07 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.3-1
- Update to 3.8.3

* Tue May 14 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Tue Apr 16 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Mon Mar 04 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Wed Feb 20 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.90-1
- Update to 3.7.90

* Tue Feb 05 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.5-1
- Update to 3.7.5

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 3.7.4-2
- Rebuild for new cogl

* Tue Jan 15 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.4-1
- Update to 3.7.4

* Tue Dec 18 2012 Florian Müllner <fmuellner@redhat.com> - 3.7.3-1
- Update to 3.7.3

* Mon Nov 19 2012 Florian Müllner <fmuellner@redhat.com> - 3.7.2-1
- Update to 3.7.2

* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Mon Oct 15 2012 Florian Müllner <fmuellner@redhat.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Florian Müllner <fmuellner@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Florian Müllner <fmuellner@redhat.com> - 3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.91-2
- Rebuild against new cogl

* Tue Sep 04 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 28 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.90-2
- Rebuild against new cogl/clutter

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Tue Aug 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.5-1
- Update to 3.5.5

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 3.5.4-1
- Update to 3.5.4

* Tue Jun 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.3-1
- Update to 3.5.3

* Fri Jun  8 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.2-3
- Make resize grip area larger

* Thu Jun 07 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.2-2
- Don't check for Xinerama anymore - it is now mandatory

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.2-1
- Update to 3.5.2
- Remove upstreamed patches

* Wed May 09 2012 Adam Jackson <ajax@redhat.com> 3.4.1-3
- mutter-never-slice-shape-mask.patch, mutter-use-cogl-texrect-api.patch:
  Fix window texturing on hardware without ARB_texture_non_power_of_two
  (#813648)

* Wed Apr 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-2
- Silence glib-compile-schemas scriplets

* Wed Apr 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-1
- Update to 3.4.1
- Conflict with gnome-shell versions older than 3.4.1

* Tue Mar 27 2012 Richard Hughes <hughsient@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92

* Sat Mar 10 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.90-2
- Rebuild against new cogl

* Sat Feb 25 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.90-1
- Update to 3.3.90

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.5-1
- Update to 3.3.5

* Fri Jan 20 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.4-1
- Update to 3.3.4

* Thu Jan 19 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.3-2
- Rebuild against new cogl

* Thu Jan  5 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Wed Nov 23 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.2-2
- Rebuild against new clutter

* Tue Nov 22 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.2-1
- Update to 3.3.2

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for glibc bug#747377

* Wed Oct 19 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Mon Sep 26 2011 Owen Taylor <otaylor@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.92-1
- Update to 3.1.92

* Wed Sep 14 2011 Owen Taylor <otaylor@redhat.com> - 3.1.91.1-1
- Update to 3.1.91.1

* Wed Aug 31 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.90.1-1
- Update to 3.1.90.1

* Wed Jul 27 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.4-1
- Update to 3.1.4

* Wed Jul 27 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.3.1-3
- Rebuild

* Mon Jul  4 2011 Peter Robinson <pbrobinson@gmail.com> - 3.1.3.1-2
- rebuild against new clutter/cogl

* Mon Jul 04 2011 Adam Williamson <awilliam@redhat.com> - 3.1.3.1-1
- Update to 3.1.3.1

* Thu Jun 30 2011 Owen Taylor <otaylor@redhat.com> - 3.1.3-1
- Update to 3.1.3

* Wed May 25 2011 Owen Taylor <otaylor@redhat.com> - 3.0.2.1-1
- Update to 3.0.2.1

* Fri Apr 29 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.1-3
- Actually apply the patch for #700276

* Thu Apr 28 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.1-2
- Make session saving of gnome-shell work

* Mon Apr 25 2011 Owen Taylor <otaylor@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Mon Apr  4 2011 Owen Taylor <otaylor@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Mon Mar 28 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.93-1
- Update to 2.91.93

* Wed Mar 23 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.92-1
- Update to 2.91.92

* Mon Mar  7 2011 Owen Taylor <otaylor@redhat.com> - 2.91.91-1
- Update to 2.91.91

* Tue Mar  1 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-2
- Build against libcanberra, to enable AccessX feedback features

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-1
- Update to 2.91.90

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.6-4
- Rebuild against newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.6-2
- Rebuild against newer gtk

* Tue Feb  1 2011 Owen Taylor <otaylor@redhat.com> - 2.91.6-1
- Update to 2.91.6

* Tue Jan 11 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.5-1
- Update to 2.91.5

* Fri Jan  7 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.4-1
- Update to 2.91.4

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.3-2
- Rebuild against new gtk
- Drop no longer needed %%clean etc

* Mon Nov 29 2010 Owen Taylor <otaylor@redhat.com> - 2.91.3-1
- Update to 2.91.3

* Tue Nov  9 2010 Owen Taylor <otaylor@redhat.com> - 2.91.2-1
- Update to 2.91.2

* Tue Nov  2 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.1-2
- Rebuild against newer gtk3

* Fri Oct 29 2010 Owen Taylor <otaylor@redhat.com> - 2.91.1-1
- Update to 2.91.1

* Mon Oct  4 2010 Owen Taylor <otaylor@redhat.com> - 2.91.0-1
- Update to 2.91.0

* Wed Sep 22 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.5-4
- Rebuild against newer gobject-introspection

* Wed Jul 14 2010 Colin Walters <walters@verbum.org> - 2.31.5-3
- Rebuild for new gobject-introspection

* Tue Jul 13 2010 Adel Gadllah <adel.gadllah@gmail.com> - 2.31.5-2
- Build against gtk3

* Mon Jul 12 2010 Colin Walters <walters@pocket> - 2.31.5-1
- New upstream version

* Mon Jul 12 2010 Colin Walters <walters@verbum.org> - 2.31.2-5
- Rebuild against new gobject-introspection

* Tue Jul  6 2010 Colin Walters <walters@verbum.org> - 2.31.2-4
- Changes to support snapshot builds

* Fri Jun 25 2010 Colin Walters <walters@megatron> - 2.31.2-3
- drop gir-repository-devel dep

* Wed May 26 2010 Adam Miller <maxamillion@fedoraproject.org> - 2.31.2-2
- removed "--with-clutter" as configure is claiming it to be an unknown option

* Wed May 26 2010 Adam Miller <maxamillion@fedoraproject.org> - 2.31.2-1
- New upstream 2.31.2 release

* Thu Mar 25 2010 Peter Robinson <pbrobinson@gmail.com> 2.29.1-1
- New upstream 2.29.1 release

* Wed Mar 17 2010 Peter Robinson <pbrobinson@gmail.com> 2.29.0-1
- New upstream 2.29.0 release

* Tue Feb 16 2010 Adam Jackson <ajax@redhat.com> 2.28.1-0.2
- mutter-2.28.1-add-needed.patch: Fix FTBFS from --no-add-needed

* Thu Feb  4 2010 Peter Robinson <pbrobinson@gmail.com> 2.28.1-0.1
- Move to git snapshot

* Wed Oct  7 2009 Owen Taylor <otaylor@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Tue Sep 15 2009 Owen Taylor <otaylor@redhat.com> - 2.27.5-1
- Update to 2.27.5

* Fri Sep  4 2009 Owen Taylor <otaylor@redhat.com> - 2.27.4-1
- Remove workaround for #520209
- Update to 2.27.4

* Sat Aug 29 2009 Owen Taylor <otaylor@redhat.com> - 2.27.3-3
- Fix %%preun GConf script to properly be for package removal

* Fri Aug 28 2009 Owen Taylor <otaylor@redhat.com> - 2.27.3-2
- Add a workaround for Red Hat bug #520209

* Fri Aug 28 2009 Owen Taylor <otaylor@redhat.com> - 2.27.3-1
- Update to 2.27.3, remove mutter-metawindow.patch

* Fri Aug 21 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.2-2
- Add upstream patch needed by latest mutter-moblin

* Tue Aug 11 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.2-1
- New upstream 2.27.2 release. Drop upstreamed patches.

* Wed Jul 29 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.1-5
- Add upstream patches for clutter 1.0

* Wed Jul 29 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.1-4
- Add patch to fix mutter --replace

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.1-2
- Updates from review request

* Fri Jul 17 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.1-1
- Update to official 2.27.1 and review updates

* Thu Jun 18 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.0-0.2
- Updates from initial reviews

* Thu Jun 18 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.0-0.1
- Initial packaging
