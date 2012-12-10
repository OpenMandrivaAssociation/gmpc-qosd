Summary:	A qosd on screen display plugin for gmpc
Name:		gmpc-qosd
Version:	0.15.5.0
Release:	%mkrel 4
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl//q-on-screen-display
Source0:	http://download.sarine.nl/download/gmpc-0.15.5/%{name}-%{version}.tar.bz2
BuildRequires:	libmpd-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	gmpc-devel
Requires:	gmpc

%description
A qosd on screen display plugin for gmpc.

%prep
%setup -q

%build
%configure2_5x

%make

%install
%makeinstall_std

%files
%{_datadir}/gmpc/plugins/qosdplugin.so
