Summary:	A Powerfull X Environment, with Toolbar and Window Manager
Summary(pl):	¦rodowisko dla X z paskiem narzêdzi i mened¿erem okien
Name:		xfce
Version:	3.4.3
Release:	1
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	http://www.xfce.org/archive/%{name}-%{version}.tar.gz
URL:		http://www.xfce.org/
Requires:	imlib-cfgeditor
BuildRequires:	gettext-devel
BuildRequires:	imlib-devel
BuildRequires:	gtk+-devel
BuildRequires:	xpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfigdir	/etc

%description
XFce is a lightweight and powerfull desktop environment for Linux and
various UNIX flavour. It has it's own toolbar and window manager.

%description -l pl
XFce jest niewielkim, ale posiadaj±cym du¿e mo¿liwo¶ci ¶rodowiskiem
dla Linuxa i innych odmian UNIXa. XFce posiada w³asy pasek na¿êdzi
oraz mened¿er okien.

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure \
	--disable-dt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README* AUTHORS TODO NEWS ChangeLog \
	$RPM_BUILD_ROOT%{_mandir}/*/*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_sysconfigdir}/xfce
%{_mandir}/*/*
%{_datadir}/xfce
