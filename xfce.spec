#
# TODO:	
# - xfsamba needs an icon.
#
%define		_xfsamba_ver	0.28

Summary:	A Powerfull X Environment, with Toolbar and Window Manager
Summary(pl):	¦rodowisko dla X z paskiem narzêdzi i mened¿erem okien
Name:		xfce
Version:	3.8.2
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://www.xfce.org/archive/%{name}-%{version}.tar.gz
Source1:	xfsamba.desktop
URL:		http://www.xfce.org/
Requires:	imlib-cfgeditor
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

%package -n xfsamba
Summary:	Xfsamba - SMB network navigator without mounting
Summary(pl):	Xfsamba - przegl±danie zasobów SMB bez mountowania ich
Version:	%{_xfsamba_ver}
Epoch:		1
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Group(de):	X11/Applikationen/Netzwerkwesen
Requires:	samba-client

%description -n xfsamba
Xfsamba is an SMB network navigator with downloading, uploading and
browsing. It does not mount remote SMB shares any time.

%description -l pl -n xfsamba
Xfsamba jest programem do przegl±dania zasobów udostêpnianych przez SMB.
Jednak, w przeciwieñstwie do wiêkszo¶ci tego typu programów, jest to
robione poprzez smbclient'a. Dziêki temu mo¿emy "szperaæ" w sieci lokalnej
bez u¿ywania smbmount.

%prep
%setup -q

rm -f acinclude.m4

%build
libtoolize --copy --force
gettextize --copy --force
aclocal
autoconf
automake -a -c
%configure \
	--disable-dt \
	--enable-gdk-pixbuf \
	--disable-imlib \
	--enable-xinerama

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

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
%attr(755,root,root) %{_bindir}/xfwm
%{_sysconfigdir}/xfce
%{_mandir}/*/*
%{_datadir}/xfce

%files -n gtk-theme-xfce
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk/themes/engines/*

%files -n xfsamba
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xfsamba
%{_applnkdir}/Network/Misc/*
