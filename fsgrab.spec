%define name fsgrab
%define version 1.1
%define release 15

Summary: Get blocks from an (ext2) filesystem on Linux
Name: %{name}
Version: %{version}
Release:	1
License: GPL
Group: File tools
Source: %name-%version.tar.bz2
Buildroot: %_tmppath/%{name}-buildroot

%description
This program allows you to seek to a given point in a file or a block device
and write a given number of blocks out from that point, without reading the
intervening material. This is useful in attempting undeletion of
files. See the Ext2fs-Undeletion howto for details.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%build
make

%install
install -m 755 -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 fsgrab $RPM_BUILD_ROOT%{_bindir}/

install -m 755 -d $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 fsgrab.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-14mdv2011.0
+ Revision: 618361
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.1-13mdv2010.0
+ Revision: 428922
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.1-12mdv2009.0
+ Revision: 245422
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.1-10mdv2008.1
+ Revision: 136423
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 1.1-10mdv2008.0
+ Revision: 70237
- use %%mkrel


* Wed Apr 20 2005 Lenny Cartier <lenny@mandriva.com> 1.1-9mdk
- rebuild

* Thu Feb 19 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.1-8mdk
- rebuild

* Fri Jan 17 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1-7mdk
- rebuild

* Wed Aug 28 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1-6mdk
- rebuild

* Tue Jul 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1-5mdk
- rebuild

* Tue Jan 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1-4mdk
- rebuild

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1-3mdk
- BM

* Wed Apr 26 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.1-2mdk
- fix files section
- fix group

* Thu Feb 17 2000 Lenny Cartier <lenny@mandrakesoft.com>
- mandrake build

