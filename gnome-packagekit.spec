Summary:	A PackageKit client for the GNOME desktop
Name:	  	gnome-packagekit
Version:	3.6.2
Release:	1
License:	GPLv2+
Group:		System/Configuration/Packaging
URL:		http://www.packagekit.org
Source0: 	http://ftp.gnome.org/pub/GNOME/sources/gnome-packagekit/3.6/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	desktop-file-utils
BuildRequires:	intltool > 0.35.0
BuildRequires:	xsltproc itstool
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(packagekit-glib2)
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	pkgconfig(upower-glib)

Requires:	%{name}-common = %{EVRD}

%description
gnome-packagekit are PackageKit client programs designed for the GNOME desktop.

%package	common
Summary:	Common files and services for GNOME PackageKit
Group:		System/Configuration/Packaging
Requires:	packagekit
Provides:	packagekit-gui
Conflicts:	gnome-packagekit < 2.29.2

%description	common
Common files and services used by GNOME PackageKit. This packages provides
D-Bus service for packages installation.

%package	extra
Summary:	Session applications to manage packages with GNOME PackageKit (extra bits)
Group:		System/Configuration/Packaging
Requires:	%{name} = %{EVRD}
Conflicts:	gnome-packagekit < 2.29.2

%description	extra
Extra GNOME applications for using PackageKit that are not normally needed.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--disable-scrollkeeper

%make

%install
%makeinstall_std

# hack around apper conflict
mv %{buildroot}%{_datadir}/dbus-1/services/org.freedesktop.PackageKit.service \
%{buildroot}%{_datadir}/dbus-1/services/gnome-org.freedesktop.PackageKit.service

%find_lang %{name} --with-gnome

%files common -f %{name}.lang
%{_bindir}/gpk-install-*
%{_bindir}/gpk-dbus-service
%{_datadir}/applications/gpk-dbus-service.desktop
%{_datadir}/applications/gpk-install-*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/GConf/gsettings/org.gnome.packagekit.gschema.migrate
%{_datadir}/glib-2.0/schemas/org.gnome.packagekit.gschema.xml
%dir %{_datadir}/gnome-packagekit
%{_datadir}/gnome-packagekit/gpk-client.ui
%{_datadir}/gnome-packagekit/gpk-error.ui
%{_datadir}/gnome-packagekit/gpk-eula.ui
%{_datadir}/gnome-packagekit/gpk-signature.ui
%{_datadir}/gnome-packagekit/icons
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/gpk-install-*
%{_mandir}/man1/gpk-backend-status*

%files 
%{_bindir}/gpk-application
%{_bindir}/gpk-distro-upgrade
%{_bindir}/gpk-log
%{_bindir}/gpk-prefs
%{_bindir}/gpk-update-*
%{_datadir}/applications/gpk-application.desktop
%{_datadir}/applications/gpk-distro-upgrade.desktop
%{_datadir}/applications/gpk-prefs.desktop
%{_datadir}/applications/gpk-update-viewer.desktop
%{_datadir}/gnome-packagekit/gpk-application.ui
%{_datadir}/gnome-packagekit/gpk-prefs.ui
%{_datadir}/gnome-packagekit/gpk-update-viewer.ui
%{_datadir}/gnome-packagekit/gpk-log.ui
%{python_sitelib}/packagekit/g*
%{_mandir}/man1/gpk-application*
%{_mandir}/man1/gpk-prefs*
%{_mandir}/man1/gpk-repo*
%{_mandir}/man1/gpk-update*

%files extra
%{_bindir}/gpk-service-pack
%{_datadir}/applications/gpk-log.desktop
%{_datadir}/applications/gpk-service-pack.desktop
%{_datadir}/gnome-packagekit/gpk-service-pack.ui

%changelog
* Sun Nov 25 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.2-1
- update to 3.6.2

* Mon Oct  8 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Fri Jun 08 2012 Bernhard Rosenkraenzer <bero@bero.eu> 3.4.2-2
+ Revision: 803665
- Rename dbus service file to avoid conflict with apper

