Summary:	Real mode 80x86 assembler and linker
Summary(de.UTF-8):	Real-Mode 80x86 Assembler und Linker
Summary(es.UTF-8):	Assembler y Linker para modo real 80x86
Summary(fr.UTF-8):	Assembleur 80x86 en mode réel et éditeur de liens
Summary(pl.UTF-8):	Assembler i konsolidator trybu rzeczywistego procesorów 80x86
Summary(pt_BR.UTF-8):	Assembler e Linker para modo real 80x86
Summary(tr.UTF-8):	Gerçek kip 80x86 çeviricisi ve bağlayıcısı
Name:		bin86
Version:	0.16.21
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://v3.sk/~lkundrak/dev86/%{name}-%{version}.tar.gz
# Source0-md5:	a94f57453500700cebfea86d7d217481
Patch0:		%{name}-x64.patch
URL:		http://v3.sk/~lkundrak/dev86/
Obsoletes:	dev86
ExclusiveArch:	%{ix86} %{x8664} x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an assembler and linker for real mode 80x86
instructions. Programs that run in real mode, including LILO and the
kernel's bootstrapping code, need to have this package installed to be
built from the sources.

%description -l de.UTF-8
Dieses Paket enthält einen Assembler und Linker für Real-Mode 80x86-
Instruktione. Für Programme, die in Real-Mode laufen, einschließlich
LILO und der Bootstrapping-Code des Kernels, muß dieses Paket
installiert sein, damit sie von den Quellen gebaut werden können.

%description -l es.UTF-8
Este paquete provee un assembler y un linker para instrucciones 80x86
modo real. Los programas que se ejecutan en modo real, incluyendo LILO
y el código de boot del kernel, necesitan tener este paquete instalado
para que se construyan los fuentes.

%description -l fr.UTF-8
Ce package fournit un assembleur et un éditeur de liens pour les
instructions du mode réel 80x86. Les programmes tournat en mode réel
dont LILO et code de bootstrapping du noyau, ont besoin de ce package
pour être reconstruits à partir des sources.

%description -l pl.UTF-8
Pakiet ten udostępnia assembler i konsolidator (linker) trybu
rzeczywistego procesorów rodziny 80x86. Pakiet ten trzeba mieć do
kompilacji programów, które pracują w trybie rzeczywistym jak LILO czy
kod startowy kernela.

%description -l pt_BR.UTF-8
Este pacote provê um assembler e um linker para instruções 80x86 modo
real. Programas que rodam em modo real, incluindo LILO e o código de
boot do kernel, necessitam ter este pacote instalado para serem
construídos dos fontes.

%description -l tr.UTF-8
Bu paket, gerçek kip 80x86 yönergeleri için bir çevirici ve bağlayıcı
sağlar. LILO ve çekirdeğin önyükleme kodları gibi gerçek kipte koşan
programlar, bu pakete gereksinim duyarlar.

%prep
%setup -q
%ifarch %{x8664} x32
%patch0 -p1
%endif

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -p as/as86 ld/ld86 $RPM_BUILD_ROOT%{_bindir}
cp -p man/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/as86
%attr(755,root,root) %{_bindir}/ld86
%{_mandir}/man1/as86.1*
%{_mandir}/man1/ld86.1*
