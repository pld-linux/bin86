Summary:	Real mode 80x86 assembler and linker
Summary(de):	Real-Mode 80x86 Assembler und Linker
Summary(fr):	Assembleur 80x86 en mode réel et éditeur de liens
Summary(pl):	Assembler i konsolidator trybu rzeczywistego procesorów 80x86
Summary(tr):	Gerçek kip 80x86 çeviricisi ve baðlayýcýsý
Name:		bin86
Version:	0.4
Release:	7
Copyright:	distributable
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Source:		ftp://sunsite.unc.edu/pub/Linux/GCC/%{name}-%{version}.tar.gz
Patch0:		bin86-glibc.patch
Patch1:		bin86-opt.patch
Buildroot:	/tmp/%{name}-%{version}-root
Exclusivearch:	i386

%description
This package provides an assembler and linker for real mode 80x86
instructions. Programs that run in real mode, including LILO and the
kernel's bootstrapping code, need to have this package installed to
be built from the sources.

%description -l de
Dieses Paket enthält einen Assembler und Linker für Real-Mode 80x86-
Instruktione. Für Programme, die in Real-Mode laufen, einschließlich LILO
und der Bootstrapping-Code des Kernels, muß dieses Paket installiert sein, 
damit sie von den Quellen gebaut werden können.

%description -l fr
Ce package fournit un assembleur et un éditeur de liens pour les
instructions du mode réel 80x86. Les programmes tournat en mode réel
dont LILO et code de bootstrapping du noyau, ont besoin de ce package
pour être reconstruits à partir des sources.

%description
PAkiet ten udostêpnia assembler i konsolidator (linker) trybu rzeczywistego
procesorów rodziny 80x86. Pakiet ten trzeba mieæ do kompilacji programów, które
pracuj± w trybie rzeczywistym jak LILO czy kod startowy kernela.

%description -l tr
Bu paket, gerçek kip 80x86 yönergeleri için bir çevirici ve baðlayýcý saðlar.
LILO ve çekirdeðin önyükleme kodlarý gibi gerçek kipte koþan programlar, bu
pakete gereksinim duyarlar.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
export PATH=$PATH:.
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -s as/as86 ld/ld86 $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*

%changelog

- added using CVS keywords in %changelog (for automating them).

* Sat Aug 22 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.4-6]
- added -q %setup parameter,
- added missing Buildroot field in header,
  non-root account).

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- use ExclusiveArch instead of Exclusive

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- minor spec file cleanups
- build rooted
- usees %attr() now

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- built against glibc

- added %attr and %defattr macros in %files (allows build package from
  non-root account),
- start at RH spec.
