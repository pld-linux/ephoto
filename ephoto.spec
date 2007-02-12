%define	_snap	20060223
Summary:	A professional slideshow creator
Summary(pl.UTF-8):	Profesjonalne narzędzie do tworzenia slajdów
Name:		ephoto
Version:	0.1
Release:	0.%{_snap}.1
License:	BSD
Group:		Applications/Multimedia
Source0:	http://sparky.homelinux.org/snaps/enli/e17/proto/%{name}-%{_snap}.tar.bz2
# Source0-md5:	a340442715e244243842e500f26480ca
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ewl-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ephoto is a professional slideshow creator with audio support.

%description -l pl.UTF-8
Ephoto to profesjonalne narzędzie do tworzenia slajdów z obsługą
dźwięku.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
