Summary:	A GTK+ based monitoring application
Summary(pl):	Oparta na GTK+ aplikacja monitoruj±ca pracê systemu
Name:		hot-babe
Version:	0.1.2
Release:	2
License:	GPL	
Group:		X11/Applications
Source0:	http://dindinx.net/hotbabe/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	ff7ca9f0b4459927ee0358aa1c66c2bf
Source1:	%{name}.desktop
Source2:	%{name}-32.png
# Do we support these?
#Source3:	%{name}-16.png
#Source4:	%{name}-48.png
URL:		http://dindinx.net/hotbabe/
BuildRequires:	gtk+-devel
BuildRequires:	gdk-pixbuf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hot-babe is a small graphical utility which display the system activity
in a very special way. When the CPU is idle, it displays a dressed girl,
and when the activity goes up, as the temperature increases, the girl
begins to undress, to finish totally naked when the system activity
reaches 100%.

Of course, if you can be shocked by nudity, don't use it!

%description -l pl
Hot-babe to ma³e graficzne narzêdzie wy¶wietlaj±ce aktywno¶æ systemu w
do¶æ specyficzny sposób. Gdy procesor jest bezczynny, program wy¶wietla
ubran± dziewczynê, a gdy aktywno¶æ lub temperatura wzrasta, dziewczyna
zaczyna siê rozbieraæ. Gdy aktywno¶æ systemu osi±gnie 100%, bohaterka
stanie siê ca³kowicie naga.

Je¶li mo¿esz poczuæ siê ura¿ony widokiem nago¶ci, nie u¿ywaj tego
programu!

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall `gtk-config --cflags` `gdk-pixbuf-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install hot-babe.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%{_desktopdir}/*
%{_pixmapsdir}/*
