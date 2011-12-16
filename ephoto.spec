Summary:	A professional slideshow creator
Summary(pl.UTF-8):	Profesjonalne narzędzie do tworzenia slajdów
Name:		ephoto
Version:	0.1.1.55225
Release:	1
License:	BSD
Group:		Applications/Multimedia
Source0:	http://download.enlightenment.org/snapshots/2010-12-03/%{name}-%{version}.tar.bz2
# Source0-md5:	67f2e817716ffc86ba1c653b6177813a
Patch0:		%{name}-elm-update.patch
URL:		http://trac.enlightenment.org/e/wiki/Ephoto
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1.6
BuildRequires:	ecore-file-devel
BuildRequires:	edje
BuildRequires:	edje-devel
BuildRequires:	efreet-devel
BuildRequires:	eio-devel
BuildRequires:	elementary-devel >= 0.8.0
BuildRequires:	ethumb-devel
BuildRequires:	gettext-devel >= 0.12.1
BuildRequires:	libexif-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ephoto is a professional slideshow creator with audio support.

%description -l pl.UTF-8
Ephoto to profesjonalne narzędzie do tworzenia slajdów z obsługą
dźwięku.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