* Wed May 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.2-1
+ Revision: 799181
- update to new version 3.4.2

* Thu May 03 2012 Guilherme Moro <guilherme@mandriva.com> 3.4.0-1
+ Revision: 795714
- Updated to version 3.4.0

* Tue Mar 13 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.1-1
+ Revision: 784837
- new version 3.2.1
- cleaned up spec

* Wed Jul 06 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.32.0-5
+ Revision: 688973
- don't disable font install support, the necessary dependencies are generated
  now
- do parallel build
- cleanups
- remove conflicts on kpackagekit
- fix gpk-update-viewer.ui being package in multiple packages

* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 2.32.0-4
+ Revision: 677072
- rebuild to add gconf2 as req

* Thu Apr 07 2011 Funda Wang <fwang@mandriva.org> 2.32.0-3
+ Revision: 651740
- add more BR
- add archlinux patch to make it build with latest libnotify
- rebuild for new libnotify

  + John Balcaen <mikala@mandriva.org>
    - Fix BR for libcanberra-gtk-devel

* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 2.32.0-2mdv2011.0
+ Revision: 592023
- Rebuild

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581672
- new version

* Thu Sep 16 2010 Götz Waschk <waschk@mandriva.org> 2.31.92-1mdv2011.0
+ Revision: 579018
- update to new version 2.31.92

* Wed Sep 01 2010 Emmanuel Andry <eandry@mandriva.org> 2.31.91-1mdv2011.0
+ Revision: 575143
- New version 2.31.91

