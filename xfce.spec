#
# TODO:
# - xfsamba needs an icon.
#
%define		_xfsamba_ver	0.33.2

Summary:	A Powerfull X Environment, with Toolbar and Window Manager
Summary(es):	Un ambiente X poderoso, con una barra de tareas y un administrador de ventanas
Summary(pl):	¶rodowisko dla X z paskiem narzÍdzi i menedøerem okien
Summary(pt_BR):	Um ambiente X poderoso, com uma barra de tarefas e um gerenciador de janelas
Summary(ru):	Û“≈ƒ¡ “¡¬œﬁ≈«œ ”‘œÃ¡ XFCE
Summary(uk):	Û≈“≈ƒœ◊…›≈ “œ¬œﬁœ«œ ”‘œÃ’ XFCE
Name:		xfce
Version:	3.8.16
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/xfce/%{name}-%{version}.tar.gz
Source1:	xfsamba.desktop
URL:		http://www.xfce.org/
Requires:	imlib-cfgeditor
Requires:	gtk-theme-xfce
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfigdir	/etc

%description
XFce is an easy-to-use and easy-to-configure environment using the
popular GTK+ toolkit for X11, featuring drag'n drop, pulldown menus
and color icons, 3D widgets, etc. It features its own Window Manager
(xfwm), a backdrop manager (xfbd), a file manager (xftree), a
clock/calendar (xfclock) and a system sound manager (xfsound) and a
user friendly interface for mouse configuration (xfmouse).

%description -l es
XFce es un ambiente de trabajo simple, que ocupa poca memoria, r·pido
y poderoso para Linux y varios tipos de Unix.

%description -l pl
XFce jest niewielkim, ale posiadaj±cym duøe moøliwo∂ci ∂rodowiskiem
dla Linuxa i innych odmian UNIXa. XFce posiada w≥asy pasek narzÍdzi
oraz menedøer okien. Zawiera wiele w≥asnych uøytecznych narzÍdzi:
xfbd, xftree, xfclock, xfsound, xfmouse...

%description -l pt_BR
O XFce È um ambiente de trabalho leve e poderoso para o Linux e v·rios
outros tipos de Unix.

%description -l ru
Û“≈ƒ¡ “¡¬œﬁ≈«œ ”‘œÃ¡ œ”Œœ◊¡ŒŒ¡— Œ¡ gtk+ … Œ¡–œÕ…Œ¡¿›¡— CDE.

%description -l uk
Û≈“≈ƒœ◊…›≈ “œ¬œﬁœ«œ ”‘œÃ’, ›œ ¬¡⁄’§‘ÿ”— Œ¡ gtk+ ‘¡ Œ¡«¡ƒ’§ CDE.

%package -n gtk-theme-xfce
Summary:	Xfce gtk+ theme
Summary(pl):	Temat do gtk+ dla xfce
Group:		Themes/Gtk

%description -n gtk-theme-xfce
Xfce Gtk+ engine theme.

%description -n gtk-theme-xfce -l pl
Temat do gtk+ dla xfce.

%package -n xfsamba
Summary:	Xfsamba - SMB network navigator without mounting
Summary(pl):	Xfsamba - przegl±danie zasobÛw SMB bez mountowania ich
Version:	%{_xfsamba_ver}
Epoch:		1
Group:		X11/Applications/Networking
Requires:	samba-client

%description -n xfsamba
Xfsamba is an SMB network navigator with downloading, uploading and
browsing. It does not mount remote SMB shares any time.

%description -n xfsamba -l pl
Xfsamba jest programem do przegl±dania zasobÛw udostÍpnianych przez
SMB. Jednak, w przeciwieÒstwie do wiÍkszo∂ci tego typu programÛw, jest
to robione poprzez smbclient'a. DziÍki temu moøemy "szperaÊ" w sieci
lokalnej bez uøywania smbmount.

%prep
%setup -q


%build
%configure2_13 \
	--disable-dt \
	--enable-gdk-pixbuf \
	--disable-imlib \
	--enable-xinerama

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

gzip -9nf README* AUTHORS TODO NEWS ChangeLog

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
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
%attr(755,root,root) %{_bindir}/xfsound
%attr(755,root,root) %{_bindir}/xfterm
%attr(755,root,root) %{_bindir}/xftrash
%attr(755,root,root) %{_bindir}/xftree
%attr(755,root,root) %{_bindir}/xfumed
%attr(755,root,root) %{_bindir}/xfwm
%attr(644,root,root) %{_mandir}/man*/*
%{_datadir}/xfce
%dir %{_sysconfigdir}/xfce
%attr(644,root,root) %{_sysconfigdir}/xfce/*

%files -n gtk-theme-xfce
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk/themes/engines/*

%files -n xfsamba
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xfsamba
%{_applnkdir}/Network/Misc/*
