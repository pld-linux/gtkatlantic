Summary:	Monopoly game client
Summary(pl):	Klient gry Monopol
Name:		gtkatlantic
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://gtkatlantic.gradator.net/downloads/v0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	4695c8bc3c738a696a400b2d6f710291
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://gtkatlantic.gradator.net/
BuildRequires:	gtk+2-devel
BuildRequires:	libpng-devel
BuildRequires:	libxml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkAtlantic is a client for playing Monopoly-like board games on
monopd network.

%description -l pl
GtkAtlantic jest klientem gier planszowych w stylu Monopoly
wykorzystywanym w sieci monopd.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png