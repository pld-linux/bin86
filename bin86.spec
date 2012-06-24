Summary:	Real mode 80x86 assembler and linker
Summary(de):	Real-Mode 80x86 Assembler und Linker
Summary(fr):	Assembleur 80x86 en mode r�el et �diteur de liens
Summary(pl):	Assembler i konsolidator trybu rzeczywistego procesor�w 80x86
Summary(tr):	Ger�ek kip 80x86 �eviricisi ve ba�lay�c�s�
Name:		bin86
Version:	0.15.5
Release:	1
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/J�zyki
Source0:	http://www.cix.co.uk/~mayday/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Exclusivearch:	%{ix86}
Obsoletes:	dev86

%description
This package provides an assembler and linker for real mode 80x86
instructions. Programs that run in real mode, including LILO and the
kernel's bootstrapping code, need to have this package installed to be
built from the sources.

%description -l de
Dieses Paket enth�lt einen Assembler und Linker f�r Real-Mode 80x86-
Instruktione. F�r Programme, die in Real-Mode laufen, einschlie�lich
LILO und der Bootstrapping-Code des Kernels, mu� dieses Paket
installiert sein, damit sie von den Quellen gebaut werden k�nnen.

%description -l fr
Ce package fournit un assembleur et un �diteur de liens pour les
instructions du mode r�el 80x86. Les programmes tournat en mode r�el
dont LILO et code de bootstrapping du noyau, ont besoin de ce package
pour �tre reconstruits � partir des sources.

%description -l pl
Pakiet ten udost�pnia assembler i konsolidator (linker) trybu
rzeczywistego procesor�w rodziny 80x86. Pakiet ten trzeba mie� do
kompilacji program�w, kt�re pracuj� w trybie rzeczywistym jak LILO czy
kod startowy kernela.

%description -l tr
Bu paket, ger�ek kip 80x86 y�nergeleri i�in bir �evirici ve ba�lay�c�
sa�lar. LILO ve �ekirde�in �ny�kleme kodlar� gibi ger�ek kipte ko�an
programlar, bu pakete gereksinim duyarlar.

%prep
%setup -q -n %{name}

%build
%{__make} CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install as/as86 ld/ld86 $RPM_BUILD_ROOT%{_bindir}
install man/* $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*.gz
