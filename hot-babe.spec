Summary:	A GTK+ based monitoring application
Summary(pl.UTF-8):	Oparta na GTK+ aplikacja monitorująca pracę systemu
Name:		hot-babe
Version:	0.2.2
Release:	1
License:	Artistic
Group:		X11/Applications
Source0:	http://dindinx.net/hotbabe/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	482a9496b493d2394601689659971042
Source1:	%{name}.desktop
Source2:	%{name}-32.png
URL:		http://dindinx.net/hotbabe/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hot-babe is a small graphical utility which display the system activity
in a very special way. When the CPU is idle, it displays a dressed girl,
and when the activity goes up, as the temperature increases, the girl
begins to undress, to finish totally naked when the system activity
reaches 100%.

Of course, if you can be shocked by nudity, don't use it!

%description -l pl.UTF-8
Hot-babe to małe graficzne narzędzie wyświetlające aktywność systemu w
dość specyficzny sposób. Gdy procesor jest bezczynny, program wyświetla
ubraną dziewczynę, a gdy aktywność lub temperatura wzrasta, dziewczyna
zaczyna się rozbierać. Gdy aktywność systemu osiągnie 100%, bohaterka
stanie się całkowicie naga.

Jeśli możesz poczuć się urażony widokiem nagości, nie używaj tego
programu!

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall `pkg-config gdk-2.0 gdk-pixbuf-2.0 --cflags` -DPREFIX=\\\"%{_prefix}\\\" -DVERSION=\\\"%{version}\\\""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/hot-babe
%{_mandir}/man1/*.1*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