* Fri Aug 27 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.31.6-2mdv2011.0
+ Revision: 573477
- remove application/x-deb from .desktop file, it can't be installed on Mandriva
  (mdv#60814)

* Tue Aug 17 2010 Emmanuel Andry <eandry@mandriva.org> 2.31.6-1mdv2011.0
+ Revision: 570976
- New version 2.31.6

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.30.3-3mdv2011.0
+ Revision: 564270
- rebuild for perl 5.12.1

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 2.30.3-1mdv2011.0
+ Revision: 561867
- new version 2.30.3

* Fri May 21 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.1-2mdv2010.1
+ Revision: 545647
- Disable font install feature by default

* Tue Apr 27 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.30.1-1mdv2010.1
+ Revision: 539810
- new version 2.30.1

* Thu Apr 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 532876
- New release 2.30.0

* Sun Mar 21 2010 Funda Wang <fwang@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 526160
- finally update BR
- New version 2.29.91

* Tue Feb 02 2010 Funda Wang <fwang@mandriva.org> 2.29.3-1mdv2010.1
+ Revision: 499459
- Bump pk BR
- New version 2.29.3

* Wed Jan 13 2010 Frederic Crozat <fcrozat@mandriva.com> 2.29.2-2mdv2010.1
+ Revision: 490568
- Provides packagekit-gui
- Conflicts with kpackagekit (both are providing GUI dbus service)

* Fri Jan 08 2010 Frederic Crozat <fcrozat@mandriva.com> 2.29.2-1mdv2010.1
+ Revision: 487546
- Release 2.29.2
- split packages in three packages :
 - common for installer D-Bus service
 - main package for main UI
 - extras for non-essential UI

* Wed Dec 09 2009 Funda Wang <fwang@mandriva.org> 2.29.1-1mdv2010.1
+ Revision: 475547
- new version 2.29.1

* Wed Dec 09 2009 Funda Wang <fwang@mandriva.org> 2.28.2-1mdv2010.1
+ Revision: 475353
- new version 2.28.2

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-1mdv2010.0
+ Revision: 458772
- Release 2.28.1

* Tue Sep 22 2009 Funda Wang <fwang@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 447118
- New version 2.28.0

* Sun Aug 09 2009 Funda Wang <fwang@mandriva.org> 2.27.5-1mdv2010.0
+ Revision: 412909
- new version 2.27.5

* Sun Jul 12 2009 Funda Wang <fwang@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 394940
- New version 2.27.3

* Fri Jun 05 2009 Funda Wang <fwang@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 382939
- update BR
- add BR
- New version 2.27.2

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 370465
- New version 2.27.1

* Sun Mar 15 2009 Funda Wang <fwang@mandriva.org> 0.4.5-1mdv2009.1
+ Revision: 355229
- update to new version 0.4.5

* Thu Mar 05 2009 Funda Wang <fwang@mandriva.org> 0.4.4-1mdv2009.1
+ Revision: 349004
- bump BR
- New version 0.4.4

* Tue Feb 03 2009 Funda Wang <fwang@mandriva.org> 0.4.3-2mdv2009.1
+ Revision: 336786
- BR unique

* Tue Feb 03 2009 Funda Wang <fwang@mandriva.org> 0.4.3-1mdv2009.1
+ Revision: 336784
- New version 0.4.3

* Fri Jan 23 2009 Funda Wang <fwang@mandriva.org> 0.4.2-1mdv2009.1
+ Revision: 332699
- new version 0.4.2
- New version 0.4.1

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 0.4.0-2mdv2009.1
+ Revision: 320276
- rebuild for new python

* Sat Dec 13 2008 Funda Wang <fwang@mandriva.org> 0.4.0-1mdv2009.1
+ Revision: 313900
- BR gnome-menu
- New version 0.4.0

* Fri Nov 28 2008 Funda Wang <fwang@mandriva.org> 0.3.11-1mdv2009.1
+ Revision: 307355
- New version 0.3.11

* Wed Nov 12 2008 Funda Wang <fwang@mandriva.org> 0.3.10-1mdv2009.1
+ Revision: 302402
- New version 0.3.10

* Mon Oct 27 2008 Funda Wang <fwang@mandriva.org> 0.3.9-1mdv2009.1
+ Revision: 297551
- New version 0.3.9

* Tue Oct 21 2008 Funda Wang <fwang@mandriva.org> 0.3.8-1mdv2009.1
+ Revision: 296134
- New version 0.3.8

* Thu Oct 16 2008 Funda Wang <fwang@mandriva.org> 0.3.7-1mdv2009.1
+ Revision: 294093
- New version 0.3.7

* Sun Oct 12 2008 Funda Wang <fwang@mandriva.org> 0.3.6-1mdv2009.1
+ Revision: 292864
- New version 0.3.6

* Wed Oct 01 2008 Funda Wang <fwang@mandriva.org> 0.3.5-1mdv2009.0
+ Revision: 290433
- add dtd package
- add preun script
- BR docbook-utils
- New version 0.3.5

* Sun Sep 21 2008 Funda Wang <fwang@mandriva.org> 0.3.3-1mdv2009.0
+ Revision: 286284
- New version 0.3.3

* Wed Sep 10 2008 Funda Wang <fwang@mandriva.org> 0.3.2-1mdv2009.0
+ Revision: 283420
- New version 0.3.2

* Sun Aug 31 2008 Funda Wang <fwang@mandriva.org> 0.3.1-1mdv2009.0
+ Revision: 277771
- New versio 0.3.1

* Thu Aug 07 2008 Funda Wang <fwang@mandriva.org> 0.2.4-2mdv2009.0
+ Revision: 265670
- rebuild for new packagekit

* Wed Aug 06 2008 Funda Wang <fwang@mandriva.org> 0.2.4-1mdv2009.0
+ Revision: 264773
- New version 0.2.4

* Tue Jul 15 2008 Funda Wang <fwang@mandriva.org> 0.2.3-2mdv2009.0
+ Revision: 235756
- fix desktop icon name

* Sun Jul 13 2008 Funda Wang <fwang@mandriva.org> 0.2.3-1mdv2009.0
+ Revision: 234323
- BR glade
- add BR
- import gnome-packagekit


