Summary:	A PackageKit client for the GNOME desktop
Name:	  	gnome-packagekit
Version:	0.2.3
Release:	%mkrel 2
License:	GPLv2+
Group:		System/Configuration/Packaging
Source0: 	http://www.packagekit.org/releases/%name-%version.tar.gz
URL:		http://www.packagekit.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	packagekit-devel
BuildRequires:	policykit-gnome-devel
BuildRequires:	libsexy-devel
BuildRequires:	libnotify-devel
BuildRequires:	libglade2-devel
BuildRequires:	intltool
BuildRequires:	gnome-doc-utils
BuildRequires:	libGConf2-devel
BuildRequires:	libxslt-proc
Requires:	packagekit

%description
gnome-packagekit are PackageKit client programs designed for the GNOME desktop.

%prep
%setup -q
sed -i -e 's#system-software-installer#system-software-install#' data/*.desktop.in

%build
%configure2_5x --disable-static --disable-schemas-install --disable-scrollkeeper
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-, root, root)
%{_sysconfdir}/gconf/schemas/%name.schemas
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/gnome/autostart/gpk-update-icon.desktop
%{_datadir}/applications/*.desktop
%{_datadir}/omf/%name
%{_iconsdir}/hicolor/*/*/*
