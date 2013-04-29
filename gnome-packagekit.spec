%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	A PackageKit client for the GNOME desktop
Name:	  	gnome-packagekit
Version:	3.6.1
Release:	2
License:	GPLv2+
Group:		System/Configuration/Packaging
Url:		http://www.packagekit.org
Source0: 	http://ftp.gnome.org/pub/GNOME/sources/gnome-packagekit/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	desktop-file-utils
BuildRequires:	intltool > 0.35.0
BuildRequires:	itstool
BuildRequires:	xsltproc
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

%description	common
Common files and services used by GNOME PackageKit. This packages provides
D-Bus service for packages installation.

%package	extra
Summary:	Session applications to manage packages with GNOME PackageKit (extra bits)
Group:		System/Configuration/Packaging
Requires:	%{name} = %{EVRD}

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

