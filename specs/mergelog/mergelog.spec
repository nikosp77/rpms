# $Id$
# Authority: dag
# Upstream: Bertrand Demiddelaer <bert$zehc,net>

Summary: Merges httpd log files by date
Name: mergelog
Version: 4.5
Release: 1.2
License: GPL
Group: Applications/File
URL: http://mergelog.sourceforge.net/

Source: http://dl.sf.net/mergelog/mergelog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
mergelog is a small and fast C program which merges by date httpd log
files in 'Common Log Format' from web servers behind round-robin DNS.
It has been designed to easily manage huge log files from highly
stressed servers. mergelog is distributed with zmergelog which supports
gzipped log files

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 4.5-1.2
- Rebuild for Fedora Core 5.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 4.5-1
- Initial package. (using DAR)
