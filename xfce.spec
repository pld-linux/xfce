Summary:	A Powerfull X Environment, with Toolbar and Window Manager
Summary(pl):	¦rodowisko dla X z paskiem narzêdzi i mened¿erem okien
Name:		xfce
Version:	3.6.3
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://www.xfce.org/archive/%{name}-%{version}.tar.gz
URL:		http://www.xfce.org/
Requires:	imlib-cfgeditor
BuildRequires:	gettext-devel
BuildRequires:	imlib-devel
BuildRequires:	gtk+-devel
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

%package -n gtk-theme-xfce
Summary:	Xfce gtk+ theme
Summary(pl):	Temat do gtk+ dla xfce
Group:		Themes/Gtk
Group(de):	Themen/Gtk
Group(pl):	Motywy/Gtk

%description -n gtk-theme-xfce
Xfce Gtk+ engine theme.

%description -l pl -n gtk-theme-xfce
Temat do gtk+ dla xfce.

%prep
%setup -q

%build
gettextize --copy --force
%configure \
	--disable-dt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README* AUTHORS TODO NEWS ChangeLog

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

%files -n gtk-theme-xfce
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk/themes/engines/*
