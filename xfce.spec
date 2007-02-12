
%define		_xfsamba_ver	0.34

Summary:	A Powerfull X Environment, with Toolbar and Window Manager
Summary(es.UTF-8):   Un ambiente X poderoso, con una barra de tareas y un administrador de ventanas
Summary(pl.UTF-8):   Środowisko dla X z paskiem narzędzi i zarządcą okien
Summary(pt_BR.UTF-8):   Um ambiente X poderoso, com uma barra de tarefas e um gerenciador de janelas
Summary(ru.UTF-8):   Среда рабочего стола Xfce
Summary(uk.UTF-8):   Середовище робочого столу Xfce
Summary(zh_CN.UTF-8):   Xfce 桌面环境, 带有窗口管理器和工具栏
Name:		xfce
Version:	3.8.18
Release:	7
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	04c197eee32d712a49170539d50279ea
Source1:	xfsamba.desktop
Source2:	xfsamba.png
Source3:	%{name}-xsession.desktop
Patch0:		%{name}-po.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.4
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	libtool
Requires:	gtk-theme-xfce
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfce is an easy-to-use and easy-to-configure environment using the
popular GTK+ toolkit for X11, featuring drag'n drop, pulldown menus
and color icons, 3D widgets, etc. It features its own Window Manager
(xfwm), a backdrop manager (xfbd), a file manager (xftree), a
clock/calendar (xfclock) and a system sound manager (xfsound) and a
user friendly interface for mouse configuration (xfmouse).

%description -l es.UTF-8
Xfce es un ambiente de trabajo simple, que ocupa poca memoria, rápido
y poderoso para Linux y varios tipos de Unix.

%description -l pl.UTF-8
Xfce jest niewielkim, ale posiadającym duże możliwości środowiskiem
dla Linuksa i innych odmian UNIXa. Xfce posiada własny pasek narzędzi
oraz zarządcę okien. Zawiera wiele własnych użytecznych narzędzi:
xfbd, xftree, xfclock, xfsound, xfmouse...

%description -l pt_BR.UTF-8
O Xfce é um ambiente de trabalho leve e poderoso para o Linux e vários
outros tipos de Unix.

%description -l ru.UTF-8
Среда рабочего стола основанная на GTK+ и напоминающая CDE.

%description -l uk.UTF-8
Середовище робочого столу, що базується на GTK+ та нагадує CDE.

%package -n gtk-theme-xfce
Summary:	Xfce GTK+ theme
Summary(pl.UTF-8):   Motyw do GTK+ dla Xfce
Group:		Themes/GTK+

%description -n gtk-theme-xfce
Xfce GTK+ engine theme.

%description -n gtk-theme-xfce -l pl.UTF-8
Motyw do GTK+ dla Xfce.

%package -n xfsamba
Summary:	Xfsamba - SMB network navigator without mounting
Summary(pl.UTF-8):   Xfsamba - przeglądanie zasobów SMB bez mountowania ich
Version:	%{_xfsamba_ver}
Epoch:		1
Group:		X11/Applications/Networking
Requires:	samba-client

%description -n xfsamba
Xfsamba is an SMB network navigator with downloading, uploading and
browsing. It does not mount remote SMB shares any time.

%description -n xfsamba -l pl.UTF-8
Xfsamba jest programem do przeglądania zasobów udostępnianych przez
SMB. Jednak, w przeciwieństwie do większości tego typu programów, jest
to robione poprzez smbclient'a. Dzięki temu możemy "szperać" w sieci
lokalnej bez używania smbmount.

%prep
%setup -q
%patch0 -p1

mv -f po/{sr,sr@Latn}.po
mv -f po/{zh_TW.Big5,zh_TW}.po
# looks like some older copy of zh_CN
rm -f po/zh.po

%{__perl} -pi -e 's/ sr / sr\@Latn /;s/ zh / /;s/zh_TW\.Big5/zh_TW/' configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-dt \
	--disable-static \
	--enable-gdk-pixbuf \
	--disable-imlib \
	--enable-xinerama \
	--enable-gtk-engine=%{_libdir}/gtk/themes/engines

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xsessions,%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README* AUTHORS TODO NEWS ChangeLog
%attr(755,root,root) %{_bindir}/CDE2Xfcepal
%attr(755,root,root) %{_bindir}/glob
%attr(755,root,root) %{_bindir}/startxfce
%attr(755,root,root) %{_bindir}/xfbd
%attr(755,root,root) %{_bindir}/xfbdmgr
%attr(755,root,root) %{_bindir}/xfce
%attr(755,root,root) %{_bindir}/xfce_remove
%attr(755,root,root) %{_bindir}/xfce_setup
%attr(755,root,root) %{_bindir}/xfce_upgrade
%attr(755,root,root) %{_bindir}/xfclock
%attr(755,root,root) %{_bindir}/xfdiff
%attr(755,root,root) %{_bindir}/xfglob
%attr(755,root,root) %{_bindir}/xfgnome
%attr(755,root,root) %{_bindir}/xfhelp
%attr(755,root,root) %{_bindir}/xflock
%attr(755,root,root) %{_bindir}/xfmenu
%attr(755,root,root) %{_bindir}/xfmountdev
%attr(755,root,root) %{_bindir}/xfmouse
%attr(755,root,root) %{_bindir}/xfpager
%attr(755,root,root) %{_bindir}/xfplay
%attr(755,root,root) %{_bindir}/xfprint
%attr(755,root,root) %{_bindir}/xfrun
%attr(755,root,root) %{_bindir}/xfskin
%attr(755,root,root) %{_bindir}/xfsound
%attr(755,root,root) %{_bindir}/xfterm
%attr(755,root,root) %{_bindir}/xftrash
%attr(755,root,root) %{_bindir}/xftree
%attr(755,root,root) %{_bindir}/xfumed
%attr(755,root,root) %{_bindir}/xfwm
%{_mandir}/man*/*
%{_datadir}/xfce
%{_datadir}/xsessions/%{name}.desktop
%dir %{_sysconfdir}/xfce
%{_sysconfdir}/xfce/*

%files -n gtk-theme-xfce
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk/themes/engines/*.so

%files -n xfsamba
%defattr(644,root,root,755)
%doc xfsamba/{README,TODO,ChangeLog}
%attr(755,root,root) %{_bindir}/xfsamba
%{_desktopdir}/xfsamba.desktop
%{_pixmapsdir}/xfsamba.png
