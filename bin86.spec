Summary:	Real mode 80x86 assembler and linker
Summary(de):	Real-Mode 80x86 Assembler und Linker
Summary(es):	Assembler y Linker para modo real 80x86
Summary(fr):	Assembleur 80x86 en mode réel et éditeur de liens
Summary(pl):	Assembler i konsolidator trybu rzeczywistego procesorów 80x86
Summary(pt_BR):	Assembler e Linker para modo real 80x86
Summary(tr):	Gerçek kip 80x86 çeviricisi ve baðlayýcýsý
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
Dieses Paket enthält einen Assembler und Linker für Real-Mode 80x86-
Instruktione. Für Programme, die in Real-Mode laufen, einschließlich
LILO und der Bootstrapping-Code des Kernels, muß dieses Paket
installiert sein, damit sie von den Quellen gebaut werden können.

%description -l es
Este paquete provee un assembler y un linker para instrucciones 80x86
modo real. Los programas que se ejecutan en modo real, incluyendo LILO
y el código de boot del kernel, necesitan tener este paquete instalado
para que se construyan los fuentes.

%description -l fr
Ce package fournit un assembleur et un éditeur de liens pour les
instructions du mode réel 80x86. Les programmes tournat en mode réel
dont LILO et code de bootstrapping du noyau, ont besoin de ce package
pour être reconstruits à partir des sources.

%description -l pl
Pakiet ten udostêpnia assembler i konsolidator (linker) trybu
rzeczywistego procesorów rodziny 80x86. Pakiet ten trzeba mieæ do
kompilacji programów, które pracuj± w trybie rzeczywistym jak LILO czy
kod startowy kernela.

%description -l pt_BR
Este pacote provê um assembler e um linker para instruções 80x86 modo
real. Programas que rodam em modo real, incluindo LILO e o código de
boot do kernel, necessitam ter este pacote instalado para serem
construídos dos fontes.

%description -l tr
Bu paket, gerçek kip 80x86 yönergeleri için bir çevirici ve baðlayýcý
saðlar. LILO ve çekirdeðin önyükleme kodlarý gibi gerçek kipte koþan
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
