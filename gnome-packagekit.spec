Summary:	A PackageKit client for the GNOME desktop
Name:	  	gnome-packagekit
Version:	2.31.6
Release:	%mkrel 2
License:	GPLv2+
Group:		System/Configuration/Packaging
Source0: 	http://ftp.gnome.org/pub/GNOME/sources/gnome-packagekit/%name-%version.tar.bz2
# (fc) 2.30.1-2mdv disable font install support
Patch0:		gnome-packagekit-2.30.1-disable-font-install.patch
URL:		http://www.packagekit.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	packagekit-devel >= 0.6.1
BuildRequires:	libnotify-devel >= 0.4.3
BuildRequires:	gnome-menus-devel >= 2.24.1
BuildRequires:	intltool > 0.35.0
BuildRequires:	gnome-doc-utils
BuildRequires:	docbook-utils
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	libGConf2-devel >= 0.22
BuildRequires:	libxslt-proc
BuildRequires:	unique-devel >= 0.9.4
BuildRequires:	libcanberra-devel >= 0.10
%if %mdkversion > 201000
BuildRequires:	UPower-devel
%else
BuildRequires:	devicekit-power-devel >= 007
%endif
BuildRequires:	libgudev-devel
Requires: %{name}-common = %{version}-%{release}

%description
gnome-packagekit are PackageKit client programs designed for the GNOME desktop.

%package common
Summary:        Common files and services for GNOME PackageKit
Group:          System/Configuration/Packaging
Requires:	packagekit >= 0.4.8
Provides:	packagekit-gui
Conflicts:	gnome-packagekit < 2.29.2
Conflicts:	kpackagekit

%description common
Common files and services used by GNOME PackageKit. This packages provides
D-Bus service for packages installation.

%package extra
Summary: Session applications to manage packages with GNOME PackageKit (extra bits)
Group:          System/Configuration/Packaging
Requires: %{name} = %{version}-%{release}
Conflicts:	gnome-packagekit < 2.29.2

%description extra
Extra GNOME applications for using PackageKit that are not normally needed.

%prep
%setup -q
%patch0 -p1 -b .disable-font-install

# .deb can't be installed in Mandriva
sed -i 's,application/x-deb;,,' data/gpk-install-file.desktop.in

%build
%configure2_5x --disable-static --disable-schemas-install --disable-scrollkeeper
make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %name --with-gnome

%clean
rm -rf %{buildroot}

%preun
%preun_uninstall_gconf_schemas %name

%files common -f %name.lang
%defattr(-, root, root)
%{_sysconfdir}/gconf/schemas/%name.schemas
%{_bindir}/gpk-install-*
%{_bindir}/gpk-dbus-service
%dir %{_datadir}/gnome-packagekit
%{_datadir}/gnome-packagekit/gpk-client.ui
%{_datadir}/gnome-packagekit/gpk-error.ui
%{_datadir}/gnome-packagekit/gpk-eula.ui
%{_datadir}/gnome-packagekit/gpk-update-viewer.ui
%{_datadir}/gnome-packagekit/gpk-signature.ui
%{_datadir}/gnome-packagekit/icons
%{_datadir}/omf/%name
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/gpk-install-*
%{_mandir}/man1/gpk-backend-status*
%{_datadir}/dbus-1/services/*.service
%{_datadir}/applications/gpk-install-*.desktop

%files 
%defattr(-, root, root)
%{_bindir}/gpk-application
%{_bindir}/gpk-log
%{_bindir}/gpk-prefs
%{_bindir}/gpk-repo
%{_bindir}/gpk-update-*
%{_datadir}/applications/gpk-application.desktop
%{_datadir}/applications/gpk-prefs.desktop
%{_datadir}/applications/gpk-update-viewer.desktop
%{python_sitelib}/packagekit/g*
%{_datadir}/gnome/autostart/gpk-update-icon.desktop
%{_mandir}/man1/gpk-application*
%{_mandir}/man1/gpk-prefs*
%{_mandir}/man1/gpk-repo*
%{_mandir}/man1/gpk-update*
%{_datadir}/gnome-packagekit/gpk-application.ui
%{_datadir}/gnome-packagekit/gpk-prefs.ui
%{_datadir}/gnome-packagekit/gpk-repo.ui
%{_datadir}/gnome-packagekit/gpk-update-viewer.ui
%{_datadir}/gnome-packagekit/gpk-log.ui

%files extra
%defattr(-, root, root)
%{_bindir}/gpk-backend-status
%{_bindir}/gpk-service-pack
%{_datadir}/applications/gpk-log.desktop
%{_datadir}/applications/gpk-repo.desktop
%{_datadir}/applications/gpk-service-pack.desktop
%{_datadir}/gnome-packagekit/gpk-backend-status.ui
%{_datadir}/gnome-packagekit/gpk-service-pack.ui
