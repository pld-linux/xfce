Summary:	A Powerfull X Environment, with Toolbar and Window Manager
Name:		xfce
Version:	3.1.2
Release:	1
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source:		%{name}-%{version}.tar.gz
Patch:		%{name}-DESTDIR.patch
URL:		http://www.xfce.org
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XFce is a lightweight and powerfull desktop environment for Linux and
various UNIX flavour.

%prep
%setup -q
%patch -p1
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure \
     --disable-dt

%build
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README INSTALL ChangeLog $RPM_BUILD_ROOT%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,INSTALL,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.gz
%{_datadir}/XFCE
