Summary:	A professional slideshow creator
Summary(pl.UTF-8):	Profesjonalne narzędzie do tworzenia slajdów
Name:		ephoto
Version:	1.6.0
Release:	1
License:	BSD
Group:		Applications/Multimedia
Source0:	https://download.enlightenment.org/rel/apps/ephoto/%{name}-%{version}.tar.xz
# Source0-md5:	d855bcd9fadbd315e5fb2ea19b594b61
URL:		http://trac.enlightenment.org/e/wiki/Ephoto
BuildRequires:	efl-devel
BuildRequires:	libexif-devel
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ephoto is a professional slideshow creator with audio support.

%description -l pl.UTF-8
Ephoto to profesjonalne narzędzie do tworzenia slajdów z obsługą
dźwięku.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%meson_install

%{__mv} $RPM_BUILD_ROOT{%{_iconsdir},%{_pixmapsdir}}/ephoto.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING* README TODO
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/ephoto
%attr(755,root,root) %{_libdir}/ephoto/ephoto_thumbnail
%{_datadir}/%{name}
%{_desktopdir}/ephoto.desktop
%{_pixmapsdir}/ephoto.png
