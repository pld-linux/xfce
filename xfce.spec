Summary:	A Powerfull X Environment, with Toolbar and Window Manager
Name:		xfce
Version:	3.3.3
Release:	1
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source:		http://www.xfce.org/archive/%{name}-%{version}.tar.gz
URL:		http://www.xfce.org
Requires:	imlib_cfgeditor
BuildRequires:	gettext-devel
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel
BuildRequires:	xpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XFce is a lightweight and powerfull desktop environment for Linux and
various UNIX flavour.

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure \
     --disable-dt

make

%install
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README* INSTALL AUTHORS COPYING TODO NEWS ChangeLog \
	$RPM_BUILD_ROOT%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
%{_datadir}/xfce
