# $Id$
# Authority: dries
# Upstream: Schuyler Erle <schuyler$nocat,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-TigerLine

Summary: TIGER/Line geographic data
Name: perl-Geo-TigerLine
Version: 0.02
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-TigerLine/

Source: http://www.cpan.org/modules/by-module/Geo/Geo-TigerLine-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a module around the TIGER/Line geographic data generated by the
U.S. Census. TIGER/Line data files contain detailed information about
roads, waterways, political and property boundaries, street addresses,
etc... Almost (but not quite) everything you need to recreate something
like Mapquest.

Geo::TigerLine has been updated to reflect the structure of the 2003
TIGER/Line data sets. If you want to use older datasets, consider
regenerating the TIGER/Line data set parsers with the mk_parsers script
distributed with this module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Geo/TigerLine.pm
%{perl_vendorlib}/Geo/TigerLine/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
