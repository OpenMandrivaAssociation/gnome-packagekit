Summary:	A PackageKit client for the GNOME desktop
Name:	  	gnome-packagekit
Version:	2.29.1
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Configuration/Packaging
Source0: 	http://ftp.gnome.org/pub/GNOME/sources/gnome-packagekit/2.28/%name-%version.tar.bz2
URL:		http://www.packagekit.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	packagekit-devel >= 0.5.5
BuildRequires:	libnotify-devel >= 0.4.3
BuildRequires:	gnome-menus-devel >= 2.24.1
BuildRequires:	intltool > 0.35.0
BuildRequires:	gnome-doc-utils
BuildRequires:	docbook-utils
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	libGConf2-devel >= 0.22
BuildRequires:	libxslt-proc
BuildRequires:	unique-devel >= 0.9.4
BuildRequires:	devicekit-power-devel >= 007
BuildRequires:	libcanberra-devel >= 0.10
Requires:	packagekit >= 0.4.8

%description
gnome-packagekit are PackageKit client programs designed for the GNOME desktop.

%prep
%setup -q

%build
%configure2_5x --disable-static --disable-schemas-install --disable-scrollkeeper
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%preun
%preun_uninstall_gconf_schemas %name

%files -f %name.lang
%defattr(-, root, root)
%{_sysconfdir}/gconf/schemas/%name.schemas
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/gnome/autostart/gpk-update-icon.desktop
%{_datadir}/applications/*.desktop
%{python_sitelib}/packagekit/g*
%{_datadir}/omf/%name
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/*
