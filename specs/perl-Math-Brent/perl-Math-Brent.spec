# $Id$
# Authority: dries
# Upstream: John A.R. Williams <J,A,R,Williams$aston,ac,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Brent

Summary: Single Dimensional Function Minimisation
Name: perl-Math-Brent
Version: 0.01
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Brent/

Source: http://search.cpan.org/CPAN/authors/id/J/JA/JARW/Math-Brent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is an implementation of Brents method for One-Dimensional minimisation
of a function without using derivatives. This algorithm cleverly uses both
the Golden Section Search and parabolic interpolation.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" "PREFIX=%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Brent.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
