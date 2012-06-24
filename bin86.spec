Summary:	Real mode 80x86 assembler and linker
Summary(de):	Real-Mode 80x86 Assembler und Linker
Summary(es):	Assembler y Linker para modo real 80x86
Summary(fr):	Assembleur 80x86 en mode r�el et �diteur de liens
Summary(pl):	Assembler i konsolidator trybu rzeczywistego procesor�w 80x86
Summary(pt_BR):	Assembler e Linker para modo real 80x86
Summary(tr):	Ger�ek kip 80x86 �eviricisi ve ba�lay�c�s�
Name:		bin86
Version:	0.16.16
Release:	1
License:	GPL
Group:		Development/Languages
#Source0Download: http://www.cix.co.uk/~mayday/
Source0:	http://www.cix.co.uk/~mayday/dev86/%{name}-%{version}.tar.gz
# Source0-md5:	48c56be9792b26702805cb59471c99e5
URL:		http://www.cix.co.uk/~mayday/
Obsoletes:	dev86
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l es
Este paquete provee un assembler y un linker para instrucciones 80x86
modo real. Los programas que se ejecutan en modo real, incluyendo LILO
y el c�digo de boot del kernel, necesitan tener este paquete instalado
para que se construyan los fuentes.

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

%description -l pt_BR
Este pacote prov� um assembler e um linker para instru��es 80x86 modo
real. Programas que rodam em modo real, incluindo LILO e o c�digo de
boot do kernel, necessitam ter este pacote instalado para serem
constru�dos dos fontes.

%description -l tr
Bu paket, ger�ek kip 80x86 y�nergeleri i�in bir �evirici ve ba�lay�c�
sa�lar. LILO ve �ekirde�in �ny�kleme kodlar� gibi ger�ek kipte ko�an
programlar, bu pakete gereksinim duyarlar.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install as/as86 ld/ld86 $RPM_BUILD_ROOT%{_bindir}
install man/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
