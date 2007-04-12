%define name fsgrab
%define version 1.1
%define release 9mdk

Summary: Get blocks from an (ext2) filesystem on Linux
Name: %{name}
Version: %{version}
Release: %{release}
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

